from django.test import TestCase
from rest_framework.test import APITestCase

from dictionary.models import Dictionary

class DictionaryCreateTestCase(APITestCase):
    def test_new_translation(self):
        initial_num_translations = Dictionary.objects.count()
        new_translation = {
            'luganda_word':'bulungi',
            'english_word':'good',
        }
        response = self.client.post('api/translations/new/', new_translation )
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(
            Dictionary.objects.count(),
            initial_num_translations + 1
        )
        for attr, exp_val in new_translation.items():
            self.assertEqual(response.data[attr], exp_val)
        
        self.assertEqual(response.data['up_votes'],1)
        self.assertEqual(response.data['down_votes'],0)

