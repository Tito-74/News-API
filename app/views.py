from flask import render_template
from app import app
from .request import get_sources, getting_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    major_source = get_sources('source')
    title = 'Home - Welcome to News Website Online'
    return render_template('index.html', title=title, major_source= major_source)
    # major_source = get_sources('general')
    # major_source = get_sources('entertainment')
    # major_source = get_sources('business')
    # major_source = get_sources('health')
    # major_source = get_sources('sports')
    # major_source = get_sources('technology')
    # title = 'Home - Welcome to News Website Online'
    # return render_template('index.html', title=title, major_source= major_source)


@app.route('/sources/<id>')
def article(id):

    '''
    View news page function that returns the news details page and its data
    '''
    articles_news = getting_articles(id)
    
    return render_template('article.html',id = id, articles = articles_news )