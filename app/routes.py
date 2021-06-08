from flask import render_template
from app import app
import requests
import os

@app.route('/')
@app.route('/index')
def index():

    key = os.environ.get('NEWS_API_KEY')
    from_date = '2021-06-01'
    r = requests.get(f"https://newsapi.org/v2/everything?q=Tesla&from={from_date}&sortBy=publishedAt&apiKey={key}")
    articles = r.json()['articles']

    return render_template('index.html', title='Home', articles=articles)

