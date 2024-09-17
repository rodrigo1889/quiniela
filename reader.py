import numpy as np 
import emcee
import matplotlib.pyplot as plt 
np.random.seed(1001)
plt.style.use('style.mplstyle')

reader = emcee.backends.HDFBackend("Backends/16Sept2024.h5", read_only=True)
chains = reader.get_chain(flat=True)

ind = np.random.randint(len(chains),size=100)

def gaussian(x,A,sigma,mu):
    #dist = (1/(np.sqrt(2*np.pi)*sigma))
    return A*np.exp(-0.5*((x-mu)**2/sigma**2))

x = np.linspace(0,1)

fsize = 10
fig, ax = plt.subplots(4,3,figsize=(10,9))
for i in range(len(ind)):
    ax[0,0].plot(x,gaussian(x,A=chains[:,0][ind[i]],sigma=chains[:,1][ind[i]],mu=chains[:,2][ind[i]]),color="deepskyblue",alpha=0.1)
    ax[0,0].set_title("Rodrigo",fontsize=fsize)
    ax[0,1].plot(x,gaussian(x,A=chains[:,3][ind[i]],sigma=chains[:,4][ind[i]],mu=chains[:,5][ind[i]]),color="darkviolet",alpha=0.1)
    ax[0,1].set_title("Ángel",fontsize=fsize)
    ax[0,2].plot(x,gaussian(x,A=chains[:,6][ind[i]],sigma=chains[:,7][ind[i]],mu=chains[:,8][ind[i]]),color="hotpink",alpha=0.1)
    ax[0,2].set_title("Liz",fontsize=fsize)
    ax[1,0].plot(x,gaussian(x,A=chains[:,9][ind[i]],sigma=chains[:,10][ind[i]],mu=chains[:,11][ind[i]]),color="maroon",alpha=0.1)
    ax[1,0].set_title("Lety",fontsize=fsize)
    ax[1,1].plot(x,gaussian(x,A=chains[:,12][ind[i]],sigma=chains[:,13][ind[i]],mu=chains[:,14][ind[i]]),color="dimgray",alpha=0.1)
    ax[1,1].set_title("Juvs",fontsize=fsize)
    ax[1,2].plot(x,gaussian(x,A=chains[:,15][ind[i]],sigma=chains[:,16][ind[i]],mu=chains[:,17][ind[i]]),color="darkgoldenrod",alpha=0.1)
    ax[1,2].set_title("Fer",fontsize=fsize)
    ax[2,0].plot(x,gaussian(x,A=chains[:,18][ind[i]],sigma=chains[:,19][ind[i]],mu=chains[:,20][ind[i]]),color="cornflowerblue",alpha=0.1)
    ax[2,0].set_title("Pao",fontsize=fsize)
    ax[2,1].plot(x,gaussian(x,A=chains[:,21][ind[i]],sigma=chains[:,22][ind[i]],mu=chains[:,23][ind[i]]),color="khaki",alpha=0.1)
    ax[2,1].set_title("Gabriel",fontsize=fsize)
    ax[2,2].plot(x,gaussian(x,A=chains[:,24][ind[i]],sigma=chains[:,25][ind[i]],mu=chains[:,26][ind[i]]),color="blue",alpha=0.1)
    ax[2,2].set_title("Juan Ángel",fontsize=fsize)
    ax[3,0].plot(x,gaussian(x,A=chains[:,27][ind[i]],sigma=chains[:,28][ind[i]],mu=chains[:,29][ind[i]]),color="darkseagreen",alpha=0.1)
    ax[3,0].set_title("Gaby",fontsize=fsize)
    ax[3,1].plot(x,gaussian(x,A=chains[:,30][ind[i]],sigma=chains[:,31][ind[i]],mu=chains[:,32][ind[i]]),color="teal",alpha=0.1)
    ax[3,1].set_title("Mickey",fontsize=fsize)
for ax in ax.flat:
    ax.label_outer()
fig.suptitle("Simulaciones J2")
plt.show()
