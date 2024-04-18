import cv2

mouse_x, mouse_y = 0,0

def get_mouse_coordinates(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x,y
        
def main():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('webcam')
    cv2.setMouseCallback('webcam',get_mouse_coordinates)
    
    
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720))
        
        if not ret:
            break
        
        print(f'x: {mouse_x}, y: {mouse_y}')
        cv2.imshow('webcam', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()