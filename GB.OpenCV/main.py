from cgi import test
import cv2

img = cv2.imread('test.jpeg')
print(img.shape)

# img = cv2.resize(img,(500,500))
# print(img.shape)

cv2.imshow("Result", img)
cv2.waitKey(0)