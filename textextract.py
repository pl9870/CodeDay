import cv2
import numpy as np
import requests
import io
import json
import os

image_file = "test.png"
img = cv2.imread(image_file)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
height, width = img.shape
roi = img
print(os.path.getsize(image_file));

url_api = "https://api.ocr.space/parse/image"
api_key = "b49437848e88957"
_, compressedImage = cv2.imencode(".jpg", roi, [1,60])
file_bytes = io.BytesIO(compressedImage)

result = requests.post(url_api, files = {image_file: file_bytes}, data = {"apikey": api_key, "language": "spa"})

result = result.content.decode()
result = json.loads(result)
if result != None:
    text_detected = result.get("ParsedResults")[0].get("ParsedText")
    f = open("demofile2.txt", "a")
    f.write(text_detected)
    f.close()
    #cv2.imshow("Castillo's Baby", roi)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    print("Translated")
else:
    print("Unfortunately, We aren't good enough!")
