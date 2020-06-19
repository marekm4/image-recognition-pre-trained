import os

from flask import Flask, send_file, request
from PIL import Image
import requests
from io import BytesIO

from model import Model

model = Model()
app = Flask('image-recognition-pre-trained')


@app.route('/')
def index():
    return send_file('./public/index.html')


@app.route('/css/app.css')
def css():
    return send_file('public/css/app.css')


@app.route('/js/app.js')
def js():
    return send_file('public/js/app.js')


@app.route('/url', methods=['POST'])
def url():
    image = Image.open(BytesIO(requests.get(request.form['url']).content))
    return model.predict(image)


@app.route('/upload', methods=['POST'])
def upload():
    image = Image.open(BytesIO(request.files['file'].read()))
    return model.predict(image)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '8080')))
