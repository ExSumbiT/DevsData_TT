from django.db import models
import uuid

booking_status = (('active', 'Active'), ('cancelled', 'Cancelled'))
# Create your models here.


class EventModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    thumbnail = models.CharField(max_length=400)
    c_date = models.DateTimeField(auto_now_add=True, blank=True)


class BookingModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    c_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(
        max_length=10, choices=booking_status, default='active')
