import cv2
import numpy
photo1= cv2.imread('cat.jpg')
photo2= cv2.imread('dog.png')

collagePhoto1= photo1[0:183, 0:200]
collagePhoto2= photo2[0:183, 0:200]

cv2.imshow('photo1',collagePhoto1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('photo1',collagePhoto2)
cv2.waitKey()
cv2.destroyAllWindows()

collage= numpy.hstack((collagePhoto1,collagePhoto2))

cv2.imshow('photo1',collage)
cv2.waitKey()
cv2.destroyAllWindows()
