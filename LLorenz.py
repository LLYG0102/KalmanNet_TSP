# 读出模拟的洛伦兹吸引子的数据，并画图显示
import os
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import torch

datafolder_path = 'Simulations/Lorenz_Atractor/data/'
data_path = os.path.join(datafolder_path, 'T100/data_lor_v20_rq020_T100.pt')
data = torch.load(data_path)
print(data[0].shape)
print(data[0][0, 0, :])
plot_data = data[0][0, :, :]
x = plot_data[0, :]
y = plot_data[1, :]
z = plot_data[2, :]
x = x.numpy().tolist()
y = y.numpy().tolist()
z = z.numpy().tolist()
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y, z)
plt.show()
