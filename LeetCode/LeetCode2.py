class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i,j = 0,1
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
                count = max(len(ll),count)
                i += 1
                j = i + 1
                ll.clear()
                ll.append(s[i])
        return count

s = Solution()
print(s.lengthOfLongestSubstring(""))