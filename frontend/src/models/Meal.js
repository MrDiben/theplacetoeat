export default class Meal {
  constructor(mealData) {
    this.setData(mealData);
  }

  setData(mealData) {
    this.mealInfo = {
      datehour: mealData.meal.datehour,
      restaurant: mealData.meal.restaurant,
      closed: mealData.meal.closed
    };
    this.pk = mealData.pk;
    this.users = [];
    this.accepted = mealData.status;
    mealData.users.forEach(userMeal => {
      this.users.push({
        is_creator: userMeal.is_creator,
        user: userMeal.user.user,
        is_accepted: userMeal.status
      });
    });
  }
}
