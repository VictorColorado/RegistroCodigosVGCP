import re
def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )
        
texto = "hola h0la Hola mola m0la M0la"
        
patrones = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}']

print (buscar(patrones, texto))