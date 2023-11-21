""""
 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 * 示例 1：
 *
 * 输入：n = 3
 * 输出：["((()))","(()())","(())()","()(())","()()()"]
 * 示例 2：
 *
 * 输入：n = 1
 * 输出：["()"]
 */"""
from typing import List

"""
    // 回溯算法，每次递归判断当前生成的字符串是否符合条件
    // 递归的两个终止条件：1、当右括号的数量大于左括号的数量时，退出，表示当前路径无法满足，返回至上一路径
    // 2、当左括号数量=右括号数量=题给条件n时，退出，说明当前已找到所有满足条件的括号对"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res_list = []
        res_str = ""
        self.back_track(n,0,0,res_list,res_str)
        return res_list

    # 递归主体
    def back_track(self,n,left,right,res_list:List[str],res_str:str):
        # 递归终止条件一：右括号数量大于左括号数量，该路径无效
        if right > left:
            return
        # 递归终止条件二：左右括号数量=给定数量，该路径走完，回溯到上一路径
        if left == right and left == n:
            res_list.append(res_str)
            return
        # 添加左括号
        if left < n:
            self.back_track(n,left + 1,right,res_list,res_str + "(")

        # 添加右括号
        if right < left:
            self.back_track(n,left,right + 1,res_list,res_str + ")")

if __name__ == "__main__":
    s =Solution()
    print(s.generateParenthesis(8))
