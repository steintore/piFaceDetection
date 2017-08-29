import cv2

camera = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("../cascades/haarcascade_frontalface_default.xml")

while True:
    (grabbed, frame) = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faceRects = faceCascade.detectMultiScale(gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (100, 100),
        flags = cv2.CASCADE_SCALE_IMAGE)
    #print("I found {} face(s)".format(len(faceRects)))

    for (fX, fY, fW, fH) in faceRects:
        #print("{} - {} - {} - {}".format(fX, fY, fW, fH))
        cv2.rectangle(frame, (fX, fY), (fX+ fW, fY + fH), (0, 0, 255), 3)

    cv2.imshow("Bilde", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
