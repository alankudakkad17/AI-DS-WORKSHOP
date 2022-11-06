import matplotlib.pyplot as mp 
import pandas as pd
import seaborn as sb
data = pd.read_csv("C:/Users/91956/Downloads/advertising.csv")
print(data.corr())
dataplot = sb.heatmap(data.corr(), cmap="YlGnBu", annot = True)
mp.show()
