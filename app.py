from flask import Flask
import csv
from ProductionCode.helper import get_subcategory_from_data

app = Flask(__name__)

@app.route('/')
def homepage():
    return "To see the list of activities, please add to the end of this URL the /category/subcategory." \
    " For example: /Personal_Care_Activities/Sleeping OR /Household_Activities/Housework"

def load_activities_data():
    '''Purpose: loads the data for the activities file
    Args: None
    Returns: a list of activities'''
    data = []
    with open('Data/activities_data.csv', newline='') as f:
         reader = csv.reader(f)
         for row in reader:
             data.append(row)
    return data

@app.route('/<category>/<subcategory>', strict_slashes=False)
def get_activities_from_subcategory(category, subcategory): 
    '''Purpose: gets the list of activities from the selected subcategory
    Args: category: the category to get the activities for
          subcategory: the subcategory to get the activities for
    Returns: a list of activities in the subcategory'''
    data = load_activities_data()
    subcategory = get_subcategory_from_data(subcategory)

    subcategory_ID = subcategory
    if subcategory_ID is None:
        return "Invalid subcategory. Please try again."
    # the array will store the activities belonging to the subcategory
    activities = []
    for row in data:
        # checks to see if the first five numbers (including the 'T') of the current row's ID, match the ID of the subcategory
        if (row[0][:5] == subcategory_ID):
            # if it does, the activity is added to the array
            activities.append(row[1])
    return '\n'.join(activities)


@app.errorhandler(404)
def page_not_found(e):
    return "Page not found. Please check the URL."

@app.errorhandler(500)
def python_bug(e):
    return "An internal error occurred. Please try again later."
    
if __name__ == '__main__':
    app.run()
