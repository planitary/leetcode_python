"""
给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
 *
 * 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
 *
 * 示例1:
 *
 * 输入: pattern = "abba", s = "dog cat cat dog"
 * 输出: true
 * 示例 2:
 *
 * 输入:pattern = "abba", s = "dog cat cat fish"
 * 输出: false
 * 示例 3:
 *
 * 输入: pattern = "aaaa", s = "dog cat cat dog"
 * 输出: false
"""
from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string:List = s.split(" ")
        s_map = {}
        pattern_map = {}
        if len(pattern) != len(string):
            return False
        for i in range(len(pattern)):
            # 如果当前pattern的字符和string都能在对应的字典中找到，则比较二者的值，不相等时直接返回false
            if pattern[i] in pattern_map and string[i] in s_map:
                if pattern_map.get(pattern[i]) != s_map.get(string[i]):
                    return False
            # 如果有一方没有找到，也返回false
            if pattern[i] in pattern_map and string[i] not in s_map:
                return False
            if pattern[i] not in pattern_map and string[i] in s_map:
                return False
            pattern_map[pattern[i]] = i
            s_map[string[i]] = i
        return True

if __name__ == "__main__":
    so = Solution()
    s = "dog cat fish"
    print(so.wordPattern("abc", s))


