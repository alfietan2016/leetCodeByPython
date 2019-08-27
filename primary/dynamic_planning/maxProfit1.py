# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
#
# 示例 2:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""
判断数组的长度，对空数组处理
一次遍历，min_price取遍历过程中的最小值（峰值最低点），求差值最大的max_price
时间复杂度为O(n)，空间复杂度O(1)
"""
def maxProfit(prices):
    max_price = 0
    l = len(prices)
    if l != 0:
        min_price = prices[0]
        for i in range(l):
            min_price = min(min_price, prices[i])
            max_price = max(max_price, prices[i]-min_price)
    return max_price


if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]
    print(maxProfit(prices1) == 5)
    print(maxProfit(prices2) == 0)

