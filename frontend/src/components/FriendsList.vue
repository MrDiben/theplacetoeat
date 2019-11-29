<template>
  <div :class="className">
    <v-list subheader>
      <v-subheader>{{ title }}</v-subheader>

      <v-list-item v-for="item in items" :key="item.id">
        <v-list-item-avatar>
          <Avatar :username="item.username" class="ml-1" />
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-text="item.username"></v-list-item-title>
        </v-list-item-content>

        <v-list-item-icon>
          <v-btn
            :height="28"
            :min-width="28"
            v-if="acceptOption === true"
            color="primary"
            dark
            class="px-1"
            @click="acceptInvitationClick(item.id)"
          >
            <v-icon dark>mdi-account-plus</v-icon>
          </v-btn>
          <span v-if="sendOption === true">
            <v-icon v-if="item.status === true"
              >mdi-checkbox-marked-circle</v-icon
            >
            <v-icon v-else>mdi-cancel</v-icon>
          </span>
        </v-list-item-icon>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "FriendsList",
  props: {
    title: {
      type: String,
      required: true
    },
    acceptOption: {
      type: Boolean,
      default: false
    },
    sendOption: {
      type: Boolean,
      default: false
    },
    items: {
      type: Array,
      required: true
    },
    className: {
      type: String,
      required: false
    }
  },
  data() {
    return {};
  },
  methods: {
    ...mapActions("user", ["sendFriendInvitation", "acceptInvitation"]),
    sendFriendInvitationClick(email) {
      this.potentialFriend = {};
      this.sendFriendInvitation(email);
    },
    acceptInvitationClick(id) {
      this.acceptInvitation(id);
      this.$emit("acceptInvitation");
    }
  }
};
</script>

<style style="scss"></style>
