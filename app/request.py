from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

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