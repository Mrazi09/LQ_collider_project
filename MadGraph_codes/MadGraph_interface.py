#!/usr/bin/env python
# coding: utf-8

import random
import os
import shutil
import subprocess
import glob
import pandas as pd

#Generate runs for t-channel runs

#Number of runs
N_max = len(glob.glob("/home/felipe/JoaoPino/1-LQsCollider_project/Cards/*"))
#N = N_max
N = 10

#Number of events
nevents = 10000

#path to MadGraph folder
path_MadGraph = "/home/felipe/MG5_aMC_v2_7_2_py3"

#path to run folder
path_run = "/home/felipe/JoaoPino/1-LQsCollider_project/Events"

#path to MadGraph parameter cards
path_ParamCards = "/home/felipe/JoaoPino/1-LQsCollider_project/Cards"

#path to save Data
path_Data = "/home/felipe/JoaoPino/Data_MadGraph"

#proton beam energy
ebeam = (13.6/2) * 1e3

#Activate or deactivate full chain (MadGraph + Pythia8 + Delphes)
Full_chain = False

#Check if folder exists. If exists, delete contents
if os.path.exists("{path}".format(path = path_run)) == True:
    shutil.rmtree("{path}".format(path = path_run))
    os.makedirs("{path}".format(path = path_run))
elif os.path.exists("{path}".format(path = path_run)) == False:
    os.makedirs("{path}".format(path = path_run))
    

if os.path.exists("{path}".format(path = path_Data)) == True:
    shutil.rmtree("{path}".format(path = path_Data))
    os.makedirs("{path}".format(path = path_Data))
elif os.path.exists("{path}".format(path = path_Data)) == False:
    os.makedirs("{path}".format(path = path_Data))
    
#Generate scripts for running MadGraph
for idx in range(N):
    
    Card_path = "{path}/Events/LQ_T_channel_{index}/Cards".format(path = path_MadGraph, index = idx)
    
    s = open("./Events/Folder_commands_{}.sh".format(idx), "x")
    s.write("import model LQ_model -modelname \n")
    s.write("define j = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    s.write("define p = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    s.write("generate p p > e2 e2bar $$ a z \n")
    s.write("output Events/LQ_T_channel_{} \n".format(idx))
    s.write("exit \n")
    s.close()

    s = open("./Events/Scan_commands_{}.sh".format(idx), "x")
    if Full_chain == True:
        s.write("!cp {path}/pythia8_card_default.dat {path}/pythia8_card.dat \n".format(path = Card_path))
        s.write("!cp {path}/delphes_card_ATLAS.dat {path}/delphes_card.dat \n".format(path = Card_path))
        s.write("launch Events/LQ_T_channel_{} \n".format(idx))
        s.write("shower=Pythia8 \n")
        s.write("detector=Delphes \n")
        s.write("set nevents {} \n".format(nevents))
        s.write("set ebeam1 {} \n".format(ebeam))
        s.write("set ebeam2 {} \n".format(ebeam))
        s.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        s.write("set iseed {} \n".format(random.randint(0, 1e8)))
        s.write("0 \n")
        s.close()
    elif Full_chain == False:
        s.write("launch Events/LQ_T_channel_{} \n".format(idx))
        s.write("shower=OFF \n")
        s.write("detector=OFF \n")
        s.write("set nevents {} \n".format(nevents))
        s.write("set ebeam1 {} \n".format(ebeam))
        s.write("set ebeam2 {} \n".format(ebeam))
        s.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        s.write("set iseed {} \n".format(random.randint(0, 1e8)))
        s.write("0 \n")
        s.close()
    
    s = open("./Events/Production_commands_{}.sh".format(idx), "x")
    s.write("cd {} \n".format(path_MadGraph))
    s.write("./bin/mg5_aMC {path}/Folder_commands_{index}.sh \n".format(path = path_run, index = idx))
    s.write("cd {} \n".format(path_MadGraph))
    s.write("./bin/mg5_aMC {path}/Scan_commands_{index}.sh \n".format(path = path_run, index = idx))
    s.write("\n")
    s.write("cd {path}/Events/LQ_T_channel_{index}/bin \n".format(path = path_MadGraph, index = idx))
    s.write("./cleanall \n")
    s.write("cd {path}/Events/run_01 \n".format(path = path_MadGraph))
    s.write("find . -name \"*.hepmc.gz\" -type f -delete \n")
    s.write("find . -name \"*.hepmc\" -type f -delete \n")
    s.write("File=$(find . -name \"*.root\" -type f) \n")
    s.write("mv $File LQ_T_channel_{}.root \n".format(idx))
    s.close()

#Run MadGraph
Features = ['mS1', 'mS2', 'mR', 'xsec_TChannel']
df = pd.DataFrame(columns=Features)

for idx in range(N):
    subprocess.call(["bash", "{path}/Production_commands_{index}.sh".format(path = path_run, index = idx)])
    
    #Read run_tag file
    Output = open('{path}/Events/LQ_T_channel_{index}/Events/run_01/run_01_tag_1_banner.txt'.format(path = path_MadGraph, index = idx), 'r')
    run_tag = Output.readlines()  
    
    #Get cross-sections
    for j in run_tag:
        if j.__contains__('Integrated'):    
                for word in j.split():
                    try:
                        xsec_TChannel = float(word)
                    except ValueError:
                        pass    
    #Get masses
    for j in run_tag:
        if j.__contains__('ms1'):    
                for word in j.split():
                    try:
                        mS1 = float(word)
                    except ValueError:
                        pass
    
    for j in run_tag:
        if j.__contains__('ms2'):    
                for word in j.split():
                    try:
                        mS2 = float(word)
                    except ValueError:
                        pass
                
    for j in run_tag:
        if j.__contains__('mr'):    
                for word in j.split():
                    try:
                        mR = float(word)
                    except ValueError:
                        pass    
    
    MadGraph_data = [mS1, mS2, mR, xsec_TChannel]
    entry = pd.DataFrame([MadGraph_data], columns=Features)
    df = df.append(entry)
    df.to_csv('{path}/Data_MadGraph.csv'.format(path = path_Data),sep=',',index=False)


