from django.urls import path
from profiles_api import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset', )

urlpatterns = [
    path('hello-view/', views.HelloApiview.as_view()),
    path('',include(router.urls)),
]
