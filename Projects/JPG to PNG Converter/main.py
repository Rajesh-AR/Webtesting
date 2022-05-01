import sys
import os
from PIL import Image

# Collect the source and target folder names:
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# Check if the source and target folder exists in the current directory:
if not os.path.exists(image_folder):
    print('Image folder does not exist, please check the soruce folder name and give the correct one')
    sys.exit()
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
    print('Target folder ' + output_folder + ' has been created !!' ) 
else:
    print('Target folder already exists')
    x = input('Do you want to continue yes/no? ')
    if x == 'yes':
        print('Rewriting the existing folder !!')
    elif x == 'no':
        print('Abording the process !!')
        sys.exit()
    else: 
        print('Incorrect option, aborting the process !!')
        sys.exit()

# Loop through the source folder images, convert them to png and save it to the target folder:

for filename in os.listdir(image_folder):
    img = Image.open(f'./{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print(filename + ' has been converted to png format')
