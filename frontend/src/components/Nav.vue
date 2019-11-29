<template>
  <div>
    <v-toolbar :color="'primary'" :dark="true">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>The Place To Eat</v-toolbar-title>
      <div class="flex-grow-1"></div>
      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
    </v-toolbar>
    <v-navigation-drawer v-model="drawer" height="35%" absolute temporary>
      <v-list-item>
        <v-list-item-avatar>
          <Avatar :username="getCurrentUser.username" />
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>{{ getCurrentUser.username }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in navItems"
          :key="item.title"
          link
          @click="$router.push(item.link)"
        >
          <v-list-item-icon>
            <v-badge v-if="item.badge > 0" color="red darken-3" :value="true">
              <template v-slot:badge>
                <span>{{ item.badge }}</span>
              </template>
              <v-icon>
                {{ item.icon }}
              </v-icon>
            </v-badge>
            <v-icon v-else>
              {{ item.icon }}
            </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Nav",
  components: {},
  data() {
    return {
      drawer: null
    };
  },
  computed: {
    ...mapGetters("user", [
      "getCurrentUser",
      "getReceivedFriendInvitations",
      "getReceivedMealInvitations"
    ]),
    navItems() {
      return [
        {
          title: this.$t("home"),
          icon: "mdi mdi-home",
          link: "/",
          badge: 0
        },
        {
          title: this.$t("account"),
          icon: "mdi mdi-account",
          link: "/account",
          badge: 0
        },
        {
          title: this.$t("meals"),
          icon: "mdi mdi-silverware-fork-knife",
          link: "/meals",
          badge: this.getReceivedMealInvitations.length
        },
        {
          title: this.$t("friends"),
          icon: "mdi mdi-account-multiple",
          link: "/friends",
          badge: this.getReceivedFriendInvitations.length
        },
        {
          title: this.$t("logout"),
          icon: "mdi mdi-exit-to-app",
          link: "/logout",
          badge: 0
        }
      ];
    }
  }
};
</script>

<i18n>
{
  "en": {
    "home": "Restaurants",
    "account": "Account",
    "meals": "Meals",
    "friends": "Friends",
    "logout": "Logout"
  },
  "fr": {
    "home": "Restaurants",
    "account": "Profil",
    "meals": "Repas",
    "friends": "Amis",
    "logout": "Se déconnecter"
  }
}
</i18n>
