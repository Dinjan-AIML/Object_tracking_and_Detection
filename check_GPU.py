import tensorflow as tf
print(tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None))
print(tf.config.list_physical_devices('GPU'))


print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

print(tf.__version__)
import os
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
