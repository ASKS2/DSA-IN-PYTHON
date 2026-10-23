# solution 1

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

for num in m:
    count=0
    for i in n:
        if i ==num:
            count+=1
    print(f"{num} occurs {count} times in the list")



    #soln2
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# Step 1: Build frequency array
hash_list = [0] * 11   # because max(n[i]) = 10
for i in n:
    hash_list[i] += 1

# Step 2: Answer queries in O(1)
for num in m:
    if num <= 10:   # within constraints
        print(f"{num} occurs {hash_list[num]} times")
    else:
        print(f"{num} occurs 0 times")
