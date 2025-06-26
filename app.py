from flask import Flask, render_template
import os
import fitz  

app = Flask(__name__)

PDF_FOLDER = 'static/pdfs'

def extract_pdf_data():
    data = []
    for filename in os.listdir(PDF_FOLDER):  
        if filename.endswith(".pdf"):
            doc = fitz.open(os.path.join(PDF_FOLDER, filename))
            text = ""
            for page in doc:
                text += page.get_text()
            data.append({
                "title": filename,
                "content": text[:1000] + "..." if len(text) > 1000 else text
            })
    return data

@app.route('/')
def index():
    pdf_data = extract_pdf_data()
    return render_template('index.html', pdf_data=pdf_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8056, debug=True)
@app.route('/static_export')
def static_export():
    pdf_data = extract_pdf_data() 
    rendered = render_template('index.html', pdf_data=pdf_data)
    os.makedirs('output', exist_ok=True)
    with open('output/index.html', 'w') as f:
        f.write(rendered)
    return "Static site exported!"
