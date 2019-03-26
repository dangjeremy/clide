import pandas as pd
import numpy as np
pd.set_option('display.float_format', lambda x: '%.2f' % x)


# rename to the file you want to read
#1551883614_A0187D
#1551885422_A0187D
#1551887085_A0187D
#1551879688_A0187D
#1551881735_A0187D

temp = pd.read_csv("/Users/richi/Desktop/HCI/Empatica Data/1551881735_A0187D/ACC.csv")
L = round(len(temp))
N = int(temp.iloc[0, 0])
print(N)
temp.drop(temp.index[:1], inplace=True)
temp["time"] = np.nan

for i in range(0, L, N):
    temp.time[i:i + N] = float(list(temp)[0]) + i / N

#temp.columns = ['value', 'time']
# for ACC
temp.columns = ['x', 'y', 'z', 'time']
print(temp.tail(20))

# rename
temp.to_csv("/Users/richi/Desktop/HCI/Empatica Data/1551881735_A0187D/ACC_withtime.csv", index=False)
