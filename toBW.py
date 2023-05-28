from PIL import Image 

image_file = Image.open("agumon_gray.jpg")
image_file = image_file.convert('1') 
image_file.save('agumon_bw.jpg')