from django.contrib import admin
from django.db.models import Count

from .models import Movie, Genre, ProductionCompany, ProductionCountry


class MovieAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    ordering = ('-release_date',)


class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super(GenreAdmin, self).get_queryset(request)
        return qs.annotate(movies_count=Count('movies')).order_by('-movies_count')


class ProductionCompanyAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super(ProductionCompanyAdmin, self).get_queryset(request)
        return qs.annotate(movies_count=Count('movies')).order_by('-movies_count')


class ProductionCountryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super(ProductionCountryAdmin, self).get_queryset(request)
        return qs.annotate(movies_count=Count('movies')).order_by('-movies_count')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(ProductionCompany, ProductionCompanyAdmin)
admin.site.register(ProductionCountry, ProductionCountryAdmin)
