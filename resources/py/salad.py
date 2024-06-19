import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "salad.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "V5","title": "Salada","image": "resources/img/V5.jpg"},
  {"number": "V6","title": "Salada c/ Frango Panado","image": "resources/img/V6.jpg"},
  {"number": "V7","title": "Salada c/ Gambas Panadas","image": "resources/img/V7.jpg"}
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)