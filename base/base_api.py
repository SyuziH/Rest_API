import json
import jsonpath as jsn
import requests


class BaseApi:

    def get_request(self, url, params=None, headers=None):
        """
        Use this method to send the get request
        :param url:  The request URL
        :param params: The request params (OPTIONAL)
        :param headers: The request headers (OPTIONAL)
        :return: response
        """
        response = requests.get(url, params=params, headers=headers, verify=False)
        return response

    def post_request(self, url, json_data, headers=None):
        """
        Use this method to send the POST request
        :param url:
        :param json_data:
        :param headers:
        :return:
        """
        response = requests.post(url, json_data, headers=headers, verify=False)
        return response

    def put_request(self, url, json_data, headers=None):
        """
        Use this method to send the PUT request
        :param url:
        :param json_data:
        :param headers:
        :return:
        """
        response = requests.put(url, json_data, headers=headers, verify=False)
        return response

    def delete_request(self, url, json_data, headers=None):
        """
        Use this method to send the DELETE request
        :param url:
        :param json_data:
        :param headers:
        :return:
        """
        response = requests.delete(url, json=json_data, headers=headers, verify=False)
        return response

    def check_status_code(self, response, expected_status_code):
        """
        Use this method to check the response status code
        :param response:
        :param expected_status_code:
        :return:
        """
        assert response.status_code == expected_status_code

    def get_json_value_by_key(self, response, key):
        """

        :param response:
        :param key:
        :return:
        """
        json_data = json.loads(response.text)
        values_in_json = jsn.jsonpath(json_data, key)
        return values_in_json

    def get_value_from_list(self, values_list, expected_value):
        """

        :param values_list:
        :param expected_value:
        :return:
        """
        for val in values_list:
            if val == expected_value:
                return val
