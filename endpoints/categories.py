from Rest_API.base.base_api import BaseApi

get_category_endpoint = "/api_testing/category/read.php"


class Categories(BaseApi):

    def get_categories(self, url, expected_status_code, expected_category):
        response = self.get_request(url + get_category_endpoint)
        self.check_status_code(response, expected_status_code)
        list = self.get_json_value_by_key(response, "$.records..name")
        actual_value = self.get_value_from_list(list, expected_category)
        assert actual_value == expected_category, f"Actual Value {actual_value} not much Expected {expected_category}"
