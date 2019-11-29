<template>
  <BaseScreen>
    <template v-slot:main-content>
      <VRow align="center" class="row-content">
        <VCol>
          <p class="mb-8 title">{{ $t("homeTitle") }}</p>
          <v-carousel
            class="restaurants-carousel"
            hide-delimiters
            :dark="$vuetify.theme.dark"
            :light="!$vuetify.theme.dark"
            height="380px"
          >
            <v-carousel-item
              v-for="resto in displayedRestaurants"
              :key="resto.id"
            >
              <v-card class="mx-auto" max-width="500">
                <v-img
                  class="white--text"
                  height="200px"
                  :src="resto.photo_header"
                >
                  <v-card-title
                    color="deep-purple accent-4"
                    class="align-end fill-height"
                  >
                    {{ resto.name }}
                  </v-card-title>
                </v-img>

                <v-card-text>
                  <span class="text--primary">
                    <span>{{ resto.formatted_address }}</span
                    ><br />
                    <a
                      v-if="
                        resto.phone_number !== undefined &&
                          resto.phone_number !== ''
                      "
                      :href="`tel:${resto.phone_number}`"
                    >
                      {{ resto.phone_number }} </a
                    ><br />
                    <a
                      v-if="resto.website !== undefined && resto.website !== ''"
                      target="_blank"
                      :href="resto.website"
                    >
                      {{ $t("webSite") }}
                    </a>
                  </span>
                </v-card-text>

                <v-card-actions>
                  <v-btn
                    text
                    color="primary"
                    @click="$router.push(`/restaurant-detail/${resto.id}`)"
                  >
                    {{ $t("detail") }}
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-carousel-item>
          </v-carousel>
        </VCol>
      </VRow>
    </template>
  </BaseScreen>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "home",
  computed: {
    ...mapGetters("user", ["getCurrentUser", "hasRestaurants"]),
    displayedRestaurants() {
      if (this.hasRestaurants) {
        return this.getCurrentUser.restaurants;
      }
      return {};
    }
  },
  methods: {}
};
</script>

<style lang="scss" scoped>
.row-content {
  height: 100%;
}
.restaurants-carousel {
  // TO DO: media query
  ::v-deep .v-window__prev {
    top: calc(40% - 70px);
  }

  ::v-deep .v-window__next {
    top: calc(40% - 70px);
    color: white;
  }
  ::v-deep .v-icon.mdi.mdi-chevron-right {
    color: white;
  }
  ::v-deep .v-icon.mdi.mdi-chevron-left {
    color: white;
  }
}
</style>

<i18n>
{
  "en": {
    "homeTitle": "Your restaurant selection for the day !",
    "webSite": "Web site",
    "detail": "Detail"
  },
  "fr": {
    "homeTitle": "Votre sélection de restaurants pour la journée !",
    "webSite": "Site web",
    "detail": "Détail"
  }
}
</i18n>
