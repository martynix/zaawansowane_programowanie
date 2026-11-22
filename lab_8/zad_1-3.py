import cv2
from PIL import Image
import pytesseract

# from matplotlib import pyplot

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


img1 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_8/1.jpg"
img2 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_8/2.jpg"
img3 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_8/3.jpg"
img4 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_8/4.jpg"
img5 = "C:/Users/marty/Desktop/magisterka/1sem/zaawansowane_programowanie/lab_8/5.jpg"

# img_preprocessed1 = cv2.cvtColor(cv2.imread(img2), cv2.COLOR_BGR2GRAY)
# pyplot.imshow(img_preprocessed1)
# pyplot.show()


def img_to_text(img):
    img_preprocessed = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(img_preprocessed)
    print(text)


img_to_text(img1)
img_to_text(img2)
img_to_text(img3)
img_to_text(img4)
img_to_text(img5)
