import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

#functions def.
def addition(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1-number_2

def multiplification(number_1, number_2):
    return number_1*number_2

def division(number_1, number_2):
    return number_1/number_2

#intro
print("Drogi Mentorze! Przetestuj mój kalkulator!")
calculations_result = None
calculations= input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
number_1 = float(input("Podaj składnik 1. "))
number_2 = float(input("Podaj składnik 2. "))

#result
if calculations == '1':
    calculations_name = "Dodaję: "
    calculations_result=addition(number_1,number_2)
elif calculations == '2':
    calculations_name = "Odejmuję: "
    calculations_result=subtraction(number_1,number_2)
elif calculations == '3':
    calculations_name = "Mnożę: "
    calculations_result=multiplification(number_1,number_2)
elif calculations == '4':
    calculations_name = "Dzielę: "
    calculations_result=division(number_1,number_2)
else:
    print("Błąd przy wpisywaniu składników")
    exit(1)

#loggi
if __name__ == "__main__":
     logging.debug(str(calculations_name) + str(number_1)+ " i " + str(number_2))
     logging.debug("Wynik to %s" % (calculations_result))