import sys
import os
from PIL import Image

# Shows script file name and agrs.
source_folder = sys.argv[1]
output_folder = sys.argv[2]
print("This is the name of the script: ", sys.argv[0])
print("You want to convert JPEG files from {} to PNG and store them in".format(source_folder), output_folder)



# Checks if new folder path exists. If not creates it and names it as sys.argv[2]
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("created folder : ", output_folder)

else:
    print(output_folder, "folder already exists.")


# Converts image from RBG to Grayscale and resizes it.
for imagess in os.listdir(source_folder):
        img = Image.open("{}/{}".format(source_folder, imagess)).convert('L')
        img.thumbnail((200, 200))
        clean_name = os.path.splitext(imagess)[0]
        img.save("{}{}.png".format(output_folder, clean_name), "png")
        print("all done")

