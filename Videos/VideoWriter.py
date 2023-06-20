import cv2

cap = cv2.VideoCapture()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#it will write the video in a new file with the specified name
out = cv2.VideoWriter('output.avi', fourcc, 25, (640, 480))

while(cv2.isOpened()):
  ret, frame = cap.read()

  if ret == True:
    print(cv2.get(cv2.CAP_FROM_FRAME_WIDTH))
    print(cv2.get(cv2.CAP_FROM_FRAME_HEIGHT))

    out.write(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break


cap.release()
out.release()
cv2.destroyAllWindows()
