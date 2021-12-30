from django.conf import settings
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import char_filter
from elasticsearch_dsl import analysis

from movies.models import Movie

en_ru_char_filter = char_filter(
    'remove_leading_and_symbol', 'mapping',
    mappings=[
        "a => ф",
        "b => и",
        "c => с",
        "d => в",
        "e => у",
        "f => а",
        "g => п",
        "h => р",
        "i => ш",
        "j => о",
        "k => л",
        "l => д",
        "m => ь",
        "n => т",
        "o => щ",
        "p => з",
        "r => к",
        "s => ы",
        "t => е",
        "u => г",
        "v => м",
        "w => ц",
        "x => ч",
        "y => н",
        "z => я",
        "A => Ф",
        "B => И",
        "C => С",
        "D => В",
        "E => У",
        "F => А",
        "G => П",
        "H => Р",
        "I => Ш",
        "J => О",
        "K => Л",
        "L => Д",
        "M => Ь",
        "N => Т",
        "O => Щ",
        "P => З",
        "R => К",
        "S => Ы",
        "T => Е",
        "U => Г",
        "V => М",
        "W => Ц",
        "X => Ч",
        "Y => Н",
        "Z => Я",
        "[ => х",
        "] => ъ",
        "; => ж",
        "< => б",
        "> => ю"
    ]
)

ru_en_analyzer = analysis.analyzer(
    'ru_en_analyzer',
    type="custom",
    tokenizer='standard',
    filter=["lowercase", "snowball"],
    char_filter=["html_strip", en_ru_char_filter]
)


@registry.register_document
class MovieDocument(Document):
    title = fields.TextField(analyzer=ru_en_analyzer)
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
            'original_title',
            'tagline',
            'overview'
        ]
