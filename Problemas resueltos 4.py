import re

frase = "Tengo 2 hijos que tienen 15 y 11 años"

patron = '[0-9]+'

print(re.findall(patron, frase))