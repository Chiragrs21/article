from flask import Flask, render_template, request
from article import extract_article_information
from filter import information
from model import summarizer_model
from model2 import complete_summarizer
from en_tamil import en_tamil
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['post'])
def getvalue():
    query = request.form['name']
    lang = request.form['language']  # language selection
    results = information(query)  # fetcher
    article1, points = summarizer_model(results.url)  # extractive
    if lang == 'tamil':
        points = en_tamil(points)
    article2 = complete_summarizer(results.url)  # abstractive
    return render_template('index.html', header=results.title, category=results.category, author=results.author, content1=article1, content2=points, content3=article2)


@app.route('/article')
def another_value1():
    return render_template('content.html')


@app.route('/article', methods=['post'])
def another_value2():
    query = """'4 experts explain why Elon Musk's plan to colonize Mars is
          'romanticized', not 'realistic', 'cosmic vandalism'"""
    lang = request.form['language']
    results = information(query)
    article1, points = summarizer_model(results.url)
    if lang == 'tamil':
        points = en_tamil(points)
    article2 = complete_summarizer(results.url)
    return render_template('content.html', header=results.title, category=results.category, author=results.author, content1=article1, content2=points, content3=article2)


if __name__ == "__main__":
    app.run(debug=True)
