import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "grilled.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "A1","title": "Gambas","image": "resources/img/A1.png"},
  {"number": "A2","title": "Vaca","image": "resources/img/A2.png"},
  {"number": "A3","title": "Frango","image": "resources/img/A3.png"},
  {"number": "A4","title": "Salmão","image": "resources/img/A4.png"},
  {"number": "A5","title": "Atum","image": "resources/img/A5.png"},
  {"number": "A7","title": "Porco","image": "resources/img/A7.png"},
  {"number": "A8","title": "Curgete","image": "resources/img/A8.png"}
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)