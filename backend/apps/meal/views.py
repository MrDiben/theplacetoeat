from datetime import datetime, date

from user.models import UserProfile
from meal.serializers import InvitationMealSerializer, MealSerializer
from meal.models import Meal, InvitationMeal
from place.models import Restaurant
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import status as rest_status
from django.utils.translation import gettext as _
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)


class MealViewSet(viewsets.ViewSet):
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
        invitation_meal = get_object_or_404(InvitationMeal, pk=pk)

        if not invitation_meal.user == user:
            return Response(status=rest_status.HTTP_404_NOT_FOUND)

        #   Accept friend invitation
        invitation_meal.status = True
        invitation_meal.save()

        meal_data = self.get_meal_with_users(invitation_meal, user)
        data = {"message": "OK", "content": meal_data}

        return Response(data, status=rest_status.HTTP_200_OK)

    def create(self, request):
        meal = request.data.get("meal")  # DateHour with restaurant id
        invited_user_emails = meal.get("guests", [])  # user email list

        if not meal:
            return Response(status=rest_status.HTTP_404_NOT_FOUND)

        try:
            user = get_object_or_404(UserProfile, user=request.user)
            restaurant = get_object_or_404(Restaurant, pk=meal["restaurant_id"])
            #  Convert hour to valid datetime with now date and sent hour
            time = datetime.strptime(meal["time"], "%H:%M").time()
            datehour = datetime.combine(date.today(), time)
        except KeyError:
            return Response(status=rest_status.HTTP_404_NOT_FOUND)

        data = {"message": "", "content": {}}
        with transaction.atomic():
            try:
                created_meal, _created = Meal.objects.get_or_create(
                    creator=user, restaurant=restaurant, datehour=datehour
                )
                #  Set status to already accepted
                creator_invitation_meal, _created = InvitationMeal.objects.get_or_create(
                    user=user, meal=created_meal, status=True
                )
                if _created:
                    data["message"] = "OK"
                else:
                    data["message"] = _(
                        "Unable to create meal, please make sure you have not already saved the same meal"
                    )
            except Exception as e:
                data["message"] = _("Unable to create meal, an unknown error occured")
                logger.error(e)
                return Response(data, status=rest_status.HTTP_200_OK)

            try:

                for invited_user_email in invited_user_emails:
                    InvitationMeal.objects.get_or_create(
                        user=UserProfile.objects.get(user__email=invited_user_email),
                        meal=created_meal,
                        status=0,
                    )
            except UserProfile.DoesNotExist:
                data["message"] = _(
                    "Unable to create invitation meal for invited users, some users does not exist"
                )
            except Exception as e:
                data["message"] = _(
                    "Unable to create invitation meal for invited users, please try later"
                )
                logger.error(e)

        data["content"] = self.get_meal_with_users(creator_invitation_meal, user)
        return Response(data, status=rest_status.HTTP_200_OK)

    def get_meal_with_users(self, meal, user):
        meal_data = {}
        meal_data["meal"] = MealSerializer(meal.meal).data
        meal_data["pk"] = meal.pk
        meal_data["status"] = meal.status
        meal_data["users"] = []
        other_users_meal = InvitationMeal.objects.filter(meal=meal.meal)
        for other_user_meal in other_users_meal:
            meal_data["users"].append(InvitationMealSerializer(other_user_meal).data)
        return meal_data

    def list(self, request):
        user = get_object_or_404(UserProfile, user=request.user)
        meals = InvitationMeal.objects.filter(user=user)
        data = []
        for meal in meals:
            meal_data = self.get_meal_with_users(meal, user)
            data.append(meal_data)
        return Response(data, status=rest_status.HTTP_200_OK)
