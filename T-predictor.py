import torch
import torch.nn as nn
import torch.nn.functional as F
import dgl
from dgl.nn import GraphConv
import re


class AttentionModule(torch.nn.Module):
    def __init__(self, D):
        super(AttentionModule, self).__init__()
        self.args = D
        self.setup_weights()
        self.init_parameters()

    def setup_weights(self):
        self.weight_matrix = torch.nn.Parameter(torch.Tensor(self.args, self.args))

    def init_parameters(self):
        torch.nn.init.xavier_uniform_(self.weight_matrix)

    def forward(self, embedding):
        global_context = torch.mean(torch.matmul(embedding, self.weight_matrix), dim=0)
        transformed_global = torch.tanh(global_context)
        sigmoid_scores = torch.sigmoid(torch.mm(embedding, transformed_global.view(-1, 1)))
        representation = torch.mm(torch.t(embedding), sigmoid_scores)
        return representation


class GCN(nn.Module):
    def __init__(self, in_feats):
        super(GCN, self).__init__()
        self.conv1 = GraphConv(in_feats, 80)
        self.conv2 = GraphConv(80, 40)
        self.mlp1 = nn.Linear(40, 30)
        self.mlp2 = nn.Linear(30,10)
        self.mlp3 = nn.Linear(10, 1)
        self.attention = AttentionModule(40)

    def forward(self, g, in_feat):
        h = self.conv1(g, in_feat)
        h = F.relu(h)
        h = self.conv2(g, h)
        h = F.relu(h)
        h = self.attention(h)
        h = torch.reshape(h, (1, 40))
        h = self.mlp1(h)
        h = F.relu(h)
        h = self.mlp2(h)
        h = F.relu(h)
        h = self.mlp3(h)
        return h


def makegraph(n, c, z1, z2, v):
    v1 = []
    v2 = []
    feat = []
    for i in range(n):
        feat.append([])
        for j in range(50):
            feat[i].append(z1[i])
        for j in range(50):
            feat[i].append(0)
        for j in range(n):
            if j != i:
                v1.append(i)
                v2.append(j)
    current = n
    for i in range(n):
        for j in range(c[i]):
            feat.append([])
            for x in range(50):
                feat[current].append(z2[i])
            for x in range(50):
                feat[current].append(v[i][j])
            v1.append(i)
            v2.append(current)
            current += 1
    g = dgl.graph((v1, v2))
    g.ndata['feat'] = torch.Tensor(feat)
    return g


def train(model, n, mt, c, z1, z2, v, g, label):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
    features = g.ndata['feat']
    labels = torch.Tensor([label])
    pred = model(g, features)
    loss = F.mse_loss(labels, pred)
    pred = pred.item()
    train_acc = (label - pred) / ((pred + label) / 2)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    loss = loss.item()
    print('train acc: ' + str(train_acc) + ' pred: ' + str(pred) + "  loss: " + str(loss) + "  label: " + str(label))
    return train_acc


predictor = GCN(100)
best_acc = 0.0
f = open('tdata_dp.txt')
for i in range(370):
    z1 = []
    z2 = []
    c = []
    v = []
    n = int(f.readline())
    mt = int(f.readline())
    for j in range(n):
        c.append(0)
        v.append([])
        z1.append(0)
        z2.append(0)
        c[j], z1[j], z2[j] = map(int, f.readline().split())
        v[j] = list(map(int, f.readline().split()))
    lab = int(f.readline())
    print("Epoch " + str(i))
    args = [n, mt, c, z1, z2, v]
    graph = makegraph(args[0], args[2], args[3], args[4], args[5])
    tmp = train(predictor, args[0], args[1], args[2], args[3], args[4], args[5], graph, lab)
f.close()
