<template>
  <div id="activate-account-view">
    <h1>{{ $t("verifyEmail") }}</h1>
    <template v-if="activationLoading">{{ $t("loading") }}</template>
    <template v-else-if="activationError">{{
      $t("errorVerifyEmail")
    }}</template>
    <template v-else-if="activationCompleted">
      {{ $t("successMessage") }}
      <router-link v-if="!isAuthenticated" to="/login">
        {{ $t("clickLogin") }}
      </router-link>
    </template>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex";

export default {
  computed: {
    ...mapGetters("auth", ["isAuthenticated"]),
    ...mapState("signup", [
      "activationCompleted",
      "activationError",
      "activationLoading"
    ])
  },
  methods: mapActions("signup", ["activateAccount", "clearActivationStatus"]),
  created() {
    this.activateAccount(this.$route.params);
  },
  beforeRouteLeave(to, from, next) {
    this.clearActivationStatus();
    next();
  }
};
</script>

<i18n>
{
  "en": {
    "verifyEmail": "Verify Email",
    "loading": "loading...",
    "clickLogin": "Click here to sign in.",
    "errorVerifyEmail": "An error occured.",
    "successMessage": "Your account is activated."
  },
  "fr": {
    "verifyEmail": "Vérifier email",
    "loading": "chargement...",
    "clickLogin": "Cliquer ici pour vous connecter.",
    "errorVerifyEmail": "Une erreur s'est produite.",
    "successMessage": "Votre compte est actif."
  }
}
</i18n>
