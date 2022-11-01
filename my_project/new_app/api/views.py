from email.message import Message
from .serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(["POST"])
def userRegistration(request):
    if request.method=="POST":
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data = {}
            user = serializer.save()
            data['Success'] = 'User has been created'
            data['username'] = user.username
            data['email'] = user.email
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    if request.method()=='POST':
        username =request.POST['username']
        password=request.POST['username']
        user =authenticate(username, password)

        if user is None:
            Messages.error(request, 'Invalid input')