import unittest
import os
from  . import app

class TestConfig(unittest.TestCase):
    def test_config_loading(self):
        assert app.config['DEBUG'] is False
        # assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////'+ os.path.join(BASE_DIR, 'feature.db')

    def test_main_page(self):
        app.testing=True
        self.app=app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)