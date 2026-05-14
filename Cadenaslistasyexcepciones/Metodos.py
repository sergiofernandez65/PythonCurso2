# Demostración del método capitalize():
print('aBcD'.capitalize())

#Resultado: Abcd


print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

#Resultado:
#Alpha
#Alpha
# Alpha
#123
#αβγδ



# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')

#Resultado: [  alpha   ]


print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

#Resultado: 
#[Beta]
#[Beta]
#[ Beta ]


# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

#Resultado: si


t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

#Resultado:
#True
#False
#False
#True


# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))

#Resultado:
#1
#-1


t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

#Resultado:
#2
#2
#0
#-1


the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

#Resultado:
#15
#80
#198
#221
#238


print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

#Resultado:
#1
#-1


# Demostración del método isalnum():
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

#Resultado:
#True
#True
#True
#False
#False
#False


t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

#Resultado:
#False
#False
#True


# Ejemplo: Demostración del método isalpha():
print("Moooo".isalpha())
print('Mu40'.isalpha())

#Resultado:
#True
#False


# Ejemplo: Demostración del método isdigit():
print('2018'.isdigit())
print("Year2019".isdigit())

#Resultado:
#True
#False


# Ejemplo: Demostración del método islower():
print("Moooo".islower())
print('moooo'.islower())

#Resultado:
#False
#True


# Ejemplo: Demostración del método isspace():
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

#Resultado:
#True
#True
#False


# Ejemplo: Demostración del método isupper():
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

#Resultado:
#False
#False
#True


# Demostración del método join():
print(",".join(["omicron", "pi", "rho"]))

#Resultado: omicron,pi,rho


# Demostración del método lower():
print("SiGmA=60".lower())

#Resultado: sigma=60


# Demostración del método lstrip():
print("[" + " tau ".lstrip() + "]")

#Resultado: [tau ]


print("www.cisco.com".lstrip("w."))

#Resultado: cisco.com

print("pythoninstitute.org".lstrip(".org"))

#Resultado: pythoninstitute.org


# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

#Resultado:
#www.pythoninstitute.org
#Thare are it!
#Apple


print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

#Resultado:
#Thare is it!
#Thare are it!

# Demostración del método rfind():
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

#Resultado:
#8
#-1
#4


# Demostración del método rstrip():
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

#Resultado:
#[ upsilon]
#cis


# Demostración del método split():
print("phi       chi\npsi".split())
#Resultado: ['phi', 'chi', 'psi']


# Demostración del método startswith():
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

#Resultado:
#False
#True


# Demostración del método swapcase():
print("Yo solo sé que no sé nada".swapcase())

print()

#Resultado: yO SOLO SÉ QUE NO SÉ NADA


# Demostración del método title():
print("Yo solo sé que no sé nada. Parte 1.".title())

print()

#Resultado: Yo Solo Sé Que No Sé Nada. Parte 1.


# Demostración del método upper():
print("Yo solo sé que no sé nada. Parte 2.".upper())

#Resultado: YO SOLO SÉ QUE NO SÉ NADA. PARTE 2.