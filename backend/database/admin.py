from django.contrib import admin
from .models import (
    BrandStore,
    BrandVacancy,
    City,
    ClientPersonInfo,
    CityTranslation,
    BrandVacancyTranslation,
)


class BrandVacancyTranslationInline(admin.TabularInline):
    model = BrandVacancyTranslation


class CitiTranslationInline(admin.TabularInline):
    model = CityTranslation


@admin.register(BrandVacancy)
class BrandVacancyAdmin(admin.ModelAdmin):
    inlines = (BrandVacancyTranslationInline,)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    inlines = [CitiTranslationInline]


admin.site.register(BrandStore)
admin.site.register(ClientPersonInfo)
