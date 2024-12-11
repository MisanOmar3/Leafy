from rest_framework.decorators import api_view
from rest_framework.response import Response #return JSON responses
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username = request.data["username"])
    if not user.check_password(request.data["password"]):
        return Response({"detail":"Not found."}, status = status.HTTP_404_NOT_FOUND)
    # token, created = Token.objects.get_or_create(user = user)
    # refresh = 
    tokens = {
        "access": str(AccessToken.for_user(user)),
        "refresh": str(RefreshToken.for_user(user))
    }
    serializer = UserSerializer(instance = user)
    return Response({"tokens":tokens, "user":serializer.data})
    
    

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username = request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        tokens = {
            "access": str(AccessToken.for_user(user)),
            "refresh": str(RefreshToken.for_user(user))
        }
        serializer = UserSerializer(instance = user)
        return Response({"tokens":tokens, "user":serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
