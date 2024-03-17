# it is to test our code if it works as expected.
import unittest
from python1.Day8.Testing import change_text


class TestChangeText(unittest.TestCase):
    
    def test_uppercase(self):            
        # function name should start with test, otherwise it will not be recognized.
        word = 'study'
        result = change_text.all_capitals(word)
        self.assertEqual(result,'STUDY')
        #self.assertEqual(result,'Study')
    
if __name__ == '__main__':
    unittest.main()
    