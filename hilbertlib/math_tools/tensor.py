import numpy as np

class Tensor:
    def __init__(self, data):
        # Accept list or numpy array
        if isinstance(data, (list, tuple)):
            self.data = np.array(data)
        elif isinstance(data, np.ndarray):
            self.data = data
        else:
            raise TypeError("Data must be list, tuple, or numpy.ndarray")
    
    def shape(self):
        return self.data.shape
    
    def __add__(self, other):
        if isinstance(other, Tensor):
            return Tensor(self.data + other.data)
        else:
            return Tensor(self.data + other)
    
    def __sub__(self, other):
        if isinstance(other, Tensor):
            return Tensor(self.data - other.data)
        else:
            return Tensor(self.data - other)
    
    def __mul__(self, other):
        if isinstance(other, Tensor):
            # Element-wise multiplication
            return Tensor(self.data * other.data)
        else:
            # Scalar multiplication
            return Tensor(self.data * other)
    
    def matmul(self, other):
        if isinstance(other, Tensor):
            return Tensor(np.matmul(self.data, other.data))
        else:
            raise TypeError("matmul requires another Tensor")
    
    def reshape(self, *shape):
        return Tensor(self.data.reshape(shape))
    
    def transpose(self, *axes):
        if axes:
            return Tensor(self.data.transpose(axes))
        else:
            return Tensor(self.data.T)
    
    def sum(self, axis=None):
        return Tensor(self.data.sum(axis=axis))
    
    def __repr__(self):
        return f"Tensor(shape={self.data.shape}, data=\n{self.data})"