import pytest
from ..models.location import Location

@pytest.mark.django_db
class TestLocationManager:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.location1 = Location.local_objects.create(
            location_name='Levis Stadium',
            location_address='4900 Marie P DeBartolo Way',
            location_city='Santa Clara',
            location_state='California',
            location_country='Estados Unidos',
            location_capacity=68500
        )
        self.location2 = Location.local_objects.create(
            location_name='Fiserv Forum',
            location_address='1111 N Vel R. Phillips Ave',
            location_city='Milwaukee',
            location_state='Wisconsin',
            location_country='Estados Unidos',
            location_capacity=17500
        )
        self.location3 = Location.local_objects.create(
            location_name='Wembley Stadium',
            location_address='London HA9 0WS',
            location_city='Londres',
            location_state='Inglaterra',
            location_country='Reino Unido',
            location_capacity=90000
        )

    def test_get_location_by_country(self):
        usa_locations = Location.local_objects.get_location_by_country('Estados Unidos')
        assert usa_locations.count() == 2
        assert self.location1 in usa_locations
        assert self.location2 in usa_locations

    def test_get_location_by_city(self):
        london_location = Location.local_objects.get_location_by_city('Londres')
        assert london_location.count() == 1
        assert self.location3 in london_location

    def test_get_location_by_name(self):
        stadium = Location.local_objects.get_location_by_name('Fiserv Forum')
        assert stadium.count() == 1
        assert self.location2 in stadium
