
import cv2
 
# Load the image
image = cv2.imread("images.png",1)
 
# Display the image
cv2.imshow("Image", image)
 
# Wait for the user to press a key
cv2.waitKey(0)
 
# Close all windows
cv2.destroyAllWindows()