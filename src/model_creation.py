from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from keras import backend as K
import random
import numpy as np

def create_shared_network(input_shape):
    model = Sequential(name='Shared_Conv_Network')
    model.add(Conv2D(filters=64,
                     kernel_size=(3,3),
                     activation='relu',
                     input_shape=input_shape))
    model.add(MaxPooling2D())
    model.add(Conv2D(filters=64,
                     kernel_size=(3,3),
                     activation='relu'))
    model.add(Flatten())
    model.add(Dense(units=128,
                    activation='sigmoid'))
    return model

def euclidean_distance(vectors):
    vector1, vector2 = vectors
    sum_square = K.sum(K.square(vector1-vector2), axis=1, keepdims=True)
    return K.sqrt(K.maximum(sum_square, K.epsilon()))



def create_pairs(X, Y, range_init, range_final):
    pairs, labels = [], []
    
    class_idx = [np.where(Y==i)[0] for i in range(range_init, range_final)]
    min_images = min(len(class_idx[i]) for i in range(range_final-range_init))

    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
    for c in range(range_final-range_init):
        for n in range(min_images):
            # Crate positive pair
            img1 = X[class_idx[c][n]]
            img2 = X[class_idx[c][random.choice(numeros[:n] + numeros[n+1:])]]
            pairs.append((img1,img2))
            labels.append(1)
            
            #create a negative pair
            #list of classes that are different from the current class
            neg_list = list(range(range_final-range_init))
            neg_list.remove(c)
            #select a random class from the negative list
            neg_c = random.sample(neg_list,1)[0]
            img3 = X[class_idx[neg_c][n]]
            pairs.append((img1,img3))
            labels.append(0)
    return np.array(pairs), np.array(labels)

def contrastive_loss(Y_true, D):
    Y_true = K.cast(Y_true, dtype='float32')
    margin = 1
    return K.mean(Y_true*K.square(D)+(1 - Y_true)*K.maximum((margin-D),0))

def accuracy(y_true, y_pred):
    return K.mean(K.equal(y_true, K.cast(y_pred < 0.5, y_true.dtype)))