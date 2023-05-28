from PIL import Image

img_rgb = Image.open('agumon.jpg')
img_gray = img_rgb.convert('L')
img_gray.save('agumon_gray.jpg')