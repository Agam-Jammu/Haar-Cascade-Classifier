import cv2

# Load the trained classifier
classifier = cv2.CascadeClassifier("trained_model_1/cascade.xml")

# Open the video file
cap = cv2.VideoCapture("sample videos/trim1.mp4")

# Loop through the video frames
while True:
    # Read a frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect objects in the frame
    objects = classifier.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3000)

    # Draw rectangles around the detected objects
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Video", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()