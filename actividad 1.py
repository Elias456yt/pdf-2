#act1
distancia= input("ingresar la distancia:")
distancia= int(distancia)
velocidad= input("ingrese la velocidad:")
velocidad= int(velocidad)

resultado= distancia + velocidad
resultado= int(resultado)

print("resultado final:", resultado)

#act1
altura= input("ingresar altura")
altura= int(altura)
base= input("ingresar base")
base= int(base)

resultado= base * altura 
resultado= int(resultado)

print("resultado final", resultado)

#act1
def calcular_factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * calcular_factorial (n - 1)

def calcular_combinaciones(n, k):
   if k > n:
    return 0
   else:
    return calcular_factorial(n) // (calcular_factorial(k) * calcular_factorial(n - k))

numero_de_personas_en_un_grupo= input("ingresar numero de personas")
numero_de_personas_en_un_grupo= int(numero_de_personas_en_un_grupo)

grupos_de_personas= input("ingresar grupos de persona")
grupos_de_personas= int(grupos_de_personas)

numeros_de_combi= calcular_combinaciones(numero_de_personas_en_un_grupo, grupos_de_personas)
print("cantidad de combinaciones", numeros_de_combi)






