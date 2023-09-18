"""
 * 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
 *
 * 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
 * （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
 * 示例 1：
 *
 * 输入：s = "abc", t = "ahbgdc"
 * 输出：true
 * 示例 2：
 *
 * 输入：s = "axc", t = "ahbgdc"
 * 输出：false
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 1:
            return s[0] == t[0]
        short,long = 0,0
        while short < len(s) and long < len(t):
            if s[short] == t[long]:
                short += 1
            long += 1

        if short < len(s):
            return False
        else: return True