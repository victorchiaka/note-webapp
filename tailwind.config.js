/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["src/webapp/templates/*.html", "/src/webapp/static/js/*.js"],
  theme: {
    extend: {
      keyframes: {
        loadDots: {
          "0%": { backgroundColor: "#88E7F2" },
          "0%, 100%": { transform: "scale(.2)" },
          "40%": { transform: "scale(1.0)" },
          "50%": { transform: "scale(1.0)", backgroundColor: "#0ED7F7" },
        },
      },
      animation: {
        loadDots: "loadDots 2.5s ease-in-out infinite",
      },
    },
  },
  plugins: [],
};
