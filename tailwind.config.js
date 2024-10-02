/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './dapp/templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        mitr: ['Mitr', 'sans-serif'],
        itim: ['Itim', 'cursive'],
        sarabun: ['Sarabun', 'sans-serif'],
        chakrapetch: ['Chakra Petch', 'sans-serif'],
        prompt: ['Prompt', 'sans-serif'],
        kanit: ['Kanit', 'sans-serif'],
      }
    },
  },
  plugins: [],
}

