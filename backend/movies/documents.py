from django.conf import settings
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from movies.models import Movie


@registry.register_document
class MovieDocument(Document):
    genres = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })
    production_companies = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })
    production_counties = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })
    spoken_languages = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })

    class Index:
        name = 'movies'
        settings = settings.ELASTICSEARCH_DEFAULT_SETTINGS

    class Django:
        model = Movie
        fields = [
            'title',
            'original_title',
            'tagline',
            'overview'
        ]
