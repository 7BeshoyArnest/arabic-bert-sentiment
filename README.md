Arabic Sentiment Analysis 

This project implements an end-to-end sentiment analysis pipeline for Arabic text using a fine-tuned transformer model.

It includes a training notebook, a FastAPI backend for model serving, and a Streamlit frontend for user interaction.

📁 Project Structure

Arabic_Sentiment_Analysis/

│

├── api/

│      ├── __init__.py

│      └── main.py           # FastAPI application for model inference

│
├── streamlit_app/

│    └── app.py            # Streamlit frontend for user-friendly UI

│

├── sentiment_analysis_env/ # Virtual environment

│

└── Arabic_Sentiment_Analysis.ipynb # Model development and training notebook

🚀 Features

Fine-tuned Model: Uses aubmindlab/bert-base-arabertv02 specifically optimized for Arabic.



Custom Emoji Tokenization: Processes Arabic text by "demojizing" and adding emojis as special tokens to the vocabulary for better sentiment capture.



Scalable API: FastAPI backend to handle inference requests.

Interactive UI: Streamlit web app for real-time sentiment prediction.

📊 Model Performance

The model was trained on the arbml/Arabic_Sentiment_Twitter_Corpus dataset, achieving high accuracy in binary classification (Positive/Negative).

Test Accuracy: ~94.55% 

F1 Score (Macro): ~94.55% 

AUC Score: 0.9861

Class     Precision, Recall, F1-Score

Negative  0.93,       0.96,    0.95

Positive  0.96,       0.93,    0.95

🛠️ Installation

1-Clone the repository:

git clone https://github.com/your-username/Arabic_Sentiment_Analysis.git

cd Arabic_Sentiment_Analysis

2-Set up the environment:

python -m venv sentiment_analysis_env

source sentiment_analysis_env/bin/activate  # On Windows: sentiment_analysis_env\Scripts\activate

pip install -r requirements.txt

💻 Usage

1. Training & Analysis

The Arabic_Sentiment_Analysis.ipynb notebook contains the full pipeline:

Dataset loading and cleaning.

Dataset-link: https://huggingface.co/datasets/arbml/Arabic_Sentiment_Twitter_Corpus

Arabic-specific emoji preprocessing.

Fine-tuning AraBERT.

Model-link: https://huggingface.co/aubmindlab/bert-base-arabertv02

Detailed evaluation with Confusion Matrix and ROC curves

2. API (FastAPI)
   
Run the backend server to expose the model as a REST API:

uvicorn api.main:app --reload

3. Frontend (Streamlit)
   
Launch the interactive web interface:

streamlit run streamlit_app/app.py

Note: For portfolio and demo purposes, the FastAPI backend is run within the Streamlit application process.

Future Improvements:

Separate backend deployment

Containerized FastAPI service

Authentication & rate limiting
