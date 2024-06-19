import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "ovo.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "24","title": "Salmão + Abacate","image": "resources/img/24.png"},
  {"number": "25","title": "Atum + Abacate","image": "resources/img/25.png"},
  {"number": "26","title": "Pepino + Abacate","image": "resources/img/26.png"},

]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)