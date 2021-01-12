import flask as flask
import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def home():
    return render_template('input.html')





if __name__ == '__main__':
    app.run(debug=True)

