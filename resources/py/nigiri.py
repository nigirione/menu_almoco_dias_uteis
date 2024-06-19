import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "nigiri.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "1","title": "Salmão","image": "resources/img/1.png"},
  {"number": "2","title": "Atum","image": "resources/img/2.png"},
  {"number": "3","title": "Enguia","image": "resources/img/3.png"},
  {"number": "4","title": "Robalo","image": "resources/img/4.png"},
  {"number": "5","title": "Gambas","image": "resources/img/5.png"},
  {"number": "6","title": "Salmão Defumado","image": "resources/img/6.png"},
  {"number": "7","title": "Salmão + Abacate","image": "resources/img/7.png"},
  {"number": "8","title": "Polvo","image": "resources/img/8.png"},
  {"number": "9","title": "Nigiri Misto","pieces": "10 Peças" ,"image": "resources/img/9.png"}
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)