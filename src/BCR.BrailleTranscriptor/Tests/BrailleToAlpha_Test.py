from Alpha import BrailleToAlphaTranscriptor 
from Alpha.languages import Spanish

samples = [
    ['«BULGARIA: 160; IRLANDA: 170»', '⠦⠨⠨⠃⠥⠇⠛⠁⠗⠊⠁⠒ ⠼⠁⠋⠚⠆ ⠨⠨⠊⠗⠇⠁⠝⠙⠁⠒ ⠼⠁⠛⠚⠦'],
    ['¡Ah, sí...!,', '⠖⠨⠁⠓⠂ ⠎⠌⠄⠄⠄⠖⠂'],
    ['«¿Vaya qué?»', '⠦⠢⠨⠧⠁⠽⠁ ⠟⠥⠮⠢⠦'],
    ['«No está mal así.»', '⠦⠨⠝⠕ ⠑⠎⠞⠷ ⠍⠁⠇ ⠁⠎⠌⠄⠦'],
    ['¿«Si»?', '⠢⠦⠨⠎⠊⠦⠢'],
    ['—¿Dónde está Nagini?', '⠤⠤⠢⠨⠙⠬⠝⠙⠑ ⠑⠎⠞⠷ ⠨⠝⠁⠛⠊⠝⠊⠢'],
    ["%", '⠸⠴'],
    ["€", '⠸⠑'],
    ["1.1", '⠼⠁⠄⠼⠁'],
    ["1ª", '⠼⠁⠄⠁'],
    ['abcdefghij klmnopqrst uvwxyz', '⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚ ⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞ ⠥⠧⠺⠭⠽⠵'],
    ['La chica de la ventana ccccccccccccccccccccccc © de esta edición: rupo Editorial Luis Vive; 2018 Impreso en Zaragoza, España Isbn: 978-84-140-1220-8 Depósito legal: Z 24-2018 Diseño de la colección: Manuel Estrada Titulo original: *A rapaza da fiestra* Ilustraciones: Fernando Llorente', 
     '⠨⠇⠁ ⠉⠓⠊⠉⠁ ⠙⠑ ⠇⠁ ⠧⠑⠝⠞⠁⠝⠁ ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉ ⠣⠨⠉⠜ ⠙⠑ ⠑⠎⠞⠁ ⠑⠙⠊⠉⠊⠬⠝⠒ ⠗⠥⠏⠕ ⠨⠑⠙⠊⠞⠕⠗⠊⠁⠇ ⠨⠇⠥⠊⠎ ⠨⠧⠊⠧⠑⠆ ⠼⠃⠚⠁⠓ ⠨⠊⠍⠏⠗⠑⠎⠕ ⠑⠝ ⠨⠵⠁⠗⠁⠛⠕⠵⠁⠂ ⠨⠑⠎⠏⠁⠻⠁ ⠨⠊⠎⠃⠝⠒ ⠼⠊⠛⠓⠤⠼⠓⠙⠤⠼⠁⠙⠚⠤⠼⠁⠃⠃⠚⠤⠼⠓ ⠨⠙⠑⠏⠬⠎⠊⠞⠕ ⠇⠑⠛⠁⠇⠒ ⠨⠵ ⠼⠃⠙⠤⠼⠃⠚⠁⠓ ⠨⠙⠊⠎⠑⠻⠕ ⠙⠑ ⠇⠁ ⠉⠕⠇⠑⠉⠉⠊⠬⠝⠒ ⠨⠍⠁⠝⠥⠑⠇ ⠨⠑⠎⠞⠗⠁⠙⠁ ⠨⠞⠊⠞⠥⠇⠕ ⠕⠗⠊⠛⠊⠝⠁⠇⠒ ⠔⠨⠁ ⠗⠁⠏⠁⠵⠁ ⠙⠁ ⠋⠊⠑⠎⠞⠗⠁⠔ ⠨⠊⠇⠥⠎⠞⠗⠁⠉⠊⠕⠝⠑⠎⠒ ⠨⠋⠑⠗⠝⠁⠝⠙⠕ ⠨⠇⠇⠕⠗⠑⠝⠞⠑'],
    ['*Muy frecuentemente, las lágrimas son la última sonrisa del amor. STENDHAL La dicha está solo en la esperanza, en la ilusión sin fin. GUY DE MAUPASSANT*',
     '⠔⠨⠍⠥⠽ ⠋⠗⠑⠉⠥⠑⠝⠞⠑⠍⠑⠝⠞⠑⠂ ⠇⠁⠎ ⠇⠷⠛⠗⠊⠍⠁⠎ ⠎⠕⠝ ⠇⠁ ⠾⠇⠞⠊⠍⠁ ⠎⠕⠝⠗⠊⠎⠁ ⠙⠑⠇ ⠁⠍⠕⠗⠄ ⠨⠨⠎⠞⠑⠝⠙⠓⠁⠇ ⠨⠇⠁ ⠙⠊⠉⠓⠁ ⠑⠎⠞⠷ ⠎⠕⠇⠕ ⠑⠝ ⠇⠁ ⠑⠎⠏⠑⠗⠁⠝⠵⠁⠂ ⠑⠝ ⠇⠁ ⠊⠇⠥⠎⠊⠬⠝ ⠎⠊⠝ ⠋⠊⠝⠄ ⠨⠨⠛⠥⠽ ⠨⠨⠙⠑ ⠨⠨⠍⠁⠥⠏⠁⠎⠎⠁⠝⠞⠔'],
    ['c h 9 Cuando Lucas decide probar el te- lescopio que le regalan sus padres por su cumpleaños, no imagina la sorpresa que le espera al otro lado de su ven- tana. Tras los cristales rotos de una fábrica en ruinas descubre a una chica con la que empieza a comunicarse con breves mensajes escritos sobre carto- nes. Con el tiempo comprenderá la re- clusión de esa muchacha y la imposibi- lidad aparente de prestarle ayuda. Xavier Estévez nació en Bélgica porque el destino así lo quiso, aunque su vida está ligada a la ciudad de Vigo desde hace muchos años. Todo el tiempo que su trabajo de profesor de primaria le permite lo de- dica a las cosas que le apasionan: la radio, la magia o la lectura de cuan- tos libros caen en sus manos. Desde niño escribe historias con todas las aventuras que siempre quiso vivir. 0349279-1', 
     '⠉ ⠓ ⠼⠊ ⠨⠉⠥⠁⠝⠙⠕ ⠨⠇⠥⠉⠁⠎ ⠙⠑⠉⠊⠙⠑ ⠏⠗⠕⠃⠁⠗ ⠑⠇ ⠞⠑⠤ ⠇⠑⠎⠉⠕⠏⠊⠕ ⠟⠥⠑ ⠇⠑ ⠗⠑⠛⠁⠇⠁⠝ ⠎⠥⠎ ⠏⠁⠙⠗⠑⠎ ⠏⠕⠗ ⠎⠥ ⠉⠥⠍⠏⠇⠑⠁⠻⠕⠎⠂ ⠝⠕ ⠊⠍⠁⠛⠊⠝⠁ ⠇⠁ ⠎⠕⠗⠏⠗⠑⠎⠁ ⠟⠥⠑ ⠇⠑ ⠑⠎⠏⠑⠗⠁ ⠁⠇ ⠕⠞⠗⠕ ⠇⠁⠙⠕ ⠙⠑ ⠎⠥ ⠧⠑⠝⠤ ⠞⠁⠝⠁⠄ ⠨⠞⠗⠁⠎ ⠇⠕⠎ ⠉⠗⠊⠎⠞⠁⠇⠑⠎ ⠗⠕⠞⠕⠎ ⠙⠑ ⠥⠝⠁ ⠋⠷⠃⠗⠊⠉⠁ ⠑⠝ ⠗⠥⠊⠝⠁⠎ ⠙⠑⠎⠉⠥⠃⠗⠑ ⠁ ⠥⠝⠁ ⠉⠓⠊⠉⠁ ⠉⠕⠝ ⠇⠁ ⠟⠥⠑ ⠑⠍⠏⠊⠑⠵⠁ ⠁ ⠉⠕⠍⠥⠝⠊⠉⠁⠗⠎⠑ ⠉⠕⠝ ⠃⠗⠑⠧⠑⠎ ⠍⠑⠝⠎⠁⠚⠑⠎ ⠑⠎⠉⠗⠊⠞⠕⠎ ⠎⠕⠃⠗⠑ ⠉⠁⠗⠞⠕⠤ ⠝⠑⠎⠄ ⠨⠉⠕⠝ ⠑⠇ ⠞⠊⠑⠍⠏⠕ ⠉⠕⠍⠏⠗⠑⠝⠙⠑⠗⠷ ⠇⠁ ⠗⠑⠤ ⠉⠇⠥⠎⠊⠬⠝ ⠙⠑ ⠑⠎⠁ ⠍⠥⠉⠓⠁⠉⠓⠁ ⠽ ⠇⠁ ⠊⠍⠏⠕⠎⠊⠃⠊⠤ ⠇⠊⠙⠁⠙ ⠁⠏⠁⠗⠑⠝⠞⠑ ⠙⠑ ⠏⠗⠑⠎⠞⠁⠗⠇⠑ ⠁⠽⠥⠙⠁⠄ ⠨⠭⠁⠧⠊⠑⠗ ⠨⠑⠎⠞⠮⠧⠑⠵ ⠝⠁⠉⠊⠬ ⠑⠝ ⠨⠃⠮⠇⠛⠊⠉⠁ ⠏⠕⠗⠟⠥⠑ ⠑⠇ ⠙⠑⠎⠞⠊⠝⠕ ⠁⠎⠌ ⠇⠕ ⠟⠥⠊⠎⠕⠂ ⠁⠥⠝⠟⠥⠑ ⠎⠥ ⠧⠊⠙⠁ ⠑⠎⠞⠷ ⠇⠊⠛⠁⠙⠁ ⠁ ⠇⠁ ⠉⠊⠥⠙⠁⠙ ⠙⠑ ⠨⠧⠊⠛⠕ ⠙⠑⠎⠙⠑ ⠓⠁⠉⠑ ⠍⠥⠉⠓⠕⠎ ⠁⠻⠕⠎⠄ ⠨⠞⠕⠙⠕ ⠑⠇ ⠞⠊⠑⠍⠏⠕ ⠟⠥⠑ ⠎⠥ ⠞⠗⠁⠃⠁⠚⠕ ⠙⠑ ⠏⠗⠕⠋⠑⠎⠕⠗ ⠙⠑ ⠏⠗⠊⠍⠁⠗⠊⠁ ⠇⠑ ⠏⠑⠗⠍⠊⠞⠑ ⠇⠕ ⠙⠑⠤ ⠙⠊⠉⠁ ⠁ ⠇⠁⠎ ⠉⠕⠎⠁⠎ ⠟⠥⠑ ⠇⠑ ⠁⠏⠁⠎⠊⠕⠝⠁⠝⠒ ⠇⠁ ⠗⠁⠙⠊⠕⠂ ⠇⠁ ⠍⠁⠛⠊⠁ ⠕ ⠇⠁ ⠇⠑⠉⠞⠥⠗⠁ ⠙⠑ ⠉⠥⠁⠝⠤ ⠞⠕⠎ ⠇⠊⠃⠗⠕⠎ ⠉⠁⠑⠝ ⠑⠝ ⠎⠥⠎ ⠍⠁⠝⠕⠎⠄ ⠨⠙⠑⠎⠙⠑ ⠝⠊⠻⠕ ⠑⠎⠉⠗⠊⠃⠑ ⠓⠊⠎⠞⠕⠗⠊⠁⠎ ⠉⠕⠝ ⠞⠕⠙⠁⠎ ⠇⠁⠎ ⠁⠧⠑⠝⠞⠥⠗⠁⠎ ⠟⠥⠑ ⠎⠊⠑⠍⠏⠗⠑ ⠟⠥⠊⠎⠕ ⠧⠊⠧⠊⠗⠄ ⠼⠚⠉⠙⠊⠃⠛⠊⠤⠼⠁'],
    ['1 Lectura *El pirata Malapata* El pirata Malapata saltó desde la cubierta del barco hasta el bote y se mojó los pies. —¡Rayas y centollos! Ahora volverán a olerme los pies a pescado podrido- resopló. El pirata llevaba tres meses navegando junto a su tripulación en busca de una isla perdida. Y durante tres meses no había dejado de llover. Sólo los últimos dos días había salido el sol los piratas habían conseguido secar su ropa colgándola en los cables del mástil. Más que un barco pirata, el galeón Boquerón parecía un tendedero.',
     '⠼⠁ ⠨⠇⠑⠉⠞⠥⠗⠁ ⠔⠨⠑⠇ ⠏⠊⠗⠁⠞⠁ ⠨⠍⠁⠇⠁⠏⠁⠞⠁⠔ ⠨⠑⠇ ⠏⠊⠗⠁⠞⠁ ⠨⠍⠁⠇⠁⠏⠁⠞⠁ ⠎⠁⠇⠞⠬ ⠙⠑⠎⠙⠑ ⠇⠁ ⠉⠥⠃⠊⠑⠗⠞⠁ ⠙⠑⠇ ⠃⠁⠗⠉⠕ ⠓⠁⠎⠞⠁ ⠑⠇ ⠃⠕⠞⠑ ⠽ ⠎⠑ ⠍⠕⠚⠬ ⠇⠕⠎ ⠏⠊⠑⠎⠄ ⠤⠤⠖⠨⠗⠁⠽⠁⠎ ⠽ ⠉⠑⠝⠞⠕⠇⠇⠕⠎⠖ ⠨⠁⠓⠕⠗⠁ ⠧⠕⠇⠧⠑⠗⠷⠝ ⠁ ⠕⠇⠑⠗⠍⠑ ⠇⠕⠎ ⠏⠊⠑⠎ ⠁ ⠏⠑⠎⠉⠁⠙⠕ ⠏⠕⠙⠗⠊⠙⠕⠤ ⠗⠑⠎⠕⠏⠇⠬⠄ ⠨⠑⠇ ⠏⠊⠗⠁⠞⠁ ⠇⠇⠑⠧⠁⠃⠁ ⠞⠗⠑⠎ ⠍⠑⠎⠑⠎ ⠝⠁⠧⠑⠛⠁⠝⠙⠕ ⠚⠥⠝⠞⠕ ⠁ ⠎⠥ ⠞⠗⠊⠏⠥⠇⠁⠉⠊⠬⠝ ⠑⠝ ⠃⠥⠎⠉⠁ ⠙⠑ ⠥⠝⠁ ⠊⠎⠇⠁ ⠏⠑⠗⠙⠊⠙⠁⠄ ⠨⠽ ⠙⠥⠗⠁⠝⠞⠑ ⠞⠗⠑⠎ ⠍⠑⠎⠑⠎ ⠝⠕ ⠓⠁⠃⠌⠁ ⠙⠑⠚⠁⠙⠕ ⠙⠑ ⠇⠇⠕⠧⠑⠗⠄ ⠨⠎⠬⠇⠕ ⠇⠕⠎ ⠾⠇⠞⠊⠍⠕⠎ ⠙⠕⠎ ⠙⠌⠁⠎ ⠓⠁⠃⠌⠁ ⠎⠁⠇⠊⠙⠕ ⠑⠇ ⠎⠕⠇ ⠇⠕⠎ ⠏⠊⠗⠁⠞⠁⠎ ⠓⠁⠃⠌⠁⠝ ⠉⠕⠝⠎⠑⠛⠥⠊⠙⠕ ⠎⠑⠉⠁⠗ ⠎⠥ ⠗⠕⠏⠁ ⠉⠕⠇⠛⠷⠝⠙⠕⠇⠁ ⠑⠝ ⠇⠕⠎ ⠉⠁⠃⠇⠑⠎ ⠙⠑⠇ ⠍⠷⠎⠞⠊⠇⠄ ⠨⠍⠷⠎ ⠟⠥⠑ ⠥⠝ ⠃⠁⠗⠉⠕ ⠏⠊⠗⠁⠞⠁⠂ ⠑⠇ ⠛⠁⠇⠑⠬⠝ ⠨⠃⠕⠟⠥⠑⠗⠬⠝ ⠏⠁⠗⠑⠉⠌⠁ ⠥⠝ ⠞⠑⠝⠙⠑⠙⠑⠗⠕⠄'],
    ['1 Prueba de la unidad 4 1. Describe qué movimiento (tras- lación, rotación, reflexión o una com- binación de ellas) permite encajar una figura sobre otra. (Figura 1) a) Figura 1.A b) Figura 1.B c) Figura 1.C d) Figura 1.D',
    '⠼⠁ ⠨⠏⠗⠥⠑⠃⠁ ⠙⠑ ⠇⠁ ⠥⠝⠊⠙⠁⠙ ⠼⠙ ⠼⠁⠄ ⠨⠙⠑⠎⠉⠗⠊⠃⠑ ⠟⠥⠮ ⠍⠕⠧⠊⠍⠊⠑⠝⠞⠕ ⠣⠞⠗⠁⠎⠤ ⠇⠁⠉⠊⠬⠝⠂ ⠗⠕⠞⠁⠉⠊⠬⠝⠂ ⠗⠑⠋⠇⠑⠭⠊⠬⠝ ⠕ ⠥⠝⠁ ⠉⠕⠍⠤ ⠃⠊⠝⠁⠉⠊⠬⠝ ⠙⠑ ⠑⠇⠇⠁⠎⠜ ⠏⠑⠗⠍⠊⠞⠑ ⠑⠝⠉⠁⠚⠁⠗ ⠥⠝⠁ ⠋⠊⠛⠥⠗⠁ ⠎⠕⠃⠗⠑ ⠕⠞⠗⠁⠄ ⠣⠨⠋⠊⠛⠥⠗⠁ ⠼⠁⠜ ⠁⠜ ⠨⠋⠊⠛⠥⠗⠁ ⠼⠁⠄⠨⠁ ⠃⠜ ⠨⠋⠊⠛⠥⠗⠁ ⠼⠁⠄⠨⠃ ⠉⠜ ⠨⠋⠊⠛⠥⠗⠁ ⠼⠁⠄⠨⠉ ⠙⠜ ⠨⠋⠊⠛⠥⠗⠁ ⠼⠁⠄⠨⠙'],
    ["123456", '⠼⠁⠃⠉⠙⠑⠋'],
    ["¡Hola!",'⠖⠨⠓⠕⠇⠁⠖'],
    ["Hola, ¿que tal?",'⠨⠓⠕⠇⠁⠂ ⠢⠟⠥⠑ ⠞⠁⠇⠢'],
    ["-a-b-c-", '⠤⠁⠤⠃⠤⠉⠤'],
    ["-123-456-", '⠤⠼⠁⠃⠉⠤⠼⠙⠑⠋⠤']
    
    ]

def process(text):
    print(sample)
    language = Spanish()
    transcriptor = BrailleToAlphaTranscriptor(language, True)
    result, appliedRules = transcriptor.transcribe(sample[1])

    print('Transcribed text (final): ' + result)
    print('Match: ', result == sample[0])
    
    print()
    print('--------------------')


for sample in samples:
    process(samples)
    pass

