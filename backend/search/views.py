import abc
from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from movies.documents import MovieDocument
from movies.serializers import MovieSerializer


class ElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """should return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            response = self.document_class.search().query(q).to_queryset()\
                .prefetch_related("production_companies", "production_countries", "spoken_languages", "genres")

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


class SearchMovies(ElasticSearchAPIView):
    serializer_class = MovieSerializer
    document_class = MovieDocument

    def generate_q_expression(self, query):
        return Q(
            'multi_match', query=query,
            fields=[
                'title^10',
                'overview^5',
                'tagline^4',
                'production_companies.name^3'
            ],
            fuzziness='auto'
        )
