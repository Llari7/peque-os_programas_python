import os
os.chdir("C:/Users/ALONSO/PycharmProjects/pequenios_programas_python/poligonos")

def lado_contiguo(puntoA, puntoB):
    if (puntoA[0] == puntoB[0] and puntoA[1] != puntoB[1]) or (puntoA[0] != puntoB[0] and puntoA[1] == puntoB[1]):
        return True
    else:
        return False

def longitud_lado(puntoA, puntoB):
    if puntoA[0] == puntoB[0]:
        return max(puntoA[1], puntoB[1]) - min(puntoA[1], puntoB[1])
    else:
        return max(puntoA[0], puntoB[0]) - min(puntoA[0], puntoB[0])

cuadrado = []
punto = []
perimetro = 0

fichero = open("coordenadas.txt")
for linea in fichero:
    if linea[0] == "(":
        cuadrado.append([int(linea[1]), int(linea[4])])
fichero.close()

if len(cuadrado) != 4:
    print("El número de puntos introducidos en el fichero es incorrecto para un cuadrado.")
    exit()

punto1 = cuadrado[0]
punto2 = cuadrado[1]
punto3 = cuadrado[2]
punto4 = cuadrado[3]

print("Se procede al cálculo del perímetro, área, longitud del lado del cuadrado cuyos 4 vértices están situados en las coordenadas: ")
for punto in cuadrado:
    print("({}, {})m".format(punto[0], punto[1]))

if lado_contiguo(punto1, punto2):
    perimetro = longitud_lado(punto1, punto2)*4
    area = longitud_lado(punto1, punto2)**2
    print("La longitud de sus lados es: {}m.".format(longitud_lado(punto1, punto2)))
elif lado_contiguo(punto1, punto3):
    perimetro = longitud_lado(punto1, punto3)*4
    area = longitud_lado(punto1, punto3)**2
    print("La longitud de sus lados es: {}m.".format(longitud_lado(punto1, punto3)))
print("El perímetro del cuadrado es: {}m.".format(perimetro))
print("El área del cuadrado es: {}m^2.".format(area))



