// Animate risk bar on load
document.addEventListener("DOMContentLoaded", () => {
  const fill = document.querySelector(".risk-bar-fill");
  if (fill) {
    const width = fill.style.width;
    fill.style.width = "0%";
    requestAnimationFrame(() => {
      setTimeout(() => { fill.style.width = width; }, 100);
    });
  }

  // Input focus glow effect
  document.querySelectorAll("input").forEach(input => {
    input.addEventListener("focus", () => {
      input.closest(".form-group").classList.add("focused");
    });
    input.addEventListener("blur", () => {
      input.closest(".form-group").classList.remove("focused");
    });
  });

  // Button loading state
  const form = document.querySelector(".form");
  const btn = document.querySelector(".btn-predict");
  if (form && btn) {
    form.addEventListener("submit", () => {
      btn.querySelector(".btn-text").textContent = "Analyzing...";
      btn.querySelector(".btn-icon").textContent = "⏳";
      btn.disabled = true;
      btn.style.opacity = "0.8";
    });
  }

  // Scroll to result if present
  const result = document.querySelector(".result-section");
  if (result) {
    setTimeout(() => {
      result.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }, 400);
  }
});
