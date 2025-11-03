import cv2 # OpenCV library for computer vision

alg = "haarcascade_frontalface_default.xml"    # Path to the Haar Cascade XML file for face detection
face_cascade = cv2.CascadeClassifier(alg)      # Load the Haar Cascade classifier
 
cam = cv2.VideoCapture(0)         # Initialize webcam capture

while True:         

    _, img = cam.read()             # Read a frame from the webcam
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)          # Convert the frame to grayscale
    face = face_cascade.detectMultiScale(grayimg, 1.3, 5)    # Detect faces in the grayscale image
    
    for (x, y, w, h) in face:                                  # Draw rectangles around detected faces
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)  # Green rectangle
                                                     # B=0, G=255, R=0 with thickness 5

 cv2.imshow("Face Detection", img)       # Display the frame with detected faces
    key = cv2.waitKey(10)
    if key == 27:
        break

cam.release()
cv2.destroyallwindows()
