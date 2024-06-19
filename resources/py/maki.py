import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "maki.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "16","title": "Salmão","image": "resources/img/16.png"},
  {"number": "17","title": "Atum","image": "resources/img/17.png"},
  {"number": "18","title": "Gambas","image": "resources/img/18.png"},
  {"number": "19","title": "Enguia","image": "resources/img/19.png"},
  {"number": "20","title": "Gambas Panadas","image": "resources/img/20.png"},
  {"number": "21","title": "Pepino","image": "resources/img/21.png"},
  {"number": "N21","title": "Manga","image": "resources/img/N21.jpg"}

]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)