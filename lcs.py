import os
import subprocess
import mimetypes
from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string

# Ensure the required packages are installed
def install_packages():
    try:
        subprocess.run(["pip", "install", "--upgrade", "Flask"], check=True)
        with open('requirements.txt', 'w') as f:
            f.write('Flask\n')
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to install packages: {e}")

try:
    install_packages()
except ImportError:
    raise ImportError("Please install Flask using 'pip install Flask'.")

app = Flask(__name__)

UPLOAD_FOLDER = "/storage/emulated/0/Cloud"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return True  # Allow all file types

def get_files_by_extension():
    files_by_extension = {}
    for root, _, files in os.walk(UPLOAD_FOLDER):
        for file in files:
            extension = file.split('.')[-1].lower()
            if extension in files_by_extension:
                files_by_extension[extension].append(file)
            else:
                files_by_extension[extension] = [file]
    return files_by_extension

@app.route('/')
def index():
    files_by_extension = get_files_by_extension()
    return render_template_string("""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DedSec1121 Local Cloud Storage</title>
            <style>
                body {
                    background-color: black;
                    color: white;
                    font-family: Arial, sans-serif;
                }
                h1, h2 {
                    color: white;
                }
                a {
                    color: white;
                    text-decoration: none;
                }
                textarea {
                    width: 100%;
                    height: 300px;
                }
                input[type="submit"], input[type="file"], input[type="search"] {
                    margin-top: 10px;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                }
                li {
                    margin-bottom: 10px;
                }
            </style>
        </head>
        <body>
            <h1>DedSec1121 Local Cloud Storage</h1>
            <h2>Upload New File</h2>
            <form method=post enctype=multipart/form-data action="/upload">
                <input type=file name=file>
                <input type=submit value=Upload>
            </form>
            <h2>Files</h2>
            <ul>
                {% for extension, files in files_by_extension.items()|sort %}
                    <li>
                        <strong>{{ extension }}</strong>
                        <ul>
                            {% for file in files|sort %}
                                <li>
                                    <a href="{{ url_for('download_file', filename=file) }}">{{ file }}</a> |
                                    <a href="{{ url_for('delete_file', filename=file) }}">Delete</a>
                                </li>
                            {% endfor %}
                        </ul>
                    </li>
                {% endfor %}
            </ul>
        </body>
        </html>
        """, files_by_extension=files_by_extension)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return redirect(url_for('index'))

@app.route('/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/delete/<filename>')
def delete_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
