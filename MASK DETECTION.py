import cv2

cap=cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

m=cv2.CascadeClassifier('cascade.xml')
print(m.load('face.xml'))

while True:
    s, f= cap.read()
    mask=m.detectMultiScale(f, 1.8 , 11)       
    for (x,y,w,h) in mask:
        cv2.rectangle(f, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.putText(f, 'Wear Mask', (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0 ,255), 2)
    cv2.imshow('video', f)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
