import re

txt = "En esta cadena se encuentra una palabra mágica"

x = re.search('mágica', txt)
print(x.start() )
print(x.end() )
print(x.span() )
print(x.string )

if x:
    print("SI se ha encontrado!")
else:
    print("NO encontrado")