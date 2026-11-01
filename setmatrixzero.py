
def markinf(matrix,row,colum):
  r = len(row)
  c = len(colum)
  for i in range(0,r):
    if matrix[i][colum] != 0:
      matrix[i][colum] = float("inf")
  for j in range(0,c):
    if matrix[row][j] != 0:
      matrix[i]= float("inf")

def setZeroes(matrix):
  row = []
  colum = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        row.append(i)
        colum.append(j)
  for i in range(len(row)):
    markinf(matrix,row[i],colum[i])
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == float("inf"):
        matrix[i][j] = 0