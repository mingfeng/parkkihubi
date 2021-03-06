import datetime

from django.contrib.gis.geos import Point
from django.utils.timezone import now

from parkings.models import Address, Operator, Parking


def test_address_instance_creation():
    Address(city="city", postal_code="12345", street="street")


def test_operator_instance_creation():
    Operator(name="name", user_id=1)


def test_parking_instance_creation():
    Parking(
        device_identifier="device_identifier",
        location=Point(60.193609, 24.951394),
        operator_id=1,
        registration_number="ABC-123",
        resident_code="A",
        special_code="SPECIAL",
        time_end=now() + datetime.timedelta(days=1),
        time_start=now(),
        zone=3,
    )
