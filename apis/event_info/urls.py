from rest_framework.routers import DefaultRouter
from .views.location_view import LocationViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='locations')

urlpatterns = router.urls
