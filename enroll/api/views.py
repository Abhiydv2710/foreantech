from enroll.models import User
from enroll.api.serializers import UserSerializer
from rest_framework import  viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer