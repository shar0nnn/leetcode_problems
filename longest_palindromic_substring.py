class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        start, max_len = 0, 1
        for i, value in enumerate(s):
            odd = s[i - max_len - 1: i + 1]
            even = s[i - max_len: i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
        return s[start: start + max_len]


s = ""
for i in range(1000):
    s += "g"

if __name__ == "__main__":
    obj = Solution()
    print(obj.longestPalindrome(s))
