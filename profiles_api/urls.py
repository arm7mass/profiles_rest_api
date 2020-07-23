<<<<<<< HEAD
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
=======
from django.urls import path
from profiles_api import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset', )
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiview.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]
>>>>>>> 6b3a6b0fa2cb8d283163dce8e6eea9f0e67751be
