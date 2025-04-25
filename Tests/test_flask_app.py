import app
import unittest

class TestFlaskApp(unittest.TestCase):
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b'hello, this is the homepage', response.data)

class TestGetActivitiesFromSubCategory(unittest.TestCase):
    def get_activities_from_subcategory(self):
        self.app = app.test_client()
        response = self.app.get('/Personal_Care_Activities/Sleeping', follow_redirects=True)
        self.assertEqual(["Sleeping","Sleeplessness"], response.data)