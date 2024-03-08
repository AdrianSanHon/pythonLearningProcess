def sum( a,  b):
    return a + b
def res(a, b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

a = int(input("Dame un numerico: "))
x = str(input("Y que operacion quiere usted? "))
b = int(input("Ahora dame otro numerico: "))

print("a = ", type(a),"//","b = ",type(b),"//","c = ", type(x))

match (x):
    case "+":
        print(type(a),type(b))
        print("La suma de ", a , " y " , b ," es ", sum(a, b))
    case "-":
        print("La suma de ", a , " y " , b ," es ", res(a, b))
    case "*":
        print("La suma de ", a , " y " , b ," es ", mult(a, b))
    case "/":
        print("La suma de ", a , " y " , b ," es ", div(a, b))

