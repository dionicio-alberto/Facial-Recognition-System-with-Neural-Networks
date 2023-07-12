from pathlib import Path
import sys
import cv2

CURRENT_DIR = Path('.').resolve()
MODULES_DIR = CURRENT_DIR.joinpath('src')
sys.path.append(str(MODULES_DIR))
DATA_DIR = CURRENT_DIR.joinpath('Data')

import face_detector 


if __name__ == '__main__':
    face_cascades = face_detector.import_cascades(CURRENT_DIR)

    files = DATA_DIR.joinpath('Sample Faces').glob('*.jpg')
    for file in files:
        img = cv2.imread(str(file))
        detected_faces, _, _ = face_detector.detect_faces(img, face_cascades)
        cv2.imwrite(str(DATA_DIR.joinpath('Detected',file.name)),detected_faces)




