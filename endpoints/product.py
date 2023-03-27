import json
from Rest_API.base.base_api import BaseApi


endpoint = "/api_testing/product/"
get_products_endpoint = endpoint + "read.php"
create_product_endpoint = endpoint + "create.php"
update_product_endpoint = endpoint + "update.php"
delete_product_endpoint = endpoint + "delete.php"


class Products(BaseApi):

    def get_product_by_name(self, url, expected_status_code, product_name):
        response = self.get_request(url + get_products_endpoint)
        self.check_status_code(response, expected_status_code)
        product_names = self.get_json_value_by_key(response, "$.records..name")
        for name in product_names:
            if name == product_name:
                return True
        return False

    def get_products(self, url, expected_status_code):
        response = self.get_request(url + get_products_endpoint)
        self.check_status_code(response, expected_status_code)
        products_list = self.get_json_value_by_key(response, "$.records..id")
        return products_list

    def check_products_data_by_length(self, data, length):
        return len(data) == length

    def create_product(self, url, json):
        response = self.post_request(url + create_product_endpoint, json)
        return response

    def edit_product(self, url, json):
        response = self.put_request(url + update_product_endpoint, json)
        return response

    def find_id_by_name(self, url, product_name):
        response = self.get_request(url + get_products_endpoint)
        products_dict = json.loads(response.text)

        for item in products_dict['records']:
            print(item)
            if item['name'] == product_name:
                return item['id']


    def delete_product(self, url, json):
        response = self.delete_request(url + delete_product_endpoint, json)
        return response.text