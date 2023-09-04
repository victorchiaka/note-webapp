const mobileNavbar = document.getElementById("mobile-nav");

const hamburgerToggler = document.getElementById("hamburger-toggler");

hamburgerToggler.addEventListener("click", () => {
  hamburgerToggler.classList.toggle("open-toggle");
  mobileNavbar.classList.toggle("open-mobile-nav");
});
