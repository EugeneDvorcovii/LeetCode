class Solution(object):
    def twoSum(self, nums, target):
        nums_copy = list()
        for elem in nums:
            nums_copy.append(elem)
        nums.sort()
        count_elem = len(nums)
        index_a, index_b = 0, count_elem - 1
        while True:
            num_a, num_b = nums[index_a], nums[index_b]
            if num_a + num_b > target:
                index_b -= 1
            elif num_a + num_b < target:
                index_a += 1
            else:
                index_true_a, index_true_b = nums_copy.index(num_a), count_elem - 1 - nums_copy[::-1].index(num_b)
                print(num_a, num_b)
                result = [index_true_a, index_true_b]
                result.sort()
                return result


a = Solution()
print(a.twoSum([3,3], 6))
