import tensorflow as tf

version = tf.__version__
# pu_ok = tf.test.is_gpu_available()
gpu_ok = tf.config.list_physical_devices("GPU")
print("tf version:", version, "\nGPU number", gpu_ok)
