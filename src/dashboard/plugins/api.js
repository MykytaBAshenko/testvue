import ApiService from "~/utils/ApiService";

export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig();
  const api = new ApiService(config.public.apiBase); // Use API base from nuxt.config.ts

  return {
    provide: {
      api,
    },
  };
});
