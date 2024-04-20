from django.urls import path

from apps.concrete_tour.views import BookingTourCreate, BookingTourList, BookingTourDetail, ConcreteTourDateCreate, \
    BookingCRMView, ConcreteTourDateList

urlpatterns = [
    path('booking/create/', BookingTourCreate.as_view(), name='booking_tour-create'),
    path('booking/list/', BookingTourList.as_view(), name='booking_tour-list'),
    path('booking/detail/<int:pk>/', BookingTourDetail.as_view(), name='booking_tour-detail'),

    path('concrete_date/create/', ConcreteTourDateCreate.as_view(), name='concrete_tour_date-create'),
    path('concrete_date/list/', ConcreteTourDateList.as_view(), name='concrete_tour_date-list'),

    path('booking/crm/', BookingCRMView.as_view(), name='booking-crm'),

]
