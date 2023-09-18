"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        signDict = {
            "(":1,
            ")":-1,
            "[":2,
            "]":-2,
            "{":3,
            "}":-3
        }
        # 左括号入栈，右括号出栈，每次出栈的时候对比出栈元素与当前元素是否相同，这里比较绝对值
        valid_list = []
        for i in s:
            if i in ["(","[","{"]:
                valid_list.append(i)
            else:
                if valid_list is None or len(valid_list) == 0:
                    return False
                sign_in_stack = valid_list.pop()
                stack_value = signDict.get(sign_in_stack)
                value = signDict.get(i)
                if abs(value) != stack_value:
                    return False
        # 如果判断完了，栈内还有元素，则数量不匹配
        if len(valid_list) > 0:
            return False
        return True

s = Solution()
print(s.isValid("]"))