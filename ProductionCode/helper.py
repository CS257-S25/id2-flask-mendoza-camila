import csv

def get_subcategory_from_data(subcategory):
    '''Purpose: gets the ID of the selected subcategory
    Args: subcategory: the subcategory to get the ID for
    Returns: the ID of the subcategory'''
    data = load_subcategories_data()
    for row in data:
        # checks to see if the subcategory is in the row
        if row['Activity_Name'] == subcategory:
            # if it is, it returns the ID stored in the row
            return row['Activity_ID']
    print("No data available found for subcategory {subcategory}, try Sleeping or Grooming")
    return None

def load_subcategories_data():
    data = []
    with open("Data/subcategories_data.csv", "r", encoding='utf-8') as file:
        reader=csv.DictReader(file)
        data = list(reader)

        return data
    
