from rest_framework import generics, viewsets
from .permissions import IsAuthenticatedOrCreate
from django.contrib.auth.models import User
from .serializers import SignUpSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('username',)

