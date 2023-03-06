class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        if 0 <= x <= 9: return True
        return True if str(x) == str(x)[::-1] else False


x = 1221

if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(x))
