<template>
  <div id="app">
    <VApp>
      <notifications group="appNotif" position="bottom center" />
      <Nav v-if="isAuthenticated" />
      <VRow>
        <router-view></router-view>
      </VRow>
      <VFooter class="font-weight-medium main-footer" color="#d6d6d6">
        <VCol class="text-center" cols="12">
          {{ new Date().getFullYear() }} - <strong>ThePlaceToEat</strong>
        </VCol>
      </VFooter>
    </VApp>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
// import './assets/css/reset.css';
import Nav from "./components/Nav.vue";

export default {
  name: "app",
  components: {
    Nav
  },
  computed: mapGetters("auth", ["isAuthenticated"]),
  data() {
    return {};
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
}
html,
body {
  overflow-x: hidden;
  overflow-y: auto;
}
.main-footer {
  box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.2),
    0px 4px 5px 0px rgba(0, 0, 0, 0.14), 0px 1px 10px 0px rgba(0, 0, 0, 0.12);
}
.vue-notification-group {
  bottom: 10px !important;
}
.v-application .vue-notification {
  font-size: 15px !important;
  color: #ffffff !important;

  &.error {
    background: #e54d42 !important;
    border-left-color: #b82e24 !important;
  }
  &.success {
    background: #68cd86 !important;
    border-left-color: #42a85f !important;
  }
}
</style>
