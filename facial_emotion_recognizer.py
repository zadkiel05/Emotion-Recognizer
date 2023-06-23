from PIL import __version__ 
from facial_emotion_recognition import EmotionRecognition
import cv2

er = EmotionRecognition(device='cpu')

cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    frame = er.recognise_emotion(frame, return_type='BGR')
    cv2.putText(frame, f'It is often exclaimed that our feelings at heart are', (40, 400), cv2.FONT_HERSHEY_COMPLEX,
                0.6, (255, 0, 0), 2)
    cv2.putText(frame, f'reflected on the face...', (40, 420), cv2.FONT_HERSHEY_COMPLEX,
                0.6, (255, 0, 0), 2)
    cv2.putText(frame, f'                                     -ZADKIEL', (120, 450), cv2.FONT_HERSHEY_COMPLEX,
                0.6, (0, 255, 0), 2)
    cv2.imshow('Emotion Recognistion', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cam.release()
cv2.destroyAllWindows()