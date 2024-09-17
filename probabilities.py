import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import main 
import emcee
import emcee_run
from scipy import optimize

def gaussian(x,A,sigma,mu):
    #dist = (1/(np.sqrt(2*np.pi)*sigma))
    return A*np.exp(-0.5*((x-mu)**2/sigma**2))

df1 = pd.DataFrame(pd.read_csv("historico2022_2023.csv"))
df2 = pd.DataFrame(pd.read_csv("historico2023_2024.csv"))
df3 = pd.DataFrame(pd.read_csv("actual2024_2025.csv"))

nombres1 = main.Analysis(df1).TR.T.columns[:-1].to_numpy()
nombres2 = main.Analysis(df2).TR.T.columns[:-1].to_numpy()


def merge_accuracies(name: str):
    p1 = main.Analysis(df1).extract_accuracy(name)
    p2 = main.Analysis(df2).extract_accuracy(name)
    p3 = main.Analysis(df3).extract_accuracy(name)
    p3 = p3[~np.isnan(p3)]
    p = np.concatenate([p1,p2,p3])
    return p

def merge_accuracies_half(name:str):
    p1 = main.Analysis(df2).extract_accuracy(name)
    p2 = main.Analysis(df3).extract_accuracy(name)
    p2 = p2[~np.isnan(p2)]
    p = np.concatenate([p1,p2])
    return p


bines = np.linspace(0,1,15)
pR = merge_accuracies("Rodrigo")
countsR,binsR = np.histogram(pR,bins=bines)
pA = merge_accuracies("Angel")
countsA,binsA = np.histogram(pA,bins=bines)
pL = merge_accuracies("Liz")
countsL,binsL = np.histogram(pL,bins=bines)
pLe = merge_accuracies("Lety")
countsLe,binsLe= np.histogram(pLe,bins=bines)
pJu = merge_accuracies("Juvs")
countsJu,binsJu= np.histogram(pJu,bins=bines)
pF = merge_accuracies("Fer")
countsF,binsF=np.histogram(pF,bins=bines)
pP = merge_accuracies("Pao")
countsP,binsP = np.histogram(pP,bins=bines)

pG = merge_accuracies_half("Gabrielito")
countsG,binsG = np.histogram(pG,bins=bines)
pJA = merge_accuracies_half("Juan-Angel")
countsJA,binsJA = np.histogram(pJA,bins=bines)
pGa = merge_accuracies_half("Gaby")
countsGa,binsGa = np.histogram(pGa,bins=bines)
pM = merge_accuracies_half("Mickey")
countsM,binsM = np.histogram(pM,bins=bines)


#fL,errL = optimize.curve_fit(gaussian,binsL[:-1],countsL,p0=[5,0.04,0.7])
#fR,errR = optimize.curve_fit(gaussian,binsR[:-1],countsR,p0=[5,0.04,0.7])
#fF,errF = optimize.curve_fit(gaussian,binsF[:-1],countsF,p0=[5,0.04,0.7])

#x= np.linspace(0,1)
#plt.scatter(binsL[:-1],countsL,color="red")
#plt.scatter(binsR[:-1],countsR,color="blue")
#plt.scatter(binsF[:-1],countsF,color="green")
#plt.plot(x,gaussian(x,*fL),color="red")
#plt.plot(x,gaussian(x,*fR),color="blue")
#plt.plot(x,gaussian(x,*fF),color="green")
#plt.show()

def lnlike(params):
    AR,sigmaR,muR = params[0:3]
    AA,sigmaA,muA = params[3:6]
    AL,sigmaL,muL = params[6:9]
    ALe,sigmaLe,muLe = params[9:12]
    AJu,sigmaJu,muJu = params[12:15]
    AF,sigmaF,muF = params[15:18]
    AP,sigmaP,muP = params[18:21]
    AG,sigmaG,muG = params[21:24]
    AJA,sigmaJA,muJA = params[24:27]
    AGa,sigmaGa,muGa = params[27:30]
    AM,sigmaM,muM = params[30:33]
    deltaR = gaussian(binsR[:-1],AR,sigmaR,muR) - countsR
    deltaA = gaussian(binsA[:-1],AA,sigmaA,muA) - countsA
    deltaL = gaussian(binsL[:-1],AL,sigmaL,muL) - countsL
    deltaLe = gaussian(binsLe[:-1],ALe,sigmaLe,muLe) - countsLe
    deltaJu = gaussian(binsJu[:-1],AJu,sigmaJu,muJu) - countsJu
    deltaF = gaussian(binsF[:-1],AF,sigmaF,muF) - countsF 
    deltaP = gaussian(binsP[:-1],AP,sigmaP,muP) - countsP
    deltaG = gaussian(binsG[:-1],AG,sigmaG,muG) - countsG
    deltaJA = gaussian(binsJA[:-1],AJA,sigmaJA,muJA) - countsJA
    deltaGa = gaussian(binsGa[:-1],AGa,sigmaGa,muGa) - countsGa
    deltaM = gaussian(binsM[:-1],AM,sigmaM,muM) - countsM
    likk = -0.5*np.sum(deltaR**2+deltaA**2+deltaL**2+deltaLe**2+deltaJu**2+deltaF**2+deltaP**2+deltaG**2+deltaJA**2+deltaGa**2+deltaM**2)
    return likk

def lnprior(params):
    for i in range(0,11):
        if 0.0 < params[3*i] < 30.0 and 0.0 < params[3*i +1] < 10.0 and 0.0 < params[3*i+2] < 1.0:
            return 0.0
        return -np.inf


def lnprob(params):
    lp = lnprior(params)
    if not np.isfinite(lp):
        return -np.inf
    return lp + lnlike(params)

initial = 11*[10,0.04,0.7]
nwalkers = 70
p0 = [np.array(initial) + 1e-6 * np.random.randn(len(initial)) for i in range(nwalkers)]
backend = emcee.backends.HDFBackend("Backends/16Sept2024.h5")
sampler = emcee_run.run(p0,nwalkers,50000,len(initial),lnprob,backend=backend)









