from flask import Flask, request, jsonify
import joblib
from pypdf import PdfReader
from dotenv import load_dotenv
import os
import google.generativeai as genai
import fitz
from flask_cors import CORS

load_dotenv()
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Make sure the .env file is correctly set.")
genai.configure(api_key=api_key)
llm_model = genai.GenerativeModel("gemini-2.0-flash")


app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
translation = {0: "positive", 1: "negative", 2: "general"}
negative_threshold = 0.80
positive_threshold = 0.95


@app.route('/')
def hello():
    return "Hello, World!"

#LLM summarizer
@app.route('/summarize-text', methods=['POST'])
def summarize_text():
    """Summarizes the extracted legal text Custom LLM"""
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"""
    You are an expert in legal document summarization.
    Your task is to generate a structured and precise summary of the given contract. 
    Focus on key elements such as parties involved, obligations, terms, payment details, 
    penalties, termination clauses, and confidentiality. The summary should be concise yet 
    comprehensive, avoiding unnecessary legal jargon.

    Here is the contract for your reference:
    {text[:5000]}
    """

    response = llm_model.generate_content(prompt)
    return jsonify({"summary": response.text})

@app.route('/pdf-to-text', methods=['POST'])
def pdf_to_text():
    data = request.get_json()
    file_path = data.get('file_path')
    pdf_reader = PdfReader(file_path)
    page_content = ""
    for indx, pdf_page in enumerate(pdf_reader.pages):
        page_content = page_content + pdf_page.extract_text()
    return page_content


@app.route('/text-analyze', methods=['POST'])
def text_analyze_endpoint():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    res = text_analyze(text)
    return extract_negative(res)


@app.route('/sentence-analyze', methods=['POST'])
def sentence_analyze_endpoint():
    data = request.get_json()
    sentence = data.get('sentence')
    res = sentence_analyze(sentence)
    return res


def sentence_analyze(sentence):
    res = ""
    prediction = ml_recognition(sentence)
    res = str(prediction["classification"])
    return res


def text_analyze(text):
    sentences = text.split('. ')
    res = []
    for sentence in sentences:
        if sentence and sentence[-1] != '.':
            sentence += '.'
        prediction = ml_recognition(sentence)
        classification = str(prediction["classification"])
        confidence = prediction["confidence"]
        pair = [sentence, classification, confidence]
        res.append(pair)
    return res


def ml_recognition(sentence):
    sentence_vect = vectorizer.transform([sentence])
    predicted_label = model.predict(sentence_vect)
    predicted_proba = model.predict_proba(sentence_vect)
    confidence = float(predicted_proba[0][predicted_label[0]])
    res = {
        "confidence": confidence,
        "classification": predicted_label[0]
    }
    return res


def extract_negative(data):
    res = []
    for sentence, classification, confidence in data:
        if int(classification) == 1 and confidence > 0.8:
            res.append(
                {
                    "sentence": sentence,
                    "classification": "negative",
                    "confidence": confidence
                }
            )
    return res

if __name__ == '__main__':
    app.run()