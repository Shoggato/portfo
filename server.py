from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route("/download/cv")
def download_my_cv():
    path = 'static/files/ErikaWalkerResume.pdf'
    return send_file(path, as_attachment=True, mimetype='application/pdf')
