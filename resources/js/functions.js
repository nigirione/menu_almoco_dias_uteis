
function togglePopupMenu(id){
  document.getElementById(id).classList.toggle("active");
}

function fetchAndDisplayMenu(jsonFile, menuDivId, menuDivClass) {
  fetch(jsonFile)
    .then(response => response.json())
    .then(data => {
      const menuDiv = document.getElementById(menuDivId);
      data.forEach(item => {
        const menuItem = document.createElement('div');
        menuItem.classList.add(menuDivClass);
        if (menuDivId === 'combi' ) {
          // Check if item has 'pieces' component
          if (item.pieces) {
            menuItem.innerHTML = `
              <img src="${item.image}" alt="${item.title}">
              <h4>${item.number}</h4>
              <h6>${item.title}</h6>
              <p>${item.pieces}</p>
              <p><strong style="color: rgb(210, 55, 57); font-size: 12px;">Disponível só no Buffet à La Carte</strong></p>
            `;
          }
        }else if (menuDivId === 'nigiri' || menuDivId === 'sashimi' ) {
          // Check if item has 'pieces' component
          if (item.pieces) {
            menuItem.innerHTML = `
              <img src="${item.image}" alt="${item.title}">
              <h4>${item.number}</h4>
              <h6>${item.title}</h6>
              <p>${item.pieces}</p>
              <p><strong style="color: rgb(210, 55, 57); font-size: 12px;">Disponível só no Buffet à La Carte</strong></p>
            `;
          }else {
            // For other menu IDs
            menuItem.innerHTML = `
              <img src="${item.image}" alt="${item.title}">
              <h4>${item.number}</h4>
              <h6>${item.title}</h6>
            `;
          }
        }else if (menuDivId === 'varied' || menuDivId === 'spicy' ) {
          if (item.number === "B5" ) {
            menuItem.innerHTML = `
              <img src="${item.image}" alt="${item.title}">
              <h4>${item.number}</h4>
              <h6>${item.title}</h6>
              <p>${item.pieces}</p>
              <p><strong style="color: rgb(210, 55, 57); font-size: 12px;">Disponível só no Buffet à La Carte</strong></p>
            `;
          }else {
            // For other menu IDs
            menuItem.innerHTML = `
              <img src="${item.image}" alt="${item.title}">
              <h4>${item.number}</h4>
              <h6>${item.title}</h6>
              <p>${item.pieces}</p>
            `;
          }
        }else if (menuDivId === 'fried' ) {
          // Check if item has 'pieces' component
          if (item.pieces) {
            menuItem.innerHTML = `
              <img src="${item.image}" alt="${item.title}">
              <h4>${item.number}</h4>
              <h6>${item.title}</h6>
              <p>${item.pieces}</p>
            `;
          }else {
            // For other menu IDs
            menuItem.innerHTML = `
              <img src="${item.image}" alt="${item.title}">
              <h4>${item.number}</h4>
              <h6>${item.title}</h6>
            `;
          }
        }else if (menuDivId === 'dessert_out' ) {
          menuItem.innerHTML = `
            <img src="${item.image}" alt="${item.title}">
            <h4>${item.number}</h4>
            <h6>${item.title}</h6>
            <p>${item.price}</p>
          `;
         
        } else {
          // For other menu IDs
          menuItem.innerHTML = `
            <img src="${item.image}" alt="${item.title}">
            <h4>${item.number}</h4>
            <h6>${item.title}</h6>
          `;
        }
        menuDiv.appendChild(menuItem);
      });
    })
    .catch(error => console.error('Error fetching menu data:', error));
}


// Sample menu items for search
const menuItems = [
  { id: 'new_new', name: 'Novidades' },
  { id: 'nigiri', name: 'Nigiri' },
  { id: 'sashimi', name: 'Sashimi / Maki' },
  { id: 'queijo', name: 'Queijo / Ovo' },
  { id: 'california', name: 'Califórnia / Wraps' },
  { id: 'wraps', name: 'Rolos Grandes / Temaki' },
  { id: 'temaki', name: 'Maki Slim / Sushi Picante' },
  { id: 'slim', name: 'Combinados' },
  { id: 'combi', name: 'Diversos' },
  { id: 'kitchen_new', name: 'Cozinha' },
  { id: 'donburi', name: 'Sobremesas' },
  { id: 'drinks_new', name: 'Bebidas' },
];
// Function to toggle the dropdown menu
function toggleDropdown() {
  const dropdown = document.getElementById('dropdown');
  dropdown.classList.toggle('show');
  populateDropdown();
}
// Function to populate the dropdown with menu items
function populateDropdown() {
  const dropdown = document.getElementById('dropdown');
  dropdown.innerHTML = ''; // Clear existing items
  menuItems.forEach(item => {
      const menuItemElement = document.createElement('div');
      menuItemElement.textContent = item.name;
      menuItemElement.onclick = () => scrollToSection(item.id);
      dropdown.appendChild(menuItemElement);
  });
}
// Function to scroll to a section
function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
  document.getElementById('dropdown').classList.remove('show'); // Hide dropdown after selection
}
// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('button')) {
      const dropdown = document.getElementById('dropdown');
      if (dropdown.classList.contains('show')) {
          dropdown.classList.remove('show');
      }
  }
}