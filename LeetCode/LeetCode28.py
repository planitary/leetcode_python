"""
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。



示例 1：

输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
示例 2：

输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

butsd   ut
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        needle_size = len(needle)
        while start < len(haystack):
            # 每次从源字符串中找出长度与目标字符串相同的子串进行比对
            sub_str = haystack[start:needle_size + start]
            if sub_str == needle:
                return start
            else:
                start += 1
        return -1

s = Solution()
print(s.strStr("butsd", "sd"))