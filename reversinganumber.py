
num = int(input("Enter the number you want to check: "))
n = num
# digit=0
result=0
while n>0:
  digit=n%10
  n=n//10
  result=result*10+digit

print(result)
  