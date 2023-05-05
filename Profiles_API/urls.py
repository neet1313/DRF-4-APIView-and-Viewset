from Profiles_API import views
from django.urls import path

urlpatterns = [
    path('hello-view', views.HelloAPIView.as_view())
]

