const mobileNavbar = document.getElementById("mobile-nav");

const hamburgerToggler = document.getElementById("hamburger-toggler");

hamburgerToggler.addEventListener("click", () => {
  hamburgerToggler.classList.toggle("open-toggle");
  mobileNavbar.classList.toggle("open-mobile-nav");
});

const flashDismiss = document.getElementById("flash-dismiss");
flashDismiss.addEventListener("click", () => {
  const flashElement = document.getElementById("flash-object");
  flashElement.remove();
});