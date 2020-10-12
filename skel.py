# Import the necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

def skeletonize(img, ct):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret,img = cv2.threshold(img, 125, 255, 0)
    name = 'threshed-' + str(ct) + '.jpg'
    cv2.imwrite(name, img)
    size = np.size(img)
    skel = np.zeros(img.shape, np.uint8)

# Get a Cross Shaped Kernel
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

    while True:
        open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
        temp = cv2.subtract(img, open)
        eroded = cv2.erode(img, element)
        skel = cv2.bitwise_or(skel,temp)
        img = eroded.copy()
        if cv2.countNonZero(img)==0:
            break
    return skel

def skelInRange(img):
    bounds = [228, 350, 194, 379]
    total = in_bounds = 0

    size = img.shape

    for x in range(bounds[0], bounds[1]):
        for y in range(bounds[2], bounds[3]):
            if int(img[x][y][2]) < 250:
                total += 1
    return total >= 4500
            

def main():
    vid = cv2.VideoCapture('inktest.mp4')
    curr_frame = 0

    while True:
        ret, frame = vid.read()
        if ret:
            curr_frame+=1
            if skelInRange(frame):
                pass
                # print("one good")
            else:
                pass
                # print("no good")
            print(("{0}: {1}").format(curr_frame, skelInRange(frame)))

            name = 'frame/skel-' + str(curr_frame) + '.jpg'
            cv2.imwrite(name, frame)
        else:
            print("Done :)")
            break

if __name__ == '__main__':
    main()