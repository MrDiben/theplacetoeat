import Vue from "vue";
import VueI18n from "vue-i18n";
import Notifications from "vue-notification";
import vuetify from "@/plugins/vuetify";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./registerServiceWorker";
import "@/utils/filters";
import useGlobalComponents from "@/setup/useGlobalComponents";

Vue.config.productionTip = false;
useGlobalComponents();
Vue.use(VueI18n);
Vue.use(Notifications);

const locale = navigator.language;
const i18n = new VueI18n({
  fallbackLocale: "fr",
  locale,
  silentFallbackWarn: true
});

new Vue({
  router,
  store,
  vuetify,
  i18n,
  render: h => h(App)
}).$mount("#app");
