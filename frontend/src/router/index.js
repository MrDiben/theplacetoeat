import Vue from "vue";
import Router from "vue-router";
import Home from "../views/Home.vue";
import RestaurantDetail from "../views/RestaurantDetail.vue";
import Account from "../views/Account.vue";
import Friends from "../views/Friends.vue";
import Meals from "../views/Meals.vue";
import Login from "../views/Login.vue";
import Lost from "../views/Lost.vue";
import PasswordReset from "../views/PasswordReset.vue";
import PasswordResetConfirm from "../views/PasswordResetConfirm.vue";
import Register from "../views/Register.vue";
import VerifyEmail from "../views/VerifyEmail.vue";
import ChangePassword from "../views/ChangePassword.vue";

import store from "../store";
import initializeUser from "./initializeUser";

const requireAuthenticated = (to, from, next) => {
  store.dispatch("auth/initialize").then(() => {
    if (!store.getters["auth/isAuthenticated"]) {
      next("/login");
    } else {
      Promise.all([initializeUser(store)]).then(() => {
        next();
      });
    }
  });
};

const requireUnauthenticated = (to, from, next) => {
  store.dispatch("auth/initialize").then(() => {
    if (store.getters["auth/isAuthenticated"]) {
      initializeUser(store);
      next("/");
    } else {
      next();
    }
  });
};

const redirectLogout = (to, from, next) => {
  store.dispatch("auth/logout").then(() => next("/login"));
};

Vue.use(Router);

export default new Router({
  mode: "history",
  saveScrollPosition: true,
  routes: [
    {
      path: "/",
      component: Home,
      beforeEnter: requireAuthenticated
    },
    {
      path: "/restaurant-detail/:id",
      component: RestaurantDetail,
      beforeEnter: requireAuthenticated
    },
    {
      path: "/account",
      component: Account,
      beforeEnter: requireAuthenticated
    },
    {
      path: "/friends",
      component: Friends,
      beforeEnter: requireAuthenticated
    },
    {
      path: "/meals",
      component: Meals,
      beforeEnter: requireAuthenticated
    },
    {
      path: "/change-password",
      component: ChangePassword,
      beforeEnter: requireAuthenticated
    },
    {
      path: "/password_reset",
      component: PasswordReset
    },
    {
      path: "/password_reset/:uid/:token",
      component: PasswordResetConfirm
    },
    {
      path: "/register/",
      component: Register
    },
    {
      path: "/register/:key",
      component: VerifyEmail
    },
    {
      path: "/login",
      component: Login,
      beforeEnter: requireUnauthenticated
    },
    {
      path: "/logout",
      beforeEnter: redirectLogout
    },
    {
      path: "*",
      component: Lost
    }
  ]
});
