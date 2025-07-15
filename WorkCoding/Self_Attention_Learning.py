print("This is a self-attention training file")
import torch.nn as nn
import torch
import math
print("CUDA Torch Available ? :", torch.cuda.is_available())
# Video Source:https://www.bilibili.com/video/BV19YbFeHETz/?spm_id_from=333.1391.0.0&vd_source=eb551c153921514090609cb558dcd8bf

# 一、基础写法
class SelfAttentionV1(nn.Module):
    def __init__(self, hidden_dim: 728):
        super(SelfAttentionV1, self).__init__()
        self.hidden_dim = hidden_dim
        self.query_roj = nn.Linear(hidden_dim, hidden_dim)
        self.key_roj = nn.Linear(hidden_dim, hidden_dim)
        self.value_roj = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, X):
        # Attention(Q,K,V) = SOFTMAX(QK^T/sqrt(k))V
        # X--> [batch, seq_len, hidden_dim]
        Q = self.query_roj(X)
        K = self.key_roj(X)
        V = self.value_roj(X)
        attention_value = torch.matmul(Q, K.transpose(-1,-2))
        # attention_value --> [batch, seq_len, seq_len]
        attention_weight = torch.softmax(attention_value / math.sqrt(self.hidden_dim), dim = -1)
        # attention_weight = [batch, seq_len, seq_len]
        print("Attention Weight \n", attention_weight)
        output = torch.matmul(attention_weight, V)
        # output --> [batch, seq_len, hidden_dim]
        return output

X = torch.randn(1, 2, 2)
print(X)

self_att_net = SelfAttentionV1(2)
output = self_att_net(X)
print("*"*30, "\n", output)

# Question: 为什么注意力矩阵要除以根号k？
# Answer:   防止两个张量的乘积维度太大，造成梯度消失，因此缩放利于训练

# 二、效率优化
class SelfAttentionV2(nn.Module):
    def __init__(self, dim):
        super(SelfAttentionV2, self).__init__()
        self.dim = dim
        self.proj = nn.Linear(dim, dim * 3)

    def forward(self, X):
        QKV = self.proj(X) # [batch, seq, dim * 3]
        Q, K, V = torch.split(QKV, self.dim, dim=-1)
        atten_weight = torch.softmax( torch.matmul(Q, K.transpose(-1,-2)) / math.sqrt(self.dim), dim=-1)
        return torch.matmul(atten_weight, V)

self_att_net2 = SelfAttentionV2(2)
output = self_att_net2(X)
print("*"*30, "\n", output)


# 三、加入细节
## 细节1： dropout的位置
## 细节2： attention_mask
## 细节3： output_proj 的矩阵映射

class SelfAttentionV3(nn.Module):
    def __init__(self, dim, dropout_rate):
        super(SelfAttentionV3, self).__init__()
        self.dim = dim
        self.proj = nn.Linear(dim, dim * 3)
        self.attention_dropout = nn.Dropout(dropout_rate)
        self.out_proj = nn.Linear(dim, dim)
    def forward(self, X, attention_mask = None):
        QKV = self.proj(X)
        Q, K, V = torch.split(QKV, self.dim, dim=-1)
        attebtion_weight = torch.matmul(Q, K.transpose(-1, -2)) / math.sqrt(self.dim)
        if attention_mask is not None:
            attebtion_weight = attebtion_weight.masked_fill(
                attention_mask == 0, -1e9
            )
        attebtion_weight = torch.softmax(attebtion_weight, dim = -1)
        print("Attention Weight \n", attebtion_weight)
        attebtion_weight = self.attention_dropout(attebtion_weight)
        attention_res = torch.matmul(attebtion_weight, V)
        output = self.out_proj(attention_res)
        return output
print("v3"*20, "\n")
X = torch.randn(3, 4, 2)
mask = torch.tensor(
    [
        [1,1,1,0],
        [1,1,0,0],
        [1,1,0,0]
    ]
)
print(mask.shape) # [batch-size, seq-len]
mask = mask.unsqueeze(dim = 1).repeat(1, 4, 1)
print(mask.shape) # [batch_size, seq-len, seq-len]
self_att_net3 = SelfAttentionV3(2, 0.001)
output = self_att_net3(X, mask)
print("*"*30, "\n", output)

# 四、面试写法
class SelfAttentionInterview(nn.Module):
    def __init__(self, dim, dropout_rate):
        super(SelfAttentionInterview, self).__init__()
        self.dim = dim
        self.query_roj = nn.Linear(dim, dim) # 自带bias
        self.key_roj = nn.Linear(dim, dim)
        self.value_roj = nn.Linear(dim, dim)
        self.attention_dropout = nn.Dropout(dropout_rate)

    def forward(self, X, attention_mask = None):
        # X --> [batch, seq, hidden]
        Q = self.query_roj(X)
        K = self.key_roj(X)
        V = self.value_roj(X)
        attention_value = torch.matmul(Q, K.transpose(-1, -2)) / math.sqrt(self.dim)
        if attention_mask is not None:
            attention_value = attention_value.masked_fill(
                attention_mask == 0, -1e9
            )
        attention_weight = torch.softmax(attention_value, dim = -1)
        attention_weight = self.attention_dropout(attention_weight)
        output = torch.matmul(attention_weight, V)
        return output
x = torch.randn(3, 4, 2)
mask = torch.tensor(
    [[1, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0]]
)
mask = mask.unsqueeze(dim = 1).repeat(1, 4, 1)
net = SelfAttentionInterview(2, 0.001)
output = net(X, mask)
print("*"*30, "\n", output)