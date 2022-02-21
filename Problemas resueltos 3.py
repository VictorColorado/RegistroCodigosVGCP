import re

frase = "Ramón y Román programan en Python"

patron = '.+n'

print(re.findall(patron, frase))

patron = '.+?n'

print(re.findall(patron, frase))