import cv2
import glob

lists=glob.glob("*.jpg")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for list in lists:
	img= cv2.imread(list)
	grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(grey_img,scaleFactor=1.2,minNeighbors=5)
	for x,y,w,h in faces:
		img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,152,0),(2))

	r_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

	cv2.imshow("pic",r_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


