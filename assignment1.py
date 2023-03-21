import cv2
import numpy as np
import os 

# Define the video file paths
video_paths = ['sample videos/trim2.mp4', 'sample videos/trim2.mp4', 'sample videos/trim3.mp4' ]

# Define the size of the crops for the negative images
crop_size = 64

# Define the size of the images
img_size = (128, 128)

# Initialize a list to store the frames
frames = []

# Loop over the video files
for video_path in video_paths:
    # Initialize the video object for the current video file
    video = cv2.VideoCapture(video_path)
    
    # Loop over the frames in the video
    while True:
        # Read a frame from the video
        ret, frame = video.read()

        if not ret:
            print(f"Error reading frame {len(frames)} from {video_path}")
            break

        try:
            # Add the frame to the list
            frames.append(frame)
        except Exception as e:
            print(f"Error reading frame {len(frames)} from {video_path}: {e}")
            continue

    # Initialize a list to store the positive and negative images
    pos_imgs = []
    neg_imgs = []

    # Loop over the frames
    for i in range(len(frames)):

        # Load the frame
        frame = frames[i]

        # Annotate the frame for positive image
        x, y, w, h = cv2.selectROI(frame)

        # Crop the frame to create a positive image
        pos_img = frame[y:y+h, x:x+w]

        # Resize the positive image
        pos_img = cv2.resize(pos_img, img_size)

        # Set the directory for the positive images
        pos_dir = "positive_images/"

        # Create the directory if it doesn't exist
        if not os.path.exists(pos_dir):
            os.makedirs(pos_dir)

        # Save the positive image
        cv2.imwrite(pos_dir + f"pos_{i}.jpg", pos_img)

        # Add the positive image to the list
        pos_imgs.append(pos_img)

        # Annotate the frame for negative image
        x, y, w, h = cv2.selectROI(frame)

        # Crop the frame to create a negative image
        neg_img = frame[y:y+h, x:x+w]

        # Resize the negative image
        neg_img = cv2.resize(neg_img, img_size)

        # Set the directory for the positive images
        neg_dir = "negative_images/"

        # Create the directory if it doesn't exist
        if not os.path.exists(neg_dir):
            os.makedirs(neg_dir)

        # Save the positive image
        cv2.imwrite(neg_dir + f"neg_{i}.jpg", neg_img)

        neg_imgs.append(neg_img)

       