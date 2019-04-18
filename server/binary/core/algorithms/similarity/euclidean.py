import numpy as np
from .util import dict_to_vector_decorator

@dict_to_vector_decorator
def euclidean_distance(vector_1, vector_2):
  return np.linalg.norm(vector_1 - vector_2)

@dict_to_vector_decorator
def euclidean(vector_1, vector_2):
  return 1 / (1 + euclidean_distance(vector_1, vector_2))

@dict_to_vector_decorator
def euclidean_norm(vector_1, vector_2):
  norm_sum = np.sqrt(np.square(np.linalg.norm(vector_1)) + np.square(np.linalg.norm(vector_2)))
  if norm_sum == 0:
    return 0
  return 1 - euclidean_distance(vector_1, vector_2) / norm_sum

@dict_to_vector_decorator
def euclidean_norm_2(vector_1, vector_2):
  norm_sum = np.linalg.norm(vector_1) + np.linalg.norm(vector_2)
  if norm_sum == 0:
    return 0
  return 1 - euclidean_distance(vector_1, vector_2) / norm_sum
