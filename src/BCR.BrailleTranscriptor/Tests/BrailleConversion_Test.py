from Alpha.BrailleUtils import *

def getCharAndLabel123(string):
    char = BrailleUtils.label010_to_chr(string)
    lbl123 = BrailleUtils.chr_to_label123(char)

    return char, lbl123
        
def writeResultsToFile(results):
    with open('brailleSymbols.txt', 'w', encoding='UTF-8') as f:
        for r in results:
            f.write(f"'{r[0]}', # char:{r[1]} puntos: {r[2]} \n")
   


symbols = [
'100000',
'110000',
'100100',
'100110',
'100010',
'110100',
'110110',
'110010',
'010100',
'010110'
]

results = []
for s in symbols:
    char, label = getCharAndLabel123(s)
    results.append([s, char, label])


writeResultsToFile(results)
