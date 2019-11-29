from user.models import UserProfile
from user.serializers import UserProfileSerializer
from relation.serializers import FriendShipSerializer
from relation.models import FriendShip
from django.shortcuts import get_object_or_404
from rest_framework import status as rest_status
from django.utils.translation import gettext as _
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)


class RelationViewSet(viewsets.ViewSet):
    """
    A simple ViewSet to create/list/accept friend invitation
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=["get"])
    def accept_invitation(self, request):
        pk = request.GET.get("pk")
        if not pk:
            return Response(status=rest_status.HTTP_404_NOT_FOUND)

        user = get_object_or_404(UserProfile, user=request.user)
        friendship = get_object_or_404(FriendShip, pk=pk)

        #    Avoid self friendship
        if not friendship.user_2 == user:
            return Response(status=rest_status.HTTP_404_NOT_FOUND)

        #   Accept friend invitation
        friendship.status = 1
        friendship.save()

        serializer = UserProfileSerializer(friendship.user_1)
        data = {"message": "OK", "content": serializer.data}

        return Response(data, status=rest_status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def pending_invitations(self, request):
        """ Return all sent and received pending invitations """

        user_profile = get_object_or_404(UserProfile, user=request.user)
        #   Get all sent pending invitation
        sent = user_profile.creator_friendships.filter(status=0)
        #  Get all received pending invitation
        received = user_profile.invited_friendships.filter(status=0)
        #   Serialize all and create a dict from it
        data = {"sent": [], "received": []}
        for friendship in sent:
            data["sent"].append(FriendShipSerializer(friendship).data)
        for friendship in received:
            data["received"].append(FriendShipSerializer(friendship).data)
        #   Return response with these 2 informations
        return Response(data, status=rest_status.HTTP_200_OK)

    def create(self, request):
        """ Invite friend based on email """

        invited_email = request.data.get("email")
        status = request.data.get("status", False)
        if not invited_email:
            return Response(status=rest_status.HTTP_404_NOT_FOUND)
        try:
            invited_user = UserProfile.objects.get(user__email=invited_email)
        except UserProfile.DoesNotExist:
            return Response(status=rest_status.HTTP_404_NOT_FOUND)

        user_sending = get_object_or_404(UserProfile, user=request.user)

        if user_sending == invited_user:
            return Response(status=rest_status.HTTP_404_NOT_FOUND)

        error = ""
        try:
            friendship, _created = FriendShip.objects.get_or_create(
                user_1=user_sending, user_2=invited_user, status=status
            )
            if not _created:
                if friendship.status:
                    error = _("You already are friend with this user")
                else:
                    error = _("A pending invitation is already created")
        except Exception:
            error = _(
                f"An error occured when user {user_sending.user.email} invited {invited_user.user.email}"
            )

        data = {}
        status = rest_status.HTTP_200_OK
        if error:
            status = rest_status.HTTP_400_BAD_REQUEST
            data["message"] = error
        else:
            serializer = FriendShipSerializer(friendship)
            data["message"] = "OK"
            data["content"] = serializer.data
        return Response(data, status=status)

    def list(self, request):
        """ List all user friends based on accepted invitations """

        user_profile = get_object_or_404(UserProfile, user=request.user)
        #   Get all sent accepted invitations
        sent = user_profile.creator_friendships.filter(status=1)
        #   Get all received accepted invitations
        received = user_profile.invited_friendships.filter(status=1)
        #    Combine results to get all friends:
        friends = []
        for friendship in sent:
            friends.append(UserProfileSerializer(friendship.user_2).data)
        for friendship in received:
            friends.append(UserProfileSerializer(friendship.user_1).data)
        return Response(friends, status=rest_status.HTTP_200_OK)
