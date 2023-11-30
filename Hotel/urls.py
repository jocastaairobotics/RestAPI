from django.urls import path, include
from .views import HotelView, HotelListView, HotelCreateView, HotelUpdateView, HotelRetrieveView, HotelDeleteView, HotelViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("santoshi", HotelViewset, basename="HotelViewset")

urlpatterns = [
    path("hotel", HotelView.as_view(), name="HotelView"),
    path("list", HotelListView.as_view(), name="HotelView"),
    path("<pk>/get", HotelRetrieveView.as_view(), name="HotelRetrieveView"),
    path("create", HotelCreateView.as_view(), name="HotelCreateView"),
    path("<pk>/update", HotelUpdateView.as_view(), name="HotelUpdateView"),
    path("<pk>/delete", HotelDeleteView.as_view(), name="HotelDeleteView"),
    path("api/", include(router.urls))
]