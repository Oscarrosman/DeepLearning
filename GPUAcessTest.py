import numpy as np
import tensorflow as tf
import torch

def GPUAccessTest():
    '''
    Check access to GPU devices for TensorFlow and PyTorch, might only work on macOS.
    '''
    # Check for TensorFlow GPU access
    print(f"\nTensorFlow has access to the following devices:\n{tf.config.list_physical_devices()}")
    # See TensorFlow version
    print(f" > TensorFlow version: {tf.version}")
    print(f' > Pytorch version', torch.__version__)
    print(f' > Is MPS built? {torch.backends.mps.is_built()}')
    print(f' > Is MPS available? {torch.backends.mps.is_available()}')

    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f' > Using device: {device}\n')

    x = torch.rand(size=(3,4)).to(device)
    print(f" > Tensor: {x}")

