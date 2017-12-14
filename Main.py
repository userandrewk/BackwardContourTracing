from Image import Picture

for i in range(1, 9):
    image = Picture("Data/test%d.jpg" % i)
    image.segmentation()
    image.find_contor()
    image.show_image()
    image.save_as("result%d.jpeg" % i)

