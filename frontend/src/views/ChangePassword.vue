<template>
  <div id="password-change-view">
    <h1>Change Password</h1>
    <template>
      <form @submit.prevent="submit">
        <input
          v-model="inputs.oldPassword"
          type="password"
          id="oldPassword"
          :placeholder="$t('oldPassword')"
        />
        <input
          v-model="inputs.newPassword1"
          type="password"
          id="newPassword1"
          :placeholder="$t('newPassword1')"
        />
        <input
          v-model="inputs.newPassword2"
          :placeholder="$t('newPassword2')"
          type="password"
          id="newPassword2"
        />
      </form>
      <button @click="sendPasswordChange(inputs)">
        {{ $t("update") }}
      </button>
      <span class="error" v-if="errors !== []">
        <p v-for="error in errors" :key="error">{{ error }}</p>
      </span>
    </template>
  </div>
</template>

<script>
import auth from "../api/auth";

export default {
  data() {
    return {
      inputs: { oldPassword: "", newPassword1: "", newPassword2: "" },
      errors: []
    };
  },
  methods: {
    async sendPasswordChange({ oldPassword, newPassword1, newPassword2 }) {
      this.errors = [];
      await auth
        .changeAccountPassword({ oldPassword, newPassword1, newPassword2 })
        .then(() => {
          this.$router.push("/");
        })
        .catch(e => {
          Object.values(e.response.data).forEach(errors =>
            errors.forEach(error => {
              this.errors.push(error);
            })
          );
        });
    }
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
    "oldPassword": "Old password",
    "newPassword1": "New password",
    "newPassword2": "Confirm new password",
    "update": "Validate"
  },
  "fr": {
    "oldPassword": "Ancien mot de passe",
    "newPassword1": "Nouveau mot de passe",
    "newPassword2": "Confirmer mot de passe",
    "update": "Valider"
  }
}
</i18n>
