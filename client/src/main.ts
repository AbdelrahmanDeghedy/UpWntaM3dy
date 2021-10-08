import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./index.css";

import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faThumbsUp, faBookmark } from "@fortawesome/free-solid-svg-icons";

import { store } from '@/store/index'


library.add(faThumbsUp, faBookmark);

export const app = createApp(App);

app.use (store);

app.component("font-awesome-icon", FontAwesomeIcon);

app.use(router)
router.replace("/signin")

app.mount("#app");

