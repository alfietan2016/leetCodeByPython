# 验证回文字符串
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
# 输入: "A man, a plan, a canal: Panama"
# 输出: true

# 示例 2:
# 输入: "race a car"
# 输出: false

# # 超出时间限制
# def isPalindrome(s):
#     s1 = ''.join([x for x in s if x.isalpha()]).lower()
#     i = 0
#     l = len(s1)
#     mid = l//2
#     while i < mid:
#         print(i)
#         if s1[i] != s1[l-i-1]:
#             print(s1[i], s1[l-i-1])
#             return False
#         i += 1
#     return True

"""
利用双指针遍历
如果该元素为字母和数字，则比较，比较如果相等则比较下一位，不想等则返回失败
若不为字母和数字，则+1/-1，再进行比较
时间复杂度为O(n)， 空间复杂度为O(1)
"""
def isPalindrome(s):
    start = 0
    end = len(s)-1
    while start < end:
        if s[start].isalnum() and s[end].isalnum():
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        elif not s[start].isalnum():
            start += 1
        else:
            end -= 1
    return True


if __name__ == '__main__':
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    print(isPalindrome(s1) == True)
    print(isPalindrome(s2) == False)