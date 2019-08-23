# Steganography

- A simple program to hide a message in a image (must be in BPM format) and another one to reveal the hidden message

# Dependencies

To execute the program you will need OPENCV library, to install it use the following command

> pip3 install python-opencv

# Execute

To hide a message, execute the file "hide.py" as follows:

> python3 hide.py texto image.bmp

where texto is the text file that you want to hide and image.bmp is the image to be used, the resulting image will be saved at resultImg/

to reveal the message, execute the file "reveal.py" as follows:

> python3 reveal.py resultImg/resultado.bmp

where resultImg/resultado.bmp is the image with the hidden message


