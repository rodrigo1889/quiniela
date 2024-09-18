import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
plt.style.use("style.mplstyle")
import plotly.graph_objects as go
import plotter 



data = pd.DataFrame(pd.read_csv("Data/winningprob.csv"))
data.index = data["Jugador"]
data = data.drop(labels=["Jugador","COM","DIV","FC","SB","TOTAL"],axis=1)



fig = go.Figure()
for name in data.index.to_numpy():
	fig.add_trace(go.Scatter(x = data.T.index,y=data.T[name],name=name,
		line=dict(color=plotter.Color_Picker(name).pick(),width=3)))
fig.update_layout(title="Probabilidades de victoria en temporada regular",template="plotly_dark")
fig.show()


