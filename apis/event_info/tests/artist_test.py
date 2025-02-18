import pytest
from ..models.artist import Artist

@pytest.mark.django_db
class TestArtistManager:
    @pytest.fixture(autouse=True)
    def setUp(self, db):
        self.artist1 = Artist.objects.create(
            artist_name='Dua Lipa',
            artist_country='Kosovo',
            artist_bio='Cantante inglesa'
        )
        self.artist2 = Artist.objects.create(
            artist_name='Kjarkas',
            artist_country='Bolivia',
            artist_bio='Agrupacion de musica Folcklorica'
        )
        self.artist3 = Artist.objects.create(
            artist_name='Don Omar',
            artist_country='Puerto Rico',
            artist_bio='Cantante'
        )
    def test_get_artist_by_name(self):
        artist = Artist.artist_objects.get_artist_by_name('Dua Lipa')
        assert artist.count() == 1
        assert self.artist1 in artist

    def test_get_artist_by_country(self):
        artist = Artist.artist_objects.get_artist_by_country('Bolivia')
        assert artist.count() == 1
        assert self.artist2 in artist
