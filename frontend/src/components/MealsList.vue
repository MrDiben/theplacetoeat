<template>
  <div class="mt-4">
    <v-card>
      <v-card-title>
        {{ title }}
        <v-spacer></v-spacer>
        <v-text-field
          v-if="searchOption"
          v-model="search"
          append-icon="mdi mdi-search"
          :label="$t('search')"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :calculate-widths="true"
        :hide-default-footer="!tableFooter"
        :hide-default-header="!tableHeader"
        :headers="headers"
        :items="getItems"
        :search="search"
      >
        <template v-slot:item.guests="{ item }">
          <Avatar
            v-for="(user, index) in item.guests"
            :key="index"
            :username="user.username"
            :withBadge="true"
            :isAccepted="user.is_accepted"
            class="ml-2"
          />
        </template>
        <template v-slot:item.accepted="{ item }">
          <v-btn
            :height="28"
            v-if="acceptOption === true"
            class="ml-2"
            color="primary"
            dark
            @click="acceptInvitationClick(item.pk)"
          >
            {{ $t("accept") }}
            <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
          </v-btn>
          <span v-else>
            <v-icon v-if="item.accepted === true"
              >mdi-checkbox-marked-circle</v-icon
            >
            <v-icon v-else>mdi-cancel</v-icon>
          </span>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "MealList",
  props: {
    title: {
      type: String,
      required: true
    },
    meals: {
      type: Array,
      required: true
    },
    acceptOption: {
      type: Boolean,
      default: false
    },
    searchOption: {
      type: Boolean,
      default: false
    },
    tableHeader: {
      type: Boolean,
      default: false
    },
    tableFooter: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Restaurant",
          align: "left",
          sortable: true,
          value: "restaurantName"
        },
        { text: "Day", value: "day" },
        { text: "What time ?", value: "dateHour" },
        { text: "Guests", value: "guests" },
        { text: "Accepted", value: "accepted" }
      ]
    };
  },
  computed: {
    getItems() {
      return this.meals.map(meal => {
        return {
          restaurantName: meal.mealInfo.restaurant.name,
          day: meal.mealInfo.datehour.substring(0, 10),
          dateHour: meal.mealInfo.datehour.substring(11, 16),
          accepted: meal.accepted,
          pk: meal.pk,
          guests: meal.users.map(user => ({
            username: user.user.username,
            is_accepted: user.is_accepted
          }))
        };
      });
    }
  },
  methods: {
    ...mapActions("user", ["acceptMealInvitation"]),

    acceptInvitationClick(pk) {
      this.$emit("acceptInvitation");
      this.acceptMealInvitation(pk);
    }
  }
};
</script>

<style style="scss"></style>

<i18n>
{
  "en": {
    "accept": "Accept",
    "search": "Search"
  },
  "fr": {
    "accept": "Accepter",
    "search": "Rechercher"
  }
}
</i18n>
