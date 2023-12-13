import cv2
import numpy as np


image = cv2.imread('image.jpg')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_distance_to_object = 60
object_width = 20

lower_bound = np.array([0, 0, 0])	 
upper_bound = np.array([300, 1000, 60])

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_bound, upper_bound)

cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_contour = max(contours, key = cv2.contourArea)
x, y, width, height = cv2.boundingRect(max_contour)
cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)

cv2.imshow('Bordered object', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

focal_length = image_distance_to_object * width / object_width

print('Фокусное расстояние:', focal_length)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        x, y, width, height = cv2.boundingRect(max_contour)
        
        camera_distance_to_object = round(focal_length * object_width / width)
        
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
        cv2.putText(frame, str(camera_distance_to_object), (0, 50), 0, 1, (0, 255, 0), 2)
        
        cv2.imshow("Camera", frame)
        
        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()
