const mobileNavbar = document.getElementById("mobile-nav");
const hamburgerToggler = document.getElementById("hamburger-toggler");
const threeDotsNavToggler = document.getElementById("three-dots-toggle");
const addNoteButton = document.getElementById("add-note-button");
const cancelAddNoteButton = document.getElementById("cancle-add-note");
const mobileNoteForm = document.getElementById("mobile-note-form");
const createNoteButton = document.getElementById("create-note");
const threeDotsNav = document.getElementById("three-dots-nav");

// const deleteNoteButton = document.getElementById("delete-note-button");

function toggleAddNoteForm() {
  mobileNoteForm.classList.toggle("hidden");
}

function deleteNote(noteId) {
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

threeDotsNavToggler.addEventListener("click", () => {
  threeDotsNav.classList.toggle("flex");
  threeDotsNav.classList.toggle("hidden");
});

createNoteButton.addEventListener("click", toggleAddNoteForm);

addNoteButton.addEventListener("click", toggleAddNoteForm);

cancelAddNoteButton.addEventListener("click", toggleAddNoteForm);

// deleteNoteButton.addEventListener("click", deleteNote);

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

