import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

import App from "@/App.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/questions",
    name: "Questions",
    component: App,
  },
  {
    path: "/questions/ask",
    name: "Ask",
    component: () => import(/* webpackChunkName: "about" */ "@/App.vue"),
  },
  {
    path: "/questions/:qId",
    name: "Question",

    component: () => import(/* webpackChunkName: "about" */ "@/App.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
