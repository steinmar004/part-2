'''2_1
Napisz program, który dla trzech liczb a, b i c wprowadzonych z klawiatury sprawdza czy
są to trójki pitagorasowe. Dodatkowo należy założyć, że a>0, b>0, c>0.''' # NO I TEŻ JEST CAŁKOWITA; NIE-tylko-float

print("Jestem programem, który sprawdzi poprawność Twioch typów do 'trójki pitagorasowej'.")

a = int(input("Podaj pierwszą liczbę, która jest bokiem trójkąta: "))
b = int(input("Podaj drugą liczbę, która jest bokiem trójkąta: "))
c = int(input("Podaj trzecią liczbę, która powinna być przeciwprostokątną tego trójkąta: "))

if a < 0 or b < 0 or c < 0:
    print("Hej, nie podawaj tutaj minusów!")
elif a**2 + b**2 == c**2:
    print("Twoje typy przyprostokątnych i przeciwprostokątnej są okej.")
else:
    print("Nie trafiłeś.")    

if a * a + b * b == c * c and a > 0 and b > 0 and c > 0:
    print("Twoje typy przyprostokątnych i przeciwprostokątnej są okej.")
elif a * a + b * b == c * c and a < 0 or b < 0 or c < 0:
    print("Hej, nie podawaj tutaj minusów!")
else:
    print("Nie trafiłeś.")

'''2_2
Napisz program, który oblicza wartość x z równania ax + b = c. Wartości a, b i c należą do zbioru liczb rzeczywistych     
i są wprowadzane z kalwiatury. Dodatkowo należy zabezpieczyć program na wypadek sytuacji, kiedy wprowadzana wartość
a jest równa 0. Dla zmiennych a, b i c oraz x należy przyjąć format wyświetlania ich z dokładnośćią do dwóch miejsc po przecinku.'''

#                                        a'x' + b = c
# a != 0 
# a, b, c, x = "{:.2f}".format()

print("Jestem programem, który obliczy wartość x z równania 'ax + b = c', z danych podanych przez Ciebie, drogi użytkowniku.")

a= float(input("Drogi użytkowniku, podaj zmienną a:\n"))
if a == 0:
    print("Nie dziel przez zero!")
else:
    b = float(input("Drogi użytkowniku, podaj zmienną b:\n"))
    c = float(input("Drogi użytkowniku, podaj zmienną c:\n"))
    print("Wprowadzone przez Ciebie dane to:")
    print("{:.2f}".format(a))
    print("{:.2f}".format(b))
    print("{:.2f}".format(c))
    x = (c - b) / a
    print(f"x= {x}")

'''2_3
Napisz program, który oblicza pierwiastki równania kwadratowego ax'2' + bx + c = 0 , gdzie zmienne
a,b,c to liczby rzeczywiste wprowadzane z kalwiatury. Dla zmiennych a,b,c,x'1' oraz x'2' należy
przyjąć format wyświetlania ich na ekranie z dokładnością do dwóch miejsc po kropce. '''

#                              V ax'2' + bx + c = 0 ,                                X1 = (-b - pierw. delty) / (2 * a)
# a != 0 
#                               x1 czy x2 = ?                                       X2 = (-b + pierw. delty) / (2 * a)
# DELTA, NIEujemna V
# Pierwiastek z delty(.sqrt) czyli delta * * 0.5         V                    


print("Mój drogi użytkowniku, jestem programem, który obliczy Tobie pierwiastki trójmianu kwadratowego.")

a = float(input("Drogi użytkowniku, podaj proszę zmienną a:\n"))
b = float(input("Drogi użytkowniku, podaj proszę zmienną b:\n"))
c = float(input("Drogi użytkowniku, podaj proszę zmienną c:\n"))

print("Okej, podałeś następujące zmienne: ", end=' ')
print("{:.2f}".format(a), end= ' ')
print("{:.2f}".format(b), end= ' ')
print("{:.2f}".format(c), end= ' ')

if a == 0:
    print("Nie dziel przez zero!")
else:

    delta = b**2 - 4*a*c
    print(f"Delta jest równa= {delta:.2f}")

    if delta > 0:
        pierw_delty = delta ** 0.5

        x1 = (-b - pierw_delty) / (2 * a)
        print("Pierwszy pierwiastek równania to: ", end= ' ')
        print("{:.2f}".format(x1))
        x2 = (-b + pierw_delty) / (2 * a )
        print(f"Drugi pierwiastek równania to: ", end= ' ')
        print("{:.2f}".format(x2))
        print(f"Pierwiatek z delty jest równy: {pierw_delty:.2f}", end = ' ')
    else:
        print("ujemna delta: to się nie uda")

    

'''2_4
Napisz program, który ilustruje działanie operatora logicznego OR'''     #  WYKORZYSTUJĄ TEŻ OD RAZU NOT

a = True
b = True

print("Ten program ilustruje działanie operatora logicznego OR")
print(f"True or True > ", a or b )
print(f"True or not True(False) > ", a or not b )
print(f"Not True(False) or not True(False) > ", not a or not b )

'''2_5
Napisz program, który ilustruje działanie operatora logicznego AND'''

a = True
b = True

print("Ten program ilustruje działanie operatora logicznego AND")
print(f"True and True > ", a and a )
print(f"True and not True(False) > ", a and not b )
print(f"Not True(False) and not True(False) > ", not a and not b )

'''2_6 
Napisz program, który ilustruje pierwsze prawo de Morgana'''

print("Ten program ilustruje działanie pierwszego prawa de Morgana")

a = True
b = True

l_side = not (a and b)                                      # zaprzeczenie koniunkcji 2 zdań
r_side = (not a) or (not b)                                 # alternatywA zaprzeczeń tych zdań

if l_side == r_side:
    print("Super, prawo de Morgana działa!")
else:
    print("Coś tutej się nie zgadza!")

'''2_7
Napisz program z wykorzystaniem trójargumentowej instrukcji warunkowej.'''

a = 2
b = 3                   # wynik_gdy_prawda if warunek else wynik_gdy_fałsz

operacja = input("Jaką operację chcesz mi zlecić? > :")

if operacja == "dodawanie": 
    print(f"wynik dodawania: ", a + b)
else:
    print("Kończymy - tego nie potrafię")
    print("Chyba, że odejmowanie:")
    print(f"wynik to:", a-b)


'''2_8
Napisz program, który korzystając z instrukcji if-else, porównuje ze sobą dwa imiona: Mirek i Marek'''
name_1 = 'Mirek'
name_2 = 'Marek'

if name_1 == name_2 :
    print("Brawo, trafione imiona")
else:
    print("Wymienione imiona różnią się od siebie.")

'''2_9
Napisz program, który korzystając z instrukcji if-else, weryfikuje wprowadzane hasło.'''

#password = "imienienazwisko"

haslo = input("Drogi użytkowniku, poproszę Ciebie teraz o podanie hasła dostępu: > :")

if haslo == 'imienienazwisko':
    print(f"Dzięki, dane do logowania: {haslo}, są poprawne.")
else:
    print("Niestety, wprowadziłeś niepoprawne dane.")
