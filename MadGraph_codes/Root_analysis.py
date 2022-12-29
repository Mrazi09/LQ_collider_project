#!/usr/bin/env python
# coding: utf-8

from __future__ import division
import ROOT
from ROOT import gSystem, gInterpreter
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import pandas as pd
from tqdm import tqdm
import math
import gc
import os
from collections import defaultdict
import warnings
warnings.filterwarnings("ignore")

gInterpreter.AddIncludePath("/home/felipe/MG5_aMC_v2_7_2_py3/Delphes/")
gInterpreter.AddIncludePath("/home/felipe/MG5_aMC_v2_7_2_py3/Delphes/external/")
gInterpreter.Declare('#include "/home/felipe/MG5_aMC_v2_7_2_py3/Delphes/classes/DelphesClasses.h"')
gInterpreter.Declare('#include "/home/felipe/MG5_aMC_v2_7_2_py3/Delphes/external/ExRootAnalysis/ExRootAnalysisLinkDef.h"')
gSystem.Load("/home/felipe/MG5_aMC_v2_7_2_py3/Delphes/libDelphes.so")

LQ_Tchannel_100GeV = ROOT.TChain("Delphes")
LQ_Tchannel_500GeV = ROOT.TChain("Delphes")
LQ_Tchannel_1TeV = ROOT.TChain("Delphes")
LQ_Tchannel_1p5TeV = ROOT.TChain("Delphes")
LQ_Tchannel_2TeV = ROOT.TChain("Delphes")
LQ_Tchannel_3TeV = ROOT.TChain("Delphes")
LQ_Tchannel_4TeV = ROOT.TChain("Delphes")

chain_list = [LQ_Tchannel_100GeV, LQ_Tchannel_500GeV, LQ_Tchannel_1TeV, LQ_Tchannel_1p5TeV,
              LQ_Tchannel_2TeV, LQ_Tchannel_3TeV, LQ_Tchannel_4TeV]

Events = {'LQ_Tchannel_100GeV':'/home/felipe/MG5_aMC_v2_7_2_py3/Events/Muon_100/Events/run_01/tag_1_delphes_events.root',
          'LQ_Tchannel_500GeV':'/home/felipe/MG5_aMC_v2_7_2_py3/Events/Muon_500/Events/run_01/tag_1_delphes_events.root',
          'LQ_Tchannel_1TeV':'/home/felipe/MG5_aMC_v2_7_2_py3/Events/Muon_1000/Events/run_01/tag_1_delphes_events.root',
          'LQ_Tchannel_1500TeV':'/home/felipe/MG5_aMC_v2_7_2_py3/Events/Muon_1500/Events/run_01/tag_1_delphes_events.root',
          'LQ_Tchannel_2TeV':'/home/felipe/MG5_aMC_v2_7_2_py3/Events/Muon_2000/Events/run_01/tag_1_delphes_events.root',
          'LQ_Tchannel_3TeV':'/home/felipe/MG5_aMC_v2_7_2_py3/Events/Muon_3000/Events/run_01/tag_1_delphes_events.root',
          'LQ_Tchannel_4TeV':'/home/felipe/MG5_aMC_v2_7_2_py3/Events/Muon_4000/Events/run_01/tag_1_delphes_events.root'}

for i,j in enumerate(Events.items()):
    chain_list[i].Add(j[1])
    print('number of events {}:'.format(j[0]),chain_list[i].GetEntries())
    
Features = ['pt_l1', 'pt_l2', 'E_l1', 'E_l2', 'eta_l1', 'eta_l2', 'phi_l1', 'phi_l2',
            'DeltaR_l1l2', 'DeltaPhi_l1l2', 'DeltaTheta_l1l2', 'DeltaEta_l1l2', 'cos_l1l2',
            'pt_l1_CM', 'pt_l2_CM', 'E_l1_CM', 'E_l2_CM', 'eta_l1_CM', 'eta_l2_CM', 'phi_l1_CM', 'phi_l2_CM',
            'DeltaR_l1l2_CM', 'DeltaPhi_l1l2_CM', 'DeltaTheta_l1l2_CM', 'DeltaEta_l1l2_CM', 'cos_l1l2_CM',
            'xs_weight']
    
for chain, proc in zip(chain_list,Events.items()):
    
    df = pd.DataFrame(columns=Features)

    for count, event in enumerate(tqdm(chain, total=chain.GetEntries())):

        #if count == 50:
        #    break
        
        out = np.empty((chain.GetEntries(),len(Features)))
        out.fill(np.nan)
        survived = 0

        #Get charged leptons (anti-electrons and electrons)
        electrons_eta = list(filter(lambda Electrons: np.abs(Electrons.Eta) <= 2.5, event.Electron))
        electrons = list(filter(lambda Electrons: Electrons.PT > 25., electrons_eta))
        electrons = sorted(electrons, key=lambda Electron: Electron.PT, reverse=True)  
        list_electron = electrons
        
        #Get charged leptons (anti-muons and muons)
        muons_eta = list(filter(lambda Muons: np.abs(Muons.Eta) <= 2.5, event.Muon))
        muons = list(filter(lambda Muons: Muons.PT > 25., muons_eta))
        muons = sorted(muons, key=lambda Muon: Muon.PT, reverse=True)  
        list_muon = muons
        
        #Charged lepton list
        list_lepton = list_electron + list_muon
        
        #Initialize the 4-vectors:
        LEP_vec_1 = ROOT.TLorentzVector()
        LEP_vec_2 = ROOT.TLorentzVector()
        
        #Begin analysis
        if (len(list_lepton) > 1):

            ####################
            LEP_vec_1.SetPtEtaPhiE(list_lepton[0].P4().Pt(), list_lepton[0].Eta, list_lepton[0].Phi, list_lepton[0].P4().E())
            ####################list_electron
            LEP_vec_2.SetPtEtaPhiE(list_lepton[1].P4().Pt(), list_lepton[1].Eta, list_lepton[1].Phi, list_lepton[1].P4().E())

            #High-level observables from final states 
                    
            # ------- Transverse momentum -------
            pt_l1 = LEP_vec_1.Pt()
            pt_l2 = LEP_vec_2.Pt()
            
            # ------- Energy -------
            E_l1 = LEP_vec_1.E()
            E_l2 = LEP_vec_2.E()
            
            # ------- Pseudorapidity -------
            eta_l1 = LEP_vec_1.Eta()
            eta_l2 = LEP_vec_2.Eta()
            
            # ------- Azimuthal angle -------
            phi_l1 = LEP_vec_1.Phi()
            phi_l2 = LEP_vec_2.Phi()      
                        
            #Angular variables between final states
            #Three vectors for everything
            T3_lep1 = LEP_vec_1.Vect()
            T3_lep2 = LEP_vec_2.Vect()
            
            # ------- Delta R -------
            DeltaR_l1l2 = LEP_vec_1.DeltaR(LEP_vec_2)
            
            # ------- Delta Phi -------
            DeltaPhi_l1l2 = LEP_vec_1.DeltaPhi(LEP_vec_2)
            
            # ------- Delta Theta -------
            DeltaTheta_l1l2 = LEP_vec_1.Theta() - LEP_vec_2.Theta()
            
            # ------- Delta eta -------
            DeltaEta_l1l2 = eta_l1 - eta_l2
            
            # ----- Cossine of polar angle ----- #
            cos_l1l2 = np.cos(T3_lep1.Angle(T3_lep2))
            
            
            ################################################################################################
            #Boost into the lepon/anti-lepton CM frame
            boost_vec = LEP_vec_1 + LEP_vec_2
            MuonAntiMuon_ref = ROOT.TLorentzVector()
            MuonAntiMuon_ref.SetPtEtaPhiE(boost_vec.Pt(), boost_vec.Eta(), boost_vec.Phi(), boost_vec.E())
            
            #Defining boosted l1
            l1_boost = ROOT.TLorentzVector()
            l1_boost.SetPtEtaPhiE(LEP_vec_1.Pt(), LEP_vec_1.Eta(), LEP_vec_1.Phi(), LEP_vec_1.E())
            
            #Defining boosted l2
            l2_boost = ROOT.TLorentzVector()
            l2_boost.SetPtEtaPhiE(LEP_vec_2.Pt(), LEP_vec_2.Eta(), LEP_vec_2.Phi(), LEP_vec_2.E())
            
            #Boosting
            mm_boost = MuonAntiMuon_ref.BoostVector()
            l1_boost.Boost(-mm_boost)
            l2_boost.Boost(-mm_boost)
            ################################################################################################
            
            
            # ------- Transverse momentum -------
            pt_l1_CM = l1_boost.Pt()
            pt_l2_CM = l2_boost.Pt()
            
            # ------- Energy -------
            E_l1_CM = l1_boost.E()
            E_l2_CM = l2_boost.E()
            
            # ------- Pseudorapidity -------
            eta_l1_CM = l1_boost.Eta()
            eta_l2_CM = l2_boost.Eta()
            
            # ------- Azimuthal angle -------
            phi_l1_CM = l1_boost.Phi()
            phi_l2_CM = l2_boost.Phi()      
                        
            #Angular variables between final states
            #Three vectors for everything
            T3_lep1_CM = l1_boost.Vect()
            T3_lep2_CM = l2_boost.Vect()
            
            # ------- Delta R -------
            DeltaR_l1l2_CM = l1_boost.DeltaR(l2_boost)
            
            # ------- Delta Phi -------
            DeltaPhi_l1l2_CM = l1_boost.DeltaPhi(l2_boost)
            
            # ------- Delta Theta -------
            DeltaTheta_l1l2_CM = l1_boost.Theta() - l2_boost.Theta()
            
            # ------- Delta eta -------
            DeltaEta_l1l2_CM = eta_l1 - eta_l2
            
            # ----- Cossine of polar angle ----- #
            cos_l1l2_CM = np.cos(T3_lep1_CM.Angle(T3_lep2_CM))
            
            #Return to normal
            l1_boost.Boost(mm_boost)
            l2_boost.Boost(mm_boost)
             
            # ------- Cross-section -------
            event_weight = [eevent.Weight for eevent in event.Event]
            xs_weight = event_weight[0] if len(event_weight) == 1 else 0

            # ------- List of all features -------
            Observables = [pt_l1, pt_l2, E_l1, E_l2, eta_l1, eta_l2, phi_l1, phi_l2,
                           DeltaR_l1l2, DeltaPhi_l1l2, DeltaTheta_l1l2, DeltaEta_l1l2, cos_l1l2,
                           pt_l1_CM, pt_l2_CM, E_l1_CM, E_l2_CM, eta_l1_CM, eta_l2_CM, phi_l1_CM, phi_l2_CM,
                           DeltaR_l1l2_CM, DeltaPhi_l1l2_CM, DeltaTheta_l1l2_CM, DeltaEta_l1l2_CM, cos_l1l2_CM,
                           xs_weight]

            entry = pd.DataFrame([Observables], columns=Features)
            df = df.append(entry)

            ###
            out[survived] = np.array(Observables)
            survived += 1
            
            df.to_csv('/home/felipe/JoaoPino/1-LQsCollider_project/Data_MadGraph/{f}.csv'.format(f=proc[0]), sep=',', index=False)


