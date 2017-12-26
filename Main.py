from Image import Picture

"""
Main module, that runs all program
"""

for i in range(1, 9):
    image = Picture("Data/test%d.jpg" % i)
    image.segmentation()
    image.find_contor()
    image.show_image()
    image.save_as("Data/result%d.jpeg" % i)

