from django.contrib import admin
from .models import (TourCurrency, TouristRegion, TypeTour, InsuranceConditions, Collection, Language,
                     Location, ComfortLevel, DifficultyLevel, Country, )


admin.site.register(DifficultyLevel)
admin.site.register(ComfortLevel)
admin.site.register(TypeTour)
admin.site.register(InsuranceConditions)

#difficulty_level, comfort_level, type_tour, insurance_conditions