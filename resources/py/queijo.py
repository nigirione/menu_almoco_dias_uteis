import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "queijo.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "22","title": "Queijo","image": "resources/img/22.png"},
  {"number": "23","title": "Queijo + Abacate","image": "resources/img/23.png"}

]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)