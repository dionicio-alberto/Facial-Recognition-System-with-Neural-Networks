from pathlib import Path
import sys
CURRENT_DIR = Path('.').resolve()


MODULES_DIR = CURRENT_DIR.joinpath('src')
sys.path.append(str(MODULES_DIR))
DATA_DIR = CURRENT_DIR.joinpath('Data')

print('va bien 1')

import cv2
video_capture = cv2.VideoCapture(0)

print('va bien 2')

import math
import face_detector

print('va bien 3')

fc_dir = CURRENT_DIR.joinpath(
    'models','haarcascade_frontalface_default.xml'
    )
face_cascades = face_detector.import_cascades(fc_dir)

print('va bien 4')

counter = 5

while True:
    _, frame = video_capture.read()
    frame, face_box, face_coords = face_detector.detect_faces(frame, face_cascades)
    text = 'Image will be taken in {}..'.format(math.ceil(counter))
    if face_box is not None:
        frame = face_detector.write_on_frame(frame, text, face_coords[0], face_coords[1]-10)
    cv2.imshow('Video',frame)
    cv2.waitKey(1)
    counter -= 0.1
    if counter <= 0:
        cv2.imwrite('true_img.png', face_box)
        break

print('va bien 5') 

video_capture.release()
cv2.destroyAllWindows()
print('Onboarding image capture')