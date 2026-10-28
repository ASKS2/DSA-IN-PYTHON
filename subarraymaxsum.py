# Brute-force maximum contiguous subarray sum.
class maxi:
    def max_subarray_sum(self, nums):
        if not nums:
            raise ValueError("nums must not be empty")

        best = float("-inf")
        for start in range(len(nums)):
            total = 0
            for end in range(start, len(nums)):
                total += nums[end]
                best = max(best, total)
        return best


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxi().max_subarray_sum(nums))



#optimal solution using Kadane's algorithm
class Kadane:
    def max_subarray_sum(self, nums):
        if not nums:
            raise ValueError("nums must not be empty")

        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global   