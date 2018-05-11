from flask import Flask, request
import base64
from io import BytesIO
import webbrowser
from PIL import Image
import pytesseract
import gsearch
import cv2
from autocorrect import spell
import time

app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    i = request.get_data()

    process_image(Image.open(BytesIO(base64.b64decode(i))))

    return 'Received'

def process_image(img):

    start_time = time.time()

    # img = Image.open("iamge.jpg")

    width = img.size[0]
    height = img.size[1]

    question = img.crop((30, 200, width - 30, 340))
    question.show()
    question_str = pytesseract.image_to_string(question).replace('\n', ' ')

    a1 = img.crop((60, 360, width - 100, 400))
    a1.show()
    a1_str = pytesseract.image_to_string(a1)

    a2 = img.crop((60, 440, width - 100, 480))
    a2.show()
    a2_str = pytesseract.image_to_string(a2)

    a3 = img.crop((60, 520, width - 100, 560))
    a3.show()
    a3_str = pytesseract.image_to_string(a3)

    new = 2

    tab_url = "https://www.google.com/#safe=strict&q="

    br = webbrowser.get("safari")
    br.open(tab_url + question_str + " " + a1_str, new=new)
    br.open(tab_url + question_str + " " + a2_str, new=new)
    br.open(tab_url + question_str + " " + a3_str, new=new)

    end_time = time.time()
    print(end_time - start_time)

process_image(Image.open("a.png"))