from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("feedback-section", FeedBackSectionViewSet, basename="feedback-section")
router.register("feedbacks", FeedBackViewSet, basename="feedbacks")
router.register("info-section", InfoSectionViewSet, basename="info-section")
router.register("messages", MessageViewSet, basename="messages")
router.register("social-media-accounts", SocialMediaAccountViewSet, basename="social-media-accounts")

urlpatterns = [
    path("contact-info/", ContactListCreateUpdateDeleteView.as_view(), name="contact-info"),
    path("slider-text/", SliderListCreateUpdateDeleteView.as_view(), name="slider-text"),
    path("about-section/", AboutListCreateUpdateDeleteView.as_view(), name="about-section"),
    path("classes-section/", ClassesListCreateUpdateDeleteView.as_view(), name="classes-section"),
    path("images/", ImageListCreateView.as_view(), name="images"),
    path("images/<int:pk>/", ImageRetrieveUpdateDeleteView.as_view(), name="image-detail"),
    path("blogs-section/", BlogsSectionListCreateUpdateDeleteView.as_view(), name="blogs-section"),
    path("blogs/", BlogListCreateView.as_view(), name="blogs"),
    path("blog-detail/<int:pk>", BlogRetrieveUpdateDeleteView.as_view(), name="blog-detail"),
    path("", include(router.urls))

]
