from PIL import Image

img = Image.open('scene.jpg')
print(img.format)
print(img.size)
area = (100, 100, 250, 250)
cropped_img = img.crop(area)

scene = Image.open('scene.jpg')
flower = Image.open('flower.jpg')
print(flower.mode)
r, g, b = scene.split()
# r.show()
foo = (1, 3, 5, 7)
a, b, c, d = foo
print(a, b, c, d)

