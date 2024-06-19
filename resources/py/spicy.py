import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "spicy.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "71","title": "Maki Frito Picante","pieces": "4 Peças","image": "resources/img/71.png"},
  {"number": "72","title": "Califórnia de Salmão Picante","pieces": "2 Peças","image": "resources/img/72.png"},
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)