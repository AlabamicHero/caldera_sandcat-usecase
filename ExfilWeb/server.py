import os
from flask import Flask, render_template, request, send_from_directory

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Ensure the "uploads" directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Save the file to the uploads directory
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return 'File uploaded successfully'

@app.route('/downloads/<filename>')
def download(filename):
    return send_from_directory(os.path.join(app.root_path, app.config['DOWNLOAD_FOLDER']), filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
