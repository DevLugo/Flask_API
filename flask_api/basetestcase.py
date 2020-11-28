from flask_testing import TestCase
from application import create_test_app, db

class BaseTestCase(TestCase):
    def create_app(self):
        # pass in test configuration
        return create_test_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()