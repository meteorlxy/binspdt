import re
import numpy as np
from ..asm import Module

def get_k_gram(seq, k):
  k_grams = set()
  if len(seq) >= k:
    for i in range(len(seq) - k + 1):
      k_grams.add(seq[i:i + k])
  return k_grams

def generate_birthmark(module, k):
  if not hasattr(module, 'k_gram_birthmark'):
    module.k_gram_birthmark = dict()
  if k not in module.k_gram_birthmark:
    birthmark = set()
    for function in module.functions.values():
      for basic_block in function.basic_blocks.values():
        mnemonic_seq = list()
        for inst in basic_block.instructions.values():
          mnemonic_seq.append(inst.mnemonic)
        birthmark = set.union(birthmark, get_k_gram(tuple(mnemonic_seq), k))
    module.k_gram_birthmark[k] = birthmark

def k_gram_similarity(birthmark_1, birthmark_2):
  intersection = set.intersection(birthmark_1, birthmark_2)
  sim = len(intersection) / len(birthmark_2)
  return sim

def analyse(db, module_1_id, module_2_id, k=3):
  # Generate K-Gram birthmark
  module_1 = Module(db=db, module_id=module_1_id).load().load_instructions()
  module_2 = Module(db=db, module_id=module_2_id).load().load_instructions()

  generate_birthmark(module_1, k)
  generate_birthmark(module_2, k)

  module_1.save(force=True)
  module_2.save(force=True)

  # Caculate K-Gram birthmark similarity
  similarity_1_to_2 = k_gram_similarity(module_1.k_gram_birthmark[k], module_2.k_gram_birthmark[k])
  similarity_2_to_1 = k_gram_similarity(module_2.k_gram_birthmark[k], module_1.k_gram_birthmark[k])

  # Generate result
  result = {
    'similarity_1_to_2': similarity_1_to_2,
    'similarity_2_to_1': similarity_2_to_1,
  }
  return result
