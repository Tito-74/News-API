from flask import render_template
from . import main
from ..requests import get_sources, getting_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    major_source = get_sources('source')
    title = 'Home - Welcome to News Website Online'
    return render_template('index.html', title=title, major_source= major_source)
  


@main.route('/sources/<id>')
def article(id):

    '''
    View news page function that returns the news details page and its data
    '''
    articles_news = getting_articles(id)
    
    return render_template('article.html',id = id, articles = articles_news )