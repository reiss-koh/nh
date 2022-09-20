import os
import csv
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.init as init
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch.autograd import Variable
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


class ConvAutoEncoder(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(ConvAutoEncoder, self).__init__()
        
        # Encoder
        self.cnn_layer1 = nn.Sequential(
                            nn.Conv1d(input_dim, 16, kernel_size=3, stride=1, padding=1),
                            nn.ReLU(),
                            nn.MaxPool1d(2,2))

        self.cnn_layer2 = nn.Sequential(
                            nn.Conv1d(16, 32, kernel_size=3, stride=1, padding=1),
                            nn.ReLU(),
                            nn.MaxPool1d(2,2))

        # Decoder
        self.tran_cnn_layer1 = nn.Sequential(
                            nn.ConvTranspose1d(32, 16, kernel_size = 2, stride = 2, padding=0),
                            nn.ReLU())

        self.tran_cnn_layer2 = nn.Sequential(
                            nn.ConvTranspose1d(16, output_dim, kernel_size = 2, stride = 2, padding=0),
                            nn.Sigmoid())
            
            
    def forward(self, x):
        output = self.cnn_layer1(x)
        # print(output.shape)
        output = self.cnn_layer2(output)
        # print(output.shape)
        output = self.tran_cnn_layer1(output)
        # print(output.shape)
        output = self.tran_cnn_layer2(output)
        # print(output.shape)

        return output

#Autoencoder에 넣어보기 위해 예시 csv 전처리
df = pd.read_csv('cus_ifo.csv')
df = df.iloc[:,3:]
del df['stk_pdt_hld_yn']
del df['ose_stk_pdt_hld_yn']
df = df.iloc[:, :-1]
df = df.truncate(df.index[0], df.index[50])

#tensor 변환
data = torch.tensor(df.values, dtype = torch.float32)

#convolutional layer input을 위한 transpose
transpose_input = torch.transpose(data,1,0)
input_dim = transpose_input.size(0)

#추후 최적화 때 실험할 output dimension 설정
output_dim = transpose_input.size(1)

#모델 통과
model = ConvAutoEncoder(input_dim, output_dim)
decoded = model(transpose_input)
transpose_output = torch.transpose(decoded,1,0)
print(transpose_output.shape)
transpose_output = transpose_output.detach().numpy()

#output dimension for T-SNE
output_dim_t_sne = 3
t_sne_model = TSNE(output_dim_t_sne)
t_sne_output = t_sne_model.fit_transform(transpose_output)

print(t_sne_output)
print(t_sne_output.shape)


