import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import main
import emcee
import plotter 


pas = pd.DataFrame(pd.read_csv("historico2023_2024.csv"))
antepas = pd.DataFrame(pd.read_csv("historico2022_2023.csv"))
actual = pd.DataFrame(pd.read_csv("actual2024_2025.csv"))

pp = plotter.Weekly(pas,antepas,actual)

pp.simple_plot("Mickey")
#pp.simple_plot("Rodrigo")
#pp.simple_plot("Fer")
#pp.simple_plot("Liz")
plt.legend()
plt.show()


#reader = emcee.backends.HDFBackend("Backends/4Sept2024.h5",read_only=True)
#chains = reader.get_chain(flat=True)

#np.random.seed(1001)
#ind = np.random.randint(len(chains),size=100)

#sample = chains[ind[0]]

#print(main.CreateMock(sample,jornada=1,maximos=maximos).fill())