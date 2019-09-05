# 加一
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

"""
定义plus_flag为1，从后面遍历，判断plus_flag为1，则+1，如果+1后的数值为10，则继续+1，否则plus_flag = 0
时间复杂度为O(n)，空间复杂度为O(1)
"""
def plusOne(digits):
    plus_flag = 1
    for i in range(len(digits)-1, -1, -1):
        if plus_flag == 1:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                plus_flag = 0
    if plus_flag == 1:
        digits.insert(0, 1)
    return digits


if __name__ == '__main__':
    digits1 = [1, 2, 3]
    digits2 = [4, 3, 2, 1]
    digits3 = [8, 9, 9, 9]
    digits4 = [9, 9, 9, 9]
    print(plusOne(digits1) == [1, 2, 4])
    print(plusOne(digits2) == [4, 3, 2, 2])
    print(plusOne(digits3) == [9, 0, 0, 0])
    print(plusOne(digits4) == [1, 0, 0, 0, 0])