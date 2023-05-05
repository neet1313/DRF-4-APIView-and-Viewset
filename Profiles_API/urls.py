from django.urls import path, include
from Profiles_API import views
from rest_framework.routers import DefaultRouter

# Registering Viewsets with routers in DRF
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, basename='hello-viewset')


urlpatterns = [
    # This is how API view is configured
    path('hello-view', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]
