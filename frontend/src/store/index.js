import Vue from "vue";
import Vuex from "vuex";
import createLogger from "vuex/dist/logger";

import auth from "./auth";
import password from "./password";
import signup from "./signup";
import UserModule from "./modules/user";

const debug = process.env.NODE_ENV !== "production";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    password,
    signup,
    user: UserModule
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
});
