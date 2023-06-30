from rest_framework.response import Response
from rest_framework.decorators import api_view
from krishna.models import Rooms
from .serializers import RoomsSerializer

@api_view(['GET','POST'])
def getHotel(request):
    items = Rooms.objects.all()
    serializer = RoomsSerializer(items,many = True)
    return Response(serializer.data)