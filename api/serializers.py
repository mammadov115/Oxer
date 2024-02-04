from rest_framework import serializers
from app.models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

class BlogsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsSection
        fields = "__all__"