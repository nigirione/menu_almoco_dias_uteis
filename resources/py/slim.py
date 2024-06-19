import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "slim.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "51","title": "Salmão + Abacate","image": "resources/img/51.png"},
  {"number": "52","title": "Gambas Panadas + Abacate","image": "resources/img/52.png"},
  {"number": "53","title": "Pepino + Abacate","image": "resources/img/53.png"},

]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)