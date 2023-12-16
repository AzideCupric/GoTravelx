import { createRouter, createWebHistory } from "vue-router";

import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/register",
    component: Register,
  },
  {
    path: "/:pathMatched(.*)*",
    component: NotFound,
    props: (route: { params: { pathMatched: string } }) => ({
      pathMatched: `/${route.params.pathMatched}`,
    }),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
