def sum( a,  b):
    return a + b
def res(a, b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

def calculator():
    while True:
        a = float(input("Dame un numerico: "))
        x = str(input("Y que operacion quiere usted? (+,-,*,/) "))
        b = float(input("Ahora dame otro numerico: "))

        if x == '+':
            res = a + b
        elif x == '-':
            res = a - b
        elif x == '*':
            res = a * b
        elif x == '/':
            res = a / b
        else:
            print("Operador no valido!!")
            continue
        print("Tipo_Variable_Primer_Dato ->", type(a))
        print("Tipo_Variable_Segundo_Dato ->", type(b))
        print("Tipo_Variable_Resultado ->", type(x))
        print("Resultado:", res)
        if input("Do you want to continue? (yes/no): ").lower() != 'yes':
            break


calculator()