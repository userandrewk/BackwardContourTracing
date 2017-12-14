from PIL import Image, ImageDraw
from Backward_contour_tracing import BackwardTracindContor
import math


class Picture:
    """

    """
    def __init__(self, name):
        """

        :param name:
        """
        self.__image = Image.open(name)
        self.__seg_im = self.__image.copy()
        self.contor = []

    def find_contor(self):
        """

        :return:
        """
        bst = BackwardTracindContor(self.__seg_im)
        self.contor = bst.contor

        return bst.contor

    def segmentation(self):
        """

        :return:
        """
        width = self.__seg_im.size[0]  # Ширина.
        height = self.__seg_im.size[1]  # Висота.
        pix = self.__seg_im.load()

        def is_black(rgb):
            """

            :param rgb:
            :return:
            """
            return math.sqrt(rgb[0] ** 2 + rgb[1] ** 2 + rgb[2] ** 2) < 100

        for i in range(width):
            for j in range(height):

                if not is_black(pix[i, j]):
                    pix[i, j] = (255, 255, 255)

                else:
                    pix[i, j] = (0, 0, 0)

    def show_image(self):
        """

        :return:
        """

        draw = ImageDraw.Draw(self.__image)

        for pixel in self.contor:
            draw.point(pixel, (0, 255, 0))

        del draw
        self.__image.show()

    def save_as(self, sava_as):
        """

        :param sava_as:
        :return:
        """
        self.__image.save(sava_as, "JPEG")

