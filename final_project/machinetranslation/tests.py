import unittest

import translator as ts 


class TestTranslator(unittest.TestCase):

    def test_englishToFrench_basic(self):
        self.assertEqual(ts.english_to_french('Hello'), 'Bonjour')

    def test_englishToFrench_null(self):
        self.assertIsNone(ts.english_to_french(None))

    def test_englishToFrench_empty(self):
        self.assertEqual(ts.english_to_french(''), '')
    
    def test_frenchToEnglish_basic(self):
        self.assertEqual(ts.french_to_english('Bonjour'), 'Hello')

    def test_frenchToEnglish_null(self):
        self.assertIsNone(ts.french_to_english(None))
    
    def test_frenchToEnglish_empty(self):
        self.assertEqual(ts.french_to_english(''), '')

if __name__=='__main__':
    unittest.main()