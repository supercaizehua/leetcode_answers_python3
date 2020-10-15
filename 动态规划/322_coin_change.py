from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass

class Solution1:
    def coinChange(self, coins: List[int], amount: int):

        # 定义：要凑出金额 n，至少要 dp(n) 个硬币
        def dp(n):
            # base case
            if n == 0: return 0
            if n < 0: return -1
            
            # 求最小值，初始化为正无穷大
            res = float('INF')
            
            # 做选择，选择需要硬币最少的那个结果
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解
                if subproblem == -1: continue

                res = min(res, 1 + subproblem)

            return res if res != float('INF') else -1

        # 题目要求的最终结果是 dp(amount)
        return dp(amount)

'''
优化，消除重叠子问题，添加一个备忘录dp table
'''

class Solution2:
    def coinChange(self, coins: List[int], amount: int):
        self.memo = dict()

        # 定义：要凑出金额 n，至少要 dp(n) 个硬币
        def dp(n):
            if n in self.memo: return self.memo[n]

            # base case
            if n == 0: return 0
            if n < 0: return -1
            
            # 求最小值，初始化为正无穷大
            res = float('INF')
            
            # 做选择，选择需要硬币最少的那个结果
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解
                if subproblem == -1: continue

                res = min(res, 1 + subproblem)

            self.memo[n] = res if res != float('INF') else -1

            return self.memo[n]

        # 题目要求的最终结果是 dp(amount)
        return dp(amount)

'''
dp 迭代解法
'''
class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [i + 1 for i in range(amount + 1)]
        dp[0] = 0
        size = len(dp)
        for i in range(size):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1 


if __name__ == '__main__':
    test1 = ([1,2,5], 11)
    test2 = ([2], 3)
    test3 = ([1], 0)
    test4 = ([1], 2)
    test5 = ([1,2,5,7], 500)
    print(Solution3().coinChange(*test5))