
// === Animation on scroll using IntersectionObserver ===
document.addEventListener('DOMContentLoaded', function () {
  const fadeIns = document.querySelectorAll('.fade-in, .fade-up');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target); // stop observing once visible (perf boost)
      }
    });
  }, { threshold: 0.1 });

  fadeIns.forEach(el => observer.observe(el));
});

// === Shrink Header on Scroll ===
window.addEventListener("scroll", function () {
  const header = document.getElementById("main-header");
  if (!header) return;

  header.classList.toggle("shrunk", window.scrollY > 50);
});

// === Modal Swipe + Open/Close Handling ===
let startY = 0;

function openModal(id) {
  const modal = document.getElementById(id);
  if (!modal) return;

  modal.style.display = "block";
  modal.addEventListener("touchstart", handleTouchStart, { passive: true });
  modal.addEventListener("touchend", (e) => handleTouchEnd(e, id), { passive: true });
}

function closeModal(id) {
  const modal = document.getElementById(id);
  if (!modal) return;

  modal.style.display = "none";
  modal.removeEventListener("touchstart", handleTouchStart);
  modal.removeEventListener("touchend", handleTouchEnd);
}

function handleTouchStart(event) {
  startY = event.changedTouches[0].clientY;
}

function handleTouchEnd(event, id) {
  const endY = event.changedTouches[0].clientY;
  const deltaY = endY - startY;

  if (deltaY > 100) {
    closeModal(id); // Swipe down closes modal
  }
}

// === Close Modal on Outside Click (Desktop) ===
window.addEventListener('click', function (event) {
  document.querySelectorAll('.modal').forEach(modal => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });
});


