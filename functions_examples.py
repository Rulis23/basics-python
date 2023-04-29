#PYTHON FUNCTIONS
def suma (x,y):
    s=x+y
    return s

def mult (x,y):
    m=x*y
    return m

def rest (x,y):
    r=x-y
    return r

x=float(input("Introduce un número: "))
y=float(input("Introduce un número: "))

z=int(input("Deseas Sumarlos (1), Multiplicarlos (2) o Restarlos(3)? Introduce el número asociado a cada operación: "))

if z==1:
    a=suma(x,y)
    print(f"La suma de {x} + {y} es {a}")
elif z==2:
    a=mult(x,y)
    print(f"La multiplicación de {x} * {y} es {a}")
elif z==3:
    a=rest(x,y)
    print(f"La resta de {x} - {y} es {a}")

#DEFAULT PARAMETERS
def mascota (animal, nombre="Firulais"):
    print(f"{nombre} es un {animal}")

mascota("perro")

def edad (nacimiento, actual=2023):
    e=actual-nacimiento
    print(f"Tu edad es de {e} años")

edad(1996)

def hello_world(h="Hello", w="World"):
    print(f"{h} {w}")

hello_world()

#KEYWORDS ARGUMENTS
mascota("gato", nombre="Garfield")

edad (1996, actual=2020)

hello_world(h="Hola", w="Mundo")


