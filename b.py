from flask import Flask, request
import base64
from io import BytesIO
import webbrowser
from PIL import Image
import pytesseract

app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    i = request.get_data()

    print(pytesseract.image_to_string(Image.open(BytesIO(base64.b64decode(i)))))
    #
    # new = 2
    #
    # tabUrl = "https://www.google.com/#safe=strict&q="
    #
    # term = "hi"
    #
    # br = webbrowser.get("safari")
    # br.open(tabUrl+term,new=new)
    # br.open(tabUrl+"hihi",new=new)
    # br.open(tabUrl+"hihihi", new=new)

    return 'Received'
