
def markinf(matrix,row,colum):
  r = len(row)
  c = len(colum)
  for i in range(0,r):
    if matrix[i][colum] != 0:
      matrix[i][colum] = float("inf")
  for j in range(0,c):
    if matrix[row][j] != 0:
      matrix[i]= float("inf")