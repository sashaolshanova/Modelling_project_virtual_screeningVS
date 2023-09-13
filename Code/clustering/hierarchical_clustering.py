import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

#%%
distance_matrix = pd.read_excel("RMSDtable.xlsx", sheet_name='Sheet1', index_col=0)
type(distance_matrix)
print(distance_matrix.shape) #tuple (8,8)
print(distance_matrix.shape[0]) #first position of tuple (8,8), number of rows
print(distance_matrix.shape[1]) #second position of tuple (8,8), number of columns
#%%

def lower_tri_to_upper(lo_tri):
    for i in range(lo_tri.shape[0]):
        for j in range(lo_tri.shape[0]):
            if j < i:
                lo_tri.iloc[j,i] = lo_tri.iloc[i,j]
                lo_tri.iloc[i,j] = 0

    return lo_tri

mirror = lower_tri_to_upper(distance_matrix)
mirror
#%%

Z = linkage(mirror, 'single', optimal_ordering=False) # single, complete, ward, average, weighted, centroid, median
fig = plt.figure()
dn = dendrogram(Z, labels=mirror.columns)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('protein structure')
plt.ylabel('distance')
plt.xticks(rotation=45)
plt.show()

#%%
Z[1]
#%%
