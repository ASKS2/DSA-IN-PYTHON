S = "azyyzyzaaaaa"
q = ["d", "a", "y", "z"]

# Step 1: Build frequency array
hash_list = [0] * 26   # 26 letters from 'a' to 'z'

for ch in S:
    ascii_val = ord(ch)       # get ASCII value
    index = ascii_val - 97    # shift so 'a' → 0, 'b' → 1, ..., 'z' → 25
    hash_list[index] += 1     # increment frequency

# Step 2: Answer queries in O(1)
for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(f"{ch} occurs {hash_list[index]} times")
