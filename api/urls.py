from django.urls import path
from .views import *

urlpatterns = [
    path("contact-info/", ContactListCreateUpdateDeleteView.as_view(), name="contact-info"),
    path("slider-text/", SliderListCreateUpdateDeleteView.as_view(), name="slider-text")

]
