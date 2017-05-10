""" 
W oparciu o beztypowy rachunek lambda zaimplementuj:
* liczebniki Churcha oraz operacje na nich (dodawanie, mnozenie) 
"""

# Liczebniki Churcha:

# 0 = λf.λx.x = x
# 1 = λf.λx.f(x) = f(x)
# 2 = λf.λx.f(f(x)) = f(f(x))
# 3 = λf.λx.f(f(f(x))) = f(f(f(x)))
# itd. 

zero = 	lambda f: lambda x: x
one = 	lambda f: lambda x: f(x)
two = 	lambda f: lambda x: f(f(x))
three =	lambda f: lambda x: f(f(f(x)))
four =	lambda f: lambda x: f(f(f(f(x))))
five = 	lambda f: lambda x: f(f(f(f(f(x)))))
six = 	lambda f: lambda x: f(f(f(f(f(f(x))))))
seven = lambda f: lambda x: f(f(f(f(f(f(f(x)))))))
eight = lambda f: lambda x: f(f(f(f(f(f(f(f(x))))))))
nine = 	lambda f: lambda x: f(f(f(f(f(f(f(f(f(x)))))))))
ten = 	lambda f: lambda x: f(f(f(f(f(f(f(f(f(f(x))))))))))

# Mnozenie:
def mul (m, n):
	return lambda f: lambda x: m(n(f))(x)
	
# Inkrementacja:
def incr (n):
	return lambda f: lambda x: f(n(f)(x))
	
# Dekrementacja:
def decr (n):
	return lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)
	
# Potegowanie:
def power (m, n):
	return n(m)

# Dodawanie:
def add (m, n):
	return lambda f: lambda x: m(f)(n(f)(x))	
	#return n(incr)(m)

# Odejmowanie:
def subtr (m, n):
	return n(decr)(m)

"""
* wartosci oraz operatory logiczne
"""

true = lambda x: lambda y: x
false = lambda x: lambda y: y

AND = lambda x: lambda y: x(y)(false)
OR = lambda x: lambda y: x(true)(y)
NOT = lambda x: x(false)(true)
XOR = lambda x: lambda y: x(NOT(y))(y)

# Funkcje pomocnicze - konwersja:
def church_to_int(n):
	return n(lambda x:x+1)(0)
	
def church_to_boolean(n):
	return n(True)(False);
	
def int_to_church(n):
	if n == 0:
		return zero
	else:
		return incr(int_to_church(n-1))

# Test dzialania funkcji:	
# print
# print "TEST DZIALANIA PROGRAMU:"
# test_num = int_to_church(17)
# print "Moja liczba: ", church_to_int(test_num) 
# print "17++ = ", church_to_int(incr(test_num)) 
# print "17-- = ", church_to_int(decr(test_num)) 
# print "2 * 17 = ", church_to_int(mul(two, test_num)) 
# print "8 + 17 = ", church_to_int(add(eight, test_num)) 
# print "17 - 12 = ", church_to_int(subtr(test_num, add(ten, two)))
# print "17^2 = ", church_to_int(power(test_num, two)) 
# print "true: ", church_to_boolean(true) # True
# print "false: ", church_to_boolean(false) # False 
# print "~ true = ", church_to_boolean(NOT(true)) # False
# print "~ false = ", church_to_boolean(NOT(false)) # True
# print "and (false, true) = ", church_to_boolean(AND(false)(true)) # False 
# print "and (false, false) = ", church_to_boolean(AND(false)(false)) # False 
# print "and (true, true) = ", church_to_boolean(AND(true)(true)) # True 
# print "and (true, false) = ", church_to_boolean(AND(true)(false)) # False 
# print "or (true, false) = ", church_to_boolean(OR(true)(false)) # True 
# print "or (false, false) = ", church_to_boolean(OR(false)(false)) # False 
# print "xor (true, false) = ", church_to_boolean(XOR(true)(false)) # True 
# print "xor (true, true) = ", church_to_boolean(XOR(true)(true)) # False 


#################################################################################
"""
Przykladowy program pokazujacy, ze to wszystko ma sens: liczenie NWD na 2 sposoby 
i testowanie skomplikowanych umiejetnosci matematycznych uzytkownika
"""
 
# Z-kombinator ograniczajacy "ekspansje" rekursji (dzieki niemu nie dziala w nieskonczonosc) - z artykulu:
Z  = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))

# Czy == 0 ?
is_zero = lambda x: x(lambda y: false)(true)

# <= 
less_or_equal = lambda m: lambda n: is_zero(subtr(m,n))

# ==
equal = lambda m: lambda n: AND(less_or_equal(m)(n))(less_or_equal(n)(m))

# >
greater_than = lambda m: lambda n: NOT(less_or_equal(m)(n))

IF  = lambda f: f 

# Modulo z wykorzystaniem Z-kombinatora - z artykulu:
MOD = Z(lambda f: lambda m: lambda n: IF(less_or_equal(n)(m))(lambda y: f(subtr(m,n))(n)(y))(m))

# Algorytm znajdowania NWD wg Euklidesa
NWD_Euklides = lambda n: lambda m: \
	IF(is_zero(n))(m) (
		IF(is_zero(m))(n) (
			IF(greater_than(m)(n)) \
				(lambda x: NWD_Euklides(n)(MOD(m)(n))(x))
				(lambda x: NWD_Euklides(m)(MOD(n)(m))(x))
		)
	)

# Algorytm znajdowania NWD w wersji "klasycznej" z odejmowaniem 
NWD_standard = lambda n: lambda m: \
	IF(is_zero(n))(m) (
		IF (is_zero(m))(n) (
			IF(equal(n)(m))(n)(
				IF(greater_than (n)(m)) \
					(lambda x: NWD_standard(subtr(n,m))(m)(x))
					(lambda x: NWD_standard(n)(subtr(m,n))(x))
			)
		)
	)
	
# Test dzialania programu:
print 
l1 = int(raw_input("Podaj pierwsza liczbe: "))
l2 = int(raw_input("Podaj druga liczbe: "))
wyn = int(raw_input("Podaj ich NWD: "))
liczba1 = int_to_church(l1)
liczba2 = int_to_church(l2)
wynik = int_to_church(wyn)
# print church_to_int(NWD_Euklides(liczba1)(liczba2))
# print church_to_int(NWD_standard(liczba1)(liczba2))
if church_to_boolean(IF(equal(NWD_Euklides(liczba1)(liczba2))(NWD_standard(liczba1)(liczba2)))): # Na wszelki wypadek - gdyby blad wynikal ze zlej implementacji 
	if church_to_boolean(IF(equal(wynik)(NWD_Euklides(liczba1)(liczba2)))):
		print "Twoj wynik jest poprawny!" 
	else:
		print "Twoja odpowiedz jest bledna :-( Prawidlowy wynik to: %i" % church_to_int(NWD_Euklides(liczba1)(liczba2))
else:
	print  "Error... Cos poszlo nie tak."
