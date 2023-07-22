#!flask/bin/python
import webbrowser
webbrowser.open('http://127.0.0.1:5000', new=2)
from app import app
app.run(debug = True)
