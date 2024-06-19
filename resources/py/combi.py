import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "combi.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "C1","title": "Sashimi Salmão e Atum, Nigiri de Salmão e Atum","pieces": "10 Peças" , "image": "resources/img/C1.png"},
  {"number": "C2","title": "Sashimi Salmão, Nigiri de Salmão e Atum, Califórnia de Salmão","pieces": "12 Peças" ,"image": "resources/img/C2.png"},
  
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)