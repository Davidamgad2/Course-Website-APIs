from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('Course', views.Course)
router.register('Instructor',views.Instructor)
router.register('Review',views.Review)


urlpatterns = [
path('',include(router.urls)),
]
