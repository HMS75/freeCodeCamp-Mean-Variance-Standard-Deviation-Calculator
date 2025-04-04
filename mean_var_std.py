import numpy as np
def calculate(lst):
    if (len(lst)!=9):
        raise ValueError("List must contain nine numbers.")
    arr = np.array(lst).reshape((3,3))
    res = {
        #find "statistic" of axis1, axis2, and flatten it.
        'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).tolist()],
        'var': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).tolist()],
        'std': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).tolist()],
        'max': [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).tolist()],
        'min': [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).tolist()],
        'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).tolist()]
    }
    #return dictionary of required result
    return res
