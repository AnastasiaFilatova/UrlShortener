import utils
import unittest
import re

class TestSanitizer(unittest.TestCase):

    def test1(self):
        words = utils.Sanitizer.sanitize_from_file('words.txt')
        with open('words.txt') as file:
            count = sum(1 for line in file)
        # Test that number of returned words is equal to number lines in the file
        self.assertEqual(len(list(words)), count)
        # Test returned words
        for word in words:
            self.assertTrue(word.islower, "{} is not lower".format(word))
            self.assertTrue(re.search(r'^[0-9a-z]+$', word), "{} contains symbols other than [0-9a-z]".format(word))
            self.assertTrue(word.strip(), "Got empty string")

    def test2(self):
        all = ['ab', 'z', 'zs', 's']
        used = []
        # First matched should be s
        self.assertEqual(utils.shortificator('zs', all, used), 's')
        # Now s is used and we should get z
        used.append({'key': 's', 'date': 123})
        self.assertEqual(utils.shortificator('zs', all, used), 'z')
        # Now s and z used and we expect zs
        used.append({'key': 'z', 'date': 124})
        self.assertEqual(utils.shortificator('zs', all, used), 'zs')
        # Now s, z, zs used and we need to test random choice somehow
        used.append({'key': 'zs', 'date': 125})
        self.assertTrue(utils.shortificator('zs', all, used) in list(set(all) - set([item['key'] for item in used])))
        # Add the rest of in order to test return oldest case
        used.append({'key': 'ab', 'date': 126})
        self.assertEqual(utils.shortificator('zs', all, used), 's')

