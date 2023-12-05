from config import API_KEY

import requests as rq


def get_auth_request_url(url: str) -> str:
    """
    Adds the API_KEY to the url.
    :param url: url to the API
    :return: url with the API_KEY
    """
    if API_KEY is None:
        raise Exception('API_KEY was not provided')
    return url + '?apiKey=' + API_KEY


class RecipiesSearch:
    """
    RecipiesSearch class is used to search for recipies using the Spoonacular API.
    """

    BASE_SEARCH_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    def __init__(self, initial_url=BASE_SEARCH_URL):
        """
        Constructor for the RecipiesSearch class.
        :param initial_url: initial url to the API
        :raises Exception: if API_KEY is not provided
        """
        self.url = initial_url
        self.url = get_auth_request_url(self.url)

    def exec_query(self, query: str) -> rq.Response:
        """
        Executes a query to the API.
        :param query: query string
        :return: response from the API
        """
        response = rq.get(self.url + '&query=' + query)
        return response


class RecipiesInfo:
    """
    RecipiesSearch class is used to search for recipies using the Spoonacular API.
    """

    BASE_SEARCH_URL = 'https://api.spoonacular.com/recipes/'

    def __init__(self, initial_url=BASE_SEARCH_URL):
        """
        Constructor for the RecipiesSearch class.
        :param initial_url: initial url to the API
        :raises Exception: if API_KEY is not provided
        """
        self.url = initial_url

    def exec_query(self, id: str) -> rq.Response:
        """
        Executes a query to the API.
        :param id: Recipe ID
        :return: response from the API
        """
        response = rq.get(get_auth_request_url(self.url + id + '/information'))
        return response
