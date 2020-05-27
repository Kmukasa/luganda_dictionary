from django.test import TestCase
from rest_framework.test import APITestCase

from dictionary.models import Dictionary

class DictionaryCreateTestCase(APITestCase):
    def test_new_translation(self):
        initial_num_translations = Dictionary.objects.count()
        new_translation = {
            'luganda_word':'bulungi',
            'english_word':'good',
            'up_votes':0,
            'down_votes':0
        }
        response = self.client.post('/api/translations/new/', new_translation, format='json')
        if response.status_code != 201:
            print(response)
        else:
            self.assertEqual(
                Dictionary.objects.count(),
                initial_num_translations + 1
            )
            for attr, exp_val in new_translation.items():
                self.assertEqual(response.data[attr], exp_val)
            
            self.assertEqual(response.data['up_votes'],0)
            self.assertEqual(response.data['down_votes'],0)

class DictionaryDestroyTestCase(APITestCase):
    def test_delete_translation(self):

        translation1= {
            'luganda_word':'paka lasti',
            'english_word':'forever',
            'up_votes':0,
            'down_votes':0
        }

        response = self.client.post('/api/translations/new/', translation1, format='json')

        initial_num_translations = Dictionary.objects.count()
        print(initial_num_translations)
        translation = Dictionary.objects.first()
        print(translation)
        translation_id = translation.id


        self.client.delete('/api/translations/{}/'.format(translation_id))
        self.assertEqual(
            Dictionary.objects.count(),
            initial_num_translations - 1
        )
        self.assertRaises(
            Dictionary.DoesNotExist,
            Dictionary.objects.get, id=translation_id
        )

class DictionaryListTestCase(APITestCase):
    def test_list_dictionary(self):

        translations = [
        {
            'luganda_word':'bulungi',
            'english_word':'good',
            'up_votes':0,
            'down_votes':0
        },
            {
            'luganda_word':'paka lasti',
            'english_word':'forever',
            'up_votes':0,
            'down_votes':0
        },
        {
            'luganda_word':'genda',
            'english_word':'to go',
            'up_votes':0,
            'down_votes':0
        }]

        for words in  translations:
            res = self.client.post('/api/translations/new/', words, format='json')
            print(res)

        translations_count = Dictionary.objects.count()
        response = self.client.get('/api/translations/')
        self.assertEqual(response.data.count, translations_count)


