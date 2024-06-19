import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "donburi.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "N40","title": "Donburi de Salmão Defumado c/ Molho","image": "resources/img/N40.jpg"},
  {"number": "N41","title": "Donburi de Gambas Panadas c/ Molho","image": "resources/img/N41.jpg"},
  {"number": "N42","title": "Donburi de Frango Panado c/ Molho","image": "resources/img/N42.jpg"},
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)