import torch
import torch.nn as nn
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_dim, num_heads, dropout = 0.1):
        super(MultiHeadAttention, self).__init__()
        self.hidden_dim = hidden_dim
        self.head_dim = hidden_dim // num_heads # (head_num * head_dim = hidden_dim)
        self.query = nn.Linear(hidden_dim, hidden_dim)
        self.key = nn.Linear(hidden_dim, hidden_dim)
        self.value = nn.Linear(hidden_dim, hidden_dim)
        self.dropout = nn.Dropout(dropout)
        self.heads_num = num_heads

    def forward(self, X, mask = None):
        batch, seq_len, dim = X.size()
        Q = self.query(X)
        K = self.key(X)
        V = self.value(X) #[b, s, h]

        # [b, s, h] --> [b, h_num, s, head_dim]
        q_state= Q.view(batch, seq_len, self.heads_num, self.head_dim).transpose(1, 2)
        k_state= K.view(batch, seq_len, self.heads_num, self.head_dim).transpose(1, 2)
        v_state= V.view(batch, seq_len, self.heads_num, self.head_dim).transpose(1, 2)

        attention = torch.matmul(
            q_state, k_state.transpose(-1, -2) #(b, head_num, s, head_dim) -> (b, head_num, head_dim, s)
        ) / math.sqrt(self.head_dim)
        if mask is not None:
            attention = attention.masked_fill(mask == 0, -1e9)
        print(attention)
        attention = self.dropout(attention)
        attention = torch.matmul(torch.softmax(attention, -1), v_state) # (b, head_num, s, head_dim)
        output = attention.transpose(1,2).contiguous() # (b, s, head_num, head_dim)
        output = output.view(batch, seq_len, dim) # (b, s, h)
        return output

mask = torch.tensor( #[b, s, s]
    [
        [0,1],
        [0,0],
        [1,1]
    ]
)
mask = mask.unsqueeze(1).unsqueeze(2).expand(3,8,2,2)
print(mask)
#mask = mask.unsqueeze(dim=1).repeat([1, 8, 1, 1])
X = torch.rand(3, 2, 128)
net = MultiHeadAttention(128, 8)
net(X, mask)
