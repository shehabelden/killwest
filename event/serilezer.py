from rest_framework.serializers import ModelSerializer

from mysite.event.models import EventModel
from mysite.ticket.models import TicketModel


class TiketSerializers(ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'
class EventSer(ModelSerializer):
    event = TiketSerializers(many = True )

    class Meta:

     model = EventModel
     fields = ["name" , "image" , "topic","event","avilabolevent"]
class EventsSer(ModelSerializer):
    class Meta:

     model  = EventModel
     fields = ["name" , "id", "image",
               "date" , "start" , "end" , "avilabolevent" , ]