from PIL import Image
import pytesseract


def extract(image,topleft,bottomright):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    img = Image.open(image)
    topleft_width, topleft_hieght = topleft
    bottomright_width, bottomright_hieght = bottomright
    img2 = img.crop((topleft_width,topleft_hieght,bottomright_width,bottomright_hieght))
    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(img2, config = config)
    return text