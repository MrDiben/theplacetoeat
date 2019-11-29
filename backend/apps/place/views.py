from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import RestaurantSerializer
from .models import Restaurant


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing restaurants.
    """

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=["get"])
    def user_recommendations(self, request):
        user_profile = self.request.user.user_profile
        #  Get all recommendations for user
        recommendations = user_profile.recommendations.all()
        restaurants = [recommendation.restaurant for recommendation in recommendations]
        restaurants_serializer = RestaurantSerializer(restaurants, many=True)
        return Response(restaurants_serializer.data)
