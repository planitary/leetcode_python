from typing import List
import time


class DP:
    def fib_with_common(self, n):
        if n < 2:
            return 1
        else:
            return self.fib_with_common(n - 1) + self.fib_with_common(n - 2)

    def fib_with_dp(self,n):
        dp = [-1] * (n + 1)
        dp[0] = dp[1] = 1
        return self.with_dp(n,dp)

    def with_dp(self,n : int,dp_ll:List):
        if dp_ll[n] !=  -1:
            return dp_ll[n]
        else:
            dp_ll[n] = self.with_dp(n - 1,dp_ll) + self.with_dp(n - 2,dp_ll)
            return dp_ll[n]

x = DP()
start1 = time.perf_counter()
print(x.fib_with_common(15))
end1 = time.perf_counter()
elapsed = (end1 - start1) * 1e3
print("普通递归求斐波那契数列用时:%.4f毫秒" %elapsed)

start2 = time.perf_counter()
print(x.fib_with_dp(15))
end2 = time.perf_counter()
elapsed2 = (end2 - start2) * 1e3
print("动态规划求斐波那契数列用时:%.4f毫秒" %elapsed2)
