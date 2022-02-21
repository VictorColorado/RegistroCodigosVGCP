import re

txt = "hola adios hola hola"
print (re.findall('hola', txt))
print (len(re.findall('hola', txt)))