import unittest
import app

class TestGetActivitiesFromSubCategory(unittest.TestCase):
    def get_activities_from_subcategory(self):
        self.app = app.test_client()
        response = self.app.get('/Personal_Care_Activities/Sleeping', follow_redirects=True)
        self.assertEqual(["Sleeping","Sleeplessness"], response.data)
        response2 = self.app.get('/Household_Activities/Housework', follow_redirects=True)
        self.assertEqual(["Interior cleaning","Laundry"], response2.data)

