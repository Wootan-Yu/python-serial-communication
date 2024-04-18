import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, (1200, 800)) #mnn window size
    frame = cv2.resize(frame, (1280, 720)) #tensorflow lite window size
    roi = cv2.selectROI("select the area", frame)
    
    print('x: ' 	 + str(roi[0]) + '\n' +
          'y: ' 	 + str(roi[1]) + '\n' +
          'width: '  + str(roi[2]) + '\n' +
          'height: ' + str(roi[3]))
    cropped_image = frame[int(roi[1]):int(roi[1] + roi[3]),
                          int(roi[0]):int(roi[0] + roi[2])]
    cv2.imwrite('/home/herobrine/Desktop/frame.png', cropped_image)
    cv2.imshow('captured roi',cropped_image)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()