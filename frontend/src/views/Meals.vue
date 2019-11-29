<template>
  <BaseScreen :header="false">
    <template v-slot:main-content>
      <v-tabs :grow="true" v-model="selectedTab">
        <v-tab href="#current">
          {{ $t("current") }}
        </v-tab>
        <v-tab href="#pending">
          <v-badge
            v-if="getReceivedMealInvitations.length > 0"
            color="red darken-3"
            :value="true"
          >
            <template v-slot:badge>
              <span>{{ getReceivedMealInvitations.length }}</span>
            </template>
            <span>{{ $t("pending") }}</span>
          </v-badge>
          <span v-else>
            {{ $t("pending") }}
          </span>
        </v-tab>
        <v-tab href="#done">
          {{ $t("closed") }}
        </v-tab>
        <v-tab-item value="current">
          <MealsList
            v-if="getCurrentMeals.length > 0"
            :title="$t('currentMeals')"
            :meals="getCurrentMeals"
          />
        </v-tab-item>
        <v-tab-item value="pending">
          <MealsList
            v-if="getReceivedMealInvitations.length > 0"
            :title="$t('pendingMeals')"
            :meals="getReceivedMealInvitations"
            :acceptOption="true"
            @acceptInvitation="changeView"
          />
        </v-tab-item>
        <v-tab-item value="done">
          <MealsList
            v-if="getClosedMeals.length > 0"
            :tableHeader="true"
            :searchOption="true"
            :title="$t('closedMeals')"
            :meals="getClosedMeals"
          />
        </v-tab-item>
      </v-tabs>
    </template>
  </BaseScreen>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import MealsList from "@/components/MealsList.vue";

export default {
  name: "Meals",
  components: {
    MealsList
  },
  data() {
    return {
      selectedTab: "current"
    };
  },
  computed: {
    ...mapGetters("user", [
      "getCurrentMeals",
      "getReceivedMealInvitations",
      "getClosedMeals"
    ])
  },
  methods: {
    ...mapActions("user", ["fetchMeals"]),
    changeView() {
      this.selectedTab = "current";
    }
  },
  created() {
    this.fetchMeals();
    if (this.$route.query.status === "done") {
      this.selectedTab = "done";
    } else if (this.$route.query.status === "pending") {
      this.selectedTab = "pending";
    } else {
      this.selectedTab = "current";
    }
  }
};
</script>

<style style="scss"></style>
<i18n>
{
  "en": {
    "pending": "Pending",
    "current": "Current",
    "closed": "Closed",
    "pendingMeals": "Pending meals",
    "currentMeals": "Current meals",
    "closedMeals": "Closed meals"
  },
  "fr": {
    "pending": "En attente",
    "current": "En cours",
    "closed": "Fermée",
    "pendingMeals": "Repas en attente",
    "currentMeals": "Repas en cours",
    "closedMeals": "Repas terminés"
  }
}
</i18n>
