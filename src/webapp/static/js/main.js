const mobileNavbar = document.getElementById("mobile-nav");
const hamburgerToggler = document.getElementById("hamburger-toggler");
const addNoteButton = document.getElementById("add-note-button");
const cancelAddNoteButton = document.getElementById("cancle-add-note");
const mobileNoteForm = document.getElementById("mobile-note-form");
const createNoteButton = document.getElementById("create-note");


const deleteNoteButton = document.querySelectorAll(".delete-note-button");

const threeDotsNavTogglers = document.querySelectorAll(".three-dots-toggler");
const threeDotsNav = document.querySelectorAll(".three-dots-nav");

for (let i = 0; i < threeDotsNavTogglers.length; i++) {
  threeDotsNavTogglers[i].addEventListener("click", () => {
    threeDotsNav[i].classList.toggle("hidden");
    threeDotsNav[i].classList.toggle("flex");
  });
}

function toggleAddNoteForm() {
  mobileNoteForm.classList.toggle("hidden");
}

function deleteNote(noteId) {
  console.log("reached");
  fetch("/home", {
    method: "DELETE",
    body: JSON.stringify({ noteId: noteId})
  }).then ((_res) => {
    window.location.href = "/home";
  });
}

hamburgerToggler.addEventListener("click", () => {
  hamburgerToggler.classList.toggle("open-toggle");
  mobileNavbar.classList.toggle("open-mobile-nav");
});

createNoteButton.addEventListener("click", toggleAddNoteForm);

addNoteButton.addEventListener("click", toggleAddNoteForm);

cancelAddNoteButton.addEventListener("click", toggleAddNoteForm);

deleteNoteButton.addEventListener("click", deleteNote);

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
    }, 2000);
  }, 3000);
});