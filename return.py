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

    print(f"{a} {chose} {b} = "+str(add(a, b)))
else:
    print(f"{a} {chose} {b} = "+str(subtract(a, b)))
