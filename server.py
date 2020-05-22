import os

from sanic import Sanic, response
from PIL import Image
import requests
from io import BytesIO

from model import Model

model = Model()

app = Sanic('image-recognition-pre-trained')
app.static('/', './public/index.html')
app.static('/css', './public/css')
app.static('/js', './public/js')


@app.route('/url', methods=['POST'])
async def url(request):
    image = Image.open(BytesIO(requests.get(request.form.get('url')).content))
    return response.text(model.predict(image))


@app.route('/upload', methods=['POST'])
async def url(request):
    image = Image.open(BytesIO(request.files.get('file').body))
    return response.text(model.predict(image))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '8080')))
