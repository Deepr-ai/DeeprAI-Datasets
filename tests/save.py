# from compress_pickle import dump, load
# import pyndb
# pyndb.save_pickle = lambda obj, fn, *args: dump(obj, fn)  # pyndb will try to send HIGHEST_PROTOCOL
# pyndb.load_pickle = lambda fn, *args: load(fn)
# from keras.datasets import mnist
# import numpy as np
# db = pyndb.PYNDatabase("mnist.pyndb.gz", filetype="pickled")
# (train_X, train_y), (test_X, test_y) = mnist.load_data()
# x = []
# y = []
# print("Priming data")
# for i in range(60000):
#     x.append([item for sublist in train_X[i] for item in sublist])
#     y1 = [0,0,0,0,0,0,0,0,0,0]
#     y1[train_y[i]] = 1.0
#     y.append(y1)
# x1 = [[number / 1000 for number in sublist] for sublist in x]
#
# inputs = np.array(x1)
# expected = np.array(y)
# y_num = np.array(train_y)
#
# inputs = inputs.astype(np.float64)
# expected = expected.astype(np.float64)
# y_num = y_num.astype(np.float64)
# print("saving data")
#
# db.set("train_X", inputs)
# db.set("train_Y", expected)
# db.set("train_Y(num)", y_num)
# db.save()
# print("finished")
#
