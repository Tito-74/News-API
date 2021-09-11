from flask import render_template
from app import app
from .request import get_sources

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


@app.route('/article/<article_id>')
def article(article_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('article.html',id = article_id)