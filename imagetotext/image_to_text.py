from pytesseract import pytesseract
from PIL import Image
tesseract_path = r"C:\Users\tkano\AppData\Local\Tesseract-OCR\tesseract.exe"
path_img1 = "Screenshot 2023-08-03 115311.png"
pytesseract.tesseract_cmd = tesseract_path
img1 = Image.open(path_img1)
text1 = pytesseract.image_to_string(img1)
print("Image 1 text:\n", text1)