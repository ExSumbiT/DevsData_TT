from rest_framework import status, viewsets
from rest_framework.response import Response
from Events.models import EventModel, BookingModel
from .serializers import EventSerializer, BookingSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(EventViewSet, self).dispatch(*args, **kwargs)
    queryset = EventModel.objects.all().order_by('-c_date')
    serializer_class = EventSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BookingViewSet, self).dispatch(*args, **kwargs)
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
