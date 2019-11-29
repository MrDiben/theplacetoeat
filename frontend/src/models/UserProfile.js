export default class UserProfile {
  constructor(userProfile) {
    this.setData(userProfile);
  }

  setData(userProfile) {
    if (!userProfile) {
      userProfile = {
        user: {},
        city: {
          country: {}
        }
      };
    }
    this.email = userProfile.user.email ? userProfile.user.email : "";
    this.first_name = userProfile.user.first_name
      ? userProfile.user.first_name
      : "";
    this.last_name = userProfile.user.last_name
      ? userProfile.user.last_name
      : "";
    this.username = userProfile.user.username ? userProfile.user.username : "";
    if (userProfile.city !== null) {
      this.city = {
        name: userProfile.city.name ? userProfile.city.name : "",
        latitude: userProfile.city.latitude ? userProfile.city.latitude : "",
        longitude: userProfile.city.longitude ? userProfile.city.longitude : "",
        country: {
          name: userProfile.city.country.name
            ? userProfile.city.country.name
            : ""
        }
      };
    } else {
      this.city = {
        country: { name: "" },
        name: "",
        latitude: "",
        longitude: ""
      };
    }
    this.restaurants = [];
    (this.friends = {
      invitations: {
        sent: [],
        received: []
      },
      list: []
    }),
      (this.meals = {
        pending: [],
        current: [],
        closed: []
      });
  }

  getNameOrEmail() {
    if (this.first_name) {
      return `${this.first_name} ${this.last_name}`;
    }
    return this.email;
  }
}
