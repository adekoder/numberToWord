import unittest
from numbertoword import Convert
class TestNumberToWordMethod(unittest.TestCase):
    
    def test_convert_to_word(self):
        convert = Convert(1000)
        self.assertEqual(convert.convert_to_word(), 'one thousand ')

    def test_convert_to_word2(self):
        convert = Convert(123423)
        self.assertEqual(convert.convert_to_word(), 'one hundred and twenty-three thousand four hundred and twenty-three ')

    def test_group_number(self):
        convert = Convert(123423)
        self.assertEqual(convert.group_number(),[423,123])


    

if __name__ == '__main__':
    unittest.main()