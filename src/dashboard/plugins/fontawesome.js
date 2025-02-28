import { library } from "@fortawesome/fontawesome-svg-core";
import { faUser,faSearch,faTimes, faBars,faTrash } from "@fortawesome/free-solid-svg-icons"; // Import icons
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faSearch, faUser,faTimes,faTrash, faBars);

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.component("FontAwesomeIcon", FontAwesomeIcon);
});
