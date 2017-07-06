import cv2
import numpy as np

image = cv2.imread("bolssonaro.jpg",0)
imageEqu = cv2.equalizeHist(image)
kernel = np.ones((6,6),np.float32)/25
filter2D = cv2.filter2D(imageEqu, -1,kernel)
blur  = cv2.blur(imageEqu,(5,5))
gaussianBlur = cv2.GaussianBlur(imageEqu,(5,5),0)
median = cv2.medianBlur(imageEqu,5)
bilateralfilter = cv2.bilateralFilter(imageEqu,9,75,75)
finalImage = np.concatenate((image,filter2D,blur,median,gaussianBlur,bilateralfilter),axis=1)
cv2.imshow("final Image",finalImage)
cv2.imwrite("nova Imagem.jpg",image)


cv2.waitKey(0)
cv2.destroyAllWindows()
