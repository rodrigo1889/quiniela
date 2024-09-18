import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

        

class Weekly:
	def __init__(self,df1: pd.DataFrame, df2: pd.DataFrame, dfactual: pd.DataFrame):
		self.actual = dfactual
		self.a1 = df1
		self.a2 = df2
		self.a1.index = self.a1["Jugador"]
		self.a1 = self.a1.drop(labels=["Jugador","TOTAL","J0","COM","DIV","FC","SB","TOTAL"],axis=1)
		self.a2.index = self.a2["Jugador"]
		self.a2 = self.a2.drop(labels=["Jugador","TOTAL","J0","COM","DIV","FC","SB","TOTAL"],axis=1)
		self.actual.index = self.actual["Jugador"]
		self.actual = self.actual.drop(labels=["Jugador","J0","TOTAL","COM","DIV","FC","SB","TOTAL"],axis=1)
	

	def obtain_color(self,name: str):
		if name == "Rodrigo":
			return "deepskyblue"
		elif name == "Angel":
			return "darkviolet"
		elif name == "Liz":
			return "hotpink"
		elif name == "Lety":
			return  "maroon"
		elif name == "Juvs":
			return "orange"
		elif name == "Mickey":
			return "teal"
		elif name == "Gabrielito":
			return "yellow"
		elif name == "Gaby":
			return "darkseagreen"
		elif name == "Pao":
			return "cornflowerblue"
		elif name == "Fer":
			return "darkgoldenrod"
	

	def simple_plot(self,name: str):
		color = self.obtain_color(name)
		try:
			plt.plot(self.a2.T[name].index,self.a2.T[name].cumsum(),lw=1,color=color,alpha=0.7)
		except:
			pass 
		plt.plot(self.a1.T[name].index,self.a1.T[name].cumsum(),lw=1,color=color,label=name+" Histórico",alpha=0.3)
		plt.plot(self.actual.T[name].index,self.actual.T[name].cumsum(),color=color,lw=2,zorder=0)
		plt.scatter(self.actual.T[name].index,self.actual.T[name].cumsum(),color=color,edgecolor='black',zorder=1,label="Actual")


class Color_Picker:
    def __init__(self, name:str):
        self.name = name
    
    def pick(self):
    	if self.name == "Rodrigo":
    		return "lime"
    	if self.name == "Angel":
    		return "darkviolet"
    	if self.name == "Juvs":
    		return "dimgray"
    	if self.name == "Fer":
    		return "darkgoldenrod"
    	if self.name == "Pao":
    		return "cornflowerblue"
    	if self.name == "Gabrielito":
    		return "yellow"
    	if self.name == "Mickey":
    		return "teal"
    	if self.name == "Liz":
    		return "hotpink"
    	if self.name == "Lety":
    		return "maroon"
    	if self.name == "Juan-Angel":
    		return "blue"
    	if self.name == "Gaby":
    		return "darkseagreen"