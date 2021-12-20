"""
date:20211209
describe:绘图
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
import math
import time


def PicSave(picPath="image", picName="defaultPic", figExtension="png", tight_layout=True, resolution=300):
    """
    describe：该函数用于保存图片，默认保存在当前目录。
    parameters：
    picPath: 保存图片的目录名称
    picName: 保存图片名字
    figExtension: 保存图片扩展名，如png
    tight_layout: 自动调整子图参数，使之填充整个图像区域
    resolution: 分辨率，默认取值300
    :return: “Picture Save Successfully!”
    """
    myPicPath = os.path.join('.', picPath)
    os.makedirs(myPicPath, exist_ok=True)
    print("Saving Picture : ", picName)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(os.path.join('.' + picPath + picName + '.' + figExtension), format=figExtension, dpi=resolution)
    print("Picture Save Successfully!")

class mySolution:

    # 定义问题参数
    def __init__(self, inputNMAX, inputZaShu, inputNeiJing, inputZaJianJU, inputDianLiu, inputCiDaoLiv, inputBeta, inputAlpha, inputTheta, inputR):
        self.NMAX = inputNMAX
        self.ZaShu = inputZaShu
        self.NeiJing = inputNeiJing
        self.ZaJianJiu = inputZaJianJU
        self.DianLiu = inputDianLiu
        self.CiDaoLiv = inputCiDaoLiv
        self.Beta = inputBeta
        self.Alpha = inputAlpha
        self.Theta = inputTheta
        self.R = inputR

    # 求解B
    def solution(self):
        BX = 0
        BY = 0
        BZ = 0
        for n in range(self.NMAX):
            t1 = (n - 0.5) * 2 * math.pi * self.ZaShu / self.NMAX

            a = self.ZaJianJiu * t1 / (2 * math.pi) + self.NeiJing
            temp = math.sqrt(pow((self.R * math.sin(self.Alpha) * math.cos(self.Theta) - a * math.sin(self.Beta) * math.cos(t1)), 2) +
                             pow((self.R * math.sin(self.Alpha) * math.sin(self.Theta) - a * math.sin(self.Beta) * math.sin(t1)), 2) +
                             pow((self.R * math.cos(self.Alpha) - a * math.cos(self.Beta)), 2))
            # otherParame = self.CiDaoLiv * self.DianLiu * a / 2 / self.NMAX
            BX = BX + ((self.R * math.cos(self.Alpha) - a * math.cos(self.Beta)) * a * math.sin(t1)) / pow(temp, 3)
            BY = BY + ((self.R * math.cos(self.Alpha)  - a * math.cos(self.Beta)) * a * math.cos(t1)) / pow(temp, 3)
            BZ = BZ +((self.R * math.sin(self.Alpha) * math.sin(self.Theta) - a * math.sin(self.Beta) * math.sin(t1))*(-1 * a * math.cos(t1)) -
                      (self.R * math.sin(self.Alpha) * math.cos(self.Theta) - a * math.sin(self.Beta) * math.cos(t1))*( a * math.sin(t1))) / pow(temp, 3)

        BX = BX * self.CiDaoLiv * self.DianLiu / 2 / self.NMAX
        BY = BY * self.CiDaoLiv * self.DianLiu / 2 / self.NMAX
        BZ = BZ * self.CiDaoLiv * self.DianLiu / 2 / self.NMAX
        # print(BX, BY, BZ)
        return BX, BY, BZ

inputNMAX = 3000
inputZaShu = 5
inputNeiJing = 0
inputZaJianJu = 0.002
inputDianLiu = 1000
inputCiDaoLv = 4*math.pi*1e-7
inputBeta = math.pi / 2 # 不变
inputAlpha = math.pi / 2 # 不变
inputTheta = math.pi / 2
inputR = 0.06
"""
直角坐标
"""
value = inputNeiJing + (inputZaShu + 2) * inputZaJianJu
print(value)
xMin = -1 * value
xMax = value
yMin = -1 * value
yMax = value
gridValue = 0.00005

X = []
Y = []
R = []
THETA = []
gridNumber = int((yMax - yMin) / gridValue + 1)
RESULT = []
B = []
# 取x值
timeA = time.time()
Time = 0
for index in range(gridNumber):
    xx = []
    yy = []
    bb = []
    tt = []

    x = xMin + index * gridValue + 0.00001
    for index1 in range(gridNumber):

        y = yMin + index1 * gridValue + 0.00001
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y, x)
        #print(x, y, theta, theta/math.pi*180)

        xx.append(x)
        yy.append(y)
        R.append(r)
        THETA.append(theta)

        # 直接计算


        inputTheta = theta
        inputR = r
        sh_solution = mySolution(inputNMAX, inputZaShu, inputNeiJing, inputZaJianJu, inputDianLiu, inputCiDaoLv,
                                 inputBeta, inputAlpha, inputTheta, inputR)
        result_x, result_y, result_z = sh_solution.solution()
        result = math.sqrt(result_x * result_x + result_y * result_y + result_z * result_z)

        result = math.log(result, 10)
        # print("x,y,r,theta,Bx_result, By_result, Bz_result, B_result : ", x, y, r, theta, result_x, result_y, result_z, result)
        del sh_solution
        RESULT.append([x, y, r, theta, result_x, result_y, result_z, result])

        bb.append(result)
        timeB = time.time()
        #print(x, y, theta)
        print("epoch : ", index * gridNumber + index1, " : ", gridNumber * gridNumber, "Time spend :", timeB - timeA)
    X.append(xx)
    Y.append(yy)
    B.append(bb)



"""# 极坐标
neijingMin = 0.00
rValue = 0.0005
neijingMax = 0.07 + rValue
PointInR = 5
rList = [float(index) * rValue for index in range(int(neijingMax / rValue))]
result = []
for r in rList:
    print("...................................")
    print("my r is : ", r)
    subResult = []
    for index in range(PointInR):
        theta = (index+1) * (2 * math.pi / PointInR)
        inputTheta = theta
        inputR = r
        sh_solution = mySolution(inputNMAX, inputZaShu, inputNeiJing, inputZaJianJu, inputDianLiu, inputCiDaoLv,
                                 inputBeta, inputAlpha, inputTheta, inputR)
        singleResult = sh_solution.solution()
        del sh_solution
        subResult.append(singleResult)
    result.append(subResult)

for index in range(len(result)):
    print("r : ", rList[index], " : ", result[index])
    

pointList = [(index + 1) for index in range(PointInR)]
"""


# 热图


"""for index in range(len(B)):

    for index1 in range(len(B[1])):
        B[index][index1] = B[index][index1]/maxValue"""

fig = plt.figure()
ax = fig.gca()
im = ax.imshow(B)
cb1 = plt.colorbar(im) # , fraction=0.02, pad=0.001

import matplotlib.ticker as ticker
tick_locator = ticker.MaxNLocator(nbins=10)  # colorbar上的刻度值个数
cb1.locator = tick_locator
cb1.update_ticks()
plt.show()

data = pd.DataFrame(data=RESULT, columns=["x", "y", "r", "theta", "result_x", "result_y", "result_z", "result"])
fig = plt.figure()
#创建3d绘图区域
ax = plt.axes(projection='3d')
ax.plot3D(data["x"], data["y"], data["result"])
ax.set_title('3D line plot')
plt.show()




