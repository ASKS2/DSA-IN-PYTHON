#For 3 digit numbers 

num = int(input("Enter the number to be checked as Armstrong number: "))
n = num
result = 0
while n>0:
  digit=n%10
  result=result+digit**3
  n=n//10

if result==num:
  print("It is a armstrong number!")
else:
  print("It is not a armstrong number!")




#For any digit of numbers

num = int(input("Enter the number to be checked as Armstrong number: "))
n = num
result = 0

num_digits = len(str(num))

while n > 0:
    digit = n % 10
    result = result + digit ** num_digits
    n = n // 10

if result == num:
    print("It is an Armstrong number!")
else:
    print("It is not an Armstrong number!")
