<template>
  <v-content>
    <v-container class="fill-height form-container" fluid>
      <v-row align="center" justify="center">
        <v-col cols="10" xs="10" sm="6" md="5">
          <v-card class="elevation-12">
            <v-toolbar color="primary" dark flat>
              <v-toolbar-title>The Place To Eat</v-toolbar-title>
              <v-spacer />
              <h5>{{ $t("createAccount") }}</h5>
            </v-toolbar>
            <v-card-text v-if="registrationLoading">
              <v-progress-circular
                class="registration-content"
                indeterminate
                size="64"
              ></v-progress-circular>
            </v-card-text>
            <div v-else-if="!registrationCompleted">
              <v-card-text>
                <v-form ref="form" v-model="valid">
                  <v-text-field
                    :label="$t('id')"
                    v-model="form.username"
                    prepend-icon="mdi mdi-account"
                    type="text"
                    :rules="[v => !!v || $t('fillId')]"
                  />
                  <v-text-field
                    :label="$t('password')"
                    v-model="form.password1"
                    prepend-icon="mdi mdi-lock"
                    type="password"
                    :rules="[
                      v => !!v || $t('dontForgetPassword'),
                      v => v.length >= 8 || $t('passwordTooShort')
                    ]"
                  />
                  <v-text-field
                    :label="$t('confirmPassword')"
                    v-model="form.password2"
                    prepend-icon="mdi mdi-lock"
                    type="password"
                    :rules="[
                      v => !!v || $t('dontForgetPassword'),
                      passwordConfirmationRule
                    ]"
                  />
                  <v-text-field
                    :label="$t('email')"
                    v-model="form.email"
                    prepend-icon="mdi mdi-email"
                    type="email"
                    :rules="[v => !!v || $t('fillEmail')]"
                  />
                </v-form>
                <div class="form-error" v-show="registrationError">
                  {{ $t("errorRegister") }}
                </div>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  @click="createAccount(form)"
                  color="primary"
                  :disabled="!valid"
                  >{{ $t("createAccount") }}</v-btn
                >
              </v-card-actions>
            </div>
            <v-card-text v-else>
              <div class="registration-content">
                <p class="title pt-10">
                  {{ $t("congrats") }}
                </p>
                <p class="title">
                  {{ $t("successMessage") }}
                </p>
                <router-link to="/login" class="title">{{
                  $t("login")
                }}</router-link>
              </div>
            </v-card-text>
          </v-card>
          <p class="mt-4">
            {{ $t("alreadyRegistered") }}
            <router-link to="/login">{{ $t("login") }}</router-link>
          </p>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  data() {
    return {
      valid: false,
      form: {
        username: "",
        password1: "",
        password2: "",
        email: ""
      }
    };
  },
  computed: {
    ...mapState("signup", [
      "registrationCompleted",
      "registrationError",
      "registrationLoading"
    ]),
    passwordConfirmationRule() {
      return () =>
        this.form.password1 === this.form.password2 ||
        "Les mots de passe ne sont pas identiques :/ !";
    }
  },
  methods: mapActions("signup", ["createAccount", "clearRegistrationStatus"]),
  beforeRouteLeave(to, from, next) {
    this.clearRegistrationStatus();
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
.registration-content {
  height: 332px !important;
}
</style>

<i18n>
{
  "en": {
    "connexion": "Login",
    "id": "Username",
    "fillId": "Fill your username !",
    "password": "Password",
    "confirmPassword": "Confirm password",
    "email": "E-mail",
    "fillEmail": "Fill your email !",
    "passwordTooShort": "Password too short ! (8 letters minimum)",
    "dontForgetPassword": "Don't forget your password !",
    "errorRegister": "Unable to create your account: username or email already used !",
    "login": "Login",
    "alreadyRegistered": "Already registered ?",
    "createAccount": "Create account",
    "congrats": "Congratulation !",
    "successMessage": "Account creation over. You should receive an email shortly to activate your account."
  },
  "fr": {
    "connexion": "Connexion",
    "id": "Identifiant",
    "fillId": "Entrez votre identifiant !",
    "password": "Mot de passe",
    "confirmPassword": "Confirmation",
    "email": "E-mail",
    "fillEmail": "Entrez votre email !",
    "passwordTooShort": "Le mot de passe est trop court (8 caractères minimum) !",
    "dontForgetPassword": "N'oubliez pas votre mot de passe !",
    "errorRegister": "Impossible de créer votre compte: Identifiant ou email déjà utilisé !",
    "login": "Se connecter",
    "alreadyRegistered": "Déjà un compte ?",
    "createAccount": "Créer un compte",
    "congrats": "Félicitations !",
    "successMessage": "Création de compte terminé. Vous devriez recevoir un email rapidement pour activer votre compte."
  }
}
</i18n>
