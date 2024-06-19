import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "yakitori.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "A11","title": "Espetadas de Gambas","image": "resources/img/A11.png"},
  {"number": "A12","title": "Espetadas de Frango","image": "resources/img/A12.png"},
  {"number": "A13","title": "Espetadas de Vitela","image": "resources/img/A13.png"},
  {"number": "A14","title": "Espetadas de Cogumelos Pretos","image": "resources/img/A14.png"},
  {"number": "A15","title": "Espetadas de Cogumelos Brancos","image": "resources/img/A15.png"},
  {"number": "A16","title": "Espetadas de Lulas","image": "resources/img/A16.png"},
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)