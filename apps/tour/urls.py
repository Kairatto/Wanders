from django.urls import path

from apps.tour.views import TourCreate, TourListDev, TourListView, TourDetail, TourAuthorList, ConcreteTourDateCRMView

urlpatterns = [
    path('create/', TourCreate.as_view(), name='tour-create'),
    path('dev/', TourListDev.as_view(), name='tour-list-dev'),
    path('list/', TourListView.as_view(), name='tour-list'),
    path('author_list/', TourAuthorList.as_view(), name='tour_author-list'),
    path('detail/<int:pk>/', TourDetail.as_view(), name='tour-detail'),

    path('crm/', ConcreteTourDateCRMView.as_view(), name='tour-crm'),

]
