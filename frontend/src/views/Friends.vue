<template>
  <BaseScreen :header="false">
    <template v-slot:main-content>
      <v-tabs :grow="true" v-model="selectedTab">
        <v-tab href="#friends" class="px-0">
          {{ $t("friends") }}
        </v-tab>
        <v-tab href="#acceptFriend" class="px-2">
          <v-badge
            v-if="receivedFriendInvitations.length > 0"
            color="red darken-3"
            :value="true"
          >
            <template v-slot:badge>
              <span>{{ receivedFriendInvitations.length }}</span>
            </template>
            <span>{{ $t("pending") }}</span>
          </v-badge>
          <span v-else>
            {{ $t("pending") }}
          </span>
        </v-tab>
        <v-tab href="#addFriend">
          {{ $t("addFriends") }}
        </v-tab>
        <v-tab-item value="friends">
          <FriendsList
            :title="$t('friends')"
            :items="getUserFriends"
            className="mt-2"
          />
        </v-tab-item>
        <v-tab-item value="acceptFriend">
          <FriendsList
            :title="$t('pendingInvitations')"
            :acceptOption="true"
            :items="receivedFriendInvitations"
            className="mt-2"
            @acceptInvitation="changeView"
          />
        </v-tab-item>
        <v-tab-item value="addFriend">
          <v-row>
            <v-col cols="12">
              <autocomplete
                ref="autocomplete"
                :placeholder="$t('searchFriends')"
                :source="distributionGroupsEndpoint"
                input-class="form-control"
                results-property="data"
                :results-display="formattedDisplay"
                :request-headers="authHeaders"
                @selected="addDistributionGroup"
              >
              </autocomplete>
            </v-col>
          </v-row>
          <v-row v-if="potentialFriend.user">
            <v-col cols="6" class="my-auto">
              {{ potentialFriend.user.username }}
            </v-col>
            <v-col cols="6" class="my-auto">
              <v-btn
                fab
                dark
                small
                color="primary"
                :width="32"
                :height="32"
                @click="sendFriendInvitationClick(potentialFriend.user.email)"
              >
                <v-icon dark>mdi-account-plus</v-icon>
              </v-btn>
            </v-col>
          </v-row>
          <FriendsList
            :title="$t('sentInvitations')"
            :sendOption="true"
            :items="sentFriendInvitations"
            className="mt-5"
          />
        </v-tab-item>
      </v-tabs>
    </template>
  </BaseScreen>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Autocomplete from "vuejs-auto-complete";
import FriendsList from "@/components/FriendsList";

export default {
  name: "Friends",
  components: {
    Autocomplete,
    FriendsList
  },
  data() {
    return {
      potentialFriend: Object,
      selectedTab: "friends"
    };
  },
  computed: {
    ...mapGetters("auth", ["getToken"]),
    ...mapGetters("user", [
      "getUserFriends",
      "getSentFriendInvitations",
      "getReceivedFriendInvitations"
    ]),
    authHeaders() {
      return {
        Authorization: `Token ${this.getToken}`
      };
    },
    sentFriendInvitations() {
      return this.getSentFriendInvitations.map(inv => ({
        username: inv.user_2.user.username,
        email: inv.user_2.user.email,
        id: inv.id,
        status: inv.status
      }));
    },
    receivedFriendInvitations() {
      return this.getReceivedFriendInvitations.map(inv => ({
        username: inv.user_1.user.username,
        email: inv.user_1.user.email,
        id: inv.id,
        status: inv.status
      }));
    }
  },
  methods: {
    ...mapActions("user", [
      "sendFriendInvitation",
      "acceptInvitation",
      "fetchFriendInvitations",
      "fetchFriends"
    ]),
    distributionGroupsEndpoint(input) {
      return `${process.env.VUE_APP_BACK_BASE_URL}/users/?query=${input}`;
    },
    addDistributionGroup(group) {
      this.potentialFriend = group.selectedObject;
      // access the autocomplete component methods from the parent
      this.$refs.autocomplete.clear();
    },
    formattedDisplay(result) {
      return `${result.user.username} (${result.user.email})`;
    },
    sendFriendInvitationClick(email) {
      this.potentialFriend = {};
      this.sendFriendInvitation(email);
    },
    acceptInvitationClick(id) {
      // Remove object from list
      this.acceptInvitation(id);
    },
    changeView() {
      this.selectedTab = "friends";
    }
  },
  created() {
    this.fetchFriends();
    this.fetchFriendInvitations();
    if (this.$route.query.status === "addFriend") {
      this.selectedTab = "addFriend";
    } else if (this.$route.query.status === "acceptFriend") {
      this.selectedTab = "acceptFriend";
    } else {
      this.selectedTab = "friends";
    }
  }
};
</script>

<style style="scss"></style>

<i18n>
{
  "en": {
    "friends": "Friends",
    "pending": "Pending",
    "addFriends": "Add Friends",
    "sentInvitations": "Sent invitations",
    "searchFriends": "Search friends",
    "pendingInvitations": "Pending invitations"
  },
  "fr": {
    "friends": "Amis",
    "pending": "En attente",
    "addFriends": "Ajouter",
    "sentInvitations": "Invitations envoyées",
    "searchFriends": "Chercher un ami",
    "pendingInvitations": "Invitations en attente"
  }
}
</i18n>
