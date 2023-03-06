import numpy as np
import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from scipy.stats import entropy
from collections import Counter
IMG_PATH = "lab1_img4.png"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def my_entropy(vals):
    entrop = 0
    for i in vals:
        entrop += -vals[i]*math.log2(vals[i])
    print("Formula entropy: ", entrop)




if __name__ == "__main__":
    img = mpimg.imread(IMG_PATH)
    grayscale = rgb2gray(img)
    unique = {}
    n = len(grayscale) * len(grayscale[0])
    for i in grayscale:
        res = Counter(i)
        for j in res:
            if round(j) in unique:
                unique[round(j)] += res[j]
            else:
                unique.update({round(j):res[j]})
    for i in unique:
        unique[i] = unique[i]/n
    unique = dict(sorted(unique.items(),key=lambda x:x[0],reverse = False))


    arr = np.array([unique[i] for i in unique])
    my_entropy(unique)
    print("Build in function entropy:", entropy(pk=arr, base=2))
    plt.hist(grayscale)
    plt.show()