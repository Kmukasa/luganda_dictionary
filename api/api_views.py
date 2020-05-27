from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from api.serializers import DictionarySerializer
from dictionary.models import Dictionary
from rest_framework.exceptions import ValidationError

from django_filters.rest_framework import DjangoFilterBackend

class DictionaryList(ListAPIView):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('luganda_word','english_word',)


class DictionaryCreate(CreateAPIView):
    serializer_class = DictionarySerializer

    def create(self, request, *args, **kwargs ):
        try:
            luganda_word = request.data.get('luganda_word')
            english_word = request.data.get('english_word')

            if luganda_word is None or luganda_word == "":
                raise ValidationError({'luganda_word': 'Must not be empty'})
            elif english_word is None or english_word == "":
                raise ValidationError({'english_word': 'Must not be empty'})
        except ValueError:
            raise ValidationError({'english_word': 'Must be a string',      'luganda_word': 'Must be a string'})
        response = super().create(request, *args, **kwargs)
        print(response)
        return response

class DictionaryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Dictionary.objects.all()
    lookup_field = 'id'
    serializer_class = DictionarySerializer

    def delete(self, request, *args, **kwargs ):
        translation_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('dictionary_data_{}'.format(translation_id))
        return response
    
    def update(self, request, *args, **kwargs):
        response=super().update(request, *args, **kwargs)
        if response.status_code==200:
            from django.core.cache import cache
            translation = response.data
            cache.set('dictionary_data_{}'.format(translation['id']), {'luganda_word':translation['luganda_word'],
             'english_word':translation['english_word'],
            })
        return response



