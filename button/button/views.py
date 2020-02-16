from django.shortcuts import render
import requests
import cv2
import numpy as np
import io
import json
import os


def button(request):
    return render(request, 'index.html')

def external(request):
    inp = request.POST.get('param')
    img = request.FILES.get('image')
    img = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    cv2.imwrite("geeks.jpg", img)
    text = lol(r"C:\xampp\htdocs\quizlet\button\geeks.jpg", inp)
    return render(request, 'index.html', {"data": text})

def lol(image_file, language):
    img = cv2.imread(image_file)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    height, width = img.shape
    roi = img
    #print(os.path.getsize(image_file));

    url_api = "https://api.ocr.space/parse/image"
    api_key = "b49437848e88957"
    _, compressedImage = cv2.imencode(".jpg", roi, [1,60])
    file_bytes = io.BytesIO(compressedImage)

    result = requests.post(url_api, files = {image_file: file_bytes}, data = {"apikey": api_key, "language": language})

    result = result.content.decode()
    result = json.loads(result)
    if result != None:
        text_detected = result.get("ParsedResults")[0].get("ParsedText")
        #f = open("demofile2.txt", "a")
        #f.write(text_detected)
        #f.close()
        #cv2.imshow("Castillo's Baby", roi)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        return text_detected
    else:
        return "Nothing"
