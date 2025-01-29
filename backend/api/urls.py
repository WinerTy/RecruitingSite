from django.urls import path, include
from .views.router import router as api_router

urlpatterns = []


urlpatterns += [path("/", include(api_router.urls))]
