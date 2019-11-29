from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for viewing userprofiles.
    """

    queryset = UserProfile.objects.filter(user__is_active=True)
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if "current" in self.request.GET:
            #   Only return current user
            return self.queryset.filter(user=self.request.user)
        elif self.request.GET.get("query"):
            return self.queryset.filter(
                user__username__icontains=self.request.GET.get("query")
            ).exclude(user=self.request.user)
        return self.queryset
