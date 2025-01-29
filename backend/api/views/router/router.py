from rest_framework.routers import DefaultRouter

from backend.api.views.city.view import CityViewSet

router: DefaultRouter = DefaultRouter()


router.register("city", CityViewSet, basename="city")
