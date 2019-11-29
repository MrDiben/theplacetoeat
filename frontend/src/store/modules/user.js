import UserProfile from "@/models/UserProfile";
import session from "@/api/session.js";
import Restaurant from "../../models/Restaurant";
import City from "../../models/City";
import Meal from "../../models/Meal";

const state = {
  currentUser: new UserProfile(),
  cities: [],
  isLoaded: false,
  creationMealLoader: false
};

const getters = {
  getCurrentUser: state => state.currentUser,
  isLoaded: state => state.isLoaded,
  creationMealLoading: state => state.creationMealLoader,
  hasRestaurants: state =>
    state.currentUser ? state.currentUser.restaurants.length > 0 : false,
  getUserRestaurantId: state => restoId =>
    state.currentUser.restaurants.find(restaurant => restaurant.id === restoId),
  getCityNames: state => state.cities.map(city => city.name),
  getUserFriends: state => state.currentUser.friends.list,
  getSentFriendInvitations: state => state.currentUser.friends.invitations.sent,
  getReceivedFriendInvitations: state =>
    state.currentUser.friends.invitations.received,
  getCurrentMeals: state => state.currentUser.meals.current,
  getReceivedMealInvitations: state => state.currentUser.meals.pending,
  getClosedMeals: state => state.currentUser.meals.closed
};

const actions = {
  async fetchUserProfile({ commit }) {
    const { data } = await session.get(
      `${process.env.VUE_APP_BACK_BASE_URL}/users/?current`
    );
    commit("SET_CURRENT_USER", data[0]);
    commit("SET_IS_LOADED", true);
  },
  async fetchCurrentUserRestaurants({ commit }) {
    const { data } = await session.get(
      `${process.env.VUE_APP_BACK_BASE_URL}/restaurants/user_recommendations`
    );
    commit("SET_CURRENT_USER_RESTAURANTS", data);
  },
  async fetchCities({ commit }) {
    const { data } = await session.get(
      `${process.env.VUE_APP_BACK_BASE_URL}/cities/`
    );
    commit("SET_CITIES", data);
  },
  async sendFriendInvitation({ commit }, email) {
    const { data } = await session.post(
      `${process.env.VUE_APP_BACK_BASE_URL}/relations/`,
      {
        email
      }
    );
    commit("SET_SINGLE_FRIEND_INV_SENT", data.content);
  },
  async fetchFriendInvitations({ commit }) {
    const { data } = await session.get(
      `${process.env.VUE_APP_BACK_BASE_URL}/relations/pending_invitations/`
    );
    commit("SET_FRIEND_INV_SENT", data.sent);
    commit("SET_FRIEND_INV_RECEIVED", data.received);
  },
  async fetchFriends({ commit }) {
    const { data } = await session.get(
      `${process.env.VUE_APP_BACK_BASE_URL}/relations/`
    );
    commit("SET_FRIENDS", data);
  },
  async acceptInvitation({ commit }, pk) {
    const { data } = await session.get(
      `${process.env.VUE_APP_BACK_BASE_URL}/relations/accept_invitation/?pk=${pk}`
    );
    commit("REMOVE_INVITATION", pk);
    commit("SET_FRIEND", data.content);
  },
  async createMeal({ commit }, { restaurantId, time, guests }) {
    const { data } = await session.post(
      `${process.env.VUE_APP_BACK_BASE_URL}/meals/`,
      {
        meal: {
          restaurant_id: restaurantId,
          time,
          guests
        }
      }
    );
    if (data.message !== "OK") {
      return "error";
    }
    commit("SET_MEAL", data.content);
    return "created";
  },
  async fetchMeals({ commit }) {
    const { data } = await session.get(
      `${process.env.VUE_APP_BACK_BASE_URL}/meals/`
    );
    commit("SET_MEALS", data);
  },
  async acceptMealInvitation({ commit }, pk) {
    const { data } = await session.get(
      `${process.env.VUE_APP_BACK_BASE_URL}/meals/accept_invitation/?pk=${pk}`
    );
    commit("REMOVE_MEAL_INVITATION", pk);
    commit("SET_MEAL", data.content);
  }
};

const mutations = {
  SET_CURRENT_USER: (store, userData) => {
    state.currentUser = new UserProfile(userData);
  },
  SET_IS_LOADED: (store, bool) => {
    state.isLoaded = bool;
  },
  LOADER_CREATION_MEAL: (store, bool) => {
    state.creationMealLoader = bool;
  },
  SET_CITIES: (store, cities) => {
    cities.forEach(cityData => {
      const city = new City(cityData);
      state.cities.push(city);
    });
  },
  SET_CURRENT_USER_RESTAURANTS: (store, restaurants) => {
    restaurants.forEach(restaurantData => {
      const restaurant = new Restaurant(restaurantData);
      state.currentUser.restaurants.push(restaurant);
    });
  },
  SET_FRIEND_INV_SENT: (store, invitations) => {
    state.currentUser.friends.invitations.sent = [];
    state.currentUser.friends.invitations.sent = invitations;
  },
  SET_FRIEND_INV_RECEIVED: (store, invitations) => {
    state.currentUser.friends.invitations.received = [];
    state.currentUser.friends.invitations.received = invitations;
  },
  SET_SINGLE_FRIEND_INV_SENT: (store, invitation) => {
    state.currentUser.friends.invitations.sent.push(invitation);
  },
  REMOVE_INVITATION: (store, pk) => {
    state.currentUser.friends.invitations.received.splice(
      state.currentUser.friends.invitations.received.findIndex(
        v => v.id === pk
      ),
      1
    );
  },
  SET_FRIEND: (store, friend) => {
    const userProfile = new UserProfile(friend);
    state.currentUser.friends.list.push(userProfile);
  },
  SET_FRIENDS: (store, friends) => {
    state.currentUser.friends.list = [];
    friends.forEach(userProfileData => {
      const userProfile = new UserProfile(userProfileData);
      state.currentUser.friends.list.push(userProfile);
    });
  },
  REMOVE_MEAL_INVITATION: (store, pk) => {
    state.currentUser.meals.pending.splice(
      state.currentUser.meals.pending.findIndex(v => v.pk === pk),
      1
    );
  },
  SET_MEAL: (store, mealData) => {
    state.currentUser.meals.current.push(new Meal(mealData));
  },
  SET_MEALS: (store, meals) => {
    state.currentUser.meals = {
      pending: [],
      current: [],
      closed: []
    };
    meals.forEach(mealData => {
      if (mealData.meal.closed === false) {
        if (mealData.status === true) {
          state.currentUser.meals.current.push(new Meal(mealData));
        } else {
          state.currentUser.meals.pending.push(new Meal(mealData));
        }
      } else {
        state.currentUser.meals.closed.push(new Meal(mealData));
      }
    });
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
