from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import UploadViewSet
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
#router.register('feed', views.UserProfileFeedViewSet)
router.register(r'upload',views. UploadViewSet, base_name="upload")

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))

]
