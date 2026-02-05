Arabic Sentiment Analysis 🧠🇸🇦

An end-to-end Arabic Sentiment Analysis system built using a fine-tuned Transformer model.

The project covers the full ML lifecycle: data preprocessing, model training, evaluation, API serving, frontend visualization, and containerization.

It is designed as a real-world NLP application, not just a notebook.

📌 Overview

This project performs binary sentiment classification (Positive / Negative) on Arabic text using a fine-tuned AraBERT model.

It supports Arabic emojis, handles noisy Twitter text, and exposes the model via a FastAPI backend with a Streamlit frontend for real-time interaction.

📁 Project Structure

Arabic_Sentiment_Analysis/

│

├── api/

│   ├── __init__.py

│   └── main.py                # FastAPI backend (model inference API)

│

├── streamlit_app/

│   └── app.py                 # Streamlit frontend UI

│

├── sentiment_analysis_env/    # Python virtual environment (local)

│

├── Arabic_Sentiment_Analysis.ipynb    # Model training & evaluation notebook

│                              

├── requirements.txt

├── Dockerfile

└── README.md

🚀 Features
🔹 Fine-Tuned Arabic Transformer

Based on aubmindlab/bert-base-arabertv02

Fine-tuned specifically for Arabic sentiment classification

Model source:

https://huggingface.co/aubmindlab/bert-base-arabertv02

🔹 Advanced Emoji Handling

Arabic tweets often rely heavily on emojis

Emojis are:

   Demojized into Arabic text
   
   Added as custom tokens to the tokenizer vocabulary

Improves sentiment signal significantly

🔹 Scalable Backend (FastAPI)

REST API for sentiment prediction

Clean request/response schema

Ready for containerization and production deployment

🔹 Interactive Frontend (Streamlit)

User-friendly web interface

Real-time predictions

Confidence scores

Clear sentiment visualization

🔹 GPU-Ready & Dockerized

Built on PyTorch 2.5.1 + CUDA 12.1

Dockerfile optimized for inference

Ready for cloud or local GPU deployment

📊 Model Performance

The model was trained on the Arabic Sentiment Twitter Corpus and evaluated on a held-out test set.

Dataset source:

https://huggingface.co/datasets/arbml/Arabic_Sentiment_Twitter_Corpus

🔹 Test Results

| Metric            | Score      |

| ----------------- | ---------- |

| Accuracy          | **94.55%** |

| F1 Score (Macro)  | **94.55%** |

| Balanced Accuracy | **94.57%** |

| AUC               | **0.9861** |

🔹 Per-Class Metrics
 
| Class    |  Precision  |  Recall |  F1    |

| -------- |  ---------  |  ------ |  ----  |

| Negative |  0.93       |  0.96   |  0.95  |

| Positive |  0.96       |  0.93   |  0.95  |


🛠️ Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/Arabic_Sentiment_Analysis.git

cd Arabic_Sentiment_Analysis

2️⃣ Create Virtual Environment

python -m venv sentiment_analysis_env

Activate:

sentiment_analysis_env\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

💻 Usage

🔹 1. Model Training & Analysis

The notebook Arabic_Sentiment_Analysis.ipynb includes:

Dataset loading and validation

Arabic-specific preprocessing

Emoji demojization and tokenizer expansion

Fine-tuning AraBERT

Comprehensive evaluation:

   Confusion Matrix
   
   ROC Curve
   
   Precision / Recall / F1

🔹 2. Run FastAPI Backend

Start the inference API:

uvicorn api.main:app --reload

API documentation (Swagger):

streamlit run streamlit_app/app.py

🔹 3. Run Streamlit Frontend

Launch the web interface:

streamlit run streamlit_app/app.py

Default UI:

http://localhost:8501

🐳 Docker Support

Build the image:

docker build -t arabic-sentiment-analysis .

Run with GPU support:

docker run --gpus all -p 8503:8503 arabic-sentiment-analysis

📝 Note

For portfolio and demonstration purposes, the FastAPI backend is executed within the same runtime environment as the Streamlit application.

🔮 Future Improvements

Separate FastAPI & Streamlit using Docker Compose

Neutral sentiment class (3-class classification)

Arabic dialect detection

Authentication & rate limiting

Model monitoring & logging

Cloud deployment (AWS / GCP / Azure)

👤 Author

Beshoy Arnest

Computer Science Graduate | AI & Data Science

GitHub: https://github.com/7BeshoyArnest

LinkedIn: https://www.linkedin.com/in/beshoy-arnest-a3548a23a/















