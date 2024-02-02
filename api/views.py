from django.shortcuts import render
from app.models import *
from .serializers import *

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ContactListCreateUpdateDeleteView(APIView):
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        contact_info = Contact.objects.first()
        serializer = self.serializer_class(instance=contact_info)
        if not contact_info:
            return Response(data={"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        objects = Contact.objects.count()
        if objects == 0:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
            
                response = {
                    "message": "Contact info created",
                    "data": serializer.data
                }
                
                return Response(data=response, status=status.HTTP_201_CREATED)
            return Response(data={"message": "There are some errors in the data"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": "Contact info currently available."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request):
        contact_info = Contact.objects.first()
        if contact_info:
            data = request.data
            serializer = self.serializer_class(instance=contact_info, data=data)
            if serializer.is_valid():
                serializer.save()

                response = {
                    "message": "Contact info updated",
                    "data": data
                }

                return Response(data=response, status=status.HTTP_200_OK)
            return Response(data={"message": "There are some errors in the data."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": "There is no data to update"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        Contact.objects.all().delete()

        return Response(data={"message":"Contact info successfully deleted."}, status=status.HTTP_200_OK)


class SliderListCreateUpdateDeleteView(APIView):
    serializer_class = SliderSerializer

    def get(self, request, *args, **kwargs):
        slider_text = Slider.objects.first()
        serializer = self.serializer_class(instance=slider_text)
        if not slider_text:
            return Response(data={"message": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        objects = Slider.objects.count()
        if objects==0:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()

                reponse = {
                    "message": "Slider object created",
                    "data": serializer.data
                }

                return Response(data=reponse, status=status.HTTP_201_CREATED)
            return Response(data={"message": "There are some errors in the data"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"Slider data currently available"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request):
        slider_text = Slider.objects.first()
        if slider_text:
            serializer = self.serializer_class(instance=slider_text, data=request.data)
            if serializer.is_valid():
                old_data = self.serializer_class(slider_text).data
                del old_data["id"]
                new_data = serializer.validated_data
                if old_data != new_data:
                    serializer.save()

                    response = {
                        "message": "Slider object successfully updated",
                        "data": serializer.validated_data
                    }

                    return Response(data=response, status=status.HTTP_200_OK)
                return Response(data={"message": "The updated data is the same as the current data"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(data={"message": "There are some errors in the data"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": "There is no data to update"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        objects = Slider.objects.all()
        if objects:
            objects.delete()
            return Response(data={"message": "Slider object successfully deleted."}, status=status.HTTP_200_OK)
        return Response(data={"message": "There is nothing to delete"}, status=status.HTTP_404_NOT_FOUND)
        