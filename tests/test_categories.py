from Rest_API.endpoints.categories import Categories


def test_get_category(app_config):
    category = Categories()
    category.get_categories(app_config.base_url, 200, "Supplements")