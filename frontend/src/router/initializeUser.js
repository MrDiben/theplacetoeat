export default async store => {
  try {
    if (!store.getters["user/isLoaded"]) {
      await store.dispatch("user/fetchUserProfile");
      await store.dispatch("user/fetchCurrentUserRestaurants");
      await store.dispatch("user/fetchCities");
      await store.dispatch("user/fetchFriendInvitations");
      await store.dispatch("user/fetchFriends");
      await store.dispatch("user/fetchMeals");
    }
  } catch (err) {
    console.log("Error fetching user");
  }
};
