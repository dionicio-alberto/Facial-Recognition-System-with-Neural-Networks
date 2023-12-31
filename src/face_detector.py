import cv2
from pathlib import Path
import pathlib

def prueba():
    print('Importacion exitosa')

def import_cascades(main_dir: pathlib.Path):
    face_cascades = cv2.CascadeClassifier(str(main_dir.joinpath(
    'models','haarcascade_frontalface_default.xml')))
    return face_cascades

def detect_faces(img, face_cascades: cv2.CascadeClassifier, draw_box: bool = True):
     # Convert image to grayscale
    
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascades.detectMultiScale(grayscale_img, scaleFactor=1.6)
    
    # Draw bounding box around detected faces
    for (x,y, width, height) in faces:
        if draw_box:
            cv2.rectangle(img, (x,y), (x+width, y+height),(0, 255,0),5)
        face_box = img[y:y+height, x:x+width]
        face_coords = [x,y,width,height]
        return img, face_box, face_coords
    
def write_on_frame(frame, text, text_x, text_y):
    (text_width, text_height) = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2)[0]
    box_coords = ((text_x, text_y), (text_x+text_width+20, text_y-text_height-20))
    cv2.rectangle(frame, box_coords[0], box_coords[1], (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, text, (text_x, text_y-10), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
    return frame