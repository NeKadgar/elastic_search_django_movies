from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CountryCodes(models.TextChoices):
    IR = "IR", "Iran"
    HU = "HU", "Hungary"
    AT = "AT", "Austria"
    DE = "DE", "Germany"
    GB = "GB", "United Kingdom"
    RS = "RS", "Serbia"
    BE = "BE", "Belgium"
    BA = "BA", "Bosnia and Herzegovina"
    CX = "CX", "Christmas Island"
    SE = "SE", "Sweden"
    CZ = "CZ", "Czechia"
    IT = "IT", "Italy"
    NL = "NL", "Netherlands"
    AU = "AU", "Australia"
    FK = "FK", "Falkland Islands"
    RO = "RO", "Romania"
    SI = "SI", "Slovenia"
    DK = "DK", "Denmark"
    CH = "CH", "Switzerland"
    IE = "IE", "Ireland"
    HR = "HR", "Croatia"
    PL = "PL", "Poland"
    LT = "LT", "Lithuania"
    CY = "CY", "Cyprus"
    BL = "BL", "Saint Barthélemy"
    FR = "FR", "France"
    DJ = "DJ", "Djibouti"
    PT = "PT", "Portugal"
    US = "US", "United States"
    AE = "AE", "United Arab Emirates"
    GD = "GD", "Grenada"
    SK = "SK", "Slovakia"
    ES = "ES", "Spain"
    NO = "NO", "Norway"
    SG = "SG", "Singapore"
    LU = "LU", "Luxembourg"
    FI = "FI", "Finland"


class Genre(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return "{}. count of movies: {}".format(self.name, self.movies.count())


class ProductionCompany(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    origin_country = models.CharField(max_length=2, choices=CountryCodes.choices, null=True, blank=True)

    def __str__(self):
        return "{}. count of movies: {}".format(self.name, self.movies.count())


class ProductionCountry(models.Model):
    origin_country = models.CharField(max_length=2, choices=CountryCodes.choices, blank=True, null=True)
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "{}. count of movies: {}".format(self.name, self.movies.count())


class MovieLanguage(models.Model):
    name = models.CharField(max_length=50, null=False)
    origin_country = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    class StatusCodes(models.TextChoices):
        RELEASED = "Released", "Released"
        IN_PRODUCTION = "In Production", "In Production"

    title = models.CharField(max_length=255, null=False)
    original_title = models.CharField(max_length=255, blank=True)
    tagline = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=25, choices=StatusCodes.choices)
    vote_average = models.DecimalField(max_digits=4, decimal_places=2,
                                       validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    revenue = models.IntegerField(validators=[MinValueValidator(0)])
    runtime = models.IntegerField(validators=[MinValueValidator(0)])
    budget = models.IntegerField(validators=[MinValueValidator(0)])
    release_date = models.DateField()
    overview = models.TextField(blank=True)
    original_language_iso = models.CharField(max_length=2)
    homepage = models.URLField(max_length=200, blank=True, null=True)
    adult = models.BooleanField(default=False)
    tmdb_id = models.IntegerField(validators=[MinValueValidator(0)])
    imdb_id = models.CharField(max_length=25, unique=True)
    poster_image = models.URLField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name="movies")
    production_companies = models.ManyToManyField(ProductionCompany, related_name="movies")
    production_countries = models.ManyToManyField(ProductionCountry, related_name="movies")
    spoken_languages = models.ManyToManyField(MovieLanguage, related_name="movies")

    def __str__(self):
        return self.title
