import webbrowser
from PIL import Image
import pytesseract

import requests
r = requests.post("http://127.0.0.1:5000/", data={'foo':'Screenshot_20180430-155602.png'})
print(r.text)

# image = Image.open("Screenshot_20180430-155602.png")
# print(pytesseract.image_to_string(image))
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


