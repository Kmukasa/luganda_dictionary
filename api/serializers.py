from rest_framework import serializers
from dictionary.models import Dictionary

class DictionarySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Dictionary
        fields = ('id', 'english_word', 'luganda_word', 'word_form', 'english_example', 'luganda_example', 'last_edited', 'up_votes', 'down_votes')
    
        