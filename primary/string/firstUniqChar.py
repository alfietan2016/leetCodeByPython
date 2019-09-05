# 字符串中的第一个唯一字符
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 案例:
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.

"""
用一个字典存储s出现的字母及次数，然后遍历s，按顺序找到字典为1的值，返回序列
时间复杂度为O(2n),空间复杂度为O(n)
"""
def firstUniqChar(s):
    d = {}
    for s1 in s:
        if s1 in d:
            d[s1] += 1
        else:
            d[s1] = 1
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1



if __name__ == '__main__':
    s1 = "leetcode"
    s2 = "loveleetcode"
    print(firstUniqChar(s1) == 0)
    print(firstUniqChar(s2) == 2)