from rest_framework import mixins , generics
from .serilezer import *


class EventApi(mixins.RetrieveModelMixin , generics.GenericAPIView):

    queryset = EventModel.objects.all()

    serializer_class = EventSer

    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EventsApi(mixins.ListModelMixin , generics.GenericAPIView):

    queryset = EventModel.objects.all()

    serializer_class = EventsSer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


