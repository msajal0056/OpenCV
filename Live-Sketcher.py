import cv2

def sketch(image):
  img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  img = cv2.flip(img, 1)
  img = cv2.GaussianBlur(img,(5,5),0)
  canny_edges = cv2.Canny(img,20,50)
  ret, mask = cv2.threshold(canny_edges,50,225,cv2.THRESH_BINARY_INV)
  return mask

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  cv2.imshow("Live Sketcher",sketch(frame))
  if cv2.waitKey(1)==13:
    break

cap.release();
cv2.destroyAllWindows()
