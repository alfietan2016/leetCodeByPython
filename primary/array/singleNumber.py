# 只出现一次的数字
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
# 输入: [2,2,1]
# 输出: 1
#
# 示例 2:
# 输入: [4,1,2,1,2]
# 输出: 4

# """
# 使用额外空间实现
# 判断新数组s是否存在nums的数组，如果有则重复出现，把它删除，如果没有，则放进新数组
# 返回数组s[0]
# 时间复杂度为O(n),空间复杂度为O(n)
# """
# def singleNumber(nums):
#     length = len(nums)
#     if len(nums) == 1:
#         return nums[0]
#     if len(nums) == 2:
#         return -1
#     s = []
#     for i in range(length):
#         if nums[i] in s:
#             s.remove(nums[i])
#         else:
#             s.append(nums[i])
#     return s[0]

"""
排序后的数组，比较前后2个数，若相等，再比较后2个数
时间复杂度为O(n^2),空间复杂度为O(1)
"""
def singleNumber(nums):
    length = len(nums)
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return -1
    nums.sort()
    i = 0
    while i < length:
        if i == length-1:
            return nums[i]
        if nums[i] == nums[i+1]:
            i += 2
        else:
            return nums[i]


if __name__ == '__main__':
    nums1 = [2, 2, 1]
    nums2 = [4, 1, 2, 1, 2]
    print(singleNumber(nums1) == 1)
    print(singleNumber(nums2) == 4)