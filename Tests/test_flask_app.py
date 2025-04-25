import unittest
import app

class TestGetActivitiesFromSubCategory(unittest.TestCase):
    def get_activities_from_subcategory(self):
        self.app = app.test_client()
        response = self.app.get('/Personal_Care_Activities/Sleeping', follow_redirects=True)
        self.assertEqual(["Sleeping","Sleeplessness"], response.data)

class TestHomepage(unittest.TestCase):
    def test_homepage(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        #self.assertEqual(response.status_code, 200)
        self.assertIn(b'To see the list of activities, please add to the end of this URL the /category/subcategory." \
    " For example: /Personal_Care_Activities/Sleeping OR /Household_Activities/Housework', response.data)