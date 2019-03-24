import unittest
import os
from  . import app

# run with python -m unittest

class TestConfig(unittest.TestCase):
    def test_config_loading(self):
        assert app.config['DEBUG'] is False
        # assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////'+ os.path.join(BASE_DIR, 'feature.db')

    def test_main_page(self):
        app.testing=True
        self.app=app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_feature_page(self):
        app.testing = True
        self.app = app.test_client()
        response = self.app.get('/feature', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        app.testing = True
        self.app = app.test_client()
        response = self.app.get('/wrong/url')
        self.assertEqual(response.status_code, 404)

    def write_task(self):
        app.testing = True
        self.app = app.test_client()
        response = self.app.post(
            '/feature',
            data=json.dumps({'title': 'Task 1', 'description':'this is the description for task 1',
                             'client':'Client A',
                             'priority':5,
                             'date':'2019-05-23',
                             'area':['Policies', 'Billing']
                             }))
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(url)