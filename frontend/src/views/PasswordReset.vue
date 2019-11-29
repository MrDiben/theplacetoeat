<template>
  <div id="password-reset-view">
    <h1>{{ $t("resetPassword") }}</h1>
    <template v-if="emailLoading">
      {{ $t("loading") }}
    </template>
    <template v-else-if="!emailCompleted">
      <form @submit.prevent="submit">
        <input
          v-model="inputs.email"
          type="text"
          id="email"
          placeholder="email"
        />
      </form>
      <button @click="sendPasswordResetEmail(inputs)">
        {{ $t("sendMail") }}
      </button>
      <span class="error" v-show="emailError">
        {{ $t("resetError") }}
      </span>
    </template>
    <template v-else>
      <div>
        {{ $t("emailMessage") }}
      </div>
      <router-link to="/login">
        {{ $t("returnLogin") }}
      </router-link>
    </template>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  data() {
    return { inputs: { email: "" } };
  },
  computed: mapState("password", [
    "emailCompleted",
    "emailError",
    "emailLoading"
  ]),
  methods: mapActions("password", [
    "sendPasswordResetEmail",
    "clearEmailStatus"
  ]),
  beforeRouteLeave(to, from, next) {
    this.clearEmailStatus();
    next();
  }
};
</script>

<style>
form input {
  display: block;
}

.error {
  color: crimson;
  font-size: 12px;
}
</style>

<i18n>
{
  "en": {
    "resetPassword": "Reset Password",
    "loading": "loading...",
    "sendMail": "send email",
    "resetError": "A error occured while processing your request.",
    "emailMessage": "Check your inbox for a link to reset your password.",
    "returnLogin": "return to login page"
  },
  "fr": {
    "resetPassword": "Modifier mot de passe",
    "loading": "chargement...",
    "sendMail": "envoyer email",
    "resetError": "Une erreur s'est produite lors de la modification du mot de passe.",
    "emailMessage": "Regardez dans votre boîte mail vous devriez recevoir un mail pour modifier votre mot de passe.",
    "returnLogin": "revenir à la page de connexion"
  }
}
</i18n>
