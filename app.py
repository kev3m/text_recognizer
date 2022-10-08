import cv2

img = cv2.imread("./test_image.jpeg")
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()