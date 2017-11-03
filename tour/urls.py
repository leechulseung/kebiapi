from django.conf.urls import url, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)

urlpatterns =[
    url(r'', include(router.urls)),
]