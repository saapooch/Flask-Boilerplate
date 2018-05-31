from flask_testing import TestCase

from app.server import db, create_app
from app.server.model import User

app = create_app()


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('app.server.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        user = User(username='admin', email="ad@min.com", password="admin_user")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
