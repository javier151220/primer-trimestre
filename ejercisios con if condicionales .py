#javier usando if


# 1 verifica si un numero es positivi negativo o cero

# numro=int(input("ingresa un numero : "))
# if numro >0:
#     print(f"es positivo, {numro}")
# elif numro<0:
#     print(f"es negativo, {numro}")
# else:
#     print(f"es zero, {numro}")


# 2  CALCULA EL MAYOR DE DOS NUMEROS INGRESADOS

# num1=int(input("ingresa un numero : "))
# num2=int(input("ingresa un numero : "))
# if num1>num2 :
#     print(f"el primer numero es es mayor")
# else:
#     print(f"el segundo numero  es mayor")

#numero3

#----3 determine si un numero es par o impar-------

# numero=int(input("ingresa un numero:"))
# if numero %2 == 0:
#     print("es par")
# else:
#     print("no es par")


# -4 DADO UN NUMERO VERIFIQUE SI ESTA DENTRO DE 10 Y 20

# NUMERO=int(input("ingrese un  numero"))

# if NUMERO>=10 and NUMERO<=20:
#     print("esta dentro del rango")
# else:
#     print("no esta dentro del rango")


# 5  DADO TRES NUMEROS  ENCUENTRA CUAL ES MAYOR  USANDO CONDICIONALES

# numero_1=int(input("ingresa un numero :"))
# numero_2=int(input("ingresa un numero :"))
# numero_3=int(input("ingresa un numero :"))

# if numero_1>numero_2 and numero_1>numero_3:
#     print(f"este numero es mayor {numero_1}")
# elif numero_2>numero_1 and numero_2>numero_3:
#     print(f"este numero es mayor {numero_2}")
# elif numero_3>numero_1 and numero_3>numero_2:
#     print(f"este numero rs mayor {numero_3}")
# else:
#     print(f"todos son guales {numero_1}, {numero_2}, {numero_3}")


# 6 calcule el precio final con un 10%  si el total es mayor a 100


# fruta=input("Ingresa una fruta :")
# pre=float(input("Ingresa el precio de la fruta"))
# if pre>100:
#     operacion=pre*0.10
#     print(f"el descuento es {operacion}" )
# else:
#     print("no hay descuento")

# 7 verifica si una persona puede votar (mayor o ihual a 18 años)

# nombre=input("ingresa tu nombre : ")
# edad=int(input("ingresa tu edad :"))
# if edad>=18:
#     print(f"puedes votar porque tienes {edad}")
# else:
#     print(f"eres menor de edad porque tienes {edad}")

# 8 dado el precio y tipo de cliente (VIP o normal),aplica un descuento del 20% solo a vip

# producto=input("Ingresa un profucto :")
# precio=float(input("Ingresa el precio :"))
# cliente=input("Que tipo de cliente eres VIP o normal :")
# if cliente=="VIP":
#     des=precio*20
#     print(f"con el descuento te queeda en  {des}")
# else:
#     print("no tienes descuento")

#9 determina si un numero es multiplo de 5 y de 3 al mismo tiempo

# numero=int(input("ingresa un numero:"))
# if numero % 3== 0 and numero % 5 == 0:
#     print("es multiplo de 3 y 5")
# else:
#     print("no es multiplo")

#10 dado un numero verifica si es divisible entre dos numero dados

# numero1=int(input("ingresa un numero : "))
# numero2=int(input("ingresa un numero : "))
# numero3=int(input("ingresa un numero : "))
# if numero1 % numero2  % numero3 == 0:
#     print(f"Si es divisible")
# else:
#     print("no es divisible")
    


#-----------TALLER DE CONDICIONALES---------------------------------------------------------------------

#1
# edad=int(input("ingrese su edad: "))
# if edad>=18 and edad<65:
#     print(f"Eres un joven porque tiens{edad} ")
# elif edad>=65:
#     print(f"Eres un adulto mayor porque tienes {edad}")
# else:
#     print(f"eres menor de edad porque tienes {edad}")

#2
# estatura=float(input("Cuanto mides :"))
# if estatura<1.5:
#     print(f"eres bajito porque mides {estatura}")
# elif estatura>=1.5 and estatura<=1.8:
#     print(f"eres una persona con estatura promedio porque  mides {estatura}")
# else:
#     print(f"eres una persona alta porque mides {estatura}")

#3
# num = int(input("Ingresa un número: "))
# if num % 2 == 0 and num % 3 == 0:
#     print(f"Es múltiplo de 2 y 3 porque el número es {num}")
# elif num % 2 == 0:
#     print(f"Es múltiplo de 2: {num}")
# elif num % 3 == 0:
#     print(f"Es múltiplo de 3: {num}")
# else:
#     print("no tiene decimal")

#4
# numero = input("Ingresa un número decimal: ")

# if '.' in numero:
#     Entera, decimal = numero.split('.')
#     cantidad_decimales = len(decimal)
#     if decimal == 1:
#         print("El número tiene 1 decimal.")
#     elif decimal == 2:
#         print("El número tiene 2 decimales.")
#     else:
#         print("El número tiene más de 2 decimales.")
# else:
#     print("El número no tiene parte decimal.")

#5
# tupla=("Colombia", "Perú", "Argentina", "México")
# print(tupla)
# pais=input("Ingresa tu pais natal : ")
# if pais in tupla:
#     print("esta dentro de la tupla ")
# else:
#     print("no esta dentro")

#6
# sangre_compatible = {
#     "O": ["O"],
#     "A": ["A", "O"],
#     "B": ["B", "O"],
#     "AB": ["A", "B", "AB", "O"]
# }

# sangre= input("Introduce tu tipo de sangre en mayuscula (A, B, AB, O): ").upper()
# if sangre in sangre_compatible:
#     print("pudes compartir sangre")
# else:
#     print("Tipo de sangre no válido., introdusca A, B, AB o O.")


#7

# tem=float(input("ingresa una temperatura en °C :"))
# if tem <10:
#     print(f"hace frio estas a {tem} °C.")
# elif tem>=10 and tem<=25:
#     print(f" estas en clima templado a {tem} °C.")
# else:
#     print(f"tomate una limonada que hace calo a {tem} °C")


#8
# print("Menú de operaciones:")
# print("1. Sumar")
# print("2. Restar")
# print("3. Multiplicar")
# print("4. dividir")
# opcion = input("Selecciona una opción (1, 2,3, 4): ")
# if opcion in ["1", "2", "3", "4"]:
#     num1 = float(input("Ingresa el primer número: "))
#     num2 = float(input("Ingresa el segundo número: "))

#     if opcion == "1":
#         resultado = num1 + num2
#         print("Resultado de la suma:", resultado)
#     elif opcion == "2":
#         resultado = num1 - num2
#         print("Resultado de la resta:", resultado)
#     elif opcion == "3":
#         resultado = num1 * num2
#         print("Resultado de la multiplicación:", resultado)
#     elif opcion == "4":
#         resultado = num1 / num2
#         print("Resultado de la divicion:", resultado)
        
# else:
#     print("Opción no válida. Por favor selecciona 1, 2 ,3,4 ")

#9
# meses = {
#     1: "enero",
#     2: "febrero",
#     3: "marzo",
#     4: "abril",
#     5: "mayo",
#     6: "junio",
#     7: "julio",
#     8: "agosto",
#     9: "septiembre",
#     10: "octubre",
#     11: "noviembre",
#     12: "diciembre"
# }

# mes = int(input("Ingresa un número del 1 al 12: "))

# if 1 <= mes <= 12:
#     print(f"El numero es {mes} es {meses[mes]}.")
# else:
#     print("por favoer un numero entre 1 y 12.")

#10
# numero = input("Ingresa un número de 4 digitos : ")
# if numero.isdigit():
#     if numero.startswith('1'):
#         print("empiza con  1 .")
#     elif numero.startswith('2'):
#         print("empieza con el numero 2.")
#     else:
#         print("es otro numero.")
# else:
#     print("No existe es letra.")



#11

# palabra = input("Escribe una palabra primera en mayuscula: ")
# if  palabra in  "aeiou":
#     print("La primera letra es una vocal.")
# elif palabra in "B, C, D, F, G, H, J, K, L, M, N, Ñ, P, Q, R, S, T, V, W, X, Y y Z ":
#     print("La primera letra es una consonante.")
# else:
#     print("no es nada.")


#12 
# precios = {"manzana": 10, 
# "pera": 12, 
# "piña": 15
# }
# fruta = input("Ingresa una fruta: ").lower()
# if fruta in precios:
#     print(f"El precio de la {fruta} es {precios[fruta]} pesos.")
# else:
#     print("pon la fruta manzana pera o piña ") 


#13
# calificacio=int(input("Ingresa la calificacion de 0  a 5 :"))
# if calificacio<3:
#     print(f"mal estudiante reprobaste tu nota es {calificacio}")
# elif calificacio>=3 and calificacio<=4:
#     print(f"bue estudiante aprobaste  tu nota es {calificacio}")
# else:
#     print(f"excelente tu nota es {calificacio}")

#14
# num=int(input("ingresa un numero : "))
# if num % 4 == 0 and num % 6 == 0:
#     print("Es divisible por el 4 y el 6")
# elif num % 4 == 0:
#     print("Es divisible por el 4 ")
# elif  num % 6 == 0:
#     print("Es divisible por el 6 ")
# else:
#     print("no es divisible")

#15


#16
# edad=int(input("po tu edad : "))
# if edad>0 and edad<=12:
#     print(f"eres un niño porque tienes {edad}")
# elif edad>=13 and edad<=17:
#     print(f"eres adolecente :")
# elif edad>=18 and edad<=64:
#     print(f"ers un adulto tienes {edad}")
# else:
#     print(f"eres adulto mayor tienes {edad}")

 
# 17
# capitales = ("caracas", "", "Berlin", "españa", "rio de janeiro")
# ciudad = input("Ingresa el nombre de una ciudad: ")
# if ciudad in capitales:
#     print(f"{ciudad} es la capital y esta en la tupla")
# else:
#     print(f"{ciudad} es una ciudad secundaria.")


#18
# precio = float(input("Ingresa el valor de la compra: "))
# if precio > 200000:
#     descuento = precio* 0.15
# elif 100000 <= precio <= 200000:
#     descuento = precio * 0.10
# else:
#     descuento = 0
# total = precio - descuento
# print(f"el decuento es de {descuento}")
# print(f"total del pago{total}")


#19



#20

# print("puntuaje de prueba :")
# pun=int(input("ingresa un puntuaje de 1 a 100 :"))
# if pun<50:
#     print(f"insuficiente pubtaje de {pun}")
# elif pun>=50 and pun<=79:
#     print(f"aceptable porque es de {pun}")
# else:
#     print(f"sobresaliente muy bien puntuaje de {pun}")
#javier