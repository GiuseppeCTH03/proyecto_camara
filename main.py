import cv2

# Si usas IP Webcam, la URL se ve algo así:
# url = "http://192.168.1.XX:8080/video" 
# Si usas el celular como webcam virtual por USB, el índice suele ser 0 o 1
cap = cv2.VideoCapture(10) 

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Aquí es donde ocurre la magia (puedes meter tu lógica de IA aquí)
    cv2.imshow('Streaming Honor 400 Smart', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()