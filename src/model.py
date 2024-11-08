import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model

class AnomalyDetector(Model):
  
  def __init__(self):
    super(AnomalyDetector, self).__init__()
    
    self.encoder = tf.keras.Sequential([ 
      layers.Dense(1024, activation="relu"),
      layers.Dense(128, activation="relu"),
      layers.Dense(64, activation="relu"),
      layers.Dense(8, activation="relu")])

    self.decoder = tf.keras.Sequential([
      layers.Dense(64, activation="relu"),
      layers.Dense(128, activation="relu"),
      layers.Dense(1024, activation="relu"),
      layers.Dense(61440, activation="sigmoid")])
    

  def call(self, x):
    encoded = self.encoder(x)
    decoded = self.decoder(encoded)
    return decoded