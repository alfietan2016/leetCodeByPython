# 存在重复
# 给定一个整数数组，判断是否存在重复元素。
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
#
# 示例 1:
# 输入: [1,2,3,1]
# 输出: true
#
# 示例 2:
# 输入: [1,2,3,4]
# 输出: false
#
# 示例 3:
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true

# """
# 双指针遍历，超出时间显示
# """
# def containsDuplicate(nums):
#     length = len(nums)
#     if length == 0 or length == 1:
#         return False
#     for i in range(length):
#         for j in range(i+1, length):
#             if nums[i] == nums[j]:
#                 print(i, j)
#                 return True
#     return False

"""
用set提取不重复的数组比较长度，长度一致时返回False，否则返回True
"""
def containsDuplicate(nums):
    length = len(nums)
    if length == 0 or length == 1:
        return False
    nums_set = set(nums)
    if len(nums_set) == length:
        return False
    else:
        return True


if __name__ == '__main__':
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums1) == True)
    print(containsDuplicate(nums2) == False)
    print(containsDuplicate(nums3) == True)