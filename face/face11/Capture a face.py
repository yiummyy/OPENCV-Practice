import numpy as np
import cv2
x = np.arange(1,10)
print(x)

cap = cv2.VideoCapture(0)
cap.open(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("test", frame)
    if cv2.waitKey(1) == ord('z'):
        break
cap.release()
cv2.destroyAllWindows()
