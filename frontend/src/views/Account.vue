<template>
  <BaseScreen :header="false">
    <template v-slot:main-content>
      <v-container class="account" fluid>
        <div class="content">
          <v-row align="center" class="mb-3">
            <v-col cols="3">
              <span>{{ $t("city") }} </span>
            </v-col>
            <v-col cols="9">
              <v-select
                v-model="userCity"
                :items="getCityNames"
                menu-props="auto"
                hide-details
                :label="$t('select')"
                class="pt-0"
                width="120px"
                single-line
              />
            </v-col>
          </v-row>
          <v-row align="center" class="mb-3">
            <v-col cols="3">
              <span>{{ $t("username") }} </span>
            </v-col>
            <v-col cols="9">
              <span>{{ getCurrentUser.username }}</span>
            </v-col>
          </v-row>
          <v-row align="center" class="mb-10">
            <v-col cols="3">
              <span>{{ $t("email") }} </span>
            </v-col>
            <v-col cols="9">
              <span>{{ getCurrentUser.email }}</span>
            </v-col>
          </v-row>
          <div class="mt-12">
            <v-btn color="primary">{{ $t("update") }}</v-btn>
          </div>
        </div>
      </v-container>
    </template>
  </BaseScreen>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Account",
  data() {
    return {
      userCity: ""
    };
  },
  computed: {
    ...mapGetters("user", ["getCityNames", "getCurrentUser"])
  },
  mounted() {
    if (this.getCurrentUser.city.name !== "") {
      this.userCity = this.getCurrentUser.city.name;
    }
  }
};
</script>

<style lang="scss" scoped>
.v-input {
  max-width: 150px;
  margin: auto;
}
</style>

<i18n>
{
  "en": {
    "city": "City: ",
    "username": "Username: ",
    "email": "E-mail: ",
    "select": "Select city",
    "update": "Update"
  },
  "fr": {
    "city": "Ville: ",
    "username": "Pseudo: ",
    "email": "E-mail: ",
    "select": "Selectionner ville",
    "update": "Valider"
  }
}
</i18n>
