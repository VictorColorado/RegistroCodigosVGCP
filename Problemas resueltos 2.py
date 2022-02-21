import re
frase = "¡Esto es una frase! Además contiene signos de puntuación. ¿Los eliminamos?"

patron = '[^¡!.¿? ]+'

print(re.findall(patron, frase))