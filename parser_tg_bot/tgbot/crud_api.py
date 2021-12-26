import requests
import json

url = "http://127.0.0.1:8080/"


class CrudApi:
    @staticmethod
    def Select_range(ids: [int]):
        response = requests.post(url + "select_by_ids", json={"ids": ids})
        json_res = response.json()
        return json_res
