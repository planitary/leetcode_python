from typing import List

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        next_ = ""
        phone = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        def back_track(next_,next_dig:str) -> None:
            if len(next_dig) == 0:
                res.append(next_)
            else:
                # 每次取出上一个迭代用完后剩下的序列
                new_ll = phone[next_dig[0]]
                for letter in new_ll:
                    # 比较完列表的当前值后，传入剩余的序列进行递归
                    back_track(next_ + letter,next_dig[1:])
        back_track(next_,digits)
        return res


s = Solution()
print(s.letterCombinations(""))