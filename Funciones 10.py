def maximo(a,b):
    if x>y:
        return x
    else:
        return y
def minimo(a,b):
    if x<y:
        return x
    else:
        return y
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))    