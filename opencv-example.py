import cv2
img = cv2.imread('demo.jpg')
while True:
    cv2.imshow("image", img)
    test = "DQ"
    cv2.putText(img,test,(20,120),cv2.FONT_HERSHEY_COMPLEX,5,(123,0,205), 1)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
