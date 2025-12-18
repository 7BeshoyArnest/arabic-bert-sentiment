from fastapi import FastAPI, HTTPException, status
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from pydantic import BaseModel
import torch
import numpy as np

app = FastAPI()

class InputText(BaseModel):
    text: str

tokenizer = AutoTokenizer.from_pretrained("7beshoyarnest/arabic-sentiment-model")
model = AutoModelForSequenceClassification.from_pretrained("7beshoyarnest/arabic-sentiment-model")
model.eval()

@app.post("/predict")
def predict_arabic_sentiment(input: InputText):
    if not input.text or input.text.strip() == "":
        raise HTTPException(
            status_code=400, 
            detail="No input provided. Please enter some arabic text."
        )
    
    else:
          # Tokenize the input text
        encoded_input = tokenizer(
            input.text, 
            return_tensors="pt", 
            truncation=True, 
            padding=True
        )
        with torch.no_grad():
            outputs = model(**encoded_input)
            logits = outputs.logits.detach().cpu().numpy()

            # softmax
            probs = np.exp(logits) / np.exp(logits).sum(axis=1, keepdims=True)

            # predicted class index
            preds = logits.argmax(axis=-1).astype(int)
        result = [
        {
            "label": int(preds[0]),
            "sentiment": "Positive" if preds[0]==1 else "Negative",
            "score": float(probs[0][preds[0]])
        }
        
    ]
        
    return {"sentiment": result[0]}
