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
#print("La suma de los primeros numeros enteros desde 1 hasta " +str(n) + " " + "es " +str(suma))

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
#peso_payaso = 112
#peso_muñeca = 75
#payasos = int(input("Numero de payasos: "))
#muñecas = int(input("Numero de muñecas: "))
#peso_total = peso_payaso * payasos + peso_muñeca * muñecas
#print("El peso total del paquete es " + str(peso_total))

#CLASE #3-----------------------------------------------------------

#Ejercicio 1:
#n=0
#n=int(input("Ingrese un numero entero: "))
#suma=(n*(n+1)/2)
#if suma > 20:
#  print("La suma de todos los numeros enteros desde 1 hasta " + str(n) + " " + "es" + " " + str(suma))
#  print("¡Que gran numero!")
#else:
#  print("La suma de todos los numeros enteros desde 1 hasta " + str(n) + "es" + " " + str(suma))

#Ejercicio 2:
#n=0
#m=0
#c=0
#r=0
#n=float(input("Ingrese el dividendo: "))
#m=float(input("Ingrese el divisor: "))
#division=(n//m)
#c=(n//m)
#print(str(n) + " dividido " + str(m) + " da " + str(division) + " y sobra " + str(float(n) % float(m)))
#if c > 1:
  #print("El resultado de la division es mayor a 1")
#elif c == 1:
  #print("El resultado de la division es igual a 1")
#else:
  #print("El resultado de la division es menor a 1")

#Ejercicio 3:
#c=0
#i=0
#años=0
#r=0.0
#c=int(input("¿Cuanto dinero quiere invertir?: "))
#i=int(input("¿Cuanto es el porcentaje de interes?: "))
#años=int(input("¿Cuantos años sera la inversion?: "))
#r=c*((i/100)+1)**años
#print("La rentabilidad da un total de: " + str(r))
#if r < 100000:
  #print("Baja rentabilidad")
#elif (r > 100000 and r < 1000000):
  #print("Rentabilidad moderada")
#else:
  #print("Es una buena inversion")

#Ejercicio 4:
#p=0
#m=0
#payaso_gr=112
#muñeca_gr=75
#p=float(input("¿Cuantos payasos son?: "))
#m=float(input("¿Cuantas muñecas son?: "))
#payaso_kg=(payaso_gr*(1/1000)*(p))
#muñeca_kg=(muñeca_gr*(1/1000)*(m))
#peso_total=(payaso_kg+muñeca_kg)
#print("El peso total de la caja es: " + str(peso_total) + "kg")
#if peso_total > 3000:
  #envio=input("¿Desea enviarlo?: ")
  #if envio=="Si":
    #print("Contenedor enviado")
  #if envio=="No":
    #print("Contenedor no enviado")

#Ejercicio 5:
#d=0
#d=float(input("¿Cuanto dinero deposito en la cuenta?: "))
#if d == 0 and d < 1000000:
  #a=(d+)

#CLASE #4 -------------------------------------------------------------------

#Ejercicio 1:
#n1=int(input("Ingrese el numero uno: "))
#n2=int(input("Ingrese el numero dos: "))
#def suma(a, b): 
  #y=a+b
  #return y
#z=suma(n1, n2)
#print(z)

#Ejercicio 2:

#n1=int(input("Ingrese un valor: "))
#n2=int(input("Ingrese otro valor: "))
#def resta(a, b):
  #res=a-b
  #return resta
#r=resta(n1, n2)
#print(r)

#Ejercicio 3:

#n1=int(input("Escriba un numero: "))
#n2=int(input("Escriba otro numero: "))
#def multiplicacion(a, b):
  #m=a*b
  #return m
#mult=multiplicacion(n1, n2)
#print(mult)

#Ejercicio 4:

#n1=int(input("Ingrese el dividendo: "))
#n2=int(input("Ingrese el divisor: "))
#def division(a, b):
  #div=a/b
  #return div
#d=division(n1, n2)
#print(d)

#Ejercicio 5:

#v1=0
#v2=0
#usuario=input("¿Que desea hacer?: ")
#v1=int(input("Ingrese un valor: "))
#v2=int(input("Ingrese otro valor: "))
#suma=v1+v2
#resta=v1-v2
#multiplicacion=v1*v2
#division=v1/v2
#def calculadora(usuario):
  #respuesta=usuario
  #return respuesta
#r=calculadora(usuario)
#if r=="Suma":
  #suma=v1+v2
#if r=="Resta":
  #resta=v1-v2
#if r=="Multiplicacion":
  #multiplicacion=v1*v2
#if r=="division":
  #division=v1/v2
#else:
  #print("Respuesta no valida")

#Ejercicio 6:

#def intereses(inv):
#  d=inv
#  if (d>0 and d<1000000):
#    return 2
#  elif(d>=1000000 and d<2000000):
#    return 5
#  else:
#    return 7

#def calbalance(int, inv):
#  n=int
#  d=inv
#  return round((d*(1+(n/100))),2)

#def ctaAhorro():
#  interes=intereses(inversion)
#  b1=calbalance(interes,inversion)
#  b2=calbalance(interes,b1)
#  b3=calbalance(interes,b2)
#  print("Balance año 1: " + str(b1) + " Balance año 2: " + str(b2) + " Balance año 3: " + str(b3))

#ctaAhorro()

#CLASE #5----------------------------------------------------------------

#def areaTriangulo(b, a):
 # return(b*a)/2

#def areaCuadrado(bc, ac):
  #return bc*ac

#def areaCirculo(r):
  #return(3.14169*(r**2))

#def areaFig():
  #area=0.0
  #figura=""
  #figura=input("Escriba la figura a la que se le desea calcular el area: ")

#if (figura.lower()=="triangulo"):
  #base=0.0
  #altura=0.0
  #base=float(input("Ingrese la base: "))
  #altura=float(input("Ingrese la altura: "))
  #area=areaTriangulo(base, altura)
  #print("El area del triangulo es: ", area)

#areaFig()

#CLASE 6 ------------------------------------------------------------

#Ejercicio 1:

#A = 0
#while A < 10:
#  print(A)
#  A=A+1

#Ejercicio 2:

#def suma():
#  a=int(input("Ingrese un valor: "))
#  b=int

#def Calculadora():
#  Menu()
#  opcion=0

#while opcion != 5:

#  opcion = int(input("Seleccione opcion\n"))

#  if (opcion==1):
#    print("La suma es:", suma())
#  elif(opcion==2):
#    print("La resta es:", resta())
#  elif(opcion==3):
#    print("La multiplicacion es:", multiplicacion())
  #elif(opcion==4):
  #  print("La division es:", division())
  #elif(opcion==5):
  #  print("Gracias por usar la calculadora! bye!.")
    #break

  #else:
  #  print("Opcion invalida, intente de nuevo")

