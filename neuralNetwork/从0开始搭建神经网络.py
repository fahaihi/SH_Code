
import numpy
import  scipy.special
import pandas as pd
from matplotlib import pyplot as plt
import time
# 定义神经网络类
class neuralNetwork:

    # 定义神经网络
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # 初始化输入节点，输出节点，隐藏节点和学习率
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate

        # 创建两个链接权重矩阵
        self.wih = (numpy.random.rand(self.hnodes, self.inodes) - 0.5)
        #输入节点和隐藏节点之间的权重矩阵，-0.5是为了初始值落在-0.5~0,。5范围
        self.who =(numpy.random.rand(self.onodes, self.hnodes) - 0.5)

        # 定义激活函数
        self.activation_function = lambda x: scipy.special.expit(x)

    # 训练神经网络
    def train(self, input_list, target_list):
        inputs = numpy.array(input_list, ndmin=2).T
        targets = numpy.array(target_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 根据误差更新权重
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0-final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))


    # 接受神经网络的输入，返回网络的输出
    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

if __name__ == "__main__":
    """input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3
    learning_rate = 0.5
    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)"""


    # 根据MNIST手写数字数据集组一些小测试
    """data_list = pd.read_csv("./mnist_test_10.csv", header=None)
    data_label = data_list[0]
    data_attribute = data_list.iloc[:, 1:]


    image_array = numpy.array(data_attribute.iloc[3]/259).reshape((28,28))
    plt.imshow(image_array, cmap='Greys', interpolation='None')
    plt.show()

    data_attribute = data_attribute/259 + 0.01   # 将输入数据归到0.01~1范围
    print(data_attribute)

    for index in range(len(data_attribute.iloc[4])):
        if data_attribute.iloc[4, index] > 0.9:
            print(data_attribute.iloc[4, index])"""

    input_nodes = 784
    hidden_nodes = 100
    output_nodes = 10
    learning_rate = 0.3

    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    # 训练神经网络
    training_data_file = open("mnist_train.csv", 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()

    """for record in training_data_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:]) / 255.0*0.99) + 0.01
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        print(targets)
        n.train(inputs, targets)"""

    # 测试神经网络
    test_data_file = open("mnist_test.csv", 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()
    """scorecard = []
    for record in test_data_list:
        print("**********************************")
        all_values = record.split(',')
        correct_label = int(all_values[0])
        print("correct label : ", correct_label)
        inputs = (numpy.asfarray(all_values[1:]) / 255.0*0.99) + 0.01
        outputs = n.query(inputs)
        label = numpy.argmax(outputs) # 返回最大数的索引
        print("predict answer : ", label)
        if (label == correct_label):
            scorecard.append(1)
        else:
            scorecard.append(0)

    scorecard_array = numpy.asarray(scorecard)

    print("*****************************")
    print("accuracy : ", scorecard_array.sum()/ scorecard_array.size)"""

    # 进行多次训练
    epochs = 40

    lr = [0.1, 0.2, 0.3, 0.4, 0.5]
    markList = ["p"]
    for lrIndex in lr:
        print("****************************************************************")
        print("lrIndex : ", lrIndex)
        input_nodes = 784
        hidden_nodes = 100
        output_nodes = 10
        learning_rate = lrIndex
        n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
        accList = []
        for e in range(epochs):

            timeA = time.time()
            print("**********************")
            print("epoch : ", e)
            print("training ......")
            scorecard = []
            for record in training_data_list:
                all_values = record.split(',')
                inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
                targets = numpy.zeros(output_nodes) + 0.01
                targets[int(all_values[0])] = 0.99
                n.train(inputs, targets)
            print("predicting ......")
            for record in test_data_list:
                all_values = record.split(',')
                correct_label = int(all_values[0])
                inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
                outputs = n.query(inputs)
                label = numpy.argmax(outputs)  # 返回最大数的索引
                if (label == correct_label):
                    scorecard.append(1)
                else:
                    scorecard.append(0)
            scorecard_array = numpy.asarray(scorecard)
            print("accuracy : ", scorecard_array.sum() / scorecard_array.size)
            print("time : ", time.time() - timeA)
            accList.append(scorecard_array.sum() / scorecard_array.size)
        x = [i + 1 for i in range(e + 1)]
        print(x)
        print(accList)
        plt.plot(x, accList, label="lr=" + str(lrIndex), linewidth=1.2)

    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.legend()
    plt.show()
    plt.savefig("myPic")






