from wsgiref.validate import validator
from rest_framework import serializers
from . models import Flight, Passenger, Reservation
import re

def isFlightNumberValid(data):
    print(data['arrivalCity'])
    print("isFlightNumberValid")


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [isFlightNumberValid]

    def validate_flightNumber(self, flightNumber):
        print("validate_flightNumber")
        if(re.match("^[a-zA-Z0-9]*$", flightNumber)== None):
            raise serializers.ValidationError("Invalid Flight number. Make sure it is alpha numeric")
        return flightNumber


    def validate(self, data):
        print("validate")
        print(data)
        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
