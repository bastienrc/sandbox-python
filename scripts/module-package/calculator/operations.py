# -----------------
# Opérations
# -----------------
def division(numerator, denominateur):
    try:
        result = numerator / denominateur
        return result
    except ZeroDivisionError:
        print("Division par zéro impossible !!!")

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b
