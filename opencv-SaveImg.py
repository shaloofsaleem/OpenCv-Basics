import cv2

img = cv2.imread("demo.jpg")

while True:
    cv2.imshow("image", img)
    cv2.imwrite("savedimge.jpg", img)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cv2.destroyAllWindows()