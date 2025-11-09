import streamlit as st
import requests

st.title("SHL Assessment Recommender (Demo)")
q = st.text_area("Enter job description or role query")
if st.button("Get recommendations"):
    try:
        resp = requests.post("https://YOUR_API_URL/recommend", json={"query": q, "k": 8})
        if resp.status_code == 200:
            data = resp.json()
            st.subheader("Top Recommendations:")
            for url in data.get('recommendations', []):
                st.write(url)
        else:
            st.error("Error: API did not respond correctly.")
    except Exception as e:
        st.error(f"Error: {e}")
