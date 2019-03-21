from calculadora import add, sub, div, mult

op = input("Elige la operacion :")
x = input("Ingresa un numero:")
y = input("ingresa un numero:")
n1 = float(x)
n2 = float(y)

if op == "sumar":
    add(n1,n2)
elif op == "restar":
    sub(n1, n2)
elif op == "dividir":
    div(n1, n2)
else:
    mult(n1,n2)
