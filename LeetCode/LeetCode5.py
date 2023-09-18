"""给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_ss = s[0]
        if len(s) <= 1:
            return s
        # 双重遍历，如果字符串首尾字母相同，判断去掉首尾剩下的是否是回文
        for i in range(len(s)):
            for j in range(i + 1,len(s)):
                if s[j] == s[i]:
                    ss = s[i:j + 1]
                    # 如果是，判断长度，更新最大值
                    if self.is_palindrome(ss):
                        if len(ss) > len(max_ss):
                            max_ss = ss[:]
            # if i < len(s) - 1:
            #     ss = s[i + 1]



        return max_ss

    def is_palindrome(self,s : str):
        return s[::-1] == s


s = Solution()
print(s.longestPalindrome("bb"))