/** @type {import('tailwindcss').Config} */
module.exports = {
  // Scan HTML-templates, Python (voor inline templates), en je eigen JS/TS in static
  content: [
    "./templates/**/*.html",
    "./app/**/*.html",
    "./**/*.py",
    "./static/js/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      // Zet hier alvast een schaalbare basis klaar (fonts, kleuren kun je later invullen)
      // fontFamily: { sans: ["Inter", "ui-sans-serif", "system-ui"] },
      // colors: { brand: { DEFAULT: "#3b82f6" } },
    },
  },
  plugins: [
    // Later kun je hier bijvoorbeeld first-party plugins toevoegen
    // require('@tailwindcss/forms'),
    // require('@tailwindcss/typography'),
  ],
  // Safelist is handig als je dynamische classnames gaat genereren vanuit Python (optioneel)
  // safelist: ["bg-red-500", /^col-span-/],
};
