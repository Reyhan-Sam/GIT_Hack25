from flask import Flask, request, jsonify
import joblib
from pypdf import PdfReader

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

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

@app.route('/analyze', methods=['POST'])
def text_analyze():
    data = request.get_json()
    text = data.get('text')
    sentences = text.split('. ')
    res = ""
    for sentence in sentences:
        if sentence and sentence[-1] != '.':
            sentence += '.'
        prediction = ml_recognition(sentence)
        print(prediction["class"])
        res = str(prediction["class"])
    return res

def ml_recognition(sentence):
    sentence_vect = vectorizer.transform([sentence])
    predicted_label = model.predict(sentence_vect)
    predicted_proba = model.predict_proba(sentence_vect)
    confidence = predicted_proba[0][predicted_label[0]]
    res = {
        "confidence": confidence,
        "class": predicted_label[0]
    }
    return res

def sentence_analyze(sentence):
    return []

if __name__ == '__main__':
    app.run()