class Solution:
    def singleNonDuplicate(self, nums) -> int:
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]


nums = [1, 1, 4, 4, 10]

if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNonDuplicate(nums))
