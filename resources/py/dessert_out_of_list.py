import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "dessert_out_of_list.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "705","title": "Banana Frita","price": "2.30€" , "image": "resources/img/705.png"},
  {"number": "706","title": "Gelado Frito","price": "2.30€" ,"image": "resources/img/706.png"},
  {"number": "707","title": "Gelado na Chapa","price": "2.30€" ,"image": "resources/img/707.png"},
  {"number": "708","title": "Lichia","price": "2.30€" ,"image": "resources/img/708.jpg"},
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)