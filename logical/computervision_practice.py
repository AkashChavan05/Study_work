import cv2 

img = cv2.imread("/home/fx/Desktop/akash/Study work/Study_work/logical/flowers.jpeg") # Read the image


# new = cv2.blur(img, (5, 5)) # blur the image
# new = cv2.GaussianBlur(img, (5, 5), 0)
# new = cv2.medianBlur(img, 5) # blur the image
# new = cv2.bilateralFilter(img, 9, 75, 75) # blur the image

# ero = cv2.erode(img, (5, 5), iterations = 1) # erode the image
# dil = cv2.dilate(img, (5, 5), iterations = 1) # dilate the image
# morph = cv2.morphologyEx(img, cv2.MORPH_OPEN, (5, 5)) # morphological transformation

# thr = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1] # threshold the image

canny = cv2.Canny(img, 100, 200) # canny edge detection

# cascade = cv2.CascadeClassifier(img)
cv2.imshow("image", canny)  # show the image

# cv2.imshow("image", img)  # show the image
cv2.waitKey(0) # Wait for any key to be pressed
cv2.destroyAllWindows() # Destroy all the windows
