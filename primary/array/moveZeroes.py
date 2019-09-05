# 移动零
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

# """
# 先统计出0的次数，再按次数删除0，再原数组后面加上相应的0
# 空间复杂度为O(1)，时间复杂度为O(n^2)
# """
# def moveZeroes(nums):
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             count += 1
#     for j in range(count):
#         nums.remove(0)
#     for k in range(count):
#         nums.append(0)
#     return nums

"""
遍历数组，使用j记录非0的位置，如果数组的值不为0，交互2个值的位置
时间复杂度为O(n)，空间复杂度为O(1)
"""
def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums


if __name__ == '__main__':
    nums1 = [0, 1, 0, 3, 12]
    nums2 = [0, 0, 1]
    print(moveZeroes(nums1) == [1, 3, 12, 0, 0])
    print(moveZeroes(nums2) == [1, 0, 0])