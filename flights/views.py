from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializer import FlightListSerializer, BookingListSerializer


class FlightsListApiView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class =FlightListSerializer
    
class BookingsListApiView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class =BookingListSerializer