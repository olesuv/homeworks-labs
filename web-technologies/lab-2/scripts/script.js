document.addEventListener("DOMContentLoaded", function () {
  const mainActionButton = document.getElementById("main-action");
  const carsSection = document.getElementById("cars");

  mainActionButton.addEventListener("click", function () {
    carsSection.scrollIntoView({ behavior: "smooth" });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const mainActionButton = document.getElementById("main-action");
  const carsSection = document.getElementById("cars");
  const priceSection = document.getElementById("price");

  mainActionButton.addEventListener("click", function () {
    carsSection.scrollIntoView({ behavior: "smooth" });
  });

  const reserveButtons = document.querySelectorAll(".car-button");

  reserveButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      priceSection.scrollIntoView({ behavior: "smooth" });
    });
  });
});
