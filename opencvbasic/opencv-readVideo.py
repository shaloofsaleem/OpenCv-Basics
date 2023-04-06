import cv2

vid = cv2.VideoCapture("Lamborghini .mp4")

while True:
    ret , frame = vid.read()
    text ="Lamborghini Mud"
    cv2.putText(frame, text,(40,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0, 225, 0), 1)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cv2.destroyAllWindows()


