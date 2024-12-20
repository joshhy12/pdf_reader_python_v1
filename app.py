from flask import Flask, render_template, jsonify, request
import PyPDF2
import os
import re

app = Flask(__name__)

# Define the path to your Bible PDFs
BIBLE_FOLDER = 'biblia'
pdf_contents = {}

def load_pdfs():

    for filename in os.listdir(BIBLE_FOLDER):
        if filename.endswith('.pdf'):
            file_path = os.path.join(BIBLE_FOLDER, filename)
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                pdf_contents[filename] = text

@app.route('/')
def index():
    pdf_files = [f for f in os.listdir(BIBLE_FOLDER) if f.endswith('.pdf')]
    return render_template('index.html', pdf_files=pdf_files)

@app.route('/read/<filename>')
def read_pdf(filename):
    if filename in pdf_contents:
        return jsonify({'content': pdf_contents[filename]})
    return jsonify({'error': 'PDF not found'})

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_term = data.get('search_term', '').strip()
    filename = data.get('filename')
    
    if filename not in pdf_contents:
        return jsonify({'error': 'PDF not found'})
    
    content = pdf_contents[filename]
    # Split content into verses using regex pattern that matches number at start and period at end
    verses = re.findall(r'\d+[^.]*\.', content)
    results = []

    # Search through verses for the term
    for verse in verses:
        if search_term.lower() in verse.lower():
            results.append(verse.strip())
    
    return jsonify({'results': results})


if __name__ == '__main__':
    load_pdfs()  # Load PDFs when starting the server
    app.run(debug=True)