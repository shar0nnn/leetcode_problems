class Solution:
    def twoSum(self, nums, target):
        lst = []
        for i in range(len(nums)):
            temp = i + 1
            while temp < len(nums):
                res = nums[i] + nums[temp]
                if res == target:
                    lst.append(i)
                    lst.append(temp)
                    return lst
                else:
                    temp += 1


nums = [-1, -2, -3, -4, -5]
target = -8

if __name__ == "__main__":
    obj = Solution()
    print(obj.twoSum(nums, target))
