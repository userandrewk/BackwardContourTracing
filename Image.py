from PIL import Image, ImageDraw
from Backward_contour_tracing import BackwardTracingContour
import math


class Picture:
    """
    Class with represent Image. Class can find contour, make new segmentation`s
    image from given, show and save image.
    """
    def __init__(self, name):
        """
        Init the class, open an image and make a copy`s image.
        :param name: str
        """
        self.__image = Image.open(name)
        self.__seg_im = self.__image.copy()
        self.contor = []

    def find_contor(self):
        """
        Find pixels with are in the contour.
        :return: list
        """
        bst = BackwardTracingContour(self.__seg_im)
        self.contor = bst.contor

        return bst.contor

    def segmentation(self):
        """
        This function make a white-black image from the normal image. And use an another function
        is_black() which are inside the segmentation().
        :return: None
        """
        width = self.__seg_im.size[0]  # Ширина.
        height = self.__seg_im.size[1]  # Висота.
        pix = self.__seg_im.load()

        def is_black(rgb):
            """
            This function take`s pixel which represent by list of rgb-colors and find
            an Evklid`s value.
            :param rgb: list
            :return: bool
            """
            return math.sqrt(rgb[0] ** 2 + rgb[1] ** 2 + rgb[2] ** 2) < 50

        for i in range(width):
            for j in range(height):

                if not is_black(pix[i, j]):
                    pix[i, j] = (255, 255, 255)

                else:
                    pix[i, j] = (0, 0, 0)

    def show_image(self):
        """
        This function draw contour onto given image and show new image.
        :return: None
        """

        draw = ImageDraw.Draw(self.__image)

        for pixel in self.contor:
            draw.point(pixel, (0, 255, 0))

        del draw
        self.__image.show()

    def save_as(self, sava_as):
        """
        This function can save ready image in JPEG format.
        :param sava_as: sting
        :return: None
        """
        self.__image.save(sava_as, "JPEG")

