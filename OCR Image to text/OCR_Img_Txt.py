# python code for ocr image to text
import ctypes

import PIL
from PIL import Image, ImageOps
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#grayscale 
img = Image.open('sample.jpg').convert('L') 

#threshold 
threshold = 150 
img = img.point(lambda p: p > threshold and 255) 

#inverted 
img = Image.open('sample.jpg').convert('L') 
img = PIL.ImageOps.invert(img)

#black and white 
img = Image.open('sample.jpg').convert('1') 

#save 
img.save('sample2.jpg') 

#ocr 
text = pytesseract.image_to_string(Image.open('sample2.jpg')) 
print(text)