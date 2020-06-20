from io import BytesIO

from server import app


def test_static():
    client = app.test_client()
    result = client.get('/')
    assert result.status_code == 200
    assert b'Image Recognition' in result.data


def test_url():
    client = app.test_client()
    result = client.post('/url', data={
        'url': 'http://2.bp.blogspot.com/-fK3T27K_qYs/UI3gA89r6EI/AAAAAAAAGs4/Paoir9nOsy8/s1600/red-fox2.jpg'})
    assert result.status_code == 200
    assert b'red_fox' in result.data


def test_upload():
    client = app.test_client()
    result = client.post('/upload', data={'file': (open('red-fox2.jpg', 'rb'), 'red-fox2.jpg')})
    assert result.status_code == 200
    assert b'red_fox' in result.data
