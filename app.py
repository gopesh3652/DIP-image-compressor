from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from compress_image import compress_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        output_filename = 'compressed_' + filename
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        
        compress_image(input_path, output_path)
        
        return render_template('index.html', result=output_filename)

if __name__ == '__main__':
    app.run()
