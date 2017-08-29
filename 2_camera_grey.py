import cv2

camera = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = camera.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Bilde", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
