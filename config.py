class Config:
    def __init__(self, env):
        self.base_url = {
            'local': 'https://localhost',

        }[env]

        self.app_port = {
            'local': ':80'
        }[env]
