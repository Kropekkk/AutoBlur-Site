from django.conf import settings
import numpy as np
import cv2

def CorrectKernelValue(value):
   if value<=0:
      value = 1
   elif value>=122:
      value = 121
   else:
      if value % 2==0:
         value+=1
   
   return value

def blur(path, sliderInfo):
   img = cv2.imread(path, 1)
 
   if type(img) is np.ndarray:
      baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
      faceCascade = cv2.CascadeClassifier(baseUrl+'haarcascade_frontalface_default.xml')
      imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)
        
      for (x, y, w, h) in faces:
         img[y:y+h, x:x+w] = cv2.medianBlur(img[y:y+h, x:x+w], CorrectKernelValue(sliderInfo))

      cv2.imwrite(path, img)
   else:
      print('Error Blur')