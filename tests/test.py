from Datasets.BostonHousing import boston_housing as b
from deeprai import models

inputs = b.load_x()
expected = b.load_y()

network = models.FeedForward()

network.add_dense(13)

network.add_dense(5, activation="tanh")

network.add_dense(1)

# trains the model
network.train_model(input_data=inputs, verify_data=expected, batch_size=36)