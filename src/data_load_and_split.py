from tensorflow.keras.utils import img_to_array, load_img
import numpy as np
from pathlib import Path

def load_and_split(face_dir: Path):
    X_train, Y_train = [], []
    X_test, Y_test = [], []
    directories = sorted([f for f in face_dir.iterdir() if f.is_dir()])

    for idx, folder in enumerate(directories):
        files = sorted(face_dir.joinpath(folder.name).glob('*.pgm'))
        for file in files:
            img = load_img(file, color_mode='grayscale')
            img = img_to_array(img).astype('float32')/255
            if idx < 35:
                X_train.append(img)
                Y_train.append(idx)
            else:
                X_test.append(img)
                Y_test.append(idx)
                
    X_test = np.array(X_test)
    X_train = np.array(X_train)
    Y_test = np.array(Y_test)
    Y_train = np.array(Y_train)
    return X_test, Y_test, X_train, Y_train
    