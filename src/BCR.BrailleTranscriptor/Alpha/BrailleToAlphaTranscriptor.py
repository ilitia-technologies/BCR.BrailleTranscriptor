# Transcribes braille to alphabet based text.


class BrailleToAlphaTranscriptor(object):

    def __init__(self, language, verbose = False):
        self.language = language
        self.language.verbose = verbose
        self.numberMode = False
        self.capitalMode = False
        self.currentWord = ''
        self.currentAlpha = ''
        self.appliedRules = []

    def transcribe(self, string):
        self.numberMode = False
        self.capitalMode = False
        self.currentWord = ''
        self.currentAlpha = ''
        self.appliedRules = []
        words = self.extractWords(string)
        for word in words:
            word = self.handleNumbers(word)
            word = self.buildWord(word) 
            self.currentAlpha += word    
        
        self.handleCapitalLetters()
        self.handleExceptions()
        return self.currentAlpha.strip(), self.appliedRules

    def extractWords(self, string):
        # Split up a sentence based on whitespace (" ") and new line ("\n") chars.
        words = string.split(" ")
        result = []
        for word in words:
            temp = word.split("\n")
            for item in temp:
                result.append(item)
        return result

    def handleNumbers(self, word):
        self.currentWord = ''
        # Translate braille numbers to standard number notation.
        for i in range(0, len(word)):
            if self.language.isNumberPrefix(word[i]):
                self.numberMode = True
                continue
            if self.numberMode and self.language.isBrailleNumber(word[i]):
                self.currentWord += self.language.getNumberFromBraille(word[i])
            elif self.language.isEndNumberSymbol(word[i]): #TODO: ver otros casos donde se pasa de numero a letra
                self.numberMode = False
                if self.language.includeEndNumberSymbol(word[i]):
                    self.currentWord += word[i] 
            else:
                self.currentWord += word[i]

        self.numberMode = False
        return self.currentWord

    def buildWord(self, word):
        self.currentWord = ''
        processed = ''
       
        for i in range(0, len(word)):
            if word[i] == processed:
                processed = ''
            elif (word[i].isdigit() or self.language.isCapitalPrefix(word[i])):
                self.currentWord += word[i]
            elif self.language.isContraction(word[i]): 
                self.currentWord += self.language.getContractionFromBraille(word[i])
            elif i < len(word)-1 and self.language.isBrailleCombinedSymbol(word[i],word[i+1]): 
                self.currentWord += self.language.getCombinedSymbol(word[i],word[i+1])
                processed = word[i+1]
            else:
                self.currentWord += self.language.getAlphaFromBraille(word[i])
        return self.currentWord + " "

    def handleCapitalLetters(self):
        # Capitalize letters after the capitalization escape code.
        result = ''
        for i in range(0, len(self.currentAlpha)):
            if i-1 >= 0 and self.language.isCapitalPrefix(self.currentAlpha[i-1]) and self.language.isCapitalPrefix(self.currentAlpha[i]):
                self.capitalMode = True
                continue
            elif self.capitalMode or (i-1 >= 0 and self.language.isCapitalPrefix(self.currentAlpha[i-1]) and self.currentAlpha[i].isalpha()):
                result += self.currentAlpha[i].upper()
                if self.currentAlpha[i] == ' ':
                    self.capitalMode = False
            elif not self.language.isCapitalPrefix(self.currentAlpha[i]):
                result += self.currentAlpha[i]
        self.currentAlpha = result
    
    def handleShortCuts(self):
        result = ''

        if any(shortCut in self.currentAlpha for shortCut in self.language.shortcuts.values()):
            for shortCut in self.language.shortcuts.items(): 
                if shortCut[1] in self.currentAlpha: 
                    result = self.currentAlpha.replace(shortCut[1],shortCut[0])
                    if (result != self.currentAlpha):
                        self.appliedRules.append({ 'name': f"Applied transformation {shortCut[1]} to {shortCut[0]}", 'textBefore':self.currentAlpha, 'textAfter': result})
                        self.currentAlpha = result
            

    def handleExceptions(self) :
        result, appliedRules = self.language.handleExceptions(self.currentAlpha)
        self.appliedRules += appliedRules
        self.currentAlpha = result
        self.handleShortCuts()
        
'''
    The Algorithm for Transcribing Braille Based Text to Spanish / English Alphabet:
    1. Split up the text into words by dividing them based on whitespace characters.
        - Whitespace includes spaces (' ') and new lines ('\n')

    2. Handle the numbers:
        - Numbers in braille use the same symbols as the first 10 letters of the alphabet.
            - The number '7' and the letter 'g' are both represented by '⠛'.
            - To differentiate between numbers and letters, an escape code (⠼) is placed before groups of numbers.
            - Therefore '7' is actually '⠼⠛' whereas 'g' is only '⠛'.
        - In this step, only the numbers are dealt with, so there will be a mix of both braille and Alphabet symbols.
            - Example: "123-456-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK"
    
    3. Transcribe symbols
        a) Transcribe combined symbols
            - Check if the symbol is part of a combined symbol
        b) Transcribe symbol
      
    4. Handle the capitals.
        - Similarly to numbers in braille, capital letters need an escape code (⠠).
        - The escape code (⠠) is added to the beginning of each capital letter and the letter is changed to lowercase.
            - Example 1: "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-⠠j⠠u⠠n⠠k". The dashes still remain.
            - Example 2: "Sweet" becomes "⠠sweet". The non-capital letters remain untouched.
    
    5. Handle shared Braille symbols:
       There are some braille symbols that have different representations in alpha, depending on their position in the text. 
       For each of those symbols there is an algoritm to decide which alpha representation to use depending on the surrounding chars.

    6. Handle ShortCuts. 
       There are some special caracters, that are respresented by combination of other caracters. 
       For example © is converted to (C) or ª is converted to .a
    '''
        
