import re
import logging

class Sanitizer():

    @staticmethod
    def sanitize_from_file(filename):
        with open(filename, 'r+') as file:
            for word in file:
                 if Sanitizer.sanitize(word):
                     yield Sanitizer.sanitize(word)

    @staticmethod
    def sanitize(word):
        sanitized_word = re.sub("[^0-9a-z]+", '', word.lower())
        logging.debug("'{}' after sanitation: {}".format(word.strip(), sanitized_word))
        return sanitized_word
