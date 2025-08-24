import cv2
import sys

cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

codes = set()

try:
    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if not data:
            continue
        code = data.split("/")[-1]
        if code in codes:
            continue
        print(code)
        codes.add(code)
except:
    sys.exit()
