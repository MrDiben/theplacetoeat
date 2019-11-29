from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from location import views as location_views
from meal import views as meal_views
from place import views as place_views
from relation import views as relation_views
from user import views as user_views

api_router = routers.SimpleRouter()

api_router.register(r"restaurants", place_views.RestaurantViewSet)
api_router.register(r"users", user_views.UserProfileViewSet)
api_router.register(r"cities", location_views.CityViewSet)
api_router.register(r"relations", relation_views.RelationViewSet, basename="relation")
api_router.register(r"meals", meal_views.MealViewSet, basename="meal")


urlpatterns = [
    #   Application URLs
    path("api/", include(api_router.urls)),
    #   Auhentication URLs
    path("api/rest-auth/get-token/", obtain_auth_token, name="api_token_auth"),
    path("api/rest-auth/", include("rest_auth.urls")),
    path("api/rest-auth/signup/", include("rest_auth.registration.urls")),
]
