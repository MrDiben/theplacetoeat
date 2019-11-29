from django.core.management.base import BaseCommand
from googleplaces import GooglePlaces, types, lang

from django.conf import settings

import simplejson as json


class Command(BaseCommand):
    help = "Get google places datas"

    def add_arguments(self, parser):
        parser.add_argument("--number", "-n", nargs="?", type=int)
        parser.add_argument("--latitude", "-lat", required=True)
        parser.add_argument("--longitude", "-lng", required=True)

    def handle(self, *args, **options):
        longitude = options.get("longitude")
        latitude = options.get("latitude")
        number = options.get("number")
        if number:
            self.number = number
        else:
            self.number = 60  # default limit from google places api doc

        YOUR_API_KEY = settings.GOOGLE_API_KEY

        self.google_places = GooglePlaces(YOUR_API_KEY)

        # You may prefer to use the text_search API, instead.
        query_result = self.google_places.nearby_search(
            lat_lng={"lat": latitude, "lng": longitude},
            radius=400,
            language=lang.FRENCH,
            types=[types.TYPE_FOOD, types.TYPE_RESTAURANT, types.TYPE_MEAL_TAKEAWAY],
        )
        self.count = 0
        self.get_page_places(query_result)

        self.stdout.write(self.style.SUCCESS(f"{self.count} PLACES LOADED"))

    def get_page_places(self, query_result, page=1):
        places_list = []
        for place in query_result.places:
            self.count += 1
            place_dict = {}
            # Returned places from a query are place summaries.
            place_dict["name"] = place.name
            place_dict["geo_location"] = place.geo_location
            place_dict["place_id"] = place.place_id

            # The following method has to make a further API call.
            place.get_details()
            # Referencing any of the attributes below, prior to making a call to
            # get_details() will raise a GooglePlacesAttributeError.
            place_dict["details"] = place.details
            place_dict["local_phone_number"] = place.local_phone_number
            place_dict["international_phone_number"] = place.international_phone_number
            place_dict["website"] = place.website
            place_dict["url"] = place.url
            place_dict["reference"] = place.reference
            place_dict["vicinity"] = place.vicinity
            place_dict["rating"] = place.rating
            place_dict["types"] = place.types
            place_dict["permanently_closed"] = getattr(place, "permanently_closed", False)

            # Getting place photos
            place_photos = []
            for photo in place.photos:
                place_photo = {}
                place_photo["orig_height"] = photo.orig_height
                place_photo["orig_width"] = photo.orig_width
                place_photo["html_attributions"] = photo.html_attributions
                place_photo["photo_reference"] = photo.photo_reference
                # 'maxheight' or 'maxwidth' is required
                photo.get(maxheight=500, maxwidth=500)
                # MIME-type, e.g. 'image/jpeg'
                place_photo["mimetype"] = photo.mimetype
                # Image URL
                place_photo["url"] = photo.url
                # Original filename (optional)
                place_photo["filename"] = photo.filename
                place_photos.append(place_photo)

            place_dict["photos"] = place_photos
            places_list.append(place_dict)

            if self.count >= self.number:
                break

        with open(f"datas/charpennes_places_{page}.json", "w") as outfile:
            json.dump(places_list, outfile, sort_keys=True, indent=4 * " ")
        # Are there any additional pages of results?
        if query_result.has_next_page_token and self.count < self.number:
            query_result_next_page = self.google_places.nearby_search(
                pagetoken=query_result.next_page_token
            )
            self.get_page_places(query_result_next_page, page=page + 1)
