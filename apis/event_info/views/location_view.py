from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.location import Location
from ..serializers.location_serializer import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @action(detail=False, methods=['get'])
    def by_country(self, request):
        country = request.query_params.get('country')
        if not country:
            return Response(
                {'error': 'The "country" parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        locations = Location.local_objects.get_location_by_country(country)
        if not locations.exists():
            return Response(
                {'error': 'No locations found for this country.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def by_city(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response(
                {'error': 'The "city" parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        locations = Location.local_objects.get_location_by_city(city)
        if not locations.exists():
            return Response(
                {'error': 'No locations found for this city.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def by_name(self, request):
        name = request.query_params.get('name')
        if not name:
            return Response(
                {'error': 'The "name" parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        locations = Location.local_objects.get_location_by_name(name)
        if not locations.exists():
            return Response(
                {'error': 'No locations found for this name.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
