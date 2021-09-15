import cv2
import numpy

arr = numpy.zeros((500,500,3))
center_coordinates = (240, 200)
radius = 40
color = (255, 255, 255)
thickness = 3
image = cv2.circle(arr, center_coordinates, radius, color, thickness)

center_coordinates = (240, 300)
radius = 60
color = (255, 255, 255)
thickness = 3
image = cv2.circle(arr, center_coordinates, radius, color, thickness)

center_coordinates = (200, 160)
radius = 15
color = (255, 255, 255)
thickness = 3
image = cv2.circle(arr, center_coordinates, radius, color, thickness)

center_coordinates = (280, 160)
radius = 15
color = (255, 255, 255)
thickness = 3
image = cv2.circle(arr, center_coordinates, radius, color, thickness)


center_coordinates = (230, 190)
radius = 2
color = (255, 255, 255)
thickness = 10
image = cv2.circle(arr, center_coordinates, radius, color, thickness)

center_coordinates = (250, 190)
radius = 2
color = (255, 255, 255)
thickness = 10
image = cv2.circle(arr, center_coordinates, radius, color, thickness)

center_coordinates = (240, 205)
radius = 2
color = (255, 255, 255)
thickness = 8
image = cv2.circle(arr, center_coordinates, radius, color, thickness)


cv2.imshow('smiley', arr)
cv2.waitKey()
cv2.destroyAllWindows()
