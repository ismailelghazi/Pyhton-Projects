def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


a = float(input("number 1: "))

b = float(input("number 2: "))

opr = ["+", "-", "/", "*"]

for n in opr:
    print(n)
chose = input("give me what do you want :")
if chose == "+":
    anser = add(a, b)
    print(f"{a} {chose} {b} = "+str(anser))
elif chose == "-":
    anser = subtract(a, b)
    print(f"{a} {chose} {b} = "+str(anser))
elif chose == "*":
    anser = multiply(a, b)

    print(f"{a} {chose} {b} = "+str(anser))
elif chose == "/":
    anser = divide(a, b)

    print(f"{a} {chose} {b} = "+str(anser))
else:
    print(f"{chose} is not a oprition ")
isr=int(input("you want contin or not 1=no or 0=yes"))

while not isr:
    n1=float(input("number 1: "))
    opr = ["+", "-", "/", "*"]

    for n in opr:
        print(n)
    chose = input("give me what do you want :")

    if chose == "+":
        anser+=n1
        print( str(anser))
    elif chose == "-":
        anser-=n1
        print(str(anser))
    elif chose=="*":
        anser*=n1
        print(str(anser))
    elif chose == "/":
        anser /= n1
        print(str(anser))
    else:
        print(f"{chose} is not a oprition ")
    isr = int(input("you want contin or not 1=no or 0=yes"))
