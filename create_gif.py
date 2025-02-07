import imageio.v3 as iio

filenames = ['dino1.png', 'dino2.png', 'dino3.png', 'dino4.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('Dino.gif', images, duration=300, loop = 0)