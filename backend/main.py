from flask import Flask, request, jsonify
from pypdf import PdfReader

app = Flask(__name__)

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
    return "[sentences that are red flags]"

def sentence_analyze(sentence):
    return []

if __name__ == '__main__':
    app.run()