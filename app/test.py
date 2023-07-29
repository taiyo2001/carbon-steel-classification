
import numpy as np

APP_PATH = '/root'

datasets_npz_x1 = np.load(APP_PATH + '/dataset_npz/x.1_dataset/sc_x10_960_x1.npz')

datasets_npz_x1 = np.load('./../dataset_npz/x.3_dataset/x5/sc_x5_1.npz')

images = datasets_npz_x1['x']
labels = datasets_npz_x1['y']

print(images)
print(labels)

print("transpose_images shape: {}".format(images.shape))
