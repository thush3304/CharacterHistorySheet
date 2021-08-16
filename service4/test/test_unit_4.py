from flask import url_for
from flask_testing import TestCase

from service4.app import app, chara

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_dama(self):

        for era in chara['eras']:
            for prof in chara['proff']:
                result = {'eras':era, 'proff': prof}
                response = self.client.post(url_for('post_order'), json=result)
                self.assert200(response)
                charav = chara['eras'][era] + chara['proff'][prof]
                self.assertEqual(response.json, charav)