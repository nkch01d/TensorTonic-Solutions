import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    arr = np.array(data, dtype=np.float64)
    if operation == "flatten":
        return arr.ravel()
    elif operation == "transpose":
        return np.transpose(arr)
    elif operation == "add_batch":
        return np.expand_dims(arr, axis=0)
