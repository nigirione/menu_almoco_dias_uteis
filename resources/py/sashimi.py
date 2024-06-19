import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "sashimi.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "10","title": "Atum","image": "resources/img/10.png"},
  {"number": "11","title": "Robalo","image": "resources/img/11.png"},
  {"number": "12","title": "Salmão","image": "resources/img/12.png"},
  {"number": "14","title": "Sashimi Misto","pieces": "15 Peças","image": "resources/img/14.png"}
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)