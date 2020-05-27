from datetime import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Dictionary(models.Model):
    english_word = models.CharField(max_length=100)
    luganda_word = models.CharField(max_length=100)
    last_edited = models.DateTimeField(auto_now=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0) 

    """ 
    Potential function: get translation - luganda to english
                                        - english to luganda
                                        - edit translation 
    """
    @classmethod
    def new_translation(cls, english_word, luganda_word):
        translation = cls(english_word=english_word, luganda_word=luganda_word)
        return translation
    
    def __repr__(self):
        english_word = self.english_word or '[No Translation]'
        luganda_word = self.luganda_word or '[No Translation]'
        return '<Dictionary Translation ({}) "{}" "{}">'.format(self.id, english_word, luganda_word)

    __str__ = __repr__

