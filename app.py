import sys  
import os
from flask import Flask, flash, request, redirect, url_for, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'videos'
ALLOWED_EXTENSIONS = {'mp4', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
  return("Inference server is alive :)")

@app.route('/upload', methods=['GET', 'POST'])
def uploader():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'saved OK'