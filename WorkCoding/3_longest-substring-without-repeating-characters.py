from collections import defaultdict

print("hello world! You Are The Best!")
# Describtion: 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
# 输入: s = "abcabcbb"
# 输出: 3

# 思路：滑动窗楼加字典的揭发
class solution:
    def longestSubstring(self, s: str) -> str:
        left = 0
        ans = 0
        cnt = defaultdict(int)
        for right, c in enumerate(s):
            cnt[c] += 1     # 统计词典中当前字符出现的次数
            while cnt[c] > 1:  # 当前窗口的值出现了重复, 要一直移出去
                cnt[s[left]] -= 1 # 移除左边窗口出现的value
                left += 1
            ans = max(ans, right - left + 1)
        return ans


slu = solution()
print(slu.longestSubstring("abcabcbb"))

