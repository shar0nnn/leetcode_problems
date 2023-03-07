class Solution(object):
    def addToArrayForm(self, num, k):
        str_temp = ""
        lst = []

        for n in num:
            str_temp += str(n)

        int_num = int(str_temp)
        res = int_num + k
        str_temp = str(res)

        for i in str_temp:
            lst.append(int(i))

        return lst


num = [2, 7, 4]
k = 181

if __name__ == "__main__":
    obj = Solution()
    print(obj.addToArrayForm(num, k))
