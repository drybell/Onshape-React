from django.contrib.auth.models import User, Group
from api.serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets, permissions, generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# class UserTokenViewSet(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated, ]
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user