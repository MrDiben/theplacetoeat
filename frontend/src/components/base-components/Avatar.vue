<template>
  <v-avatar color="primary" size="35" :class="className">
    <v-badge :color="getColorStatus(isAccepted)" :value="true" v-if="withBadge">
      <template v-slot:badge>
        <v-icon dark>
          {{ getIconStatus(isAccepted) }}
        </v-icon>
      </template>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <span v-on="on" class="white--text headline title">{{
            username | badgeName
          }}</span>
        </template>
        <span>{{ username }}</span>
      </v-tooltip>
    </v-badge>
    <v-tooltip bottom v-else>
      <template v-slot:activator="{ on }">
        <span v-on="on" class="white--text headline title">{{
          username | badgeName
        }}</span>
      </template>
      <span>{{ username }}</span>
    </v-tooltip>
  </v-avatar>
</template>

<script>
export default {
  name: "Avatar",
  props: {
    username: {
      type: String,
      required: true
    },
    className: {
      type: String,
      required: false
    },
    withBadge: {
      type: Boolean,
      default: false
    },
    isAccepted: {
      type: Boolean,
      required: false
    }
  },
  data() {
    return {};
  },
  methods: {
    getColorStatus(isAccepted) {
      if (isAccepted === true) {
        return "teal";
      }
      return "red darken-3";
    },
    getIconStatus(isAccepted) {
      if (isAccepted === true) {
        return "mdi-check";
      }
      return "mdi-close";
    }
  }
};
</script>

<style style="scss"></style>
