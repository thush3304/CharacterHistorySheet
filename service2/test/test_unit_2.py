from flask import url_for
from flask_testing import TestCase
from service2.app import app, era

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_getera(self):

        for i in range(20):
            response = self.client.get(url_for('get_era'))
            self.assert200(response)
            self.assertIn(response.data.decode(), era)