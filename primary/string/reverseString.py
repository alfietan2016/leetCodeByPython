# 反转字符串
#
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
#
# 示例 1：
# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
#
# 示例 2：
# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]

"""
遍历一半的数组，首尾位置交换
时间复杂度为O(n/2),空间复杂度为O(1)
"""
def reverseString(s):
    l = len(s)
    for i in range(l//2):
        s[i], s[l-1-i] = s[l-1-i], s[i]
    return s


if __name__ == '__main__':
    s1 = ["h", "e", "l", "l", "o"]
    s2 = ["H", "a", "n", "n", "a", "h"]
    print(reverseString(s1) == ["o", "l", "l", "e", "h"])
    print(reverseString(s2) == ["h", "a", "n", "n", "a", "H"])