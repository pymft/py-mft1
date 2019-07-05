import urllib.request


with urllib.request.urlopen('http://python.org') as req:
    text = req.read()
    text_string = text.decode('utf-8')
