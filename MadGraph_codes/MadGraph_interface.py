#!/usr/bin/env python
# coding: utf-8

import random
import os
import shutil
import subprocess
import glob
import pandas as pd

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
path_Data = "/home/felipe/JoaoPino/1-LQsCollider_project/Data_MadGraph"

#proton beam energy
ebeam = (13.6/2) * 1e3

#Activate or deactivate full chain (MadGraph + Pythia8 + Delphes)
Full_chain = False

#Run which topology
Cond_GluonSplit_BB = False
Cond_GluonSplit_BC = True
Cond_GluonSplit_BS = True
Cond_TChannel = False

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
    
    Card_path_TChannel = "{path}/Events/LQ_T_channel_{index}/Cards".format(path = path_MadGraph, index = idx)
    Card_path_GluonSplit = "{path}/Events/LQ_GluonSplit_channel_{index}/Cards".format(path = path_MadGraph, index = idx)
    Card_path_GluonSplit_bc = "{path}/Events/LQ_GluonSplitBC_channel_{index}/Cards".format(path = path_MadGraph, index = idx)
    Card_path_GluonSplit_bs = "{path}/Events/LQ_GluonSplitBS_channel_{index}/Cards".format(path = path_MadGraph, index = idx)
    
    Tchannel = open("./Events/F_Tchannel_{}.sh".format(idx), "x")
    Tchannel.write("import model LQ_model -modelname \n")
    Tchannel.write("define j = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    Tchannel.write("define p = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    Tchannel.write("generate p p > e2 e2bar $$ a z h \n")
    Tchannel.write("output Events/LQ_T_channel_{} \n".format(idx))
    Tchannel.write("exit \n")
    Tchannel.close()
    
    GluonSplit = open("./Events/F_GluonSplit_{}.sh".format(idx), "x")
    GluonSplit.write("import model LQ_model -modelname \n")
    GluonSplit.write("define j = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    GluonSplit.write("define p = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    GluonSplit.write("generate p p > e2 e2bar d3 d3bar $$ a z h \n")
    GluonSplit.write("output Events/LQ_GluonS_channel_{} \n".format(idx))
    GluonSplit.write("exit \n")
    GluonSplit.close()
    
    GluonSplit_BC = open("./Events/F_GluonSplit_BC_{}.sh".format(idx), "x")
    GluonSplit_BC.write("import model LQ_model -modelname \n")
    GluonSplit_BC.write("define j = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    GluonSplit_BC.write("define p = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    GluonSplit_BC.write("generate p p > e2 e2bar d3 u2bar $$ a z h \n")
    GluonSplit_BC.write("output Events/LQ_GluonS_BC_channel_{} \n".format(idx))
    GluonSplit_BC.write("exit \n")
    GluonSplit_BC.close()
    
    GluonSplit_BS = open("./Events/F_GluonSplit_BS_{}.sh".format(idx), "x")
    GluonSplit_BS.write("import model LQ_model -modelname \n")
    GluonSplit_BS.write("define j = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    GluonSplit_BS.write("define p = u1 u1bar u2 u2bar d1 d1bar d2 d2bar g \n")
    GluonSplit_BS.write("generate p p > e2 e2bar d3 d2bar $$ a z h \n")
    GluonSplit_BS.write("output Events/LQ_GluonS_BS_channel_{} \n".format(idx))
    GluonSplit_BS.write("exit \n")
    GluonSplit_BS.close()

    Tchannel = open("./Events/S_Tchannel_{}.sh".format(idx), "x")
    GluonSplit = open("./Events/S_GluonSplit_{}.sh".format(idx), "x")
    GluonSplit_BC = open("./Events/S_GluonSplit_BC_{}.sh".format(idx), "x")
    GluonSplit_BS = open("./Events/S_GluonSplit_BS_{}.sh".format(idx), "x")
    
    if Full_chain == True:
        Tchannel.write("!cp {path}/pythia8_card_default.dat {path}/pythia8_card.dat \n".format(path = Card_path_TChannel))
        Tchannel.write("!cp {path}/delphes_card_ATLAS.dat {path}/delphes_card.dat \n".format(path = Card_path_TChannel))
        Tchannel.write("launch Events/LQ_T_channel_{} \n".format(idx))
        Tchannel.write("shower=Pythia8 \n")
        Tchannel.write("detector=Delphes \n")
        Tchannel.write("set nevents {} \n".format(nevents))
        Tchannel.write("set ebeam1 {} \n".format(ebeam))
        Tchannel.write("set ebeam2 {} \n".format(ebeam))
        Tchannel.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        Tchannel.write("set iseed {} \n".format(random.randint(0, 1e8)))
        Tchannel.write("0 \n")
        Tchannel.close()
        
        GluonSplit.write("!cp {path}/pythia8_card_default.dat {path}/pythia8_card.dat \n".format(path = Card_path_GluonSplit))
        GluonSplit.write("!cp {path}/delphes_card_ATLAS.dat {path}/delphes_card.dat \n".format(path = Card_path_GluonSplit))
        GluonSplit.write("launch Events/LQ_GluonS_channel_{} \n".format(idx))
        GluonSplit.write("shower=Pythia8 \n")
        GluonSplit.write("detector=Delphes \n")
        GluonSplit.write("set nevents {} \n".format(nevents))
        GluonSplit.write("set ebeam1 {} \n".format(ebeam))
        GluonSplit.write("set ebeam2 {} \n".format(ebeam))
        GluonSplit.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        GluonSplit.write("set iseed {} \n".format(random.randint(0, 1e8)))
        GluonSplit.write("0 \n")
        GluonSplit.close()
        
        GluonSplit_BC.write("!cp {path}/pythia8_card_default.dat {path}/pythia8_card.dat \n".format(path = Card_path_GluonSplit_bc))
        GluonSplit_BC.write("!cp {path}/delphes_card_ATLAS.dat {path}/delphes_card.dat \n".format(path = Card_path_GluonSplit_bc))
        GluonSplit_BC.write("launch Events/LQ_GluonS_BC_channel_{} \n".format(idx))
        GluonSplit_BC.write("shower=Pythia8 \n")
        GluonSplit_BC.write("detector=Delphes \n")
        GluonSplit_BC.write("set nevents {} \n".format(nevents))
        GluonSplit_BC.write("set ebeam1 {} \n".format(ebeam))
        GluonSplit_BC.write("set ebeam2 {} \n".format(ebeam))
        GluonSplit_BC.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        GluonSplit_BC.write("set iseed {} \n".format(random.randint(0, 1e8)))
        GluonSplit_BC.write("0 \n")
        GluonSplit_BC.close()
        
        GluonSplit_BS.write("!cp {path}/pythia8_card_default.dat {path}/pythia8_card.dat \n".format(path = Card_path_GluonSplit_bs))
        GluonSplit_BS.write("!cp {path}/delphes_card_ATLAS.dat {path}/delphes_card.dat \n".format(path = Card_path_GluonSplit_bs))
        GluonSplit_BS.write("launch Events/LQ_GluonS_BS_channel_{} \n".format(idx))
        GluonSplit_BS.write("shower=Pythia8 \n")
        GluonSplit_BS.write("detector=Delphes \n")
        GluonSplit_BS.write("set nevents {} \n".format(nevents))
        GluonSplit_BS.write("set ebeam1 {} \n".format(ebeam))
        GluonSplit_BS.write("set ebeam2 {} \n".format(ebeam))
        GluonSplit_BS.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        GluonSplit_BS.write("set iseed {} \n".format(random.randint(0, 1e8)))
        GluonSplit_BS.write("0 \n")
        GluonSplit_BS.close()
        
    elif Full_chain == False:
        Tchannel.write("launch Events/LQ_T_channel_{} \n".format(idx))
        Tchannel.write("shower=OFF \n")
        Tchannel.write("detector=OFF \n")
        Tchannel.write("set nevents {} \n".format(nevents))
        Tchannel.write("set ebeam1 {} \n".format(ebeam))
        Tchannel.write("set ebeam2 {} \n".format(ebeam))
        Tchannel.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        Tchannel.write("set iseed {} \n".format(random.randint(0, 1e8)))
        Tchannel.write("0 \n")
        Tchannel.close()
        
        GluonSplit.write("launch Events/LQ_GluonS_channel_{} \n".format(idx))
        GluonSplit.write("shower=OFF \n")
        GluonSplit.write("detector=OFF \n")
        GluonSplit.write("set nevents {} \n".format(nevents))
        GluonSplit.write("set ebeam1 {} \n".format(ebeam))
        GluonSplit.write("set ebeam2 {} \n".format(ebeam))
        GluonSplit.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        GluonSplit.write("set iseed {} \n".format(random.randint(0, 1e8)))
        GluonSplit.write("0 \n")
        GluonSplit.close()
        
        GluonSplit_BC.write("launch Events/LQ_GluonS_BC_channel_{} \n".format(idx))
        GluonSplit_BC.write("shower=OFF \n")
        GluonSplit_BC.write("detector=OFF \n")
        GluonSplit_BC.write("set nevents {} \n".format(nevents))
        GluonSplit_BC.write("set ebeam1 {} \n".format(ebeam))
        GluonSplit_BC.write("set ebeam2 {} \n".format(ebeam))
        GluonSplit_BC.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        GluonSplit_BC.write("set iseed {} \n".format(random.randint(0, 1e8)))
        GluonSplit_BC.write("0 \n")
        GluonSplit_BC.close()
        
        GluonSplit_BS.write("launch Events/LQ_GluonS_BS_channel_{} \n".format(idx))
        GluonSplit_BS.write("shower=OFF \n")
        GluonSplit_BS.write("detector=OFF \n")
        GluonSplit_BS.write("set nevents {} \n".format(nevents))
        GluonSplit_BS.write("set ebeam1 {} \n".format(ebeam))
        GluonSplit_BS.write("set ebeam2 {} \n".format(ebeam))
        GluonSplit_BS.write("{path}/param_card_{index}.dat \n".format(path = path_ParamCards, index = idx))
        GluonSplit_BS.write("set iseed {} \n".format(random.randint(0, 1e8)))
        GluonSplit_BS.write("0 \n")
        GluonSplit_BS.close()
    
    Tchannel = open("./Events/P_Tchannel_{}.sh".format(idx), "x")
    Tchannel.write("cd {} \n".format(path_MadGraph))
    Tchannel.write("./bin/mg5_aMC {path}/F_Tchannel_{index}.sh \n".format(path = path_run, index = idx))
    Tchannel.write("cd {} \n".format(path_MadGraph))
    Tchannel.write("./bin/mg5_aMC {path}/S_Tchannel_{index}.sh \n".format(path = path_run, index = idx))
    Tchannel.write("\n")
    Tchannel.write("cd {path}/Events/LQ_T_channel_{index}/bin \n".format(path = path_MadGraph, index = idx))
    Tchannel.write("./cleanall \n")
    Tchannel.write("cd {path}/Events/run_01 \n".format(path = path_MadGraph))
    Tchannel.write("find . -name \"*.hepmc.gz\" -type f -delete \n")
    Tchannel.write("find . -name \"*.hepmc\" -type f -delete \n")
    Tchannel.write("File=$(find . -name \"*.root\" -type f) \n")
    Tchannel.write("mv $File LQ_T_channel_{}.root \n".format(idx))
    Tchannel.close()
    
    GluonSplit = open("./Events/P_GluonSplit_{}.sh".format(idx), "x")
    GluonSplit.write("cd {} \n".format(path_MadGraph))
    GluonSplit.write("./bin/mg5_aMC {path}/F_GluonSplit_{index}.sh \n".format(path = path_run, index = idx))
    GluonSplit.write("cd {} \n".format(path_MadGraph))
    GluonSplit.write("./bin/mg5_aMC {path}/S_GluonSplit_{index}.sh \n".format(path = path_run, index = idx))
    GluonSplit.write("\n")
    GluonSplit.write("cd {path}/Events/LQ_GluonS_channel_{index}/bin \n".format(path = path_MadGraph, index = idx))
    GluonSplit.write("./cleanall \n")
    GluonSplit.write("cd {path}/Events/run_01 \n".format(path = path_MadGraph))
    GluonSplit.write("find . -name \"*.hepmc.gz\" -type f -delete \n")
    GluonSplit.write("find . -name \"*.hepmc\" -type f -delete \n")
    GluonSplit.write("File=$(find . -name \"*.root\" -type f) \n")
    GluonSplit.write("mv $File LQ_GluonS_channel_{}.root \n".format(idx))
    GluonSplit.close()

    GluonSplit_BC = open("./Events/P_GluonSplit_BC_{}.sh".format(idx), "x")
    GluonSplit_BC.write("cd {} \n".format(path_MadGraph))
    GluonSplit_BC.write("./bin/mg5_aMC {path}/F_GluonSplit_BC_{index}.sh \n".format(path = path_run, index = idx))
    GluonSplit_BC.write("cd {} \n".format(path_MadGraph))
    GluonSplit_BC.write("./bin/mg5_aMC {path}/S_GluonSplit_BC_{index}.sh \n".format(path = path_run, index = idx))
    GluonSplit_BC.write("\n")
    GluonSplit_BC.write("cd {path}/Events/LQ_GluonS_BC_channel_{index}/bin \n".format(path = path_MadGraph, index = idx))
    GluonSplit_BC.write("./cleanall \n")
    GluonSplit_BC.write("cd {path}/Events/run_01 \n".format(path = path_MadGraph))
    GluonSplit_BC.write("find . -name \"*.hepmc.gz\" -type f -delete \n")
    GluonSplit_BC.write("find . -name \"*.hepmc\" -type f -delete \n")
    GluonSplit_BC.write("File=$(find . -name \"*.root\" -type f) \n")
    GluonSplit_BC.write("mv $File LQ_GluonS_BC_channel_{}.root \n".format(idx))
    GluonSplit_BC.close()
    
    
    GluonSplit_BS = open("./Events/P_GluonSplit_BS_{}.sh".format(idx), "x")
    GluonSplit_BS.write("cd {} \n".format(path_MadGraph))
    GluonSplit_BS.write("./bin/mg5_aMC {path}/F_GluonSplit_BS_{index}.sh \n".format(path = path_run, index = idx))
    GluonSplit_BS.write("cd {} \n".format(path_MadGraph))
    GluonSplit_BS.write("./bin/mg5_aMC {path}/S_GluonSplit_BS_{index}.sh \n".format(path = path_run, index = idx))
    GluonSplit_BS.write("\n")
    GluonSplit_BS.write("cd {path}/Events/LQ_GluonS_BS_channel_{index}/bin \n".format(path = path_MadGraph, index = idx))
    GluonSplit_BS.write("./cleanall \n")
    GluonSplit_BS.write("cd {path}/Events/run_01 \n".format(path = path_MadGraph))
    GluonSplit_BS.write("find . -name \"*.hepmc.gz\" -type f -delete \n")
    GluonSplit_BS.write("find . -name \"*.hepmc\" -type f -delete \n")
    GluonSplit_BS.write("File=$(find . -name \"*.root\" -type f) \n")
    GluonSplit_BS.write("mv $File LQ_GluonS_BS_channel_{}.root \n".format(idx))
    GluonSplit_BS.close()
    
#Run MadGraph
Features = ['mS1', 'mS2', 'mR']

if Cond_TChannel == True:
    Features = Features + ['xsec_TChannel (fb)']

if Cond_GluonSplit_BB == True:
    Features = Features + ['xsec_GluonSplit (fb)']
    
if Cond_GluonSplit_BC == True:
    Features = Features + ['xsec_GluonSplit_BC (fb)']

if Cond_GluonSplit_BS == True:
    Features = Features + ['xsec_GluonSplit_BS (fb)']

df = pd.DataFrame(columns=Features)

for idx in range(N):
    
    if Cond_TChannel == True: 
        subprocess.call(["bash", "{path}/P_Tchannel_{index}.sh".format(path = path_run, index = idx)])
    
    if Cond_GluonSplit_BB == True:
        subprocess.call(["bash", "{path}/P_GluonSplit_{index}.sh".format(path = path_run, index = idx)])
    
    if Cond_GluonSplit_BC == True:
        subprocess.call(["bash", "{path}/P_GluonSplit_BC_{index}.sh".format(path = path_run, index = idx)])
    
    if Cond_GluonSplit_BS == True:
        subprocess.call(["bash", "{path}/P_GluonSplit_BS_{index}.sh".format(path = path_run, index = idx)])
    
    #Read run_tag file
    if Cond_TChannel == True:  
        Output_tchannel = open('{path}/Events/LQ_T_channel_{index}/Events/run_01/run_01_tag_1_banner.txt'.format(path = path_MadGraph, index = idx), 'r')
        run_tag_tchannel = Output_tchannel.readlines() 
    
    if Cond_GluonSplit_BB == True:
        Output_gluonsplit = open('{path}/Events/LQ_GluonS_channel_{index}/Events/run_01/run_01_tag_1_banner.txt'.format(path = path_MadGraph, index = idx), 'r')
        run_tag_gluonsplit = Output_gluonsplit.readlines() 
    
    if Cond_GluonSplit_BC == True:
        Output_gluonsplit_BC = open('{path}/Events/LQ_GluonS_BC_channel_{index}/Events/run_01/run_01_tag_1_banner.txt'.format(path = path_MadGraph, index = idx), 'r')
        run_tag_gluonsplit_BC = Output_gluonsplit_BC.readlines() 
        
    if Cond_GluonSplit_BS == True:
        Output_gluonsplit_BS = open('{path}/Events/LQ_GluonS_BS_channel_{index}/Events/run_01/run_01_tag_1_banner.txt'.format(path = path_MadGraph, index = idx), 'r')
        run_tag_gluonsplit_BS = Output_gluonsplit_BS.readlines() 
    
    while True:
        if 'run_tag_tchannel' in vars():
            mass_run = run_tag_tchannel
            break
        elif 'run_tag_gluonsplit' in vars():
            mass_run = run_tag_gluonsplit
            break
        elif 'run_tag_gluonsplit_BC' in vars():
            mass_run = run_tag_gluonsplit_BC
            break
        elif 'run_tag_gluonsplit_BS' in vars():
            mass_run = run_tag_gluonsplit_BS
            break
        break
    
    #Get masses
    for j in mass_run:
        if j.__contains__('ms1'):    
                for word in j.split():
                    try:
                        mS1 = float(word)
                    except ValueError:
                        pass
    
    for j in mass_run:
        if j.__contains__('ms2'):    
                for word in j.split():
                    try:
                        mS2 = float(word)
                    except ValueError:
                        pass
                
    for j in mass_run:
        if j.__contains__('mr'):    
                for word in j.split():
                    try:
                        mR = float(word)
                    except ValueError:
                        pass
    
    #Get cross-sections
    if Cond_TChannel == True: 
        for j in run_tag_tchannel:
            if j.__contains__('Integrated'):    
                    for word in j.split():
                        try:
                            xsec_TChannel = float(word)*1e3
                        except ValueError:
                            pass
    
    if Cond_GluonSplit_BB == True:
        for j in run_tag_gluonsplit:
            if j.__contains__('Integrated'):    
                    for word in j.split():
                        try:
                            xsec_GluonSplit = float(word)*1e3
                        except ValueError:
                            pass
    if Cond_GluonSplit_BC == True:
        for j in run_tag_gluonsplit_BC:
            if j.__contains__('Integrated'):    
                    for word in j.split():
                        try:
                            xsec_GluonSplit_BC = float(word)*1e3
                        except ValueError:
                            pass
    
    if Cond_GluonSplit_BS == True:
        for j in run_tag_gluonsplit_BS:
            if j.__contains__('Integrated'):    
                    for word in j.split():
                        try:
                            xsec_GluonSplit_BS = float(word)*1e3
                        except ValueError:
                            pass
    
    MadGraph_data = [mS1, mS2, mR]
    
    if Cond_TChannel == True:
        MadGraph_data = MadGraph_data + [xsec_TChannel]
    
    if Cond_GluonSplit_BB == True:
        MadGraph_data = MadGraph_data + [xsec_GluonSplit]
    
    if Cond_GluonSplit_BC == True:
        MadGraph_data = MadGraph_data + [xsec_GluonSplit_BC]
    
    if Cond_GluonSplit_BS == True:
        MadGraph_data = MadGraph_data + [xsec_GluonSplit_BS]
        
    entry = pd.DataFrame([MadGraph_data], columns=Features)
    df = df.append(entry)
    df.to_csv('{path}/Data_MadGraph.csv'.format(path = path_Data),sep=',',index=False)
        

