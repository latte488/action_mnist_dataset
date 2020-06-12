from torchvision import datasets
import os
import numpy as np

def load():
    root = 'data'
    if not os.path.exists(root):
        os.makedirs(root)
    train_dataset = datasets.MNIST(root=root, train=True, download=True)
    test_dataset = datasets.MNIST(root=root, train=False, download=True)
    return train_dataset, test_dataset

train_d, test_d = load()
image, label = train_d[0]
print(type(label))
image = np.array(image, dtype=np.uint8)
print(image.shape)
