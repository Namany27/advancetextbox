export default {
  plugins: [],
  svelte: {
    preprocess: [],
  },
  server:{
    host: true,
    allowedHost:"all"
  },
  build: {
    target: "modules",
  },
};