from datetime import datetime

from django.db import models
from django.utils import timezone 

# Create your models here.
class Dictionary(models.Model):

    ''' first element in each tuple is the actual 
    value to be set on the model, and the second 
    element is the human-readable name'''
    WORD_FORM_CHOICES = [
        ('NOUN', 'Noun'),
        ('VERB', 'Verb'),
        ('PRONOUN', 'Pronoun'),
        ('ADJECTIVE', 'Adjective'),
        ('PREPOSITION', 'Preposition'),
        ('ADVERB', 'Adverb'),
        ('CONJUNCTION', 'Conjunction'),
        ('INTERJECTION', 'Interjection'),
        ('PHRASE', 'Phrase'),
        ('UNKNOWN','Unknown' ),
    ]
    DATE_INPUT_FORMATS = ['%d-%m-%Y']

    english_word    = models.CharField(max_length=100)
    luganda_word    = models.CharField(max_length=100)
    word_form       = models.CharField(max_length=12,choices=WORD_FORM_CHOICES,default="UNKNOWN")
    english_example = models.CharField(max_length=20,default="")
    luganda_example = models.CharField(max_length=20,default="")
    last_edited     = models.DateField(default=datetime.now)
    up_votes        = models.IntegerField(default=0)
    down_votes      = models.IntegerField(default=0)


    """ 
    Potential function: get translation - luganda to english
                                        - english to luganda
                                        - edit translation 
    """
    @classmethod
    def new_translation(cls, english_word, luganda_word):
        translation = cls(english_word=english_word, luganda_word=luganda_word)
        return translation

    def add_luganda_example(self, example):
        self.luganda_example = example

    def add_english_example(self, example):
        self.english_example = example
    
    def __repr__(self):
        english_word = self.english_word or '[No Translation]'
        luganda_word = self.luganda_word or '[No Translation]'
        return '<Dictionary Translation ({}) "{}" "{}">'.format(self.id, english_word, luganda_word)

    __str__ = __repr__

