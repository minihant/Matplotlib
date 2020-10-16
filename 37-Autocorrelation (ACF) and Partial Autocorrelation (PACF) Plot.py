# https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#1.-Scatter-plot
# ACF圖顯示了時間序列與其自身滯後的相關性。 每條垂直線（在自相關圖上）表示序列與從滯後0開始的滯後之間的相關性。
# 圖中的藍色陰影區域是顯著性水平。 那些位於藍線上方的滯後就是巨大的滯後。
# 那麼如何解釋呢？
# 對於AirPassengers，我們看到多達14個滯後時間已越過藍線，因此意義重大。 這意味著，距今已有14年之久的航空客運量對今天的客運量產生了影響。
# 另一方面，PACF顯示了任何給定的（時間序列）滯後與當前序列之間的自相關，但是去除了兩者之間的滯後。
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
# set the fontsize and some other elements
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
'legend.fontsize': med,
'figure.figsize': (16, 10),
'axes.labelsize': med,
'axes.titlesize': med,
'xtick.labelsize': med,
'ytick.labelsize': med,
'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")
#%matplotlib inline
# Print Version
print(mpl.__version__)
print(sns.__version__)
#-------------------------------------
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Import Data
df = pd.read_csv('data/AirPassengers.csv')

# Draw Plot
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(16,6), dpi= 80)
plot_acf(df.value.tolist(), ax=ax1, lags=50)
plot_pacf(df.value.tolist(), ax=ax2, lags=20)

# Decorate
# lighten the borders
ax1.spines["top"].set_alpha(.3); ax2.spines["top"].set_alpha(.3)
ax1.spines["bottom"].set_alpha(.3); ax2.spines["bottom"].set_alpha(.3)
ax1.spines["right"].set_alpha(.3); ax2.spines["right"].set_alpha(.3)
ax1.spines["left"].set_alpha(.3); ax2.spines["left"].set_alpha(.3)

# font size of tick labels
ax1.tick_params(axis='both', labelsize=12)
ax2.tick_params(axis='both', labelsize=12)
plt.show()