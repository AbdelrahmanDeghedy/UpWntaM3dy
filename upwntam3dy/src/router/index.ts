import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import { store } from '@/store/index';

import App from "@/App.vue";

const routes: Array<RouteRecordRaw> = [
    {
      path: "/user_id/questions",
      name: "Questions",
      component: App,
      meta: { requiresAuth: true }
    },
    {
      path: "/user_id/questions/ask",
      name: "Ask",
      component: () => import("@/App.vue"),
      meta: { requiresAuth: true }
    },
    {
      path: "/user_id/questions/:qId",
      name: "Question",
      component: () => import("@/App.vue"),
      meta: { requiresAuth: true }
    },
    {
      path: "/user_id/profile",
      name: "Profile",
      component: () => import("@/App.vue"),
      meta: { requiresAuth: true }
    },
    {
      path: "/signin",
      name: "Signin",

      component: () => import("@/App.vue"),
    },
    {
      path: "/signup",
      name: "Signup",

      component: () => import("@/App.vue"),
    },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

const validateAuthedUser = (to, from, next) => {
  if (!to.meta.requiresAuth) return next();

  if (!to.params.user_id) {
    // redirect to sign in page
    router.push({ name: "Signin" });
    store.commit("setPageMode", "auth");
    return next()
  }

}

router.beforeEach(validateAuthedUser);

export default router;
