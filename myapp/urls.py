from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'careers', views.CareerViewSet, basename='career')

urlpatterns = [
    path('', include(router.urls)),
]