import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "wraps.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "w1","title": "Frango Panado","image": "resources/img/w1.jpg"},
  {"number": "w2","title": "Salmão","image": "resources/img/w2.jpg"},
  {"number": "w3","title": "Gambas Panadas","image": "resources/img/w3.jpg"},

]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)