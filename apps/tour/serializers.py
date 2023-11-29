from rest_framework import serializers

from apps.guide.models import Guide
from apps.tour.models import Tour, Question
from apps.days.models import Days, DaysImage
from apps.tour_images.models import TourImages
from apps.cancel_reservation.models import CancelReservation
from apps.impressions.models import Impression, ImpressionImages
from apps.tour_description.models import TourDescription, DescriptionDetail
from apps.tags.models import Collection, Country, Activity, Location, TouristRegion, City
from apps.accommodation.models import (Accommodation, Hotel, HotelImages, AccommodationImages,
                                       AnotherHotel, AnotherHotelImages)

from apps.tags.serializers import (CollectionSerializer, CountrySerializer, LocationSerializer,
                                   TouristRegionSerializer, ActivitySerializer, CitySerializer)
from apps.cancel_reservation.serializers import CancelReservationSerializer
from apps.tour_description.serializers import TourDescriptionSerializer
from apps.accommodation.serializers import AccommodationSerializer
from apps.tour_images.serializers import TourImagesSerializer
from apps.impressions.serializers import ImpressionSerializer
from apps.guide.serializers import GuideSerializer
from apps.days.serializers import DaysSerializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'answer')


class TourSerializer(serializers.ModelSerializer):
    cancel_reservation = CancelReservationSerializer(many=True)
    tour_description = TourDescriptionSerializer(many=True)
    accommodations = AccommodationSerializer(many=True)
    tour_images = TourImagesSerializer(many=True)
    impression = ImpressionSerializer(many=True)
    question = QuestionSerializer(many=True)
    guide = GuideSerializer(many=True)
    days = DaysSerializer(many=True)

    city = CitySerializer(many=True)
    country = CountrySerializer(many=True)
    activity = ActivitySerializer(many=True)
    location = LocationSerializer(many=True)
    collection = CollectionSerializer(many=True)
    tourist_region = TouristRegionSerializer(many=True)

    class Meta:
        model = Tour
        fields = ('slug', 'title', 'language', 'amount_of_days', 'min_people', 'max_people',
                  'min_age', 'max_age', 'difficulty_level', 'comfort_level', 'tour_currency', 'type_tour',
                  'recommendations', 'list_of_things', 'insurance_conditions', 'included_in_the_price',
                  'not_included_in_the_price', 'tour_description', 'tour_images', 'days', 'accommodations', 'guide',
                  'question', 'impression', 'cancel_reservation', 'activity', 'country', 'collection', 'location',
                  'tourist_region', 'city', 'address_point', 'description_point', 'is_active', 'create_date')

    def create(self, validated_data):
        cancel_reservations_data = validated_data.pop('cancel_reservation')
        tour_descriptions_data = validated_data.pop('tour_description')
        accommodation_data = validated_data.pop('accommodations')
        tour_images_data = validated_data.pop('tour_images')
        impression_data = validated_data.pop('impression')
        questions_data = validated_data.pop('question')
        guide_data = validated_data.pop('guide')
        days_data = validated_data.pop('days')

        city_data = validated_data.pop('city')
        countries_data = validated_data.pop('country')
        locations_data = validated_data.pop('location')
        activities_data = validated_data.pop('activity')
        collections_data = validated_data.pop('collection')
        tourist_regions_data = validated_data.pop('tourist_region')

        tour = Tour.objects.create(**validated_data)

        for cities_data in city_data:
            city, created = City.objects.get_or_create(**cities_data)
            tour.city.add(city)

        for activity_data in activities_data:
            activity, created = Activity.objects.get_or_create(**activity_data)
            tour.activity.add(activity)

        for collection_data in collections_data:
            collection, created = Collection.objects.get_or_create(**collection_data)
            tour.collection.add(collection)

        for country_data in countries_data:
            country, created = Country.objects.get_or_create(**country_data)
            tour.country.add(country)

        for location_data in locations_data:
            location, created = Location.objects.get_or_create(**location_data)
            tour.location.add(location)

        for tourist_region_data in tourist_regions_data:
            tourist_region, created = TouristRegion.objects.get_or_create(**tourist_region_data)
            tour.tourist_region.add(tourist_region)

        for question_data in questions_data:
            Question.objects.create(tour=tour, **question_data)

        for guides_data in guide_data:
            guides_data.pop('guide', [])
            Guide.objects.create(tour=tour, **guides_data)

        for tour_image_data in tour_images_data:
            tour_image_data.pop('tour_images', [])
            TourImages.objects.create(tour=tour, **tour_image_data)

        for day_data in days_data:
            days_images_data = day_data.pop('days_images', [])
            days = Days.objects.create(tour=tour, **day_data)

            for image_data in days_images_data:
                DaysImage.objects.create(day=days, **image_data)

        for cancel_reservation_data in cancel_reservations_data:
            cancel_reservation_data.pop('cancel_reservation', [])
            CancelReservation.objects.create(tour=tour, **cancel_reservation_data)

        for impressions_data in impression_data:
            impression_image_data = impressions_data.pop('impression_images', [])
            impressions = Impression.objects.create(tour=tour, **impressions_data)

            for impression_images_data in impression_image_data:
                ImpressionImages.objects.create(impression=impressions, **impression_images_data)

        for tour_description_data in tour_descriptions_data:
            description_details_data = tour_description_data.pop('description_details', [])
            tour_descriptions = TourDescription.objects.create(tour=tour, **tour_description_data)

            for details_data in description_details_data:
                DescriptionDetail.objects.create(tour_description=tour_descriptions, **details_data)

        for accommodations_data in accommodation_data:
            hotel_data = accommodations_data.pop('hotels', [])
            accommodation_image_data = accommodations_data.pop('accommodation_images', [])
            accommodations = Accommodation.objects.create(tour=tour, **accommodations_data)

            for accommodation_images_data in accommodation_image_data:
                AccommodationImages.objects.create(accommodation=accommodations, **accommodation_images_data)

            for hotels_data in hotel_data:
                hotels_images_data = hotels_data.pop('hotel_images', [])
                another_hotels_data = hotels_data.pop('another_hotels', [])
                hotels = Hotel.objects.create(accommodation=accommodations, **hotels_data)

                for hotel_image_data in hotels_images_data:
                    HotelImages.objects.create(hotel=hotels, **hotel_image_data)

                for another_hotels_data in another_hotels_data:
                    another_hotels_images_data = another_hotels_data.pop('another_hotel_images', [])
                    another_hotels = AnotherHotel.objects.create(hotel=hotels, **another_hotels_data)

                    for another_hotel_images_data in another_hotels_images_data:
                        AnotherHotelImages.objects.create(another_hotel=another_hotels, **another_hotel_images_data)

        return tour
