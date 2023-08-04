import cv2
img = cv2.imread("E:\DSML\openCV image size\images.png",1)
print(img.shape)
img_resized=cv2.resize(img,(900,400),interpolation = cv2.INTER_NEAREST)
cv2.imshow("Resized",img_resized)
cv2.imwrite('img_resize.jpg',img_resized)
img_cw_180 = cv2.rotate(img_resized, cv2.ROTATE_180)
cv2.imshow("Image rotated by 180 degree", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

