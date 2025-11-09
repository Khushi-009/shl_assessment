# SHL Assessment Recommender

This repository contains a working baseline system for the SHL Generative AI Internship assessment.

## 🚀 Quickstart
1. **Clone the repo:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/shl-assessment-recommender.git
   cd shl-assessment-recommender
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API locally:**
   ```bash
   python app.py
   ```
   Access the health check at http://localhost:8080/health

4. **Test recommend endpoint:**
   ```bash
   curl -X POST http://localhost:8080/recommend -H "Content-Type: application/json" -d '{"query":"data analyst","k":5}'
   ```

5. **Streamlit frontend (optional):**
   ```bash
   streamlit run app_streamlit.py
   ```

6. **Deploy:**
   - Use free services like Render, Railway, or Heroku.
   - Or deploy Streamlit app on [Streamlit Cloud](https://share.streamlit.io).

## 📂 Files
- `app.py` → Flask API
- `app_streamlit.py` → Frontend
- `tfidf.joblib`, `train.pkl`, `X_train_sparse.joblib` → Model artifacts
- `requirements.txt` → Dependencies
- `README.md` → Docs

## 📬 Endpoints
- `/health` → Status check
- `/recommend` → POST with `{ "query": "role description", "k": 10 }`

## 🧠 Notes
This TF-IDF + Nearest Neighbors baseline can be upgraded to embeddings (SBERT or OpenAI) and FAISS ANN retrieval for higher recall.
