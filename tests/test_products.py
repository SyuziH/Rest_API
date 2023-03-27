from Rest_API.endpoints.product import Products
from Rest_API.utils.jsonmodels import product_json

products = Products()


def test_get_product(app_config):
    assert products.check_products_data_by_length(products.get_products(app_config.base_url, 200), 18)


def test_get_product_by_name(app_config):
    assert products.get_product_by_name(app_config.base_url, 200, "Apple")


def test_create_product(app_config):
    json = product_json.create_product_json("Samsung", "TV", 500, 2)
    response = products.create_product(app_config.base_url, json)
    products.check_status_code(response, 201)


def test_get_products_after_create_item(app_config):
    prod_list = products.get_products(app_config.base_url, 200)
    products.check_products_data_by_length(prod_list, 19)


def test_edit_product(app_config):
    id = products.find_id_by_name(app_config.base_url, "Polo Shirt")
    json = product_json.update_product_json(id, "Adidas Shirt", "--", 1001, 4)
    response = products.edit_product(app_config.base_url, json)
    assert products.check_status_code(response, 200)


def test_delete_product(app_config):
    id = products.find_id_by_name(app_config.base_url, "Adidas Shirt")
    json = product_json.delete_product_json(id)
    products.delete_product(app_config.base_url, json)
    prod_list = products.get_products(app_config.base_url, 200)
    products.check_products_data_by_length(prod_list, 18)
