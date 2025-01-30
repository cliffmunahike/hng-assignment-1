from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    results = UserSerializer(users, many=True)
    return Response(results.data)
