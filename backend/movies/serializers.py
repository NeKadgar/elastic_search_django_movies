from django.db import transaction
from rest_framework import serializers
from .models import Movie, Genre, ProductionCompany, ProductionCountry, MovieLanguage


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ("id",)
        extra_kwargs = {
            'name': {'validators': []},
        }


class ProductionCompanySerializer(serializers.ModelSerializer):
    origin_country = serializers.CharField(required=False)

    class Meta:
        model = ProductionCompany
        fields = "__all__"
        extra_kwargs = {
            'name': {'validators': []},
        }


class ProductionCountrySerializer(serializers.ModelSerializer):
    origin_country = serializers.CharField(required=False)

    class Meta:
        model = ProductionCountry
        fields = "__all__"


class MovieLanguageSerializer(serializers.ModelSerializer):
    origin_country = serializers.CharField(required=False)

    class Meta:
        model = MovieLanguage
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    production_companies = ProductionCompanySerializer(many=True, required=False)
    production_counties = ProductionCountrySerializer(many=True, required=False)
    spoken_languages = MovieLanguageSerializer(many=True, required=False)
    depth = 99

    class Meta:
        model = Movie
        exclude = ("id",)

    @transaction.atomic
    def create(self, validated_data):
        genres_data = validated_data.pop("genres", [])
        production_companies_data = validated_data.pop("production_companies", [])
        production_counties_data = validated_data.pop("production_countries", [])
        spoken_languages_data = validated_data.pop("spoken_languages", [])
        movie = Movie.objects.create(**validated_data)
        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            movie.genres.add(genre)
        for prod_company_data in production_companies_data:
            prod_company, _ = ProductionCompany.objects.get_or_create(**prod_company_data)
            movie.production_companies.add(prod_company)
        for prod_country_data in production_counties_data:
            prod_country, _ = ProductionCountry.objects.get_or_create(**prod_country_data)
            movie.production_counties.add(prod_country)
        for lang_data in spoken_languages_data:
            lang_data, _ = MovieLanguage.objects.get_or_create(**lang_data)
            movie.spoken_languages.add(lang_data)
        return movie
