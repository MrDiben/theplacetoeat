<template>
  <v-content>
    <v-container class="fill-height form-container" fluid>
      <v-row align="center" justify="center">
        <v-col cols="10" xs="10" sm="6" md="5">
          <v-card class="elevation-12">
            <v-toolbar color="primary" dark flat>
              <v-toolbar-title>{{ $t("siteName") }}</v-toolbar-title>
              <v-spacer />
              <h5>{{ $t("connexion") }}</h5>
            </v-toolbar>
            <v-card-text>
              <v-form ref="form" v-model="valid">
                <v-text-field
                  :label="$t('connexion')"
                  v-model="form.username"
                  prepend-icon="mdi mdi-account"
                  type="text"
                  :rules="[v => !!v || $t('fillId')]"
                />

                <v-text-field
                  :label="$t('password')"
                  v-model="form.password"
                  prepend-icon="mdi mdi-lock"
                  type="password"
                  :rules="[v => !!v || $t('dontForgetPassword')]"
                />
              </v-form>
              <div class="form-error" v-show="error">
                {{ $t("errorLogin") }}
              </div>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn @click="login(form)" color="primary" :disabled="!valid">{{
                $t("login")
              }}</v-btn>
            </v-card-actions>
          </v-card>
          <p class="mt-4">
            {{ $t("new") }}
            <router-link to="/register/">{{ $t("createAccount") }}</router-link>
          </p>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
export default {
  data() {
    return {
      valid: false,
      form: {
        username: "",
        password: ""
      },
      error: false
    };
  },
  methods: {
    login({ username, password }) {
      if (this.$refs.form.validate()) {
        this.$store
          .dispatch("auth/login", { username, password })
          .then(() => this.$router.push("/"))
          .catch(() => {
            this.error = true;
          });
      }
    }
  }
};
</script>

<style lang="scss">
.form-error {
  color: red;
}
.form-container {
  background-color: #f0f7ff;
}
</style>

<i18n>
{
  "en": {
    "connexion": "Login",
    "siteName": "The Place To Eat",
    "id": "Username",
    "fillId": "Fill your username !",
    "password": "Password",
    "dontForgetPassword": "Don't forget your password !",
    "errorLogin": "Username or password uncorrect !",
    "login": "Login",
    "new": "Are you new ?",
    "createAccount": "Create account"
  },
  "fr": {
    "connexion": "Connexion",
    "siteName": "The Place To Eat",
    "id": "Identifiant",
    "fillId": "Entrez votre identifiant !",
    "password": "Mot de passe",
    "dontForgetPassword": "N'oubliez pas votre mot de passe !",
    "errorLogin": "Identifiant ou mot de passe incorrect !",
    "login": "Se connecter",
    "new": "Vous êtes nouveau ?",
    "createAccount": "Créer un compte"
  }
}
</i18n>
