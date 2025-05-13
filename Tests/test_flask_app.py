import unittest
from app import app
from flask import Flask

class TestGetActivitiesFromSubCategory(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_activities_from_subcategory(self):
        '''tests the get_activities_from_subcategory function'''
        response = self.client.get('/Personal_Care_Activities/Sleeping', follow_redirects=True)
        self.assertEqual("Sleeping\nSleeplessness", response.data.decode('utf-8'))
        response2 = self.client.get('/Household_Activities/Housework', follow_redirects=True)
        self.assertEqual("Interior cleaning\nLaundry", response2.data.decode('utf-8'))

    def test_invalid_subcategory(self):
        '''tests the get_activities_from_subcategory function with an invalid subcategory'''
        response = self.client.get('/Personal_Care_Activities/Invalid_Subcategory', follow_redirects=True)
        self.assertEqual("Invalid subcategory. Please try again.", response.data.decode('utf-8'))
    
    def test_invalid_category(self):
        '''tests the get_activities_from_subcategory function with an invalid category'''
        response = self.client.get('/Invalid_Category/Sleeping', follow_redirects=True)
        self.assertEqual("Invalid subcategory. Please try again.", response.data.decode('utf-8'))
