class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = 0

        while i < len(nums) - 1 - j:
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
                nums.append("_")
                i = 0
                j += 1
            else:
                i += 1

        if "_" in nums:
            return nums.index("_")
        return len(nums)


nums = [1, 1, 1, 1]

if __name__ == "__main__":
    obj = Solution()
    print(obj.removeDuplicates(nums))
