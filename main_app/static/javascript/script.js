document.addEventListener("DOMContentLoaded", function () {
  const filterBtns = document.querySelectorAll(
    ".index-nav-category-detail-btn"
  );
  const indexHeader = document.querySelector(".index-header-title");
  const indexHeaderDes = document.querySelector(".index-header-description");

  filterBtns.forEach(function (button) {
    button.addEventListener("click", function () {
      const filterValue = this.dataset.filter;
      updateHeader(filterValue);
      filterProducts(filterValue);
    });
  });

  function filterProducts(filterValue) {
    const productCards = document.querySelectorAll(".index-product");

    productCards.forEach(function (card) {
      const productOrigin = card.dataset.origin;
      const productRoast = card.dataset.roast;

      const originMatch =
        productOrigin === "All" || filterValue === productOrigin;
      const roastMatch = productRoast === "All" || filterValue === productRoast;

      if (originMatch) {
        card.style.display = "block";
      } else if (roastMatch) {
        card.style.display = "block";
      } else if (filterValue === "All") {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  }

  function updateHeader(filterValue) {
    if (filterValue === "All") {
      indexHeader.innerText = "All Coffee";
      indexHeaderDes.innerText = "Browse all Karma coffee";
      console.log("Updating header with filterValue:", filterValue);
    } else if (filterValue === "Colombia") {
      indexHeader.innerText = "Colombia";
      indexHeaderDes.innerText =
        "Colombian coffee boasts a rich and balanced flavor profile and a journey into intricate flavors and scents";
    } else if (filterValue === "Ethiopia") {
      indexHeader.innerText = "Ethiopia";
      indexHeaderDes.innerText =
        "Ethiopian coffee offers exotic and aromatic elegance from coffee's birthplace";
    } else if (filterValue === "Brazil") {
      indexHeader.innerText = "Brazil";
      indexHeaderDes.innerText =
        "A mellow cup of coffee from Brazil invites you to the essence of South American warmth";
    } else if (filterValue === "India") {
      indexHeader.innerText = "India";
      indexHeaderDes.innerText =
        "Indian coffee delights the palate with its spicy and vibrant, a sensory journey through India's flavors";
    } else if (filterValue === "D") {
      indexHeader.innerText = "Dark Roast";
      indexHeaderDes.innerText =
        "A bold and intense cup, with deep, smoky flavors and a robust character";
    } else if (filterValue === "M") {
      indexHeader.innerText = "Medium Roast";
      indexHeaderDes.innerText =
        "A harmonious balance of flavor and aroma, showcasing the coffee's nuanced qualities";
    } else if (filterValue === "L") {
      indexHeader.innerText = "Light Roast";
      indexHeaderDes.innerText =
        "Delicate and bright, this roast preserves the coffee's vibrant acidity and intricate notes";
    }
  }
});


// ADDING SCRIPT FOR THE CARET SYMBOLS TO ANIMATE

document.addEventListener('show.bs.collapse', function(event) {
  let collapseContent = event.target;
  let button = collapseContent.previousElementSibling;
  let icon = button.querySelector('i');
  icon.classList.replace('bi-caret-right-fill', 'bi-caret-down-fill');
});

document.addEventListener('hide.bs.collapse', function(event) {
  let collapseContent = event.target;
  let button = collapseContent.previousElementSibling;
  let icon = button.querySelector('i');
  icon.classList.replace('bi-caret-down-fill', 'bi-caret-right-fill');
});
