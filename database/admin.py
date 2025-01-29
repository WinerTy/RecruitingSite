from django.contrib import admin
from .models import BrandStore, BrandVacancy, City, ClientPersonInfo


admin.site.register(BrandStore)
admin.site.register(BrandVacancy)
admin.site.register(City)
admin.site.register(ClientPersonInfo)
