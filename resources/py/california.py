import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "california.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "27","title": "Salmão","image": "resources/img/27.png"},
  {"number": "28","title": "Atum","image": "resources/img/28.png"},
  {"number": "29","title": "Gambas","image": "resources/img/29.png"},
  {"number": "30","title": "Gambas Panadas","image": "resources/img/30.png"},
  {"number": "31","title": "Pepino","image": "resources/img/31.png"},
  {"number": "32","title": "Morangos","image": "resources/img/32.png"},
  {"number": "33","title": "Frango Panado","image": "resources/img/33.png"},
  {"number": "34","title": "Manga","image": "resources/img/34.png"},
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)