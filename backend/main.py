from flask import Flask, request, jsonify
import joblib
from pypdf import PdfReader
from flask_cors import CORS


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