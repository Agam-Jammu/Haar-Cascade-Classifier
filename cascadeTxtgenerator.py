import os

# Set the paths to the positive and negative image directories
pos_dir = "positive_images\\"
neg_dir = "negative_images\\"

# Define the path to the output positive and negative text files
pos_txt_file = "positive.txt"
neg_txt_file = "negative.txt"

# Generate the positive text file
with open(pos_txt_file, "w") as f:
    for filename in os.listdir(pos_dir):
        if filename.endswith(".jpg"):
            f.write(f"{os.path.join(pos_dir, filename)} 1 0 0 24 24\n")

# Generate the negative text file
with open(neg_txt_file, "w") as f:
    for filename in os.listdir(neg_dir):
        if filename.endswith(".jpg"):
            f.write(f"{os.path.join(neg_dir, filename)}\n")
