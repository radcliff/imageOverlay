# http://pillow.readthedocs.org/en/latest/reference/Image.html
# http://pillow.readthedocs.org/en/latest/handbook/tutorial.html

from PIL import Image
from urllib.request import urlopen
import io

response = urlopen("https://dujk9xa5fr1wz.cloudfront.net/course/240x135/23887_a82a_4.jpg")
file = io.BytesIO(response.read())
image = Image.open(file).convert("RGBA") #<= convert to RGB from RGBA?

overlay = Image.open(file).convert("<mode>") #<= must match background image

output = Image.alpha_composite(image, overlay)
output.save("path/filename.jpg")
