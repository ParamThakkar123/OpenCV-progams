import cv2

cap = cv2.VideoCapture()

while(cv2.isOpened()):
  ret, frame = cap.read()

  print(cv2.get(cv2.CAP_FROM_FRAME_WIDTH))
  print(cv2.get(cv2.CAP_FROM_FRAME_HEIGHT))

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame', gray)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
