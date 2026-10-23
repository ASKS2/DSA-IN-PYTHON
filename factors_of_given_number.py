# my solution o(n)
num = int(input("Enter the number: "))
list=[]
for i in range(1,num+1):
  if num%i==0:
    list.append(i)
  else:
    continue

print(list)


#better soltion ( to reduce the time complexity)

num = int(input("Enter the number: "))
divisors = [1]  

for i in range(2, (num // 2) + 1):
    if num % i == 0:
        divisors.append(i)

divisors.append(num)  
print(divisors)


#optimal solution 


from math import sqrt

def get_divisors(num):
    result = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if num // i != i:  
                result.append(num // i)
    return sorted(result)
