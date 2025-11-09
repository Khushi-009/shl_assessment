from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

vectorizer = joblib.load('tfidf.joblib')
train_df = pd.read_pickle('train.pkl')
X_train = joblib.load('X_train_sparse.joblib')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/recommend', methods=['POST'])
def recommend():
    payload = request.json
    query_text = payload.get('query', '')
    k = int(payload.get('k', 10))
    q_vec = vectorizer.transform([query_text])
    sims = cosine_similarity(q_vec, X_train).flatten()
    idxs = sims.argsort()[::-1]
    recs = []
    for i in idxs:
        url = train_df.iloc[i]['Assessment_url']
        if url not in recs:
            recs.append(url)
        if len(recs) >= k:
            break
    return jsonify({'query': query_text, 'recommendations': recs})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
