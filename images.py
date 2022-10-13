from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')
# print(img.format)
# print(img.size)
# print(img.mode)
# filtered_img.save("grey.png", "png")
# resize = filtered_img.resize((300, 300))
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png", "png")