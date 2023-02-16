#Funcicon en Python
def nuevoTema(tema):
    print("\n========", tema, "========\n")

#Este es un comentar
'''Este es un comentario 
   de varias lineas'''
nuevoTema("Operadores Aritmaticos")
print("Operador Division entera (10 // 3): ", 10 // 3)
print("Operador Potencia (5 ** 3): ", 5 ** 3)

nuevoTema("Operadores Logicos")
print("Operador and (True and False): ", True and False)

#Actividad: Imprimir la tabla de verdad de los Operadores Logicos.
print("---       and      ---")
print("        Operandos ")
print(" ----------------------- Resultado")
print("  Izquierdo   Derechos ")
print("-----------------------------------")
print("Operador and (True and True): ", True and True)
print("Operador and (True and False): ", True and False)
print("Operador and (False and True): ", False and True)
print("Operador and (False and False): ", False and False)
print("  ")
print("---       not      ---")
print("----------------------")
print("   Operando   Resultado ")
print("--------------------------------")
print("Operador and (True): ", not True)
print("Operador and (False): ", not False)
print("  ")
print("---       or      ---")
print("        Operandos ")
print("----------------------- Resultado")
print("  Izquierdo   Derechos ")
print("---------------------------------")
print("Operador and (True or True): ", True or True)
print("Operador and (True or False): ", True or False)
print("Operador and (False or True): ", False or True)
print("Operador and (False or False): ", False or False)
print(" ")
print(" ")
print("---Operadoes de Comparacion---")
print("2 == 3",2 == 3)
print("-------------------------------")
#Actividad: Agregar los demas Operadores de Comparacion
print("Es igual que... 2 == 3 ->",2 == 3)
print("Es distinto que... 2 != 3 ->",2 != 3)
print("Es menor que... 2 < 3 ->",2 < 3)
print("Es menor o Igual que... 2 <= 3 ->",2 <= 3)
print("Es mayor que... 2 > 3 ->",2 > 3)
print("Es mayor o Igual que... 2 >= 3 ->",2 >= 3)
print("  ")
print("  ")
nuevoTema("Variables")
variable1 = 10
_variable2 = 6.2456
Variable3 = "Juancho"
dosPalabras = "Hola"
dos_Palabras = "Hello"

print(variable1, _variable2, Variable3, dosPalabras, dos_Palabras)

a, b, c= 10, 5.16, "Palabra"
print(a, b, c)

nuevoTema("Numeros Enteros")
w=105
x=651651618131334
y=-356
z=0b0011010
h=0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Numeros Flotantes")
x=1297.685
print(x,type(x))
y = 0.5985
print(y, type(y))

nuevoTema("Numeros Complejos")
x= -45j
y= 12+45j
z= 2j
print(x, type(x))
print(y, type(y))
print(z, type(z))

nuevoTema("Booleanos")
lis=[8]
print(lis, "es",bool(lis))
t=()
print(t, "es",bool(t))
new ="Hello"
print(new, "es", bool (new))
num = 99
print(num, "es", bool(num))
comp = 1+0j
print(comp, "es", bool (comp))
val=None #equivale a NULL
print(val,"es", bool(val))

nuevoTema("Listas") #No son arreglos
a =[10, 20.5, "Python list"]
print(a)
print(a[1])
a[0]="Hola"
print(a)

nuevoTema("Tuplas")
t= (25, "tupla", 1+10j)
print(t)
print(t[2])
print("t[1:4]: ", t[1:4])
#t[1]= 34 Operacion no valida en la Tupla

nuevoTema("Conjuntos")
t = {50, 20, 30, 40, 10, 50}
print("Conjunto t=", t ,type(t))

nuevoTema("Diccionarios")
d = {1:"Valor1", "Valor2":2j}
print(d, type(d))
print("d[Valor2]:", d["Valor2"])

nuevoTema("Cadenas")
cadena1 = "Cadena con comillas dobles"
cadena2 = 'Cadena con comillas simples'

print(cadena1, type(cadena1))
print(cadena2, type(cadena2))

cadenaMultilinea = '''Esta es una cadena
de varias lineas    con tabulares y
saltos de linea'''

print(cadenaMultilinea)
print("Segentacion de cadenas")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1]) #desde el caracter 0 a 18 y avanzade 1 en 1
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1="Hola"
cadena4= (cadena1 + " ")*5 #se multiplica la cadena
print(cadena4)
cadena5 = cadena4.upper()
print(cadena5)
