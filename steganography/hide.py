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
        aux = aux[2:]
        aux = aux.zfill(8)
        #print(aux) 
        list_ += (aux)
        
    list_ = list_ + '00000011'
    return list_

def openimage(imagepath):
    return cv.imread(imagepath)

def hidemsg(msg, image):
    print('')
    flag = False
    for x in range(0, image.shape[1]):
        for y in range(0, image.shape[0]):
            for i in range(0, image.shape[2]):
                if(len(msg) > 0):
                    aux = bin(image[y][x][i])
                    aux = aux[:-1] + msg[0]
                    aux = aux[2:].zfill(8)
                    #print(aux)
                    msg = msg[1:]
                    newValue = int(aux,2)
                    image.itemset((x, y, i), newValue)
                else:
                    flag = True
            if flag:
                break
        if flag:
            break
    cv.imwrite('resultImg/resultado.bmp', image)
                


def main():
    filename = sys.argv[1]
    imagepath = sys.argv[2]
    hidemsg(convert(readfile(filename)), openimage(imagepath))

if __name__ == '__main__':
    main()

