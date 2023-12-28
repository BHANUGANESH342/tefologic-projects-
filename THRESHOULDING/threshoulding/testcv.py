import cv2 as cv
import numpy as np
image = cv.imread(r"C:\Users\rkssp\Desktop\bharathi.jpg")
cv.imshow("original ", image)
cv.waitKey(0)
cv.destroyAllWindows
#blurrr
kernal = np.ones((7,7),np.float32)/49
cv.imshow("kernal ", kernal)
blurr =cv.filter2D(image,-1,kernal)
cv.imshow("burr", blurr)
cv.waitKey(0)
cv.destroyAllWindows()
#threshould
_,threshould = cv.threshold(image , 100,500, cv.THRESH_BINARY)
cv.imshow("Threshould", threshould)
cv.waitKey(0)
cv.destroyAllWindows()
_,threshouldi = cv.threshold(image , 100,500, cv.THRESH_BINARY_INV)
cv.imshow("Threshould inves", threshouldi)
cv.waitKey(0)
cv.destroyAllWindows()