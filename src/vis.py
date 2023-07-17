import matplotlib.pyplot as plt
import numpy as np

def one_subject(subject_idx, X, Y):
    fig, ((ax1,ax2,ax3),(ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3,3,figsize=(10,10))
    subject_img_idx = np.where(Y==subject_idx)[0].tolist()

    for i, ax in enumerate([ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9]):
        img = X[subject_img_idx[i]]
        img = np.squeeze(img)
        ax.imshow(img, cmap='gray')
        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])
    plt.tight_layout()
    plt.show()
    
def subjects(X, Y, subs = range(10)):
    fig, ((ax1,ax2,ax3),(ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(
        3,3,figsize=(10,12))
    subject_img_idx = [np.where(Y==i)[0].tolist()[0] for i in subs]
    for i, ax in enumerate([ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9]):
        img = X[subject_img_idx[i]]
        img = np.squeeze(img)
        ax.imshow(img, cmap='gray')
        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title("Subject {}".format(i))
    plt.show()
    plt.tight_layout()