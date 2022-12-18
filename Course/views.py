from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from . import Serializers, models
# Create your views here.

class Course(viewsets.ModelViewSet):
    """ Handling classes ineteractions """
    serializer_class=Serializers.CourseSerializer
    queryset=models.Course.objects.all()

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class Instructor(viewsets.ModelViewSet):
    """" Handling methods for the Instructor"""
    serializer_class=Serializers.InstructorSerializer
    queryset=models.Instructor.objects.all()
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    


class Review(viewsets.ModelViewSet):
    """" Handling method for the review """
    serializer_class=Serializers.ReviewSerializer
    queryset=models.Review.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class Content(viewsets.ModelViewSet):
    """" Handling method for the review """
    serializer_class=Serializers.ContentSerializer
    queryset=models.Review.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class Chapter(viewsets.ModelViewSet):
    """" Handling method for the review """
    serializer_class=Serializers.ChapterSerializer
    queryset=models.Review.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)