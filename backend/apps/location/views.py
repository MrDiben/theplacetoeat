from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import CitySerializer
from .models import City


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing cities.
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
