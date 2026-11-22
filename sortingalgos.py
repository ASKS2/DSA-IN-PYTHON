# Sorting algorithms in simple Python (no modules needed)
# Each function sorts the list it receives and returns it.


# 1. BUBBLE SORT
# Compare neighbours, swap if the left one is bigger.
# After each pass, the biggest item reaches the end.
# Time: O(n^2), best O(n) | Space: O(1) | Stable
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:          # no swaps -> already sorted
            break
    return arr


# 2. SELECTION SORT
# Find the smallest item in the unsorted part and put it in front.
# Time: O(n^2) always | Space: O(1) | Not stable
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr


# 3. INSERTION SORT
# Like arranging playing cards: take one item and insert it
# into its correct place in the sorted part on the left.
# Time: O(n^2), best O(n) | Space: O(1) | Stable
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]      # shift bigger items right
            j -= 1
        arr[j + 1] = key
    return arr


# 4. SHELL SORT
# Insertion sort on items that are 'gap' apart; keep halving the gap.
# Time: about O(n^1.5) | Space: O(1) | Not stable
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap = gap // 2
    return arr


# 5. MERGE SORT
# Divide the list in two halves, sort each half, then merge them.
# Time: O(n log n) always | Space: O(n) | Stable
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]       # add leftovers
    result += right[j:]
    return result


# 6. QUICK SORT
# Choose the last item as pivot. Put smaller items on its left,
# bigger on its right. Then repeat for both sides.
# Time: O(n log n) average, O(n^2) worst | Space: O(log n) | Not stable
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1                      # final position of pivot


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


# 7. HEAP SORT
# Build a max-heap (parent >= children), then repeatedly move
# the root (biggest) to the end and fix the heap.
# Children of index i are 2i+1 and 2i+2.
# Time: O(n log n) always | Space: O(1) | Not stable
def heapify(arr, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):    # build max-heap
        heapify(arr, n, i)
    for end in range(n - 1, 0, -1):        # move max to the end
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)
    return arr


# 8. COUNTING SORT  (non-negative integers only)
# Count how many times each value appears, then rebuild the list.
# Time: O(n + k), k = max value | Space: O(k)
def counting_sort(arr):
    if len(arr) == 0:
        return arr
    count = [0] * (max(arr) + 1)
    for x in arr:
        count[x] += 1
    result = []
    for value in range(len(count)):
        result += [value] * count[value]
    return result


# 9. RADIX SORT  (non-negative integers only)
# Sort by last digit, then tens digit, then hundreds... (using buckets).
# Time: O(d * n), d = number of digits | Space: O(n)
def radix_sort(arr):
    if len(arr) == 0:
        return arr
    place = 1
    while max(arr) // place > 0:
        buckets = [[] for _ in range(10)]
        for x in arr:
            digit = (x // place) % 10
            buckets[digit].append(x)
        arr = []
        for b in buckets:
            arr += b
        place *= 10
    return arr


# 10. BUCKET SORT
# Spread items into buckets by range, sort each bucket, join them.
# Works best when data is spread evenly.
# Time: O(n + k) average, O(n^2) worst | Space: O(n)
def bucket_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    low, high = min(arr), max(arr)
    if low == high:
        return arr
    buckets = [[] for _ in range(n)]
    for x in arr:
        index = (x - low) * (n - 1) // (high - low)
        buckets[index].append(x)
    result = []
    for b in buckets:
        result += insertion_sort(b)
    return result


# 11. COCKTAIL SORT
# Bubble sort that goes left->right, then right->left.
# Time: O(n^2), best O(n) | Space: O(1) | Stable
def cocktail_sort(arr):
    start, end = 0, len(arr) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1
        for i in range(end, start, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        start += 1
    return arr


# ---------------- Test all the sorts ----------------
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11, 90, 25, 3, 0, 47]
    print("Original :", data)

    algorithms = [bubble_sort, selection_sort, insertion_sort, shell_sort,
                  merge_sort, quick_sort, heap_sort, counting_sort,
                  radix_sort, bucket_sort, cocktail_sort]

    for sort in algorithms:
        result = sort(data[:])          # data[:] = copy, keeps original safe
        status = "OK" if result == sorted(data) else "WRONG"
        print(f"{sort.__name__:15} {result}  {status}")