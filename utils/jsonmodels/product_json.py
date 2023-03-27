import json


def create_product_json(name, description, price, category_id):
    data = {
        "name": name,
        "description": description,
        "price": price,
        "category_id": category_id
    }

    json_data = json.dumps(data)
    return json_data


def update_product_json(id, name, description, price, category_id):
    data = {
        "id": id,
        "name": name,
        "description": description,
        "price": price,
        "category_id": category_id
    }

    json_data = json.dumps(data)
    return json_data


def delete_product_json(id):
    data = {
        "id": id
    }

    return data