from flask import url_for
from flask_testing import TestCase
from requests_mock import mock
from service1.application import app, db
class TestBase(TestCase):

    #Creates a standalone databse for testing
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY="TEST_SECRET_KEY",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )

        return app

    
    #Destroys previous database and creates a new one
    def setUp(self):
        
        db.drop_all()
        db.create_all()


    #Destroys database after running tests
    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_home(self):

        with mock() as m:
            m.get('http://service-2:5000/get/era', text="WWII")
            m.get('http://service-3:5000/get/accessories', text="General")
            m.post('http://service-4:5000/post/order', json="Alan Mathison Turing OBE FRS was an English mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist.")

            response = self.client.get(url_for('home'))
        
        self.assert200(response)
        self.assertIn("WWII", response.data.decode())
        self.assertIn("General", response.data.decode())
        self.assertIn("Alan Mathison Turing OBE FRS was an English mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist.", response.data.decode())