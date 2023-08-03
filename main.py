#HolaMundo
#Ejercicio 1:
#print ("Hola Mundo")

#Ejercicio 2:
#a = "¡Hola Mundo!"
#print(a)

#Ejercicio 3:
#nombre = input("Escribe tu nombre: ")
#print("Hola "+nombre)

#Ejercicio 4:
#print(((3+2)/(2*5))**2)

#Ejercicio 5:
#horas = float(input("¿Cuantas horas trabajas al dia? "))
#costo = float(input("¿Cuanto te pagan por hora? "))
#pago = horas*costo
#print("Tu pago total fue: "+ str(pago))

#Ejercicio 6:
#n = int(input("Entero positivo: "))
#suma = n*(n+1)/2
#print("La suma de los primeros numeros enteros desde 1 hasta " +str(n) + "es" +str(suma))

#Ejercicio 7:
#peso = input("¿Cual es tu peso? ")
#estatura = input("¿Cual es tu estatura? ")
#imc = round(float(peso)/float(estatura)**2,2)
#print("Tu indice de masa corporal es " +str(imc))

#Ejercicio 8:
#n = input("¿Cual es el numerador? ")
#m = input("¿Cual es el denominador? " )
#print(n + " " + "dividido" + " " + m + " " + "da" + " " + str(int(n) // int(m)) + " " + "y sobra" + " " + str(int(n) % int(m)))

#Ejercicio 9:
#cantidad = float(input("¿Cuanto quisiera invertir? "))
#interes = float(input("¿Cual es el interes anual? "))
#años = float(input("Numero de años "))
#print("Capital obtenida: " + str(round(cantidad * (interes/100+1) ** años, 2)))

#Ejercicio 10:
peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Numero de payasos: "))
muñecas = int(input("Numero de muñecas: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es" + str(peso_total))