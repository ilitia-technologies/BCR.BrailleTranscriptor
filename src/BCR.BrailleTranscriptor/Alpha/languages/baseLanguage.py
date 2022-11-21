from ..BrailleUtils import *

class BaseLanguage(object):
    """description of class"""
    def __init__(self):
        pass

    UNRECOGNIZED = '%'
        
    numbers_alphaToBraille = {
           '1' : '100000', # char:⠁ puntos: 1 
           '2' : '110000', # char:⠃ puntos: 12 
           '3' : '100100', # char:⠉ puntos: 14 
           '4' : '100110', # char:⠙ puntos: 145 
           '5' : '100010', # char:⠑ puntos: 15 
           '6' : '110100', # char:⠋ puntos: 124 
           '7' : '110110', # char:⠛ puntos: 1245 
           '8' : '110010', # char:⠓ puntos: 125 
           '9' : '010100', # char:⠊ puntos: 24 
           '0' : '010110', # char:⠚ puntos: 245 
           }

    numbers_brailleToAlpha = {
           '100000': '1', # char:⠁ puntos: 1 
           '110000': '2', # char:⠃ puntos: 12 
           '100100': '3', # char:⠉ puntos: 14 
           '100110': '4', # char:⠙ puntos: 145 
           '100010': '5', # char:⠑ puntos: 15 
           '110100': '6', # char:⠋ puntos: 124 
           '110110': '7', # char:⠛ puntos: 1245
           '110010': '8', # char:⠓ puntos: 125 
           '010100': '9', # char:⠊ puntos: 24 
           '010110': '0'  # char:⠚ puntos: 245 
           }


    def getBrailleFromNumber(self, chr:str, addNumberPrefix:bool):
        if addNumberPrefix:
            return BrailleUtils.label010_to_chr(self.NUMBER) + BrailleUtils.label010_to_chr(self.numbers_alphaToBraille.get(chr))
        else:
            return BrailleUtils.label010_to_chr(self.numbers_alphaToBraille.get(chr))


    def getBrailleFromAlpha(self, char):
        # Convert an alphabetic char to braille.

        if self.__isBraille__(char):
            return char
        elif char == "\n":
            return "\n"
        elif char in self.letters_alphaToBraille and char.isupper():
            return self.getCapitalPrefix() + self.getLetterToBraille(char)
        elif char in self.letters_alphaToBraille:
            return  self.getLetterToBraille(char)
        elif char in self.punctuation_alphaToBraille:
            return self.getPunctuationToBraille(char)
        else:
            if self.verbose:
                print("Unrecognized Symbol:", char)
            return ''

    def getNumberPrefix(self):
        return BrailleUtils.label010_to_chr(self.NUMBER)

    def isNumberPrefix(self, char):
        return self.getNumberPrefix() == char

    def isEndNumberSymbol(self, char):
        return BrailleUtils.chr_to_label010(char) in self.endNumberAndIncludeSymbols or BrailleUtils.chr_to_label010(char) in self.endNumberSymbols

    def includeEndNumberSymbol(self, char):
        return BrailleUtils.chr_to_label010(char) in self.endNumberAndIncludeSymbols

    def getCapitalPrefix(self):
        return BrailleUtils.label010_to_chr(self.CAPITAL)

    def isCapitalPrefix(self, char):
        return self.getCapitalPrefix() == char

    def getNumberFromBraille(self, chr):
        return self.numbers_brailleToAlpha.get(BrailleUtils.chr_to_label010(chr))

    def getAlphaFromBraille(self, char):
        lbl_char = BrailleUtils.chr_to_label010(char)
        if lbl_char in self.letters_brailleToAlpha:
            return self.letters_brailleToAlpha.get(lbl_char)
        elif lbl_char in self.punctuation_brailleToAlpha:
            return self.punctuation_brailleToAlpha.get(lbl_char)
        elif lbl_char in self.sharedBrailleSymbols or lbl_char == self.CAPITAL:
            return char
        else:
            if self.verbose:
                print("Unrecognized Symbol:", lbl_char, "with unicode:", ord(char))
            return char

    def getLetterToBraille(self, chr):
        return BrailleUtils.label010_to_chr(self.letters_alphaToBraille.get(chr))

    def getPunctuationToBraille(self, chr):
        return BrailleUtils.label010_to_chr(self.punctuation_alphaToBraille.get(chr))
   
    def isBrailleCombinedSymbol(self, chr, nextchr):
        return f"{BrailleUtils.chr_to_label010(chr)}-{BrailleUtils.chr_to_label010(nextchr)}" in self.combinedSymbols_brailleToAlpha 

    def isCombinedSymbol(self, chr):
        return chr in self.combinedSymbols_alphaToBraille

    def getCombinedSymbol(self, chr, nextchr):
        return self.combinedSymbols_brailleToAlpha.get(f"{BrailleUtils.chr_to_label010(chr)}-{BrailleUtils.chr_to_label010(nextchr)}")

    def getCombinedSymbolToBraille(self, chr):
        symbol = self.combinedSymbols_alphaToBraille.get(chr).split("-")
        return BrailleUtils.label010_to_chr(symbol[0])+BrailleUtils.label010_to_chr(symbol[1])
    
    def isContraction(self, word):
        return word in self.contractions_alphaToBraille 

    def isBrailleNumber(self, char):
        return BrailleUtils.chr_to_label010(char) in self.numbers_brailleToAlpha 

    def isBrailleLetter(self, char):
        return BrailleUtils.chr_to_label010(char) in self.letters_brailleToAlpha 

    def isBrailleContraction(self, char):
        return BrailleUtils.chr_to_label010(char) in self.contractions_brailleToAlpha 

    def isBraillePunctuation(self, char):
        return BrailleUtils.chr_to_label010(char) in self.punctuation_brailleToAlpha 

    def __isBraille__(self, char):
        lbl_char = BrailleUtils.chr_to_label010(char)
        return lbl_char in self.numbers_brailleToAlpha \
            or lbl_char in self.letters_brailleToAlpha \
            or lbl_char in self.punctuation_brailleToAlpha \
            or lbl_char in self.contractions_brailleToAlpha \
            or lbl_char == self.CAPITAL \
            or lbl_char == self.NUMBER

 
