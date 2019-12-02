<template>
  <BaseScreen :header="false">
    <template v-slot:main-content>
      <VRow class="flex-column">
        <VCol class="font-weight-bold">{{ $t("restaurantSheet") }}</VCol>
      </VRow>
      <VRow class="flex-column restaurant-card">
        <VCol class="subcontent-2">
          <v-card :loading="mealLoading" class="mx-auto mb-12" max-width="600">
            <v-carousel height="250" delimiter-icon="mdi-minus">
              <v-carousel-item
                v-for="(photo, i) in restaurant.photos"
                :key="i"
                :src="photo.url"
                height="250"
                reverse-transition="fade-transition"
                transition="fade-transition"
                delimiter-icon="mdi mdi-minus"
              ></v-carousel-item>
            </v-carousel>

            <v-card-title>{{ restaurant.name }}</v-card-title>
            <v-card-text class="pb-0">
              <VRow justify="space-around">
                <VCol>
                  <v-rating
                    :value="restaurant.rating.google_rating_average"
                    color="blue"
                    half-increments
                    dense
                    size="14"
                    readonly
                  ></v-rating>

                  <span class="grey--text"
                    >{{ restaurant.rating.google_rating_average }} ({{
                      restaurant.rating.google_user_ratings_total
                    }})</span
                  >
                </VCol>
                <VCol>
                  <v-chip color="blue" text-color="white" class="px-2">
                    <v-icon
                      class="body-2"
                      v-for="i in restaurant.price_indicator.length"
                      :key="i"
                      >mdi-currency-eur</v-icon
                    >
                  </v-chip>
                </VCol>
              </VRow>
            </v-card-text>

            <!-- Restaurant Description -->
            <v-card-text class="pt-0" v-if="book == 0">
              <div class="mb-2 subtitle-1">
                <span v-for="ct in restaurant.cook_types" :key="ct.name">
                  <v-chip
                    class="ma-2"
                    color="primary"
                    label
                    text-color="white"
                    >{{ ct.name }}</v-chip
                  >
                </span>
              </div>

              <div>{{ restaurant.description }}</div>
            </v-card-text>

            <!-- Restaurant reservation -->
            <v-card-text v-else>
              <v-form ref="form" v-model="valid" :lazy-validation="lazy">
                <h3 class="text--primary mb-2">{{ $t("createMealSheet") }}</h3>
                <v-divider />
                <!-- Checkbox alone or not -->
                <v-checkbox
                  v-model="alone"
                  :label="$t('eatAlone')"
                  required
                ></v-checkbox>
                <!-- Select multiple friend -->
                <v-select
                  v-if="alone === false"
                  v-model="guests"
                  :items="getUserFriends"
                  :rules="guestsRules"
                  :label="$t('inviteFriends')"
                  item-text="username"
                  item-value="email"
                  multiple
                >
                  <template v-slot:selection="{ item, index }">
                    <v-chip v-if="index === 0">
                      <span>{{ item.username }}</span>
                    </v-chip>
                    <span v-if="index === 1" class="grey--text caption"
                      >(+{{ guests.length - 1 }} {{ $t("others") }})</span
                    >
                  </template>
                </v-select>
                <!-- Time selection -->
                <v-select
                  v-model="timeSelect"
                  :items="restaurant.timeSelection"
                  :rules="[v => !!v || $t('selectMealInv')]"
                  label="Pour quelle heure ?"
                  required
                ></v-select>
              </v-form>
            </v-card-text>

            <v-divider class="mx-4"></v-divider>

            <v-card-text v-if="book == 0">
              <div class="title text--primary">{{ $t("openingDay") }}</div>
              <v-chip-group>
                <VRow>
                  <VCol>
                    <v-chip
                      v-for="todayHour in restaurant.todayHours"
                      :key="todayHour.id"
                      >{{ todayHour.displayHour }}</v-chip
                    >
                  </VCol>
                </VRow>
              </v-chip-group>
            </v-card-text>
            <v-card-text v-if="book == 0">
              <div>
                <a
                  v-if="
                    restaurant.phone_number !== undefined &&
                      restaurant.phone_number !== ''
                  "
                  class="mr-7"
                  :href="`tel:${restaurant.phone_number}`"
                  >{{ restaurant.phone_number }}</a
                >
                <a
                  v-if="
                    restaurant.website !== undefined &&
                      restaurant.website !== ''
                  "
                  class="ml-7"
                  target="_blank"
                  :href="restaurant.website"
                  >{{ $t("website") }}</a
                >
              </div>
            </v-card-text>

            <v-card-actions>
              <v-btn color="primary" text @click="handleBookButton()">{{
                getButtonText
              }}</v-btn>
              <v-btn
                v-if="book == 1"
                :disabled="!valid"
                color="primary"
                class="mr-4"
                @click="validate"
                outlined
                >{{ $t("create") }}</v-btn
              >
            </v-card-actions>
          </v-card>
        </VCol>
      </VRow>
    </template>
  </BaseScreen>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Restaurant from "@/models/Restaurant";

export default {
  name: "RestaurantDetail",
  data: () => ({
    timeSelection: 1,
    book: 0,
    mealLoading: false,
    // Form
    valid: true,
    lazy: false,
    alone: true,
    guests: [],
    timeHours: ["12:00", "13:00"],
    timeSelect: null
  }),
  computed: {
    ...mapGetters("user", ["getUserRestaurantId", "getUserFriends"]),
    restaurant() {
      if (this.getUserRestaurantId(parseInt(this.$route.params.id))) {
        return this.getUserRestaurantId(parseInt(this.$route.params.id));
      }
      return new Restaurant();
    },
    guestsRules() {
      return [v => v.length > 0 || this.$t("selectFriendsWarn")];
    },
    getButtonText() {
      if (this.book === 0) {
        return this.$t("createMeal");
      }
      return this.$t("back");
    }
  },
  methods: {
    ...mapActions("user", ["createMeal"]),
    handleBookButton() {
      if (this.book === 0) {
        this.book = 1;
      } else {
        this.book = 0;
      }
    },
    validate() {
      if (this.$refs.form.validate()) {
        this.mealLoading = true;
        this.createMeal({
          restaurantId: this.$route.params.id,
          time: this.timeSelect,
          guests: this.guests
        }).then(response => {
          setTimeout(() => {
            if (response === "created") {
              this.$notify({
                group: "appNotif",
                type: "success",
                title: "Félicitations votre repas a été créé !",
                text: `Le repas au restaurant ${this.restaurant.name} a bien été enregistré.`
              });
              this.book = 0;
              this.$router.push("/meals?status=current");
            } else {
              this.$notify({
                group: "appNotif",
                type: "error",
                title: "Oh non ! Impossible de créer votre repas !",
                text:
                  "Il est possible que vous ayez déjà réservé une table à cette heure-ci."
              });
            }
            this.mealLoading = false;
          }, 1000);
        });
      }
    }
  }
};
</script>

<style lang="scss">
.v-label {
  color: #424242 !important;
}
</style>

<i18n>
{
  "en": {
    "restaurantSheet": "Restaurant sheet",
    "createMealSheet": "Create meal sheet",
    "eatAlone": "Do you eat alone ?",
    "others": "others",
    "inviteFriends": "Invite your friends !",
    "selectMealInv": "You must select an hour for your meal invitation",
    "openingDay": "Opening of the days",
    "webSite": "Web site",
    "create": "Create",
    "createMeal": "Create meal",
    "selectFriendsWarn": "You must select some guests if you don't eat alone",
    "back": "Back"
  },
  "fr": {
    "restaurantSheet": "Fiche restaurant",
    "createMealSheet": "Création d'une fiche repas",
    "eatAlone": "Mangez-vous tout seul ?",
    "others": "autres",
    "inviteFriends": "Inviter vos amis !",
    "selectMealInv": "Sélectionne une heure pour ton repas !",
    "openingDay": "Ouvertures du jour",
    "webSite": "Site web",
    "create": "Créer",
    "createMeal": "Créer repas",
    "selectFriendsWarn": "Sélectionnez des amis si vous ne mangez pas tout seul !",
    "back": "Retour"
  }
}
</i18n>
