from rest_framework import serializers
from Events.models import BookingModel, EventModel


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    event_id = serializers.UUIDField()

    class Meta:
        model = BookingModel
        fields = ('id', 'event_id', 'username', 'surname', 'email', 'status')
        extra_kwargs = {'event_id': {'required': True}, }
        # 'username': {'required': True}, 'surname': {
        #     'required': True}, 'email': {'required': True}, }


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventModel
        fields = ('id', 'name', 'start_date', 'end_date', 'thumbnail')
