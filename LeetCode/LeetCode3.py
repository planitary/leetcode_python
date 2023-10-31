"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
 *
 * 示例 1:
 *
 * 输入: s = ""abcabcbb""
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 * 示例 2:
 *
 * 输入: s = "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 * 示例 3:
 *
 * 输入: s = "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 *      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口，左指针固定，右指针开始遍历，遇到与左右指针包含的序列中相同的字符时，移动左指针至出现相同元素的后一个位置
        # 右指针继续移动，每次遇到重复的值时进行长度的计算，取每次对比的最大值
        left, right = 0, 1
        max_length = -1
        while right < len(s):
            sub_str: str = s[left:right]
            if s[right] in sub_str:
                # find函数查找子字符串的索引，find(sub,start,end)
                index = s.find(s[right], left)
                current_length = right - left
                max_length = max(max_length, current_length)
                left = index + 1
            right += 1

        max_length = max(max_length, len(s) - left)
        return max_length

    def common_lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i, j = 0, 1
        ll = []
        count = 0
        ll.append(s[0])
        while True:
            if j == len(s):
                count = max(len(ll), count)
                break
            if s[j] not in ll:
                ll.append(s[j])
                j += 1
            else:
                count = max(len(ll), count)
                i += 1
                j = i + 1
                ll.clear()
                ll.append(s[i])
        return count


if __name__ == "__main__":
    solution = Solution()
    s = "pwwkew"
    print(solution.common_lengthOfLongestSubstring(s))
