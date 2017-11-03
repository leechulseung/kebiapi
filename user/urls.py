from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)

urlpatterns = [
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
    url(r'', include(router.urls)),
]