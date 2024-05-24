from PIL import Image

image = Image.open('пасха.jpg')
image_crop = image.crop((200, 150, 600, 300))
image_crop.save('пасха_crop.jpg')