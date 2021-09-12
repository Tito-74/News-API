from app import app
import urllib.request,json
from .models import source
from .models import article
from datetime import datetime

Source = source.Source

Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
base_article_url = app.config["ARTICLES_API_BASE_URL"]

def get_sources(source):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_news_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_news_list:
        id = source_item .get('id')
        name = source_item .get('name')
        description = source_item .get('description')
        url = source_item .get('url')
        category = source_item .get('category')
        country = source_item .get('country')

        source_object = Source(id,name,description,url,category,country)
        source_results.append(source_object)

    return source_results

def getting_articles(id):
    getting_article_url = base_article_url.format(id,api_key)
    with urllib.request.urlopen(getting_article_url) as url:
        article_news_data = url.read()
        article_news_response = json.loads(article_news_data)

        article_news_results = None
        # if article_news_response:
        #     author = article_news_response.get('author')
        #     title = article_news_response.get('title')
        #     description = article_news_response.get('description')
        #     url = article_news_response.get('url')
        #     image = article_news_response.get('urlToImage')
        #     publishedAt = article_news_response.get('publishedAt')
        #     content = article_news_response.get('content')

        #     article_object = Article(author,title,description,url,image,publishedAt,content)

        if article_news_response['articles']:
            article_news_list = article_news_response['articles']
            article_news_results = process_articles(article_news_list)


    return article_news_results

def process_articles(articles_list):
        '''
        Function that processes the articles results and transform them to a list of Objects
        Args:
            article_list: A list of dictionaries that contain sources details
        Returns:
            article_results: A list of sources objects
        '''
        articles_object = []
        for article_response in articles_list:
            # id = article_response.get('id')
            author = article_response.get('author')
            title = article_response.get('title')
            description = article_response.get('description')
            url = article_response.get('url')
            image = article_response.get('urlToImage')
            publishedAt = article_response.get('publishedAt')
            content = article_response.get('content')
            dates = datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
            date = dates.strftime('%Y-%m-%d')
            articles_result = Article( author, title, description, url, image, date, content)
            articles_object.append(articles_result)
        return articles_object
    





# def get_sources(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_source_url = base_url.format(category,api_key)

#     with urllib.request.urlopen(get_source_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)

#         source_results = None

#         if get_sources_response['sources']:
#             source_results_list = get_sources_response['sources']
#             source_results = process_results(source_results_list)


#     return source_results

# def process_results(source_news_list):
#     '''
#     Function  that processes the source result and transform them to a list of Objects

#     Args:
#         source_list: A list of dictionaries that contain source details

#     Returns :
#         source_results: A list of source objects
#     '''
#     source_results = []
#     for source_item in source_news_list:
#         id = source_item .get('id')
#         name = source_item .get('name')
#         description = source_item .get('description')
#         url = source_item .get('url')
#         category = source_item .get('category')
#         country = source_item .get('country')

#         source_object = Source(id,name,description,url,category,country)
#         source_results.append(source_object)

#     return source_results

