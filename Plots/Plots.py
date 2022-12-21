#!/usr/bin/env python
# coding: utf-8

from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns

mpl.rcParams['text.usetex']=True 
mpl.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams.update({'font.size': 20})
mpl.rcParams["legend.framealpha"] = 1.0
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams["figure.figsize"] = [7.5, 4.5]

Data_1_electron = pd.read_csv('/home/felipe/JoaoPino/1-LQsCollider_project/Data_MadGraph/Data_MadGraph_Electrons_1.csv', sep=',')
Data_2_electron = pd.read_csv('/home/felipe/JoaoPino/1-LQsCollider_project/Data_MadGraph/Data_MadGraph_Electrons_2.csv', sep=',')
Data_3_electron = pd.read_csv('/home/felipe/JoaoPino/1-LQsCollider_project/Data_MadGraph/Data_MadGraph_Electrons_3.csv', sep=',')
Data_electron = pd.concat([Data_1_electron, Data_2_electron, Data_3_electron], axis=0)

Data_1_muon = pd.read_csv('/home/felipe/JoaoPino/1-LQsCollider_project/Data_MadGraph/Data_MadGraph_Muons_1.csv', sep=',')
Data_muon = pd.concat([Data_1_muon], axis=0)

plt.figure(figsize=(10.5, 4.5))
ax = plt.subplot(111)
xs = Data_electron['mS1']
ys = Data_electron['xsec_TChannel (fb)']
zs = Data_electron['mS2']
scat = ax.scatter(x=xs, y=ys, s=5.0, c=zs, marker="o", cmap="RdYlGn_r", rasterized=True)
colorb=plt.colorbar(scat,pad=0.05,fraction=0.2)
colorb.set_label(r'$\mathrm{M_{S_2}~(GeV)}$', fontsize=25)

### RUN-III sensitivity line ###
N = 1000
run_III = 1/300
sen_III = run_III*np.ones(N)
xline = np.linspace(1400, 10000, 1000)
run_III_xsec = ("$"+str(f"{run_III:.2e}").replace("e", "\\times 10^{")+"}$").replace("03", "3")

plt.text(7150,1.8*run_III,'({Xsec})~\\textbf{{Run-III}}'.format(Xsec = run_III_xsec),fontsize=17)
plt.plot(xline,sen_III,'--k')

### HL-LHC sensitivity line ###
N = 1000
run_HL = 1/3000
sen_HL = run_HL*np.ones(N)
xline = np.linspace(1400, 10000, 1000)
run_HL_xsec = ("$"+str(f"{run_HL:.2e}").replace("e", "\\times 10^{")+"}$").replace("04", "4")

plt.text(6950,0.2*run_HL,'({Xsec})~\\textbf{{HL-LHC}}'.format(Xsec = run_HL_xsec),fontsize=17)
plt.fill_between(x=xline,y1=0,y2=run_HL,alpha=0.5,color="#bad4d4")
plt.plot(xline,sen_HL,'--k')


plt.xlabel(r'$\mathrm{M_{S_1}~(GeV)}$')
plt.ylabel(r'$\sigma (qq\rightarrow e^+e^-)~(\mathrm{fb})$')
plt.yscale('log')
#plt.xscale('log')
plt.ylim([1e-7, 20])
plt.xlim([1000, 10000])
plt.grid()
ax.set_axisbelow(True)
#plt.show()
plt.tight_layout()
plt.savefig('/home/felipe/JoaoPino/1-LQsCollider_project/Plots/mS1_vs_xsecTchannel_mS2_electron.png', bbox_inches='tight', dpi=1000.0)
plt.savefig('/home/felipe/JoaoPino/1-LQsCollider_project/Plots/mS1_vs_xsecTchannel_mS2_electron.pdf', bbox_inches='tight', dpi=500.0)

plt.figure(figsize=(10.5, 4.5))
ax = plt.subplot(111)
xs = Data_electron['mS1']
ys = Data_electron['xsec_GluonSplit (fb)']
zs = Data_electron['mS2']
scat = ax.scatter(x=xs, y=ys, s=5.0, c=zs, marker="o", cmap="RdYlGn_r", rasterized=True)
colorb=plt.colorbar(scat,pad=0.05,fraction=0.2)
colorb.set_label(r'$\mathrm{M_{S_2}~(GeV)}$', fontsize=25)


### RUN-III sensitivity line ###
N = 1000
run_III = 1/300
sen_III = run_III*np.ones(N)
xline = np.linspace(1400, 10000, 1000)
run_III_xsec = ("$"+str(f"{run_III:.2e}").replace("e", "\\times 10^{")+"}$").replace("03", "3")

plt.text(7150,1.9*run_III,'({Xsec})~\\textbf{{Run-III}}'.format(Xsec = run_III_xsec),fontsize=17)
plt.plot(xline,sen_III,'--k')

### HL-LHC sensitivity line ###
N = 1000
run_HL = 1/3000
sen_HL = run_HL*np.ones(N)
xline = np.linspace(1400, 10000, 1000)
run_HL_xsec = ("$"+str(f"{run_HL:.2e}").replace("e", "\\times 10^{")+"}$").replace("04", "4")

plt.text(6950,0.15*run_HL,'({Xsec})~\\textbf{{HL-LHC}}'.format(Xsec = run_HL_xsec),fontsize=17)
plt.fill_between(x=xline,y1=0,y2=run_HL,alpha=0.5,color="#bad4d4")
plt.plot(xline,sen_HL,'--k')

plt.xlabel(r'$\mathrm{M_{S_1}~(GeV)}$')
plt.ylabel(r'$\sigma (gg\rightarrow 1b + 1b + e^+e^-)~\mathrm{(fb)}$')
plt.yscale('log')
#plt.xscale('log')
plt.ylim([1e-8, 20])
plt.xlim([1000, 10000])
plt.grid()
ax.set_axisbelow(True)
#plt.show()
plt.tight_layout()
plt.savefig('/home/felipe/JoaoPino/1-LQsCollider_project/Plots/mS1_vs_xsecGluonSplit_mS2_electron.png', bbox_inches='tight', dpi=1000.0)
plt.savefig('/home/felipe/JoaoPino/1-LQsCollider_project/Plots/mS1_vs_xsecGluonSplit_mS2_electron.pdf', bbox_inches='tight', dpi=500.0)

plt.figure(figsize=(10.5, 4.5))
ax = plt.subplot(111)
xs = Data_muon['mS1']
ys = Data_muon['xsec_TChannel (fb)']
zs = Data_muon['mS2']
scat = ax.scatter(x=xs, y=ys, s=5.0, c=zs, marker="o", cmap="RdYlGn_r", rasterized=True)
colorb=plt.colorbar(scat,pad=0.05,fraction=0.2)
colorb.set_label(r'$\mathrm{M_{S_2}~(GeV)}$', fontsize=25)

### RUN-III sensitivity line ###
N = 1000
run_III = 1/300
sen_III = run_III*np.ones(N)
xline = np.linspace(1400, 10000, 1000)
run_III_xsec = ("$"+str(f"{run_III:.2e}").replace("e", "\\times 10^{")+"}$").replace("03", "3")

plt.text(7150,1.9*run_III,'({Xsec})~\\textbf{{Run-III}}'.format(Xsec = run_III_xsec),fontsize=17)
plt.plot(xline,sen_III,'--k')

### HL-LHC sensitivity line ###
N = 1000
run_HL = 1/3000
sen_HL = run_HL*np.ones(N)
xline = np.linspace(1400, 10000, 1000)
run_HL_xsec = ("$"+str(f"{run_HL:.2e}").replace("e", "\\times 10^{")+"}$").replace("04", "4")

plt.text(6950,0.15*run_HL,'({Xsec})~\\textbf{{HL-LHC}}'.format(Xsec = run_HL_xsec),fontsize=17)
plt.fill_between(x=xline,y1=0,y2=run_HL,alpha=0.5,color="#bad4d4")
plt.plot(xline,sen_HL,'--k')


plt.xlabel(r'$\mathrm{M_{S_1}~(GeV)}$')
plt.ylabel(r'$\sigma (qq\rightarrow \mu^+\mu^-)$')
plt.yscale('log')
#plt.xscale('log')
plt.ylim([1e-7, 20])
plt.xlim([1000, 10000])
plt.grid()
ax.set_axisbelow(True)
#plt.show()
plt.tight_layout()
plt.savefig('/home/felipe/JoaoPino/1-LQsCollider_project/Plots/mS1_vs_xsecTchannel_mS2_muon.png', bbox_inches='tight', dpi=1000.0)
plt.savefig('/home/felipe/JoaoPino/1-LQsCollider_project/Plots/mS1_vs_xsecTchannel_mS2_muon.pdf', bbox_inches='tight', dpi=500.0)

plt.figure(figsize=(10.5, 4.5))
ax = plt.subplot(111)
xs = Data_muon['mS1']
ys = Data_muon['xsec_GluonSplit (fb)']
zs = Data_muon['mS2']
scat = ax.scatter(x=xs, y=ys, s=5.0, c=zs, marker="o", cmap="RdYlGn_r", rasterized=True)
colorb=plt.colorbar(scat,pad=0.05,fraction=0.2)
colorb.set_label(r'$\mathrm{M_{S_2}~(GeV)}$', fontsize=25)


### RUN-III sensitivity line ###
N = 1000
run_III = 1/300
sen_III = run_III*np.ones(N)
xline = np.linspace(1400, 10000, 1000)
run_III_xsec = ("$"+str(f"{run_III:.2e}").replace("e", "\\times 10^{")+"}$").replace("03", "3")

plt.text(7150,1.9*run_III,'({Xsec})~\\textbf{{Run-III}}'.format(Xsec = run_III_xsec),fontsize=17)
plt.plot(xline,sen_III,'--k')

### HL-LHC sensitivity line ###
N = 1000
run_HL = 1/3000
sen_HL = run_HL*np.ones(N)
xline = np.linspace(1400, 10000, 1000)
run_HL_xsec = ("$"+str(f"{run_HL:.2e}").replace("e", "\\times 10^{")+"}$").replace("04", "4")

plt.text(6950,0.15*run_HL,'({Xsec})~\\textbf{{HL-LHC}}'.format(Xsec = run_HL_xsec),fontsize=17)
plt.fill_between(x=xline,y1=0,y2=run_HL,alpha=0.5,color="#bad4d4")
plt.plot(xline,sen_HL,'--k')

plt.xlabel(r'$\mathrm{M_{S_1}~(GeV)}$')
plt.ylabel(r'$\sigma (gg\rightarrow 1b + 1b + \mu^+\mu^-)~\mathrm{(fb)}$')
plt.yscale('log')
#plt.xscale('log')
plt.ylim([1e-8, 2])
plt.xlim([1000, 10000])
plt.grid()
ax.set_axisbelow(True)
#plt.show()
plt.tight_layout()
plt.savefig('/home/felipe/JoaoPino/1-LQsCollider_project/Plots/mS1_vs_xsecGluonSplit_mS2_muon.png', bbox_inches='tight', dpi=1000.0)
plt.savefig('/home/felipe/JoaoPino/1-LQsCollider_project/Plots/mS1_vs_xsecGluonSplit_mS2_muon.pdf', bbox_inches='tight', dpi=500.0)