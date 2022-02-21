import re
def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )
texto = "hola adios hola hola"
patrones = ['hla', 'hola', 'hoola']
print (buscar(patrones, texto))