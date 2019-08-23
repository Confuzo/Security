import cv2 as cv
import numpy as np
import sys

def openimage(imagepath):
    return cv.imread(imagepath)
def revealmsg(image):
    aux = ''
    decodemsg = ''
    flag = False
    for y in range(0, image.shape[1]):
        for x in range(0, image.shape[0]):
            for i in range(0, image.shape[2]):
                a = image[y][x][i]
                a = bin(a)
                aux = aux + a[-1]
                if(len(aux) == 8):
                    if(int(aux,2) != 3):
                        decodemsg = decodemsg + str(chr(int(aux,2)))
                        aux = ''
                    else:
                        flag = True
            if flag:
                break
        if flag:
            break
    
    print(decodemsg)
    
def main():
    imagepath = sys.argv[1]
    revealmsg(openimage(imagepath))

if __name__ == '__main__':
    main()