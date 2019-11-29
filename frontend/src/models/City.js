export default class City {
  constructor(city) {
    this.setData(city);
  }

  setData(city) {
    if (!city) {
      city = {};
    }
    this.name = city.name ? city.name : "";
    this.latitude = city.latitude ? city.latitude : null;
    this.longitude = city.longitude ? city.longitude : null;
    this.country = {
      name: city.country.name ? city.country.name : ""
    };
  }
}
