import cv2

cat = cv2.imread('cat.jpg')
dog = cv2.imread('dog.png')

cv2.imshow('cat',cat)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('dog',dog)
cv2.waitKey()
cv2.destroyAllWindows()

ccat = cat[40:145,  93:200].copy()

cv2.imshow('ccat',ccat)
cv2.waitKey()
cv2.destroyAllWindows()

cdog = dog[18:123,  89:196]

cv2.imshow('cdog',cdog)
cv2.waitKey()
cv2.destroyAllWindows()

cat[40:145,  93:200] = cdog

dog[18:123,  89:196] = ccat

cv2.imshow('photo1',cat)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('photo2',dog)
cv2.waitKey()
cv2.destroyAllWindows()
