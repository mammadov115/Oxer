from django.shortcuts import render
from app.models import *
from .serializers import *

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins

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


class AboutListCreateUpdateDeleteView(APIView):
    serializer_class = AboutSerializer

    def get(self, request, *args, **kwargs):
        about_section = About.objects.first()
        serializer = self.serializer_class(instance=about_section)
        if not about_section:
            return Response(data={"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(data={"data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        objects = About.objects.first()
        if not objects:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()

                response = {
                    "message": "About object created",
                    "data": serializer.data
                }

                return Response(data=response, status=status.HTTP_201_CREATED)
            response = {
                "message": "There are some errors in the data",
                "erorrs": serializer.errors
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": "About data currently available"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def put(self, request):
        about_section = About.objects.first()
        if about_section:
            serializer = self.serializer_class(instance=about_section, data=request.data)
            if serializer.is_valid():
                old_data = self.serializer_class(about_section).data
                del old_data["id"]
                new_data = serializer.validated_data
                if old_data != dict(new_data):
                    serializer.save()

                    response = {
                        "message": "About section successfully update",
                        "data": serializer.data
                    }

                    return Response(data=response, status=status.HTTP_200_OK)
                return Response(data={"message": "No changes dedected"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(data={"message": "There are some errors in the data"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": "There is no data to update"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        objects = About.objects.all()
        if objects:
            objects.delete()
            return Response(data={"message": "About section object successfully deleted."}, status=status.HTTP_200_OK)
        return Response(data={"message": "There is nothing to delete"}, status=status.HTTP_404_NOT_FOUND)
               

class ClassesListCreateUpdateDeleteView(APIView):
    serializer_class = ClassesSerializer

    def get(self, request, *args, **kwargs):
        class_section = Classes.objects.first()
        if class_section:
            serializer = self.serializer_class(instance=class_section)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={"message": "Classes section not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, *args, **kwargs):
        objects = Classes.objects.first()
        if not objects:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()

                response = {
                    "message": "Classes section data successfully saved",
                    "data": serializer.data
                }

                return Response(data=response, status=status.HTTP_200_OK)
            
            response = {
                "message": "There are some errors in ",
                "data": serializer.errors
            }

            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": "Classes section data currently available"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def put(self, request):
        classes_section = Classes.objects.first()
        data = request.data
        serializer = self.serializer_class(instance=classes_section, data=data)
        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Data updated",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_200_OK)
        
        response = {
            "message": "There are some errors in the data",
            "data": serializer.errors
        }

        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        Classes.objects.all().delete()
        return Response(data={"message": "Classes section data deleted"}, status=status.HTTP_200_OK)
        

class ImageListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ImageRetrieveUpdateDeleteView(generics.GenericAPIView,
                                     mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                         mixins.DestroyModelMixin):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request,*args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)
        

class BlogsSectionListCreateUpdateDeleteView(generics.GenericAPIView,
                                                  mixins.ListModelMixin,
                                                    mixins.CreateModelMixin,
                                                      mixins.UpdateModelMixin,
                                                        mixins.DestroyModelMixin):
    
    serializer_class = BlogsSectionSerializer
    queryset = BlogsSection.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if not self.get_queryset():
            return self.create(request, *args, **kwargs)
        return Response(data={"message": "Blog section data currently available."}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = BlogsSection.objects.first()
        serializer = self.serializer_class(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        self.queryset.delete()
        return Response(data={"message": "Successfully deleted"}, status=status.HTTP_200_OK)



        
    