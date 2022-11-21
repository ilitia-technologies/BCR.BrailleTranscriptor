from .baseLanguage import *
from ..BrailleUtils import *

class Spanish(BaseLanguage):
    """description of class"""

    def __init__(self):
        BaseLanguage.__init__(self)  

    CAPITAL = '000101'  # ⠨
    NUMBER = '001111'  # ⠼
    endNumberAndIncludeSymbols = [CAPITAL, '001000', '000111']
    endNumberSymbols = ['000010']
    
    punctuation_alphaToBraille = {
        ',': '010000', # char:⠂ puntos: 2 
        '.': '001000', # char:⠄ puntos: 3 
        ';': '011000', # char:⠆ puntos: 23 
        ':': '010010', # char:⠒ puntos: 25 
        '+': '011010', # char:⠖ puntos: 235 
        '¡': '011010', # char:⠖ puntos: 235 
        '!': '011010', # char:⠖ puntos: 235 
        '¿': '010001', # char:⠢ puntos: 26 
        '?': '010001', # char:⠢ puntos: 26 
        '=': '011011', # char:⠶ puntos: 2356 
        '#': '001111', # char:⠼ puntos: 3456 
        '-': '001001', # char:⠤ puntos: 36 
        '(': '110001', # char:⠣ puntos: 126 
        ')': '001110', # char:⠜ puntos: 345 
        '@': '000010', # char:⠐ puntos: 5 
        '*': '001010', # char:⠔ puntos: 35 
        '«': '011001', # char:⠦ puntos: 236 
        '»': '011001', # char:⠦ puntos: 236 
        '¨': '000100', # char:⠈ puntos: 4 
        '’': '001000', # char:⠄ puntos: 3 
        }

    punctuation_brailleToAlpha = {
        '010000': ',', # char:⠂ puntos: 2 
        '011000': ';', # char:⠆ puntos: 23 
        '010010': ':', # char:⠒ puntos: 25 
        '011011': '=', # char:⠶ puntos: 2356 
        '001111': '#', # char:⠼ puntos: 3456 
        '001001': '-', # char:⠤ puntos: 36 
        '110001': '(', # char:⠣ puntos: 126 
        '001110': ')', # char:⠜ puntos: 345 
        '000010': '@', # char:⠐ puntos: 5  
        '001010': '*', # char:⠔ puntos: 35  
        '010011': ':', # char:⠲ puntos: 256
        '000100': '¨'  # char:⠈ puntos: 4
    }

    combinedSymbols_brailleToAlpha = {
        '000111-001011' : '%',
        '000111-100010' : '€',
        '001001-001001' : '—'
        
    }

    combinedSymbols_alphaToBraille = {
        '%': '000111-001011',
        '€': '000111-100010',
        '—': '001001-001001' 
    }

    contractions_brailleToAlpha = {}
    contractions_alphaToBraille = {}

    letters_alphaToBraille = {
        'a': '100000', # char:⠁ puntos: 1 
        'b': '110000', # char:⠃ puntos: 12 
        'c': '100100', # char:⠉ puntos: 14 
        'd': '100110', # char:⠙ puntos: 145 
        'e': '100010', # char:⠑ puntos: 15 
        'f': '110100', # char:⠋ puntos: 124 
        'g': '110110', # char:⠛ puntos: 1245 
        'h': '110010', # char:⠓ puntos: 125 
        'i': '010100', # char:⠊ puntos: 24 
        'j': '010110', # char:⠚ puntos: 245 
        'k': '101000', # char:⠅ puntos: 13 
        'l': '111000', # char:⠇ puntos: 123 
        'm': '101100', # char:⠍ puntos: 134 
        'n': '101110', # char:⠝ puntos: 1345 
        'o': '101010', # char:⠕ puntos: 135 
        'p': '111100', # char:⠏ puntos: 1234 
        'q': '111110', # char:⠟ puntos: 12345 
        'r': '111010', # char:⠗ puntos: 1235 
        's': '011100', # char:⠎ puntos: 234 
        't': '011110', # char:⠞ puntos: 2345 
        'u': '101001', # char:⠥ puntos: 136 
        'v': '111001', # char:⠧ puntos: 1236 
        'w': '010111', # char:⠺ puntos: 2456 
        'x': '101101', # char:⠭ puntos: 1346 
        'y': '101111', # char:⠽ puntos: 13456 
        'z': '101011', # char:⠵ puntos: 1356 
        'á': '111011', # char:⠷ puntos: 12356 
        'é': '011101', # char:⠮ puntos: 2346 
        'í': '001100', # char:⠌ puntos: 34 
        'ó': '001101', # char:⠬ puntos: 346 
        'ú': '011111', # char:⠾ puntos: 23456 
        'ü': '110011', # char:⠳ puntos: 1256 
        'ñ': '110111', # char:⠻ puntos: 12456 
    }

    letters_brailleToAlpha = {
            '100000' : 'a', # char:⠁ puntos: 1 
            '110000' : 'b', # char:⠃ puntos: 12 
            '100100' : 'c', # char:⠉ puntos: 14 
            '100110' : 'd', # char:⠙ puntos: 145 
            '100010' : 'e', # char:⠑ puntos: 15 
            '110100' : 'f', # char:⠋ puntos: 124 
            '110110' : 'g', # char:⠛ puntos: 1245 
            '110010' : 'h', # char:⠓ puntos: 125 
            '010100' : 'i', # char:⠊ puntos: 24 
            '010110' : 'j', # char:⠚ puntos: 245 
            '101000' : 'k', # char:⠅ puntos: 13 
            '111000' : 'l', # char:⠇ puntos: 123 
            '101100' : 'm', # char:⠍ puntos: 134 
            '101110' : 'n', # char:⠝ puntos: 1345 
            '101010' : 'o', # char:⠕ puntos: 135 
            '111100' : 'p', # char:⠏ puntos: 1234 
            '111110' : 'q', # char:⠟ puntos: 12345 
            '111010' : 'r', # char:⠗ puntos: 1235 
            '011100' : 's', # char:⠎ puntos: 234 
            '011110' : 't', # char:⠞ puntos: 2345 
            '101001' : 'u', # char:⠥ puntos: 136 
            '111001' : 'v', # char:⠧ puntos: 1236 
            '010111' : 'w', # char:⠺ puntos: 2456 
            '101101' : 'x', # char:⠭ puntos: 1346 
            '101111' : 'y', # char:⠽ puntos: 13456 
            '101011' : 'z', # char:⠵ puntos: 1356 
            '111011' : 'á', # char:⠷ puntos: 12356 
            '011101' : 'é', # char:⠮ puntos: 2346 
            '001100' : 'í', # char:⠌ puntos: 34 
            '001101' : 'ó', # char:⠬ puntos: 346 
            '011111' : 'ú', # char:⠾ puntos: 23456 
            '110011' : 'ü', # char:⠳ puntos: 1256 
            '110111' : 'ñ'  # char:⠻ puntos: 12456 
           }

    shortcuts = {
        '©': '(C)',
        'ª': '.a',
        'º': '.o'
    }

    # simbolos compartidos
    sharedBrailleSymbols = {
        '001000' : ".’",    # char:⠄ puntos: 3 
        '011010' : '¡!+',   # char:⠖ puntos: 235 
        '010001' : '¿?',    # char:⠢ puntos: 26
        '011001' : '«»*',   # char:⠦ puntos: 236
    }

    def transcribe_011010(self, string, result):
        tempString = ""
        for i in range(0, len(string)):
            # Decipher whether "⠖" should be "+" or "¡" or "!".
            # Use ¡ at the beginning of the word, if previous letter is whitespace, - or , or if next letter is alpha
            # Use + if previous or next letter is digit
            if BrailleUtils.chr_to_label010(string[i]) == '011010':
                if i == 0 or (i > 0 and string[i-1] in [' ', '—', '-', ',']) or (i+1 <= len(string) and string[i+1].isalpha()): 
                    tempString += "¡"
                elif  (i-1 >= 0 and string[i-1].isdigit()) or (i+1 <= len(string) and string[i+1].isdigit()):
                    tempString += "+"
                else:
                    tempString += "!"
            else:
                tempString += string[i]   
        if (string != tempString):
            result.append({ 'name': "Transcribed ⠖ to + ¡ !: ",  'textBefore':string,  'textAfter':tempString})
            if self.verbose: 
                print(f"Rule applied: {result[-1][0]}, before: {result[-1][1]}, after: {result[-1][2]}")
        return tempString, result

    def transcribe_010001(self, string, result):
        tempString = ""
        for i in range(0, len(string)):
            # Decipher whether "⠢" should be "¿" or "?".
            # Use ¿ at the beginning of the word, if previous letter is whitespace, - or , or if next letter is alpha
            if BrailleUtils.chr_to_label010(string[i]) == '010001':
                if i == 0 or (i > 0 and string[i-1] in [' ', '—', '-', ',']) or (i+1 <= len(string) and string[i+1].isalpha()): 
                    tempString += "¿"
                else:
                    tempString += "?"
            else:
                tempString += string[i]   
        if (string != tempString):
            result.append({ 'name': "Transcribed ⠢ to ¿ ?: ",  'textBefore':string,  'textAfter':tempString})
            if self.verbose:
                print(f"Rule applied: {result[-1][0]}, before: {result[-1][1]}, after: {result[-1][2]}")
        return tempString, result

    def transcribe_011001(self, string, result):
        tempString = ""
        for i in range(0, len(string)):
            # Decipher whether "⠦" should be "«" "»" or "*".
            # Use * if previous and next char is no white space and at least one of them is digit  
            # Use » if previous letter is a letter, a digit or .!? or a braille symbol (not yet transcribed)
            # Use « in all other cases
            if BrailleUtils.chr_to_label010(string[i]) == '011001':
                if i-1 >= 0 and i+1 <= len(string) and (string[i-1] != ' ' and string[i+1] != ' ') and (string[i-1].isdigit() or string[i+1].isdigit()):
                    tempString += "*"
                elif i-1 >= 0 and (string[i-1].isalpha() or string[i-1].isdigit() or string[i-1] in  ['.', '!', '?'] or self.__isBraille__(string[i-1])):
                    tempString += "»"
                else:
                    tempString += "«"
            else:
                tempString += string[i]   
        if (string != tempString):
            result.append({ 'name': "Transcribed ⠦ to « » *: ",  'textBefore':string,  'textAfter':tempString})
            if self.verbose:
                print(f"Rule applied: {result[-1][0]}, before: {result[-1][1]}, after: {result[-1][2]}")
        return tempString, result

    def transcribe_001000(self, string, result):
        tempString = ""
        for i in range(0, len(string)):
            # Decipher whether "⠄" should be . or '.
            # Use ' if previous and next char are alpha and next letter is lower
            if BrailleUtils.chr_to_label010(string[i]) == '001000':
                if i-1 >= 0 and i+1 <= len(string) and (string[i-1].isalpha() and string[i+1].isalpha()) and string[i+1].islower():
                    tempString += "’"
                else:
                    tempString += "."
            else:
                tempString += string[i]   
        if (string != tempString):
            result.append({ 'name': "Transcribed ⠦ to . ': ",  'textBefore':string,  'textAfter':tempString})
            if self.verbose:
                print(f"Rule applied: {result[-1][0]}, before: {result[-1][1]}, after: {result[-1][2]}")
        return tempString, result

    def handleExceptions(self, string):
        # Fix exceptions where a braille symbol can have multiple meanings.
        tempString = ""
        result = []

        for braille in self.sharedBrailleSymbols:
            func = getattr(self, f"transcribe_{braille}")           
            string, result = func(string, result)      

        return string, result



    sharedAlpha = {
        '*': ['001010','011001'], # ⠔ (* como dos puntos) o  ⠦ (* como simbolo de resta)
        ':': ['010011', '010011'] # ⠒ (: como dos puntos) o ⠲ (: como simbolo de division)
        }
