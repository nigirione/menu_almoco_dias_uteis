import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "varied.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "B1","title": "Maki Frito","pieces": "4 Peças" , "image": "resources/img/B1.png"},
  {"number": "B2","title": "Califórnia Frito","pieces": "4 Peças" , "image": "resources/img/B2.png"},
  {"number": "B3","title": "Califórnia c/ cebola","pieces": "4 Peças" , "image": "resources/img/B3.png"},
  {"number": "B4","title": "Califórnia de Delícias c/ cebola","pieces": "4 Peças" , "image": "resources/img/B4.png"},
  {"number": "B5","title": "Dragão","pieces": "8 Peças" , "image": "resources/img/B5.png"},
  {"number": "B6","title": "Gunkan de Ovas","pieces": "2 Peças" , "image": "resources/img/B6.png"},
  {"number": "B7","title": "Tofu c/ Salmão","pieces": "2 Peças" , "image": "resources/img/B7.png"},
  {"number": "B8","title": "Salmão e Atum","pieces": "4 Peças" , "image": "resources/img/B8.png"},
  {"number": "B9","title": "Atum e Salmão","pieces": "4 Peças" , "image": "resources/img/B9.png"},
  {"number": "B10","title": "Delícias e Panado de Gambas","pieces": "4 Peças" , "image": "resources/img/B10.png"},
  {"number": "B11","title": "Morangos e Frutas","pieces": "4 Peças" , "image": "resources/img/B11.png"},
  {"number": "B12","title": "Manga e Frutas","pieces": "4 Peças" , "image": "resources/img/B12.png"},
  {"number": "B14","title": "Futomaki Misto","pieces": "2 Peças" , "image": "resources/img/B14.png"},
  {"number": "B15","title": "Delícias e Batata Frita","pieces": "4 Peças" , "image": "resources/img/B15.png"},
  {"number": "B16","title": "Panado de Frango e Cebola","pieces": "4 Peças" , "image": "resources/img/B16.png"},
  
  
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)