from unittest.util import _MAX_LENGTH
from rest_framework import serializers
#from challenges import models
from . import models


class CourseSerializer(serializers.ModelSerializer):
    """Handling serializers for the Course"""
    class Meta:
        model = models.Course
        fields = ('name', 'price', 'includes', 'image',
                  'description', 'overview', 'language', 'rate')
        

class InstructorSerializer(serializers.ModelSerializer):
    """Handling serializers for new instructors"""

    class Meta:
        model=models.Instructor
        fields=('name','description','number','courses')

class ReviewSerializer(serializers.ModelSerializer):
    """Handling serializers for instructors"""
    
    class Meta:
        model= models.Review
        fields=('name','comment','rate')



    