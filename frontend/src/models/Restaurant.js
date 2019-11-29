import Photo from "./Photos.js";
import formatDate from "../utils/formatDate";

[
  {
    id: 14,
    week_day: "Friday",
    open_hour: "11:00:00",
    close_hour: "23:00:00",
    restaurant: 11
  }
];
export default class Restaurant {
  constructor(restaurant) {
    this.setData(restaurant);
  }

  setData(restaurant) {
    if (!restaurant) {
      restaurant = {
        photos: [],
        rating: {},
        city: { country: {} },
        cook_types: []
      };
    }
    this.photos = [];
    if (restaurant.photos.length > 0) {
      restaurant.photos.forEach(photo => {
        this.photos.push(new Photo(photo));
      });
    }
    this.cook_types = restaurant.cook_types;
    this.price_indicator = restaurant.price_indicator;
    this.id = restaurant.id;
    this.name = restaurant.name ? restaurant.name : "";
    this.description = restaurant.description ? restaurant.description : "";
    this.website = restaurant.website ? restaurant.website : "";
    this.latitude = restaurant.latitude ? restaurant.latitude : null;
    this.longitude = restaurant.longitude ? restaurant.longitude : null;
    this.formatted_address = restaurant.formatted_address
      ? restaurant.formatted_address
      : "";
    this.phone_number = restaurant.phone_number ? restaurant.phone_number : "";
    this.google_place_id = restaurant.google_place_id
      ? restaurant.google_place_id
      : "";
    this.google_map_url = restaurant.google_map_url
      ? restaurant.google_map_url
      : "";
    this.photo_header = restaurant.photo_header ? restaurant.photo_header : "";
    this.rating = {
      google_rating_average: restaurant.rating.google_rating_average
        ? restaurant.rating.google_rating_average
        : null,
      google_user_ratings_total: restaurant.rating.google_user_ratings_total
        ? restaurant.rating.google_user_ratings_total
        : null,
      rating_average: restaurant.rating.rating_average
        ? restaurant.rating.rating_average
        : null,
      user_ratings_total: restaurant.rating.user_ratings_total
        ? restaurant.rating.user_ratings_total
        : null
    };
    this.city = {
      name: restaurant.city.name ? restaurant.city.name : "",
      latitude: restaurant.city.latitude ? restaurant.city.latitude : "",
      longitude: restaurant.city.longitude ? restaurant.city.longitude : "",
      country: {
        name: restaurant.city.country.name ? restaurant.city.country.name : ""
      }
    };
    this.todayHours = [];
    this.timeSelection = [];
    if (restaurant.today_hours.length > 0) {
      restaurant.today_hours.forEach(today_hour => {
        const openHour = today_hour.open_hour.substring(0, 5);
        const closeHour = today_hour.close_hour.substring(0, 5);
        this.timeSelection = this.timeSelection.concat(
          formatDate.getIntervals(openHour, closeHour, 1, 15)
        );
        const displayHour = `${openHour} - ${closeHour}`;
        this.todayHours.push({
          id: today_hour.id,
          openHour,
          closeHour,
          displayHour
        });
      });
    }
    this.timeSelection.sort();
  }
}
