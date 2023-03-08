class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]

        least_word = str(min(strs, key=len))
        del strs[strs.index(least_word)]
        longest_prefix = ""
        i = 0

        for letter in least_word:
            for _, element in enumerate(strs):
                if letter == element[i]:
                    continue
                else:
                    return longest_prefix
            i += 1
            longest_prefix += letter
        return longest_prefix


strs = ['plow', 'flower', 'flight']

if __name__ == "__main__":
    obj = Solution()
    print(obj.longestCommonPrefix(strs))
