x = input('digite o x ')
operador = input('digite o operador ')
y = input(' digite o y ')
if operador == '+':
    resultado = int(x)+int(y)
elif operador == '-':
    resultado = int(x)-int(y)
elif operador == '*':
    resultado = int(x)*int(y)
elif operador == '/':
    resultado = int(x)/int(y)
print ('o resultado é ', resultado)
