def lcs(list_1, list_2, exact=False):
  m = len(list_1)
  n = len(list_2)

  L = [[None] * (n + 1) for i in range(m + 1)]

  if exact:
    result = 0
    for i in range(m + 1):
      for j in range(n + 1):
        if i == 0 or j == 0:
          L[i][j] = 0
        elif list_1[i - 1] == list_2[j - 1]:
          L[i][j] = L[i - 1][j - 1] + 1
          result = max(L[i][j], result)
        else:
          L[i][j] = 0
    return result
  else:
    for i in range(m + 1):
      for j in range(n + 1):
        if i == 0 or j == 0:
          L[i][j] = 0
        elif list_1[i - 1] == list_2[j - 1]:
          L[i][j] = L[i - 1][j - 1] + 1
        else:
          L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]
