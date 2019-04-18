import numpy as np

def dict_to_vector(dict_1, dict_2):
  vector_1 = list()
  vector_2 = list()
  for k in dict_1.keys():
    vector_1.append(dict_1[k])
    if k in dict_2.keys():
      vector_2.append(dict_2[k])
    else:
      vector_2.append(0)

  for k in dict_2.keys():
    if k in dict_1.keys():
      continue
    vector_1.append(0)
    vector_2.append(dict_2[k])

  return vector_1, vector_2

def dict_to_vector_decorator(func):
  def wrapper(vector_1, vector_2, *args, **kwargs):
    if type(vector_1).__name__ == 'dict' and type(vector_2).__name__ == 'dict':
      vector_1, vector_2 = dict_to_vector(vector_1, vector_2)
    return func(np.array(vector_1), np.array(vector_2), *args, **kwargs)
  return wrapper
