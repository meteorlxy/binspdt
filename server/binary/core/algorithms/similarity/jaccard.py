def jaccard(set_1, set_2):
  union = set_1 | set_2
  intersection = set_1 & set_2
  if len(union) == 0 or len(intersection) == 0:
    return 0
  return len(intersection) / len(union)

def jaccard_avg_length(set_1, set_2):
  intersection = set_1 & set_2
  if len(intersection) == 0:
    return 0
  return 2 * len(intersection) / (len(set_1) + len(set_2))
