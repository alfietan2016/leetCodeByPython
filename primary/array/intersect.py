# 两个数组的交集 II
#
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
#
# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
#
# 说明：
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
#
# 进阶:
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？


# """
# 用新的字典将nums1储存，再遍历nums2数组，发现重复就-1，再存储到新的数组中
# 时间复杂度为O(n)，空间复杂度为O(n)
# """
# def intersect(nums1, nums2):
#     nums = []
#     dicts = {}
#     for num1 in nums1:
#         if num1 in dicts:
#             dicts[num1] += 1
#         else:
#             dicts[num1] = 1
#     for num2 in nums2:
#         if num2 in dicts and dicts[num2] != 0:
#             dicts[num2] -= 1
#             nums.append(nums2)
#     return nums

"""
用collections.Counter将数组变为字典，减少代码量
时间复杂度为O(n)，空间复杂度为O(n)
"""
import collections
def intersect(nums1, nums2):
    count = collections.Counter(nums1)
    res = []
    for num in nums2:
        if count[num] > 0:
            res.append(num)
            count[num] -= 1
    return res


if __name__ == '__main__':
    nums11 = [1, 2, 2, 1]
    nums12 = [2, 2]
    nums21 = [4, 9, 5]
    nums22 = [9, 4, 9, 8, 4]
    print(intersect(nums11, nums12) == [2, 2])
    print(intersect(nums21, nums22) == [4, 9])