
def shortestWay(source, target):
    def f(i, j):
        while i < m and j < n:
            if source[i] == target[j]:
                j += 1
            i += 1
        return j

    m, n = len(source), len(target)
    ans = j = 0
    while j < n:
        k = f(0, j)
        if k == j:
            return -1
        j = k
        ans += 1
    return ans
# 测试示例
source = "xyz"
target = "xzyxz"
print(shortestWay(source, target))