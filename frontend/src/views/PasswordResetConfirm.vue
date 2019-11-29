<template>
  <div id="password-reset-confirm-view">
    <h1>{{ $t("resetConfirm") }}</h1>
    <template v-if="resetLoading">
      {{ $t("loading") }}
    </template>
    <template v-else-if="!resetCompleted">
      <form @submit.prevent="submit">
        <input
          v-model="inputs.password1"
          type="password"
          id="password1"
          :placeholder="$t('password')"
        />
        <input
          v-model="inputs.password2"
          type="password"
          id="password2"
          :placeholder="$t('confirmPasswordPlaceHolder')"
        />
      </form>
      <button @click="resetPassword(inputs)">
        {{ $t("resetPassword") }}
      </button>
      <span class="error" v-show="resetError">
        {{ $t("errorResetConfirm") }}
      </span>
    </template>
    <template v-else>
      {{ $t("successMessage") }}
      <router-link to="/login">{{ $t("returnLogin") }}</router-link>
    </template>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  data() {
    return {
      inputs: {
        password1: "",
        password2: "",
        uid: this.$route.params.uid,
        token: this.$route.params.token
      }
    };
  },
  computed: mapState("password", [
    "resetCompleted",
    "resetError",
    "resetLoading"
  ]),
  methods: mapActions("password", ["resetPassword", "clearResetStatus"])
};
</script>

<style>
form input {
  display: block;
}
</style>

<i18n>
{
  "en": {
    "resetConfirm": "Reset Password Confirm",
    "loading": "loading...",
    "password": "password",
    "confirmPasswordPlaceHolder": "confirm password",
    "resetPassword": "reset password",
    "returnLogin": "return to login page",
    "errorResetConfirm": "An error occured while processing your request.",
    "successMessage": "Your password has been reset."
  },
  "fr": {
    "resetConfirm": "Confirmer la modification du mot de passe",
    "loading": "chargement...",
    "password": "mot de passe",
    "confirmPasswordPlaceHolder": "confirmer mot de passe",
    "resetPassword": "modifier mot de passe",
    "returnLogin": "revenir à la page de connexion",
    "errorResetConfirm": "Une erreur s'est produite lors de la modification du mot de passe.",
    "successMessage": "Votre mot de passe a été mis à jour."
  }
}
</i18n>
