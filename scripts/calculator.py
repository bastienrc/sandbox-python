#
# Calculator
#

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


# -----------------
# Main
# -----------------
def input_two_number():
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    return num1, num2

def menu():
    print("««« MENU »»»")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    selection = input("Sélectionner votre opération ? (1 à 4) : ")

    while selection not in ["1", "2", "3", "4"]:
        selection = input("Sélection invalide. Entrez votre selection ? (1 à 4) : ")

    return selection

def calcul(selection):
    num1, num2 = input_two_number()
    match selection:
        case '1':
            result = addition(num1, num2)
        case '2':
            result = substraction(num1, num2)
        case '3':
            result = multiplication(num1, num2)
        case '4':
            result = division(num1, num2)
        case _:
            print("Selection invalide !!!")

    return result

print("Bienvenue sur ma calculatrice !")
selection = menu()
print(calcul(selection))
