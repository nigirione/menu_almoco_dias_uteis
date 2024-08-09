import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "new_dishes.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "80","title": "Califórnia de Gambas Panadas c/ Molho de Frutas","pieces": "4 Peças" ,"image": "resources/img/80.jpg"},
  {"number": "81","title": "Maki Frito c/ Molho de Frutas","pieces": "4 Peças" ,"image": "resources/img/81.jpg"},
  {"number": "82","title": "Califórnia Frito c/ Molho de Frutas","pieces": "4 Peças" ,"image": "resources/img/82.jpg"},
  {"number": "84","title": "Califórnia de Manga c/ Molho de Frutas","pieces": "4 Peças" ,"image": "resources/img/84.jpg"},
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)