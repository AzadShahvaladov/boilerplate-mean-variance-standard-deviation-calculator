import numpy as np

class ValueError(Exception):
    pass

def calculate(list):

    calculations = {'mean': [],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum': []
            }

    if(len(list) == 9):
        a = np.array(list).reshape(3, 3)
    else:
        raise ValueError('List must contain nine numbers.')

    calculations['mean'].append(np.mean(a, axis=0).tolist()), calculations['mean'].append(np.mean(a, axis=1).tolist()), calculations['mean'].append(np.mean(a).tolist())
    calculations['variance'].append(np.var(a, axis=0).tolist()), calculations['variance'].append(np.var(a, axis=1).tolist()), calculations['variance'].append(np.var(a).tolist())
    calculations['standard deviation'].append(np.std(a, axis=0).tolist()), calculations['standard deviation'].append(np.std(a, axis=1).tolist()), calculations['standard deviation'].append(np.std(a).tolist())
    calculations['max'].append(np.max(a, axis=0).tolist()), calculations['max'].append(np.max(a, axis=1).tolist()), calculations['max'].append(np.max(a).tolist())
    calculations['min'].append(np.min(a, axis=0).tolist()), calculations['min'].append(np.min(a, axis=1).tolist()), calculations['min'].append(np.min(a).tolist())
    calculations['sum'].append(np.sum(a, axis=0).tolist()), calculations['sum'].append(np.sum(a, axis=1).tolist()), calculations['sum'].append(np.sum(a).tolist())

    for key in calculations:
        print(key, ': ', calculations[key])
