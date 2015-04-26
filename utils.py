import random
import re
import logging
from multiprocessing import Pool

# We are using global variable to pass as a second parameter to a matcher
# function below that will be called from by pool.map
# pool.map expects to get function with only one argument and that's why we
# are using global to pass second.
# It is possible to make a tuples using lambda and pass both but that will be
# more costly on large lists so we consider this short cut acceptable
base_url = None

def matcher(word):
    if re.findall(word, base_url):
        return word

def shortificator(url, all_words, used_words):
    """
    Pick a key word from provided list of words
    Logic is the following
    * Select available words for pick up by subtracting used words from all
    * If no words available then pick oldest from used words
    * If there are available words return first matched(in alphabetical order)
    * If there are no matching words then return random from available
    :param url: String to look up words
    :param all_words: List of all key words
    :param used_words: List of dictionaries [{key, date}, ...]
                       where date is date in milliseconds
    :return: selected key word
    """
    global base_url
    base_url = url
    pool = Pool(processes=8)
    available_words = list(set(all_words) - set([item['key'] for item in used_words]))
    # If no available words return oldest
    if not available_words:
        # Sort used_words by date and return first key word
        return sorted(used_words, key=lambda k: k['date'])[0]['key']
    # We have available words to check so lets check them
    matched_words = sorted(set(pool.map(matcher, available_words)))
    # We might get None in the resulting list. Remove it from there
    if None in matched_words: matched_words.remove(None)
    # If we got a match return first since list is already sorted
    if matched_words: return matched_words[0]
    # Last resort. Return random from available
    return random.choice(available_words)

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

