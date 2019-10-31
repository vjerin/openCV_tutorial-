import cv2,time
import numpy as np

'''
NOTE:
- change all the file paths according to you system
'''




# reading image

img=cv2.imread('/home/jerin/code/openCV_tutorial/fruit_0000.jpg',1)  # 1 for BGR and 0 for grayscale
print(type(img))
print(img)
print(img.shape)

# display image

cv2.imshow('fruit',img)
cv2.waitKey(0)            # press any key to exit
cv2.destroyAllWindows()   # destry window displaying image 

# resizing image

img=cv2.resize(img,(900,900))

# face detector

face_clf=cv2.CascadeClassifier('/home/jerin/code/openCV_tutorial/haarcascade_frontalface_default.xml')  # importing xml file containing classifier

img2=cv2.imread('/home/jerin/code/openCV_tutorial/person_0002.jpg')
g_img=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)                                                             # convert to gray scale

face=face_clf.detectMultiScale(g_img,scaleFactor=1.05)                                                  # Detect face change scale factor till you get the best border

for x,y,w,h in face:
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),2)
    


cv2.imshow('face_detect',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()   


# video capture (frame)

video=cv2.VideoCapture(0)  # start video camera

check,frame=video.read()
print(check)
print(frame)

time.sleep(3)

cv2.imshow('frame',frame)  # display frame
cv2.waitKey(0)
cv2.destroyAllWindows()

video.release()            # stop camera 


# video capture (video)

video2=cv2.VideoCapture(0)

a=1
while True:
    a=a+1
    check,frame=video2.read()
    cv2.imshow('video',frame)
    key=cv2.waitKey(3)
    if key==ord('s'):
        break

cv2.destroyAllWindows()  
video.release()      
print(a)  


# video capture with face detection

face_clf=cv2.CascadeClassifier('/home/jerin/code/openCV_tutorial/haarcascade_frontalface_default.xml')
video2=cv2.VideoCapture(0)

a=1
while True:
    a=a+1
    check,frame=video2.read()
    g_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face=face_clf.detectMultiScale(g_img,scaleFactor=1.05)

    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)



    cv2.imshow('video',frame)
    key=cv2.waitKey(1)
    if key==ord('s'):
        break

cv2.destroyAllWindows()      
video2.release()  
print(a)  
