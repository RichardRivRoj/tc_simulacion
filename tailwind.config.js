/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/*.py',
    './**/*.html',  // Ajusta la ruta para que incluya tus archivos HTML generados
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#2563eb',
        'primary-variant': '#1b49a6',
        'secondary': '#ff5757',
        'accent': '#121063',
      },
    },
  },
};

