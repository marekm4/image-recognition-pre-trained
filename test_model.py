from PIL import Image

from model import Model


def test_model():
    image = Image.open('red-fox2.jpg')
    model = Model()
    label = model.predict(image)
    assert label == 'red_fox'
