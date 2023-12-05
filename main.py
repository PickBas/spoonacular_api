from config import API_KEY

import requests as rq

BASE_SEARCH_URL = 'https://api.spoonacular.com/recipes/complexSearch'


class RecipiesSearch:

    def __init__(self, initial_url=BASE_SEARCH_URL):
        self.url = initial_url
        if API_KEY is None:
            raise Exception('API_KEY was not provided')
        self.url = self.__get_auth_request_url(self.url)

    def exec_query(self, query: str) -> rq.Response:
        response = rq.get(self.url + "&query=" + query)
        return response

    @staticmethod
    def __get_auth_request_url(url: str) -> str:
        return url + "?apiKey=" + API_KEY


def main():
    rs = RecipiesSearch()
    response = rs.exec_query("pasta")
    print(response.json())


if __name__ == '__main__':
    main()
