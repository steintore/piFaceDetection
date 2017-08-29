import cv2

camera = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("../cascades/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("../cascades/haarcascade_eye.xml")

while True:
    (grabbed, frame) = camera.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceRects = faceCascade.detectMultiScale(image,
        scaleFactor = 1.1,
        minNeighbors = 2,
        minSize = (300, 300),
        flags = cv2.CASCADE_SCALE_IMAGE)

    for (fX, fY, fW, fH) in faceRects:
        faceROI = frame[fY:fY + fH, fX:fX + fW]
        cv2.rectangle(frame, (fX, fY), (fX+ fW, fY + fH), (255, 0, 0), 2)

        eyeRects = eyeCascade.detectMultiScale(faceROI,
            scaleFactor = 1.15,
            minNeighbors = 20,
            minSize = (30,30),
            flags = cv2.CASCADE_SCALE_IMAGE)

        for (eX, eY, eW, eH) in eyeRects:
            cv2.rectangle(frame, (fX + eX, fY + eY), (fX + eX + eW, fY + eY + eH), (0, 255, 0), 2)

    cv2.imshow("Bilde", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
