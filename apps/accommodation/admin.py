from django.contrib import admin

from apps.accommodation.models import Place, PlaceResidence, PlaceResidenceImages

admin.site.register(Place)
admin.site.register(PlaceResidence)
admin.site.register(PlaceResidenceImages)
