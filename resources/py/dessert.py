import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "dessert.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "701","title": "Salada de Fruta","image": "resources/img/701.png"},
  {"number": "702","title": "Pudim","image": "resources/img/702.png"},
  {"number": "703","title": "Gelatina","image": "resources/img/703.png"},
  {"number": "704","title": "Bola de Gelado","image": "resources/img/704.png"}

]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)