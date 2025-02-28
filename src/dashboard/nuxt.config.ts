// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    app: {
        head: {
            title: 'DataCose: Code Challenge',
        },
    },
    runtimeConfig: {
        public: {
          apiBase: "http://127.0.0.1:8000", // Change this to your actual API URL
        },
    },
    ssr: false,
    devtools: { enabled: true },
    pages: true,
    modules: ['@nuxt/ui'],
    plugins: ["~/plugins/fontawesome.js"],
});
