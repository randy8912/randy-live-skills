// Scroll reveal via IntersectionObserver
(function () {
  const els = document.querySelectorAll(".reveal");
  console.debug("[ui] reveal elements:", els.length);
  if (!els.length) return;

  const mql = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (mql.matches) {
    els.forEach((el) => el.classList.add("reveal-in"));
    return;
  }

  const io = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("reveal-in");
          obs.unobserve(entry.target);
        }
      });
    },
    { rootMargin: "0px 0px -10% 0px", threshold: 0.1 }
  );

  els.forEach((el, i) => {
    el.style.transitionDelay = Math.min(i * 0.06, 0.3) + "s";
    io.observe(el);
  });
})();

// Cursor spotlight (radial-gradient die de muis volgt)
(function () {
  const overlay = document.querySelector("[data-spotlight]");
  if (!overlay) return;
  console.debug("[ui] spotlight enabled");

  const mql = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (mql.matches) {
    overlay.style.display = "none";
    return;
  }

  let x = 0,
    y = 0;
  let raf = null;

  function update() {
    overlay.style.background = `radial-gradient(220px 220px at ${x}px ${y}px, rgba(255,255,255,0.28), transparent 60%)`;
    raf = null;
  }

  window.addEventListener(
    "mousemove",
    (e) => {
      x = e.clientX;
      y = e.clientY;
      if (!raf) raf = requestAnimationFrame(update);
    },
    { passive: true }
  );

  // subtiele fade-in
  overlay.style.opacity = "0";
  requestAnimationFrame(() => {
    overlay.style.transition = "opacity .35s ease";
    overlay.style.opacity = "1";
  });
})();

// Theme toggle (dark mode via HTML class)
(function () {
  const root = document.documentElement;
  const TOGGLE_ATTR = "[data-theme-toggle]";
  const btn = document.querySelector(TOGGLE_ATTR);
  if (!btn) return;

  // Initial state from localStorage
  const saved = localStorage.getItem("theme");
  if (saved === "dark") root.classList.add("dark");

  btn.addEventListener("click", () => {
    const isDark = root.classList.toggle("dark");
    localStorage.setItem("theme", isDark ? "dark" : "light");
  });
})();
