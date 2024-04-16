import cv2;
from cvzone.HandTrackingModule import HandDetector;

capture = cv2.VideoCapture(1) #You may need to change the number based on which webcam you are using.
detector = HandDetector(maxHands=1) 

offset = 50

while True:
    success, img = capture.read()
    hands, img = detector.findHands(img, draw=False) #set draw to True if you want to see the hand skeleton

    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("Image", img)
    cv2.waitKey(1)

