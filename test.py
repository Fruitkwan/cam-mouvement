import numpy as np
import matplotlib.pyplot as plt
import math  

from scipy.spatial.distance import cosine
import cv2

cap = cv2.VideoCapture(0)

#create 



while True:
    _, frame = cap.read()
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()