import sanitizer
import unittest
import re

class TestSanitizer(unittest.TestCase):

    def test1(self):
        words = sanitizer.Sanitizer.sanitize_from_file('../words.txt')
        with open('../words.txt') as file:
            count = sum(1 for line in file)
        # Test that number of returned words is equal to number lines in the file
        self.assertEqual(sum(1 for i in words), count)
        # Test returned words
        for word in words:
            self.assertTrue(word.islower, "{} is not lower".format(word))
            self.assertTrue(re.search(r'^[0-9a-z]+$', word), "{} contains symbols other than [0-9a-z]".format(word))
            self.assertTrue(word.strip(), "Got empty string")
