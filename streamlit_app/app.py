import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import requests
import threading
from api.main import app as fastapi_app
import uvicorn

def run_fastapi():
    uvicorn.run(
        fastapi_app,
        host="0.0.0.0",
        port=8000,
        log_level="warning"
    )
    
# Start FastAPI server in a separate thread
threading.Thread(target=run_fastapi, daemon=True).start()
# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"

# Page configuration
st.set_page_config(
    page_title="Arabic Sentiment Analysis",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Arabic Sentiment Analysis")
st.write("Analyze Arabic text sentiment using a deep learning model.")

# Text input
text_input = st.text_area(
    "Arabic Text",
    placeholder="اكتب النص العربي هنا...",
    height=150
)

# Analyze button
if st.button("Analyze Sentiment"):
    if text_input.strip() == "":
        st.warning("Please enter some Arabic text.")
    else:
        try:
            # Spinner while calling the API
            with st.spinner("Analyzing..."):
                response = requests.post(
                    API_URL,
                    json={"text": text_input},
                    timeout=15
                )

            if response.status_code == 200:
                result = response.json()["sentiment"]

                # Display result based on sentiment
                if result["sentiment"] == "Positive":
                    st.success("Positive 😊")
                else:
                    st.error("Negative 😠")

                # Confidence score
                st.markdown(
                    f"**Confidence Score:** `{result['score']:.4f}`"
                )

            else:
                st.error(f"API Error: {response.json()['detail']}")

        except requests.exceptions.RequestException:
            st.error("❌ Could not connect to the FastAPI server.")
