def summ(sum,i,n):
  if i>n:
    print(sum)
    return
  summ(sum+i,i+1,n)


summ(0,1,4)

#..............................................


def funcc(n):
  if n==1:
    return 1
  return n +funcc(n-1)

funcc(10)