import os
os.environ["OMP_NUM_THREADS"] = '1'
import csv
import sys
from tqdm import tqdm
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.init as init
import torchvision.datasets as dset
import torchvision.transforms as transforms
from bonwoo import autoencoder
from bonwoo import conv_autoencoder
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.cluster import MiniBatchKMeans
from scipy.cluster.vq import vq
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt



class k_clustering():
    def __init__(self, dataframe, dim):
        self.df = dataframe
        self.df_values = self.df.values
        self.data = torch.tensor(self.df_values, dtype = torch.float32)
        self.dim = dim
    
    def preprocess_with_autoencoder(self, t_sne_dim, decoder_dim= None):
        #autoencoder input dimension
        input_dim = self.data.size(1)

        #output dimension 설정
        if decoder_dim != None:
            output_dim = decoder_dim
        else:
            output_dim = self.data.size(1)

        #모델 통과
        model = autoencoder.Autoencoder(input_dim, output_dim)
        output = model(self.data)
        print("autoencoder output shape:", output.shape)

        #tensor numpy로 변환
        output = output.detach().numpy()
        # print(output)

        #T-SNE로 차원 축소
        t_sne_model = TSNE(t_sne_dim)
        t_sne_output = t_sne_model.fit_transform(output)
        print("T-SNE output shape:", t_sne_output.shape)


        return t_sne_output


    def preprocess_with_conv_autoencoder(self, t_sne_dim, decoder_dim=None):
        #convolutional layer input을 위한 transpose
        transpose_input = torch.transpose(self.data,1,0)
        input_dim = transpose_input.size(0)

        #추후 최적화 때 실험할 output dimension 설정
        if decoder_dim != None:
            output_dim = decoder_dim
        else:
            output_dim = transpose_input.size(1)

        #모델 통과
        model = conv_autoencoder.ConvAutoEncoder(input_dim, output_dim)
        decoded = model(transpose_input)
        transpose_output = torch.transpose(decoded,1,0)
        print("Conv Autoencoder output shape:", transpose_output.shape)

        #Numpy 변환
        transpose_output = transpose_output.detach().numpy()

        #output dimension for T-SNE
        t_sne_model = TSNE(t_sne_dim)
        t_sne_output = t_sne_model.fit_transform(transpose_output)
        print("T-SNE output shape:", t_sne_output.shape)

        return t_sne_output
    
    def k_means_clustering(self, num_cluster, autoencoder_type):
        clustering_input = None
        if str(autoencoder_type) == ("linear" or "Linear"):
            clustering_input = self.preprocess_with_autoencoder(2)
        elif str(autoencoder_type) == ("conv" or "Conv"):
            clustering_input = self.preprocess_with_conv_autoencoder(2)
        else:
            assert autoencoder_type == "linear" or autoencoder_type == "conv"

        print("Clustering input dimension:", clustering_input.shape)

        k_means = KMeans(init= "k-means++", n_clusters = num_cluster)
        k_means.fit(clustering_input)
        cluster = k_means.predict(clustering_input)
        labels = k_means.labels_
        centers = k_means.cluster_centers_

        #Medoid 찾기
        closest, distances = vq(centers, clustering_input)
        print("Closest Medoid Indexs are", closest)

        #2차원인 경우 그래프 그리기
        if clustering_input.shape[1] == 2:
            fig = plt.figure(figsize=(6, 4))
            colors = plt.cm.Spectral(np.linspace(0, 1, len(set(labels))))
            graph = fig.add_subplot(1, 1, 1)

            for k, col, close_idx in zip(range(6), colors, closest):
                my_members = (labels == k)
                if my_members[close_idx] == True:
                    graph.plot(clustering_input[close_idx, 0], clustering_input[close_idx, 1], markerfacecolor=col, marker = 'h', markeredgecolor='b', markersize=20)
                graph.plot(clustering_input[my_members, 0], clustering_input[my_members, 1], mec ='k', mew= 0.5, markerfacecolor=col, marker='o', markersize = 5)
                # graph.plot(input_data[close_center, 0], input_data[close_center, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=20)

            graph.set_title('K-Means')
            graph.set_xticks(())
            graph.set_yticks(())
            plt.show()
    
    #실루엣 지수로 최적화
    def optimize_clustering(self, autoencoder_type):
        clustering_input = None
        if str(autoencoder_type) == ("linear" or "Linear"):
            clustering_input = self.preprocess_with_autoencoder(2)
        elif str(autoencoder_type) == ("conv" or "Conv"):
            clustering_input = self.preprocess_with_conv_autoencoder(2)
        else:
            assert autoencoder_type == "linear" or autoencoder_type == "conv"

        print("Clustering input dimension:", clustering_input.shape)

        best_num_cluster = 0
        best_silhouette_score = -1
        k_range = range(4,10)
        inertia_list = []
        for k in k_range:
            # k_means = MiniBatchKMeans(init="k-means++", n_clusters=k, n_init=5, random_state = 1, batch_size=5)
            k_means = KMeans(init="k-means++", n_clusters=k, random_state = 1)
            k_means.fit(clustering_input)
            cluster = k_means.predict(clustering_input)

            #silhouette score calculation
            score = silhouette_score(clustering_input, cluster)
            print('k:', k, "silhouette score:", score)

            inertia = k_means.inertia_
            inertia_list.append(inertia)

            if score > best_silhouette_score:
                best_num_cluster = k
                best_silhouette_score = score

        print("Best number of clusters:", best_num_cluster, "Score:", best_silhouette_score)

        return best_num_cluster

# plt.plot(k_range, inertia_list)
# plt.title('Elbow Method')
# plt.xlabel('Num clusters')
# plt.ylabel('Inertia')
# plt.show()

# input_data, _ = make_blobs(n_samples=15, random_state=1)

if __name__ == "__main__":
    #Autoencoder에 넣어보기 위해 예시 csv 전처리
    #최종 csv 파일을 read_csv만 하면 됨
    df = pd.read_csv('./reiss/cus_ifo.csv')
    df = df.iloc[:,3:]
    del df['stk_pdt_hld_yn']
    del df['ose_stk_pdt_hld_yn']
    df = df.iloc[:, :-1]
    df = df.truncate(df.index[0], df.index[100])

    model = k_clustering(df, 2)
    #parameter = "linear" or "conv"
    optimal_num_cluster = model.optimize_clustering('conv')
    # optimal_num_cluster = 5
    model.k_means_clustering(optimal_num_cluster, "conv")