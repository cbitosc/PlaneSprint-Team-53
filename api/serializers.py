from rest_framework import serializers
from krishna.models import Rooms

class RoomsSerializer(serializers.ModelSerializer):
    class Mets:
        model = Rooms
        fields = '__all__'