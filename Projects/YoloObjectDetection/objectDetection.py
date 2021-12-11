import cv2 as cv
import numpy as np
import time

img = cv.imread("../../Photos/horse.jpg")
cv.imshow('Window', img)
cv.waitKey(1)

#Give the configuration and weight file for the model and load the network
net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)

ln = net.getLayerNames()
print(len(ln), ln)

#construct a blob for the image
blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB = True, crop = False)
r = blob[0, 0, :, :]

cv.imshow('Blob', r)
text = f'Blob shape = {blob.shape}'
cv.displayOverlay('blob', text)
cv.waitKey(1)

net.setInput(blob)
t0 = time.time()
outputs = net.forward(ln)
t = time.time()

cv.displayOverlay('Window', f'forward propogation time= {t-t0}')
cv.imshow('Window', img)
cv.waitKey(0)
cv.destroyAllWindows()