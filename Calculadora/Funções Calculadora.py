#Funções
def soma(x,y):
    r=(x+y)
    return r

def div(x,y):
    r=(x/y)
    return r

def mult(x,y):
    r=(x*y)
    return r

def sub(x,y):
    r=(x-y)
    return r



#Programa Principal
x = input('digite o x ')
operador = input('digite o operador ')
y = input(' digite o y ')
if operador == '+':
    resultado = soma(float(x),float(y))
elif operador == '-':
    resultado = sub(float(x),float(y))
elif operador == '*':
    resultado = mult(int(x),int(y))
elif operador == '/':
    resultado = div(int(x),int(y))
print ('o resultado é ', resultado)
