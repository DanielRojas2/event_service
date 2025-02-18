from rest_framework.routers import DefaultRouter
from .views.location_view import LocationViewSet
from .views.artist_view import ArtistListView

router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'artists', ArtistListView, basename='artists')

urlpatterns = router.urls
