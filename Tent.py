import math


class Tent:
    def __init__(self, pixel, pixels, start_position):
        """

        :param pixel:
        :param pixels:
        :param start_position:
        """
        self.__pixels = pixels
        self.__pixel = pixel
        self.tent = self.__create_tent()
        self.clock_num = start_position
        self.non_clock_num = start_position

    def __create_tent(self):
        """

        :return:
        """
        tent = [(self.__pixel[0], self.__pixel[1] - 1), (self.__pixel[0] + 1, self.__pixel[1] - 1),
                (self.__pixel[0] + 1, self.__pixel[1]), (self.__pixel[0] + 1, self.__pixel[1] + 1),
                (self.__pixel[0], self.__pixel[1] + 1), (self.__pixel[0] - 1, self.__pixel[1] + 1),
                (self.__pixel[0] - 1, self.__pixel[1]), (self.__pixel[0] - 1, self.__pixel[1] - 1)]

        return tent

    def clock_next(self):
        """

        :return:
        """
        self.clock_num += 1

        if self.clock_num > 7:
            self.clock_num = 0

        return self.tent[self.clock_num]

    def non_cloc_next(self):
        """

        :return:
        """
        self.non_clock_num -= 1
        if self.non_clock_num < 0:
            self.non_clock_num = 7

        return self.tent[self.non_clock_num]

    @staticmethod
    def is_black(pixel):
        """

        :param pixel:
        :return:
        """
        return math.sqrt(pixel[0] ** 2 + pixel[1] ** 2 + pixel[2] ** 2) < 80

    def is_contor(self, position):
        if position == 0:
            next = 1
            previous = 7
        elif position == 7:
            next = 0
            previous = 6
        else:
            next = position + 1
            previous = position - 1

        try:
            p_pixel = self.__pixels[self.tent[previous]]
        except IndexError:
            p_pixel = (0, 0, 0)

        try:
            n_pixel = self.__pixels[self.tent[next]]
        except IndexError:
            n_pixel = (0, 0, 0)

        try:
            pixel = self.__pixels[self.tent[position]]
        except IndexError:
            pixel = (0, 0, 0)

        if not Tent.is_black(pixel) \
                and (Tent.is_black(n_pixel) or Tent.is_black(p_pixel)):

            return True

        return False
