from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import gettext as _
from django.db import transaction
from django.utils.timezone import make_aware

from place.models import Restaurant, OpenHour
from location.models import City, Country
from ratings.models import Review, Rating
from photos.models import Photo

import simplejson as json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


GOOGLE_MATCHING_DAYS = {
    0: _("Sunday"),
    1: _("Monday"),
    2: _("Tuesday"),
    3: _("Wednesday"),
    4: _("Thursday"),
    5: _("Friday"),
    6: _("Saturday"),
}


class Command(BaseCommand):
    help = "Get google places datas"

    def add_arguments(self, parser):
        parser.add_argument("--files", "-f", nargs="?", type=str, required=True)

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Save json to db"))
        files = options.get("files")
        if files:
            files = files.split(",")
        else:
            raise CommandError(
                "You must provide files argument with coma separated, example: file1.json,file2.json"
            )

        self.count = 0
        for file_name in files:
            with open(f"datas/{file_name}", "r") as data_file:
                self.stdout.write(self.style.SUCCESS(f"Processing {file_name}"))
                datas = json.load(data_file)
                for place in datas:
                    self.create_or_update_place(place)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully update or create {self.count} places")
        )

    def create_or_update_place(self, place):
        place_obj, place_obj_created = Restaurant.objects.get_or_create(
            google_place_id=place["place_id"]
        )
        city_name, country_name = self._get_place_locations(
            place["details"]["address_components"]
        )

        place_obj.name = place["name"]

        #   Get place city
        country, country_created = Country.objects.update_or_create(name=country_name)
        city, city_created = City.objects.update_or_create(name=city_name, country=country)
        place_obj.city = city

        #   Get place openhours
        if place["details"].get("opening_hours"):
            for period in place["details"]["opening_hours"]["periods"]:
                day, openhour, closehour = self._get_days_open_close_hours(period)
                #  Case when place opened 24/7
                if openhour == closehour:
                    times = [("11:00", "14:00"), ("18:30", "22:00")]
                    for time in times:
                        OpenHour.objects.update_or_create(
                            restaurant=place_obj,
                            week_day=day,
                            open_hour=time[0],
                            close_hour=time[1],
                        )
                else:
                    OpenHour.objects.update_or_create(
                        restaurant=place_obj,
                        week_day=day,
                        open_hour=openhour,
                        close_hour=closehour,
                    )
        else:
            logger.warning(
                f"No Opening hours for place {place_obj.name} {place_obj.google_place_id}"
            )

        #   Store reviews:
        if place["details"].get("reviews"):
            for review in place["details"]["reviews"]:
                Review.objects.update_or_create(
                    restaurant=place_obj,
                    author_name=review["author_name"],
                    author_url=review["author_url"],
                    profile_photo_url=review["profile_photo_url"],
                    rating=review["rating"],
                    relative_time_description=review["relative_time_description"],
                    content=review["text"],
                    created_at=make_aware(datetime.fromtimestamp(review["time"])),
                )
        else:
            logger.warning(
                f"No Reviews for place {place_obj.name} {place_obj.google_place_id}"
            )

        #   Get Google Rating:
        rating, created = Rating.objects.get_or_create(restaurant=place_obj)
        if place.get("rating"):
            rating.google_rating_average = place["rating"]
        if place["details"].get("user_ratings_total"):
            rating.google_user_ratings_total = place["details"]["user_ratings_total"]
        rating.save()

        #    Get latitude longitude:
        place_obj.latitude = place["geo_location"]["lat"]
        place_obj.longitude = place["geo_location"]["lng"]

        #    Get phone number:
        place_obj.phone_number = place["international_phone_number"]

        #    Get photos:
        for photo in place["photos"]:
            Photo.objects.update_or_create(
                restaurant=place_obj,
                filename=photo["filename"],
                width=photo["orig_width"],
                height=photo["orig_height"],
                url=photo["url"],
                google_photo_reference=photo["photo_reference"],
            )

        place_obj.google_map_url = place["url"]
        place_obj.formatted_address = place["vicinity"]
        place_obj.website = place["website"]

        place_obj.is_active = not place["permanently_closed"]
        place_obj.from_google = True

        place_obj.save()

        self.count += 1

    def _get_place_locations(self, address_components):
        city = None
        country = None
        for component in address_components:
            if "locality" in component["types"]:
                city = component["long_name"]
            elif "country" in component["types"]:
                country = component["long_name"]
        #   Handle google places errors:
        if city and country:
            city = self._handle_gplaces_city_errors(city, country)
        return city, country

    def _handle_gplaces_city_errors(self, address_part, country):
        #   address_part can be a city or a full address
        if "Lion" in address_part and country == "France":
            return "Lyon"
        if "Lyon-Villeurbanne" in address_part and country == "France":
            address_part = address_part.replace("Lyon-Villeurbanne", "Villeurbanne")
        return address_part

    def _get_days_open_close_hours(self, period):
        day = GOOGLE_MATCHING_DAYS[period["open"]["day"]]
        openhour = f"{period['open']['time'][:2]}:{period['open']['time'][-2:]}"

        closehour = None
        if period.get("close"):
            closehour = f"{period['close']['time'][:2]}:{period['close']['time'][-2:]}"
        else:
            #  It means open 24/24
            closehour = openhour

        return day, openhour, closehour
