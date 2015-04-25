from django.shortcuts import render
import re


def startpage(request):
    return render(request, 'startpage.html')

def clean_wordlist(self):
    with open('words.txt', 'w') as file:
        for word in file:
            print "word: ", word
            word.lower()
            match = re.search(r'^[0-9a-z]+$', word)
            word = word[:match.start()] + word[match.end():]
            print "cleaned word: ", word

