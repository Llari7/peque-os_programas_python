from time import sleep

from polygons.rectangle import Rectangle, COOR_X, COOR_Y

FILE_NAME = "coordinates.save"


def print_point(point):
    print("({}, {})".format(point[COOR_X], point[COOR_Y]))


def biggest_point(point1, point2, point3, point4):
    if ((max(point1[COOR_X], point2[COOR_X], point3[COOR_X], point4[COOR_X]) == point1[COOR_X]) and
            (max(point1[COOR_Y], point2[COOR_Y], point3[COOR_Y], point4[COOR_Y]) == point1[COOR_Y])):
        return point1
    elif ((max(point1[COOR_X], point2[COOR_X], point3[COOR_X], point4[COOR_X]) == point2[COOR_X]) and
          (max(point1[COOR_Y], point2[COOR_Y], point3[COOR_Y], point4[COOR_Y]) == point2[COOR_Y])):
        return point2
    elif ((max(point1[COOR_X], point2[COOR_X], point3[COOR_X], point4[COOR_X]) == point3[COOR_X]) and
          (max(point1[COOR_Y], point2[COOR_Y], point3[COOR_Y], point4[COOR_Y]) == point3[COOR_Y])):
        return point3
    else:
        return point4


def smallest_point(point1, point2, point3, point4):
    if ((min(point1[COOR_X], point2[COOR_X], point3[COOR_X], point4[COOR_X]) == point1[COOR_X]) and
            (min(point1[COOR_Y], point2[COOR_Y], point3[COOR_Y], point4[COOR_Y]) == point1[COOR_Y])):
        return point1
    elif ((min(point1[COOR_X], point2[COOR_X], point3[COOR_X], point4[COOR_X]) == point2[COOR_X]) and
          (min(point1[COOR_Y], point2[COOR_Y], point3[COOR_Y], point4[COOR_Y]) == point2[COOR_Y])):
        return point2
    elif ((min(point1[COOR_X], point2[COOR_X], point3[COOR_X], point4[COOR_X]) == point3[COOR_X]) and
          (min(point1[COOR_Y], point2[COOR_Y], point3[COOR_Y], point4[COOR_Y]) == point3[COOR_Y])):
        return point3
    else:
        return point4


def main():
    points = []

    with open(FILE_NAME) as file_reader:
        for line in file_reader:
            if line[0] == "(":
                points.append([int(line[1]), int(line[4])])
    file_reader.close()

    if len(points) != 4:
        print("El número de puntos introducidos en el fichero es incorrecto para un cuadrado.")
        exit()

    small_point = smallest_point(points[0], points[1], points[2], points[3])
    big_point = biggest_point(points[0], points[1], points[2], points[3])
    medium_points = []
    for point in points:
        if point != small_point and point != big_point:
                medium_points.append(point)
    if len(medium_points) != 2:
        print("Ha habido un ocurridoun error inseperado en el programa.")
        print("Saliendo del programa...")
        sleep(3)
        exit()

    print("Se procede al cálculo del perímetro, área,"
          " longitud del lado del cuadrado cuyos 4 vértices"
          " están situados en las coordenadas: ")
    sleep(3)

    rectangle = Rectangle(small_point, medium_points[0], medium_points[1], big_point)
    print("Los lados son de {}m el lado largo y {}m el lado corto. ".format(rectangle.longer_side_length(),
                                                                            rectangle.shorter_side_length()))
    print("El perímetro del rectángulo es de {}m.".format(rectangle.perimeter()))
    print("El área del rectángulo es de {}m^2.".format(rectangle.area()))


if __name__ == "__main__":
    main()
