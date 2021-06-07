#importer les modules 
import cv2  # opencv va permettre de gérer les caméras
import time,os.path # time permet de gérer le temps et os permet de gérer les chemins et les fichiers
from time import sleep
import os
# initialiser les cameras
# Ici nous utilisons quatre caméra sur un seul raspberry pi
camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(2)
camera3 = cv2.VideoCapture(4)
camera4 = cv2.VideoCapture(6)



while True:
    ret1, frame1 = camera1.read()
    ret2, frame2 = camera2.read()
    ret3, frame3 = camera3.read()
    ret4, frame4 = camera4.read()
    
    # les différents chemin pour enregistrer les chemin de chaque caméra
    path1 ="./Bureau/Imagetest/Camera1"
    path2 ="./Bureau/Imagetest/Camera2"
    path3 ="./Bureau/Imagetest/Camera3"
 
    path4 ="./Bureau/Imagetest/Camera4"
    # le timelapse 
    sleep(20) # une nouevelle image chaque 2à seconde on peut changer la valeur en fonction du besion
    
   
    if ret1:
       # cv2.imshow("camera1", frame1)
        cv2.imwrite(os.path.join(path1, "image1_" + time.strftime("%d-%m-%Y-%H-%M-%S_")  + ".png"),frame1)
        camera1.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        camera1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
       
     
    if ret2:
       # cv2.imshow("camera2", frame2)
        cv2.imwrite(os.path.join(path2, "image2_" + time.strftime("%d-%m-%Y-%H-%M-%S_")  + ".png"),frame2)
        camera2.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # Définir la résolution  et cette ligne on a la hauteur 
        camera2.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080) # on a ici la largeur de la résolution 
       
    if ret3:
        #cv2.imshow("camera3", frame3)
       cv2.imwrite(os.path.join(path3, "image3_" + time.strftime("%d-%m-%Y-%H-%M-%S_")  + ".png"),frame3)
       camera3.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
       camera3.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
       
     
    if ret4:
      # cv2.imshow("camera4", frame4)
       cv2.imwrite(os.path.join(path4, "image4_" + time.strftime("%d-%m-%Y-%H-%M-%S_")  + ".png"),frame4)
       camera4.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
       camera4.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
       
     
        
    if cv2.waitKey(1) & 0xff ==ord('a'):   # si on clique sur la touche a on ferme le code 
        
          break
          
        
 
  
camera1.release()
camera2.release()
camera3.release()
camera4.release()
cv2.destroyAllWindows()
