from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer

@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({
        "email": "cliffike47@gmail.com"
        }).data)
