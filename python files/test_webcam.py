import cv2

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("no stream")
    exit()
    
while True:
    ret, frame = stream.read()
    if not ret:
        print("no more Stream")
        break
    
    cv2.imshow("webcam!", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
stream.release()
cv2.destroyAll()