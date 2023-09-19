const mobileNavbar = document.getElementById("mobile-nav");
const hamburgerToggler = document.getElementById("hamburger-toggler");
const addNoteButton = document.getElementById("add-note-button");
const cancelAddNoteButton = document.getElementById("cancle-add-note");
const mobileNoteForm = document.getElementById("mobile-note-form");
const createNoteButton = document.getElementById("create-note");

const threeDotsNavTogglers = document.querySelectorAll(".three-dots-toggler");
const threeDotsNav = document.querySelectorAll(".three-dots-nav");

threeDotsNavTogglers.forEach((threeDotsNavToggler, index) => {
  threeDotsNavToggler.addEventListener("click", () => {
    threeDotsNav[index].classList.toggle("flex");
    threeDotsNav[index].classList.toggle("hidden");
  });
});

function toggleAddNoteForm() {
  mobileNoteForm.classList.toggle("hidden");
}

function triggerDeleteAccount(userId) {
  if (window.confirm("Sure to delete account")) {
    fetch("/delete_account", {
      method: "DELETE",
      body: JSON.stringify({ userId: userId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
}

function deleteNote(noteId) {
  fetch("/home", {
    method: "DELETE",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
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
