import cv2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


img1 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_9/1.jpg"
img2 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_9/2.jpg"
img3 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_9/3.jpg"
img4 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_9/4.jpg"
img5 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_9/5.jpg"
img6 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_9/clean_example.jpg"


def img_to_text(img):
    img_preprocessed = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)
    # blur = cv2.bilateralFilter(img_preprocessed, 9, 75, 75)
    # converted_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    converted_img = cv2.medianBlur(img_preprocessed, 3)
    # converted_img = cv2.threshold(cv2.GaussianBlur(converted_img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # converted_img = cv2.threshold(cv2.bilateralFilter(converted_img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # converted_img = cv2.threshold(cv2.medianBlur(converted_img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(img_preprocessed, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # converted_img = cv2.adaptiveThreshold(cv2.bilateralFilter(converted_img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # converted_img = cv2.adaptiveThreshold(cv2.medianBlur(converted_img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    text = pytesseract.image_to_string(converted_img)
    print(text)


img_to_text(img1)
img_to_text(img2)
img_to_text(img3)
img_to_text(img4)
img_to_text(img5)
img_to_text(img6)
