#%%
import tensorflow as tf
tf.debugging.set_log_device_placement(True)

gpus = tf.config.experimental.list_logical_devices('GPU')
if gpus:
  # 여러 GPU에 계산을 복제
  c = []
  for gpu in gpus:
    with tf.device(gpu.name):
      a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
      b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
      c.append(tf.matmul(a, b))

  with tf.device('/CPU:1'):
    matmul_sum = tf.add_n(c)

  print(matmul_sum)


#%%
from tensorflow.python.client import device_lib 

device_lib.list_local_devices()
