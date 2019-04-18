import numpy as np
from .util import dict_to_vector_decorator

@dict_to_vector_decorator
def cosine(vector_1, vector_2, precision = 4):
  norm_1 = np.linalg.norm(vector_1)
  norm_2 = np.linalg.norm(vector_2)
  dot_product = np.matmul(vector_1.T, vector_2)
  norm_product = norm_1 * norm_2
  
  if norm_product == 0:
    sim = 0
  else:
    sim = dot_product / norm_product

  return round(sim, precision)

@dict_to_vector_decorator
def cosine_projection(vector_1, vector_2, precision = 4):
  norm_1 = np.linalg.norm(vector_1)
  norm_2 = np.linalg.norm(vector_2)

  norm_1_cos = norm_1 * cosine(vector_1, vector_2, precision = 4)

  norm_max = max(norm_1_cos, norm_2)

  if norm_max == 0:
    return 0

  return min(norm_1_cos, norm_2) / norm_max
