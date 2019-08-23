import cv2 as cv
import numpy as np
import sys

def readfile(filename):
    with open(filename, 'r') as f:
        filestring = f.read()
        return filestring

def convert(msg):
    list_ = ''
    for i in msg:
        aux = bin(ord(i))
        list_ += (aux[2:])
    print(list_)
    return list_

def openimage(imagepath):
    return cv.imread(imagepath)

def hidemsg(msg, image):
    mask = '00000011'
    flag = False
    for x in range(0, image.shape[1]):
        for y in range(0, image.shape[0]):
            for i in range(0, image.shape[2]):
                if(len(msg) > 0):
                    aux = bin(image[y][x][i])
                    aux = aux[:6] + msg[0]
                    msg = msg[1:]
                    image[y][x][i] = int(aux, 2)
                else:
                    if(len(mask) > 0):
                        aux = bin(image[y][x][i])
                        aux = aux[:6] + mask[0]
                        mask = mask[1:]
                        aux = "".join(aux)
                        image[y][x][i] = int(aux, 2)
                    else:
                        flag = True
            if flag:
                break
        if flag:
            break
    cv.imwrite('resultado.bmp', image)
                


def main():
    filename = sys.argv[1]
    imagepath = sys.argv[2]
    hidemsg(convert(readfile(filename)), openimage(imagepath))

if __name__ == '__main__':
    main()