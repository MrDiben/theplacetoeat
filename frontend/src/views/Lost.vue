<template>
  <v-container>
    <div id="lost-view">
      <h1>{{ $t("notFound") }}</h1>
      <h4>{{ $t("lost") }}</h4>
      <router-link to="/">{{ $t("backHome") }}</router-link>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "lost"
};
</script>

<i18n>
{
  "en": {
    "notFound": "Page Not Found",
    "lost": "One of us is lost.",
    "backHome": "Take me home."
  },
  "fr": {
    "notFound": "Page non trouvée",
    "lost": "L'un de nous est perdu.",
    "backHome": "Revenir à la maison."
  }
}
</i18n>
