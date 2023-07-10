import PIL
from PIL import Image
from PIL import ImageDraw

img = Image.new("RGBA", (200, 200), (0, 0, 0))
draw = ImageDraw.Draw(img)
draw.text((0, 0), "This is a test", (255, 255, 0))
draw.chord((100, 75, 125, 100), 0, 360, fill='green')
draw.chord((75, 100, 100, 125), 0, 360, fill='blue')
draw.chord((125, 125, 150, 150), 0, 360, fill='yellow')

# img.save("test.png")
img.show()
