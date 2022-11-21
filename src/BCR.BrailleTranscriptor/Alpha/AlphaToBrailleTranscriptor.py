# Transcribes alphabet based text to braille.
from .languages import *
import re

class AlphaToBrailleTranscriptor(object):

    def __init__(self, language, verbose = False):
        self.language = language
        self.language.verbose = verbose
        self.currentWord = ''
        self.currentBraille = ''
        self.appliedRules = []


    def transcribe(self, string):
        # Convert alphabetic text to braille.
        self.currentBraille = ''
        self.appliedRules = []
        words = self.extractWords(string)
        for word in words:
            self.currentWord = word
            self.handleShortcuts()
            self.handleNumbers()
            self.handleCapitalLetters()
            self.currentBraille += self.buildWord()
        
        return self.currentBraille.strip()

    def extractWords(self, string):
        # Split up a sentence based on whitespace (" ") and new line ("\n") chars.
        words = string.split(" ")
        result = []
        for word in words:
            temp = word.split("\n")
            for item in temp:
                result.append(item)
        return result

    def handleShortcuts(self):
        # Replace special shortcuts with string representation.

        if any(shortCut in self.currentWord for shortCut in self.language.shortcuts.keys()):
            for shortCut in self.language.shortcuts.items(): 
                if shortCut[0] in self.currentWord: 
                    result = self.currentWord.replace(shortCut[0],shortCut[1])
                    if (result != self.currentWord):
                        self.appliedRules.append({ 'name': f"Applied transformation {shortCut[0]} to {shortCut[1]}", 'textBefore':self.currentWord, 'textAfter': result})
                        self.currentWord = result

    def handleNumbers(self):
        # Replace each group of numbers in a word to their respective braille representation.
        result = ''
        for i in range(0, len(self.currentWord)):
            if self.currentWord[i].isdigit():
                if i == 0 or not self.currentWord[i-1].isdigit():
                    result += self.language.getBrailleFromNumber(self.currentWord[i], True)
                else:
                    result += self.language.getBrailleFromNumber(self.currentWord[i], False)
            else:
                result += self.currentWord[i]
        self.currentWord = result

    def handleCapitalLetters(self):
        # Put the capital escape code before each capital letter.
        result = ''

        if self.currentWord.isupper() and len(''.join(ch for ch in self.currentWord if ch.isalpha()))>1: 
            pos = AlphaToBrailleTranscriptor.__getFirstLetterPosition__(self.currentWord)
            result += self.currentWord[0:pos].lower() + self.language.getCapitalPrefix() + self.language.getCapitalPrefix() + self.currentWord[pos:].lower()
        else:
            for char in self.currentWord:
                if char.isupper():
                    result += self.language.getCapitalPrefix() + char.lower()
                else:
                    result += char.lower()
        self.currentWord = result

    def __getFirstLetterPosition__(s):
        m = re.search(r'[a-z]', s, re.I)
        if m is not None:
            return m.start()
        return -1

    def buildWord(self):
        result = ''
        for i in range(0, len(self.currentWord)):
            if self.language.isCombinedSymbol(self.currentWord[i]):
                result += self.language.getCombinedSymbolToBraille(self.currentWord[i])
            else: 
                result += self.language.getBrailleFromAlpha(self.currentWord[i])
        return result + " "
       

    '''
    The Algorithm for Translating Alphabet Based Text to Spanish / English Braille:
    1. Split up the text into words by dividing them based on whitespace characters.
        - Whitespace includes spaces (' ') and new lines ('\n')
    2. For each word, handle the shortCuts first. There are some special caracters, that are respresented by combination of other caracters. 
       For example © is converted to (C) or ª is converted to .a

    3. Handle the numbers:
        - Numbers in braille use the same symbols as the first 10 letters of the alphabet.
            - The number '7' and the letter 'g' are both represented by '⠛'.
            - To differentiate between numbers and letters, an escape code (⠼) is placed before groups of numbers.
            - Therefore '7' is actually '⠼⠛' whereas 'g' is only '⠛'.
        - In this step, only the numbers are dealt with, so there will be a mix of both braille and Alphabet symbols.
            - Example: "123-456-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK"
    4. Handle the capitals.
        - Similarly to numbers in braille, capital letters need an escape code (⠠).
        - The escape code (⠠) is added to the beginning of each capital letter and the letter is changed to lowercase.
            - Example 1: "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-⠠j⠠u⠠n⠠k". The dashes still remain.
            - Example 2: "Sweet" becomes "⠠sweet". The non-capital letters remain untouched.
    
    5. Build the translation.
        a) Translate combined symbols
            - Check if the symbol is part of a combined symbol
        b) Translate symbol
      
    '''
