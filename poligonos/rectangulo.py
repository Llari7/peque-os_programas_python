from time import sleep
import os
os.chdir("C:/Users/ALONSO/PycharmProjects/pequenios_programas_python/poligonos")

FILE_NAME = "coordinates.save"


def adjacent_side(a_point, b_point):
    if not (not (a_point[0] == b_point[0] and a_point[1] != b_point[1]) and not (
            a_point[0] != b_point[0] and a_point[1] == b_point[1])):
        return True
    else:
        return False


def side_length(a_point, b_point):
    if a_point[0] == b_point[0]:
        return max(a_point[1], b_point[1]) - min(a_point[1], b_point[1])
    else:
        return max(a_point[0], b_point[0]) - min(a_point[0], b_point[0])


def main():
    square = []
    perimeter = 0
    area = 0

    with open(FILE_NAME) as file_reader:
        for line in file_reader:
            if line[0] == "(":
                square.append([int(line[1]), int(line[4])])
    file_reader.close()

    if len(square) != 4:
        print("El número de puntos introducidos en el fichero es incorrecto para un cuadrado.")
        exit()

    point1 = square[0]
    point2 = square[1]
    point3 = square[2]

    print("Se procede al cálculo del perímetro, área,"
          " longitud del lado del cuadrado cuyos 4 vértices"
          " están situados en las coordenadas: ")
    sleep(3)

    for point in square:
        print("({}, {})m".format(point[0], point[1]))
        sleep(1)

    if adjacent_side(point1, point2):
        perimeter = side_length(point1, point2)*4
        area = side_length(point1, point2)**2
        print("La longitud de sus lados es: {}m.".format(side_length(point1, point2)))
    elif adjacent_side(point1, point3):
        perimeter = side_length(point1, point3)*4
        area = side_length(point1, point3)**2
        print("La longitud de sus lados es: {}m.".format(side_length(point1, point3)))
    sleep(1)
    print("El perímetro del cuadrado es: {}m.".format(perimeter))
    sleep(1)
    print("El área del cuadrado es: {}m^2.".format(area))


if __name__ == "__main__":
    main()
