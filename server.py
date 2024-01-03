from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/index.html')
def my_home():
    return render_template('index.html')

@app.route("/download/cv")
def download_my_cv():
    path = 'static/files/ErikaWalkerResume.pdf'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')