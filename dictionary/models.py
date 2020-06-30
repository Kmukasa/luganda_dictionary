from datetime import datetime

from django.db import models
from django.utils import timezone 

# Create your models here.
class Dictionary(models.Model):

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

class LugandaDict(models.Model):
    
    # ''' first element in each tuple is the actual 
    # value to be set on the model, and the second 
    # element is the human-readable name'''

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

    WORD_CLASS_CHOICES = [
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V'),
        ('VI', 'VI'),
        ('VII', 'VII'),
        ('VII', 'VIII'),
        ('IX','IX' ),
        ('V', 'X'),
        ('UNKNOWN','Unknown' ),
    ]
    DATE_INPUT_FORMATS = ['%d-%m-%Y']

    luganda_word    = models.CharField(max_length=50)
    word_form       = models.CharField(max_length=12,choices=WORD_FORM_CHOICES,default="UNKNOWN")
    class_form      = models.CharField(max_length=12,choices=WORD_CLASS_CHOICES,default="UNKNOWN")
    luganda_example = models.CharField(max_length=20,default="")
    last_edited     = models.DateField(default=datetime.now)

    @classmethod
    def new_luganda_translation(cls, luganda_word, word_form):
        new_translation = cls(luganda_word=luganda_word, word_form=word_form)
        return new_translation

    def add_luganda_example(self, example):
        self.luganda_example = example
    
    def add_luganda_class(self, class_type):
        self.class_form = class_type

    def __repr__(self):
        luganda_word = self.luganda_word or '[No Translation]'
        word_form    = self.word_form or '[No Word Type]'
        return '<Dictionary Translation ({}) "{}" "{}">'.format(self.id, luganda_word, word_form)

    __str__ = __repr__

class EnglishDict(models.Model):

    # ''' first element in each tuple is the actual 
    # value to be set on the model, and the second 
    # element is the human-readable name'''

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

    english_word    = models.CharField(max_length=50)
    word_form       = models.CharField(max_length=12,choices=WORD_FORM_CHOICES,default="UNKNOWN")
    english_example = models.CharField(max_length=20,default="")
    last_edited     = models.DateField(default=datetime.now)
    translations    = models.ManyToManyField(LugandaDict)

    @classmethod
    def new_english_translation(cls, english_word, word_form):
        new_translation = cls(english_word=english_word, word_form=word_form)
        return new_translation

    def add_english_example(self, example):
        self.english_example = example
    
    def __repr__(self):
        ennglish_word = self.english_word or '[No Translation]'
        word_form     = self.word_form or '[No Word Type]'
        return '<Dictionary Translation ({}) "{}" "{}">'.format(self.id, english_word, word_form)

    __str__ = __repr__

