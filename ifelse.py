# IF ELSE STATEMENT
peso = float(input('Introduce tu peso en kg: '))
altura= float(input('Introduce tu altura en m: '))

if peso > 0 and altura > 0 :
    imc=peso/(altura*altura)
    print(f"Tu IMC es {imc}")
    
    if imc >= 30:
        print("Tienes condición de obesidad")
    elif imc >=25:
        print("Tienes condición de sobrepeso")
    elif imc >=20:
        print("Tienes condición de peso normal") 
    else:
        print("Tienes condición de peso bajo")

else:
    print ("Introduce valores válidos")


if altura > 1.8:
    print("Eres elegible para jugar baloncesto")
else:
    print("Es preferible que practiques otro deporte que no sea baloncesto") 

if peso > 100:
    print ("Es recomendable que cheques tu salud")
else:
    print ("Monitorea tu salud")    

# TERNARY OPERATOR
age=17
print ("Eres mayor de edad") if age >= 18 else print ("Eres menor de edad")

genero="M"
print ("Masculino") if genero =="M" else print ("Femenino")

civil="Soltero"
print ("Casado") if civil == "Casado" else print ("Soltero")

#FOR LOOP WITH RANGE
nac = int(input('Introduce año en que naciste: '))
años=0
for num in range(nac,2023,1):
    años=años+1

print (f"Tienes {años} años")

for dado1 in range (5):
    for dado2 in range (5):
        sumadados=dado1+1+dado2+1
        if sumadados==7:
            print (f"Esta combinación da valores en el lanzamiento de dos dados es 7: {dado1+1} y {dado2+1}")

for x in range (1,100,1):
    if x%7 == 0:
        print (f"Entre el 1 y 100, {x} es múltiplo de 7")


#WHILE
#Este ejemplo calcula los años que tienes
c=0
while nac<2023:
    c=c+1
    nac=nac+1
print (f"Tienes {años} años")

#Este ejemplo construye una lista de artículos hasta que introducimos "fin"
articulo=""
lista_compras=[]
while articulo.lower() != 'fin':
    articulo=input("Introduce un artículo en la lista de compras: ")
    lista_compras.append(articulo)
print("La lista de compras es:")
print(lista_compras)

#Este ejemplo suma los números que introduces hasta que introducimos 0
suma=0
n=1
while n != 0:
    n=float(input("Introduce un numero: "))
    suma=suma+n

print(f"La suma de los numeros es: {suma}")