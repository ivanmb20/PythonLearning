import numpy as np
#Este es un ejemplo de una función simple sin usar *args
def perimetro(lado1,lado2,lado3,lado4):
  perimetro=lado1+lado2+lado3+lado4
  
  return perimetro

perimetro=perimetro(1,2,3,4)

print(perimetro)

#O podemos usar *args

def calc_perimetro(*args):
    print(args)
    perimetro=0
    for lado in args:
      perimetro += lado
    return perimetro
  
perimetro=calc_perimetro(1,2,3,4)
#Aqui nos va a devolver la tupla que usamos en la variable args
print(perimetro)

#Ahora calculamos el perimetro de un poligono de 3 lados, ie un triangulo

triangulo=calc_perimetro(1,2,3)
print(triangulo)
#Y ahora si podemos calcular el perimetro de cualquier poligono

def funcion_kwargs(**kwargs):
   print(kwargs)
   for llave, valor in kwargs.items():
        print(f"llave: {llave},valor:{valor}")
   print(kwargs["nombre"],kwargs["apellido"])

funcion_kwargs(nombre="Paco",apellido="Taibo")        
   

#Veamos el orden de una función que tiene kwargs y args

def parametros_ordenados(nombres,apellido,*args,**kwargs):
  pass

#Esta función marcará error debido a que primero van los args y luego los kwargs
def parametros_desordenados(nombres,apellido,**kwargs,*args):
  pass