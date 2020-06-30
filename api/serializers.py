from rest_framework import serializers
from dictionary.models import Dictionary
from dictionary.models import LugandaDict
from dictionary.models import EnglishDict

class DictionarySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Dictionary
        fields = ('id', 'english_word', 'luganda_word', 'word_form', 'english_example', 'luganda_example', 'last_edited', 'up_votes', 'down_votes')

class LugandaDictSerializer(serializers.ModelSerializer):
    class Meta:
        model   = LugandaDict 
        fields  = ('id', 'luganda_word', 'word_form', 'class_form', 'luganda_example', 'last_edited')

class EnglishDictSerializer(serializers.ModelSerializer):
    class Meta:
        model   = EnglishDict
        fields  = ('english_word', 'word_form', 'english_example', 'last_edited','translations')
    
        