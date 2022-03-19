"""
describe:DFT的原始计算方法
author:孙辉
Data：20211220
ref web：https://zhuanlan.zhihu.com/p/129641014
     https://www.jianshu.com/p/8e34331296c6
"""

import numpy as np
from matplotlib import pyplot as plt
def myDFT(inputSig, isPrintW=False):
    """
    输入：
        inputSig：指输入信号，我希望它是array格式。
        isPrintW：可以指定是否输出那个W矩阵
    输出：
        DFT计算出的结果
    """
    sigLen = len(inputSig)
    n = np.arange(0, sigLen).reshape(1, sigLen)

    k = n.reshape(sigLen, 1)

    base = np.exp(-1j * 2 * np.pi / sigLen)  # 基低

    w = np.dot(k, n)  # 指数矩阵

    W = base ** w  # W矩阵
    print(W)

    outputSig = np.dot(W, inputSig)
    if isPrintW:
        return outputSig, W
    else:
        return outputSig

N = 16
n = np.arange(N)
y = np.cos(2*np.pi*2*(n/N)+np.pi/3)+0.5*np.cos(2*np.pi*5*(n/N))




plt.stem(n, y) #茎叶图
plt.plot(n, y)
plt.show()

myDFT(y, isPrintW=True)

