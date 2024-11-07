/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    "./views/**/*.{html,py}", // Archivos HTML en la carpeta de templates
    "./layouts/**/*.py",            // Si tienes una carpeta src con HTML
    "./views/**/*.py",          // Ajusta según la estructura del proyecto
    "./components/**/*.py",     // Incluye componentes en HTML si existen
    "./**/*.py"                   // Archivos Python donde puedes tener clases de Tailwind en strings  // Ajusta la ruta para que incluya tus archivos HTML generados
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

