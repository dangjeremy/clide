import pandas as pd
import numpy as np
pd.set_option('display.float_format', lambda x: '%.2f' % x)
import matplotlib.pyplot as plt

# replace with the file of interest
temp = pd.read_csv("/Users/richi/Desktop/HCI/Empatica Data/1551881735_A0187D/TEMP.csv")
L = round(len(temp))
N = int(temp.iloc[0])
temp.drop(temp.index[:1], inplace=True)
temp["time"] = np.nan

for i in range(0, L, N):
    temp.time[i:i + 4] = float(list(temp)[0]) + i / 4

temp.columns = ['value', 'time']


marker = pd.read_csv("/Users/richi/Desktop/HCI/Empatica Data/1551881735_A0187D/tags.csv", header = None)
marker = round(marker)
marker = marker.iloc[:, 0].values.tolist()
print(marker)

xcoords = marker
for xc in xcoords:
    plt.axvline(x=xc)
plt.plot(temp.time, temp.value)
plt.show()


