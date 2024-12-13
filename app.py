from flask import Flask, render_template, request, jsonify
import PyPDF2
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    
    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        content = read_pdf(filepath)
        return jsonify({'content': content})

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_term = data.get('search_term', '').lower()
    content = data.get('content', '').lower()
    
    results = []
    start = 0
    while True:
        index = content.find(search_term, start)
        if index == -1:
            break
            
        context_start = max(0, index - 50)
        context_end = min(len(content), index + len(search_term) + 50)
        context = content[context_start:context_end]
        results.append(context)
        start = index + 1
        
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
