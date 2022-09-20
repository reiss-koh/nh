import os
import csv
import sys
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

class Autoencoder(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(Autoencoder,self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,32),
            nn.ReLU(),
            nn.Linear(32,16),
        )
        self.decoder = nn.Sequential(
            nn.Linear(16,32),
            nn.ReLU(),
            nn.Linear(32,64),
            nn.ReLU(),
            nn.Linear(64,128),
            nn.ReLU(),
            nn.Linear(128,output_dim),
            nn.Sigmoid(),
        )
                
    def forward(self,x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)  
        return decoded

#Autoencoder에 넣어보기 위해 예시 csv 전처리
df = pd.read_csv(f'{os.getcwd()}/reiss/cus_ifo.csv')
df = df.iloc[:,3:]
del df['stk_pdt_hld_yn']
del df['ose_stk_pdt_hld_yn']
df = df.iloc[:, :-1]
df = df.truncate(df.index[0], df.index[50])

#tensor 변환
data = torch.tensor(df.values, dtype = torch.float32)
input_dim = data.size(1)

#output dimension 설정
output_dim = data.size(1)

#모델 통과
model = Autoencoder(input_dim, output_dim)
output = model(data)
print(output.shape)
output = output.detach().numpy()

#output dimension for T-SNE
output_dim_t_sne = 2
t_sne_model = TSNE(output_dim_t_sne)
t_sne_output = t_sne_model.fit_transform(output)

print(t_sne_output)
print(t_sne_output.shape)
