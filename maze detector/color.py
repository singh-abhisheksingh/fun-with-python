import cv2
import numpy as np 

img = cv2.imread('maze.png')
list1=[]
list2=[]
list3=[]
list4=[]
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([110,245,215])
upper_blue = np.array([130,265,295])
lower_white = np.array([-10,-10,215])
upper_white = np.array([10,10,295])
lower_green = np.array([50,245,215])
upper_green = np.array([70,265,295])

 
# Here we are defining range of bluecolor in HSV
# This creates a mask of blue coloured 
# objects found in the frame.
mask = cv2.inRange(hsv, lower_blue, upper_blue)
mask2 = cv2.inRange(hsv, lower_white, upper_white)
mask3 = cv2.inRange(hsv, lower_green, upper_green)
_,contours,h = cv2.findContours(mask,1,2)
_,contours2,h = cv2.findContours(mask2,1,2)
_,contours3,h = cv2.findContours(mask3,1,2)

for cnt in contours:
	M = cv2.moments(cnt)
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])
	list1.append((cx,cy))

for cnt in contours2:
	M = cv2.moments(cnt)
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])
	list2.append((cx,cy))

for cnt in contours3:
	M = cv2.moments(cnt)
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])
	list3.append((cx,cy))


# The bitwise and of the frame and mask is done so 
# that only the blue coloured objects are highlighted 
# and stored in res
res = cv2.bitwise_and(img,img, mask= mask)
#cv2.imshow('img',img)
#cv2.imshow('mask',mask)
#cv2.imshow('mask2',mask2)
#cv2.imshow('mask3',mask3)
#cv2.imshow('res',res)

#print (list1)
#print (list2)
#print (list3)
list4=list2+list3
cv2.waitKey(0)
# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()