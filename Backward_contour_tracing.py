from Tent import Tent
import math


class BackwardTracingContour:
    """
    This class represent the backward tracing contour algorithms.
    And have only two function find_pixel(), find_contour().
    """
    def __init__(self, image):
        """
        Classes init the and init matrix of pixels from image and
        init a width and height of image.
        :param image:
        """
        self.__pixels = image.load()
        self.__width = image.size[0]
        self.__height = image.size[1]

        self.Ps = self.__first_pixel()  # Стартовий піксель
        self.Pn = None  # Сусідній піксель за годиником
        self.nPn = None  # Сусідній піксель проти годинника
        self.Pe = 0  # Кінцевий піксель
        self.Pa = None  # Активний піксель
        self.Pc = None  # Контурний піксель
        self.Pf = None  # Фоновий піксель
        self.Pcn = None  # Сусідній фоновий піксель
        self.contor = []  # Контурні пікселі

        self.find_contor()

    def __first_pixel(self):
        """
        Проводиться пошук стартового пікселя Pa
        :return: tuple(int, int)
        """
        for i in range(self.__width):
            for j in range(self.__height):
                pix = self.__pixels[i, j]
                if math.sqrt(pix[0] ** 2 + pix[1] ** 2 + pix[2] ** 2) > 80:
                    return i, j

    def find_contor(self):
        """
        Find contour of given segmentation`s image
        by backward tracing contour algorithms.
        :return: None
        """
        self.contor.append(self.Ps)
        self.Pa = self.Ps

        tent = Tent(self.Pa, self.__pixels, start_position=-1)

        while self.Pcn != self.Pe:

            for i in range(8):  # Пошук  сусіднього  контурного  піксела Pn за  годинником
                self.Pn = tent.clock_next()

                if tent.is_contor(tent.clock_num):  # Перевірка чи піксель є контуром
                    self.Pcn = self.Pn
                    break

                elif i == 7 and not tent.is_contor(7):  # Застереження
                    print("erorr1")
                    self.Pn = None
                    pass

            if self.Pa == self.Ps:

                for i in range(8):  # Пошук  сусіднього  контурного  піксела nPn проти годинника
                    self.nPn = tent.non_cloc_next()

                    if tent.is_contor(tent.clock_num):  # Перевірка чи піксель є контуром
                        break

                    else:
                        print("error2")

            else:
                self.nPn = self.Pa

            if self.Pn == self.nPn:
                self.Pf = self.Pa
                self.__pixels[self.Pf] = (0, 0, 0)

                if self.Pn in self.contor and self.Pn != self.Pe:

                    try:
                        self.contor.pop(self.contor.index(self.Pa))
                    except ValueError:
                        pass

                    self.Pa = self.contor[-1]

            else:
                self.Pe = self.contor[0]
                self.Pa = self.Pcn
                self.contor.append(self.Pa)

            d = math.fmod(tent.clock_num + 6, 8)
            tent = Tent(self.Pa, self.__pixels, int(d) - 1)
