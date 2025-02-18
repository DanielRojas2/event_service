from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.artist import Artist
from ..serializers.artist_serializer import ArtistSerializer

class ArtistListView(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @action(detail=False, methods=['get'])
    def by_name(self, request):
        name = request.query_params.get('name')
        if not name:
            return Response(
                {'error': 'the "name" parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        artists = Artist.artist_objects.get_artist_by_name(name)
        if not artists.exists():
            return Response(
                {'error': 'No artists found for this name.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def by_country(self, request):
        country = request.query_params.get('country')
        if not country:
            return Response(
                {'error': 'the "country" parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        countries = Artist.artist_objects.get_artist_by_country(country)
        if not countries.exists():
            return Response(
                {'error': 'No artists found for this country.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
