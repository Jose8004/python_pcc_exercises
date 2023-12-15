import pytest
import unittest

from chapter_11 import convert_to_celsius, reverse_string

class Test_different_values(unittest.TestCase):

    def test_convert_to_celsius(self):
        assert convert_to_celsius(98.6) == pytest.approx(37.0, 0.1)
        assert convert_to_celsius(-459.67) == pytest.approx(-273.15, 0.1)
        assert convert_to_celsius(1000) == pytest.approx(537.78, 0.1)
        assert convert_to_celsius(140) == pytest.approx(60.00, 0.1)
    
    def invalid_convertion(self):
        self.assertNotEqual(convert_to_celsius(140), 62)
 
if __name__ == '__main__':
    pytest.main()

class Test_reversed_strings(unittest.TestCase):

    def test_correct_reversal(self):
        assert reverse_string("hello") == "olleh"
        assert reverse_string("The only true wisdom is in knowing you know nothing.") == ".gnihton wonk uoy gniwonk ni si modsiw eurt ylno ehT"
        assert reverse_string("It does not matter how slowly you go as long as you do not stop.") == ".pots ton od uoy sa gnol sa og uoy ylwols woh rettam ton seod tI"
        assert reverse_string("The only thing we have to fear is fear itself.") == ".flesti raef si raef ot evah ew gniht ylno ehT"

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")
    
    def test_invalid_string(self):
        self.assertIsNone(reverse_string(1234))

if __name__ == '__main__':
    pytest.main()