import flask as flask
import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('input.html')

@app.route('/camera-populer')
def camera_terpopuler():
    html_doc = requests.get('https://id.carousell.com/categories/photography-6/')
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    camera_terpopuler = soup.find(attrs={'class': '_2RJeLsMmpi'})
    titles = camera_terpopuler.findAll(attrs={'class': 'TpQXuJG_eo'})

    return render_template('input.html', titles=titles)

if __name__ == '__main__':
    app.run(debug=True)
