COOR_X = 0
COOR_Y = 1


def side_length(bigger_point, smaller_point):
    if smaller_point[COOR_X] == bigger_point[COOR_X]:
        return bigger_point[COOR_Y] - smaller_point[COOR_Y]
    else:
        return bigger_point[COOR_X] - smaller_point[COOR_X]


class Rectangle:

    def __init__(self, small_point, med_point_1, med_point_2, big_point):
        self.small_point = small_point
        self.med_point_1 = med_point_1
        self.med_point_2 = med_point_2
        self.big_point = big_point

    def shorter_side_length(self):
        if side_length(self.med_point_1, self.small_point) > side_length(self.med_point_2, self.small_point):
            return side_length(self.med_point_2, self.small_point)
        else:
            return side_length(self.med_point_1, self.small_point)

    def longer_side_length(self):
        if side_length(self.med_point_1, self.small_point) > side_length(self.med_point_2, self.small_point):
            return side_length(self.med_point_1, self.small_point)
        else:
            return side_length(self.med_point_2, self.small_point)

    def perimeter(self):
        return 2 * self.longer_side_length() + 2 * self.shorter_side_length()

    def area(self):
        return self.longer_side_length() * self.shorter_side_length()

    def getsmallpoint(self):
        return self.small_point

    def setsmallpoint(self, point):
        self.small_point = point

    def getmedpoint1(self):
        return self.med_point_1

    def setmedpoint1(self, point):
        self.med_point_1 = point

    def getmedpoint2(self):
        return self.med_point_2

    def setmedpoint2(self, point):
        self.med_point_2 = point

    def getbigpoint(self):
        return self.big_point

    def setbigpoint(self, point):
        self.big_point = point

    def tostring(self):
        return "Rectangle: small_point = ({}, {});" \
               " med_point_1 = ({}, {});" \
               " med_point_2 = ({}, {});" \
               " big_point = ({}, {})".format(self.small_point[COOR_X],
                                              self.small_point[COOR_Y],
                                              self.med_point_1[COOR_X],
                                              self.med_point_1[COOR_Y],
                                              self.med_point_2[COOR_X],
                                              self.med_point_2[COOR_Y],
                                              self.big_point[COOR_X],
                                              self.big_point[COOR_Y])
