import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "big_roles.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "41","title": "Califórnia de Salmão,Delícias do Mar, Abacate, Ovas de Salmão","image": "resources/img/41.png"},
  {"number": "42","title": "Maki Frito de Salmão e Alho francês","image": "resources/img/42.png"},
  {"number": "43","title": "Maki de Gambas Panadas","image": "resources/img/43.png"},
  {"number": "44","title": "Rolo Ameixa Salmão e Coentros","image": "resources/img/44.png"},
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)