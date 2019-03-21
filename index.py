from calc import add, sub, div, mult

op = input("Elige la operacion :")
x = input("Ingresa un numero:")
y = input("ingresa un numero:")
tx = x.replace()
ty = y.replace()
n1 = float(tx)
n2 = float(ty)

if op == "sumar":
    add(n1,n2)
elif op == "restar":
    sub(n1, n2)
elif op == "dividir":
    div(n1, n2)
else:
    mult(n1,n2)
