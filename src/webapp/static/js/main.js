const mobileNavbar = document.getElementById("mobile-nav");

const hamburgerToggler = document.getElementById("hamburger-toggler");

hamburgerToggler.addEventListener("click", () => {
  hamburgerToggler.classList.toggle("open-toggle");
  mobileNavbar.classList.toggle("open-mobile-nav");
});

document.addEventListener("DOMContentLoaded", function () {

  const flashDismiss = document.getElementById("flash-dismiss");
  const flashObject = document.getElementById("flash-object");

  flashDismiss.addEventListener("click", () => {
    flashObject.style.opacity = "0";
    flashObject.style.transition = "opacity 1.2s";
    setTimeout(() => {
      flashObject.style.display = "none";
    }, 3000);
  });

  setTimeout(() => {
    flashObject.style.opacity = "0";
    flashObject.style.transition = "opacity 1.2s";
    setTimeout(() => {
      flashObject.style.display = "none";
    }, 3000);
  }, 4000);
  document.addEventListener("DOMContentLoaded", function () {
  });
  
});