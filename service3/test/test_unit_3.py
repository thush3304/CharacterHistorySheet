from flask import url_for
from flask_testing import TestCase
from service3.app import app, prof

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_get_profession(self):

        for i in range(20):
            response = self.client.get(url_for('get_prof'))
            self.assert200(response)
            self.assertIn(response.data.decode(), prof)