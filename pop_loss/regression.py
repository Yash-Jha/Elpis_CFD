import tensorflow as tf
from tensorflow import keras

import numpy as np

dataset1 = tf.contrib.data.CsvDataset('API_EN.POP.DNST_DS2_en_csv_v2_10182003.csv',[['']], header=True, select_cols=[0])

iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()

with tf.Session() as sess:
    for i in range(10):
        value = sess.run(next_element)
        print(value)
