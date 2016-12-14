import numpy as np
from matplotlib import pyplot as plt
import cv2
print np.max([2,3])

x=np.array([2,5])

a=x>2
print a 

for i in x :
	print i 

# creating look-up table

feature_spaces=np.array([(1,1,1),(2,2,1),(1,1,0),(2,2,-1),(1,1,-1),(2,1,2),(2,1,1),(2,1,0),(2,1,-1),(2,1,-2),(1,0,1),(2,0,1),(1,0,0),
(2,0,-1),(1,0,-1),(2,-1,2),(2,-1,1),(2,-1,0),(2,-1,-1),(2,-1,-2),(1,-1,1),(2,-2,1),(1,-1,0),(2,-2,-1),(1,-1,-1),(1,2,2),(1,2,1),(1,2,0),
(1,2,-2),(1,2,-1),(1,1,2),(1,1,-2),(1,0,2),(1,0,-2),(1,-1,2),(1,-1,-2),(1,-2,2),(1,-2,1),(1,-2,0),(1,-2,-1),(1,-2,-2),(0,1,1)
,(0,2,1),(0,1,0),(0,2,-1),(0,1,-1),(0,1,2),(0,1,-2),(0,0,1)])

print "hell"
x=np.array([25,25,45])
y=x+5
print y
y=y.astype('float')
y=(y/100)*6
y=y.astype('int')
print y
import cv2
cap=cv2.VideoCapture("socin.mp4")
ret,frame=cap.read()
cv2.imwrite("soctest.png",frame)
