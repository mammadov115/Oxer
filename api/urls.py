from django.urls import path
from .views import *

urlpatterns = [
    path("contact-info/", ContactListCreateUpdateDeleteView.as_view(), name="contact-info"),
    path("slider-text/", SliderListCreateUpdateDeleteView.as_view(), name="slider-text"),
    path("about-section/", AboutListCreateUpdateDeleteView.as_view(), name="about-section"),
    path("classes-section/", ClassesListCreateUpdateDeleteView.as_view(), name="classes-section"),
    path("images/", ImageListCreateView.as_view(), name="images"),
    path("images/<int:pk>/", ImageRetrieveUpdateDeleteView.as_view(), name="image-detail"),
    path("blogs-section/", BlogsSectionListCreateUpdateDeleteView.as_view(), name="blogs-section")

]
