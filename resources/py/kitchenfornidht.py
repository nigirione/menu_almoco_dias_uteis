import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "kitchen.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "601","title": "Gambas c/ piri-piri","image": "resources/img/601.png"},
  {"number": "602","title": "Gambas c/ Bambu e Cogumelos","image": "resources/img/602.png"},
  {"number": "603","title": "Gambas c/ Caril","image": "resources/img/603.png"},
  {"number": "604","title": "Vaca c/ Bambu e Cogumelos","image": "resources/img/604.png"},
  {"number": "605","title": "Vaca c/ Molho de Ostras","image": "resources/img/605.png"},
  {"number": "606","title": "Porco c/ Cogumelos","image": "resources/img/606.png"},
  {"number": "607","title": "Porco Agridoce","image": "resources/img/607.png"},
  {"number": "608","title": "Frango c/ Amêndoas","image": "resources/img/608.png"},
  {"number": "609","title": "Frango c/ piri-piri","image": "resources/img/609.png"},
  {"number": "610","title": "Pato Assado c/ Molho","image": "resources/img/610.png"},
  {"number": "611","title": "Amêijoas","image": "resources/img/611.png"},
  {"number": "612","title": "Frango c/ Caril","image": "resources/img/612.png"},
  {"number": "613","title": "Vitela c/ Caril","image": "resources/img/613.png"},
  {"number": "614","title": "Frango c/ Molho","image": "resources/img/614.png"},
  {"number": "615","title": "Arroz Chao Chao","image": "resources/img/615.png"},
  {"number": "616","title": "Udon Frito c/ Gambas","image": "resources/img/616.png"},
  {"number": "617","title": "Massa","image": "resources/img/617.png"},
  {"number": "618","title": "Massa de Arroz","image": "resources/img/618.png"},
  {"number": "619","title": "Raviolios","image": "resources/img/619.png"}
  

]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)