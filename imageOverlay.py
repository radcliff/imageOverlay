# http://pillow.readthedocs.org/en/latest/reference/Image.html
# http://pillow.readthedocs.org/en/latest/handbook/tutorial.html

from PIL import Image
from urllib.request import urlopen
import io

response = urlopen(imageURL)
file = io.BytesIO(response.read())
image = Image.open(file).convert('RGBA')

overlay = Image.open(pathToOverlay).convert('RGBA') #<= must be RGBA && match background

output = Image.alpha_composite(image, overlay)

#output.save("images/example.jpg")
#output.show()
