import requests


class BaseTestModel:

    @staticmethod
    def get(url, **kwargs):
        return requests.request(method='GET', url=url, **kwargs)

    @staticmethod
    def post(url, json_data, **kwargs):
        return requests.request(method='POST', url=url, json=json_data, **kwargs)

    @staticmethod
    def put(url, json_data, **kwargs):
        return requests.request(method='PUT', url=url, json=json_data, **kwargs)

    @staticmethod
    def delete(url, json_data=None, **kwargs):
        return requests.request(method='DELETE', url=url, json=json_data, **kwargs)
