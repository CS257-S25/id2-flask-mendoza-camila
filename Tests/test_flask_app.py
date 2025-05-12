import unittest
import app
import json
from flask import Flask

app = Flask(__name__)

class TestGetActivitiesFromSubCategory(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_activities_from_subcategory(self):
        '''tests the get_activities_from_subcategory function'''
        response = self.client.get('/Personal_Care_Activities/Sleeping', follow_redirects=True)
        self.assertEqual(['Sleeping','Sleeplessness'], json.loads(response.data))
        response2 = self.client.get('/Household_Activities/Housework', follow_redirects=True)
        self.assertEqual(["Interior cleaning","Laundry"], json.loads(response.data)

