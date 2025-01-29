from rest_framework.routers import DefaultRouter

from api.views.brand_vacancy.view import VacancyViewSet
from api.views.city.view import CityViewSet

router: DefaultRouter = DefaultRouter()


router.register(r"cities", CityViewSet)
router.register(r"vacancies", VacancyViewSet)
