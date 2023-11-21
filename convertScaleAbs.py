#change the brightness of image
import cv2 as cv

image=cv.imread("E://openCV_images/pic2.jpg")

new_image=cv.convertScaleAbs(image,alpha=1.5,beta=20)
#beta= lighting  alpha=contrast

cv.imshow("orginal image",image)
cv.imshow("new image",new_image)

cv.waitKey(0)
cv.destroyAllWindows()