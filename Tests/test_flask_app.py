import unittest
import app
import json
from flask import Flask

app = Flask(__name__)

class TestGetActivitiesFromSubCategory(unittest.TestCase):

    def test_get_activities_from_subcategory(self):
        '''tests the get_activities_from_subcategory function'''
        response = app.get('/Personal_Care_Activities/Sleeping', follow_redirects=True)
        self.assertEqual(['Sleeping','Sleeplessness'], response.data)
        response2 = app.get('/Household_Activities/Housework', follow_redirects=True)
        self.assertEqual(["Interior cleaning","Laundry"], response2.data)

