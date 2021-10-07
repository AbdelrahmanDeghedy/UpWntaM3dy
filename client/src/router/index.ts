import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import { store } from '@/store/index';

import App from "@/App.vue";

const routes: Array<RouteRecordRaw> = [
    {
      path: "/:user_id/questions",
      name: "Questions",
      component: App,
      meta: { requiresAuth: true }
    },
    {
      path: "/:user_id/questions/ask",
      name: "Ask",
      component: () => import("@/App.vue"),
      meta: { requiresAuth: true }
    },
    {
      path: "/:user_id/questions/:qId",
      name: "Question",
      component: () => import("@/App.vue"),
      meta: { requiresAuth: true }
    },
    {
      path: "/:user_id/profile",
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
    {
      path: '/:pathMatch(.*)',
      name: "NotFound",

      component: () => import("@/App.vue"),
    },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});


function jwtDecode(t: string) {
  const payload = JSON.parse(window.atob(t.split('.')[1]));
  return payload
}

const validateAuthedUser = (to, from, next) => {
  if (!to.meta.requiresAuth) return next();
  
  if (store.state.token) {
    console.log("looged in");
    store.commit("setPageMode", "questions");
    if (to.name === "Questions" || to.name === "Profile" || to.name === "Ask" || to.name === "Question") return next()
    
    next ({ name: "Questions", params: { user_id: jwtDecode(store.state.token).sub } });
  } else  {
    store.commit("setPageMode", "auth");
    next ({ name: "Signin" });
  }
}

router.beforeEach(validateAuthedUser);

export default router;
