from django.conf import settings
import numpy as np
import cv2
 
def blur(path):
   img = cv2.imread(path, 1)
 
   if (type(img) is np.ndarray):
      baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
      faceCascade = cv2.CascadeClassifier(baseUrl+'haarcascade_frontalface_default.xml')
      imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)
 
      for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 3)
 
      cv2.imwrite(path, img)
   else:
      print('Error Blur')