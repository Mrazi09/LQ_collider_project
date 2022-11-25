(* ::Package:: *)

ParticleDefinitions[GaugeES] = {

(* ------------------------- Higgs ------------------------- *)
      {H0,{
          Description -> "Neutral component of the Higgs doublet",    
          PDG -> {0},
          PDG . IX -> {0},
          Width -> 0, 
          Mass -> Automatic,
          FeynArtsNr -> 1,
          LaTeX -> "H^0",
          OutputName -> "H0" }},                       
          
      {Hp,{
          Description -> "Charged component of the Higgs doublet",
          PDG -> {0},
          PDG . IX -> {0},
          Width -> 0, 
          Mass -> Automatic,
          FeynArtsNr -> 11111,
          LaTeX -> "H^+",
          ElectricCharge -> 1,
          OutputName -> "Hp" }}, 
          
      {s,{
          Description -> "First generation Leptoquark S",
          PDG -> {999014},
          Width -> Automatic, 
          Mass -> Automatic,
          FeynArtsNr -> 100,
          ElectricCharge -> 1/3,
          LaTeX -> "S",
          OutputName -> "S" }}, 
          
      {rm,{
          Description -> "First generation Leptoquark R (component 2)",
          PDG -> {999024},
          Width -> Automatic, 
          Mass -> Automatic,
          FeynArtsNr -> 200,
          ElectricCharge -> -1/3,
          LaTeX -> "R^{-1/3}",
          OutputName -> "Rm" }}, 
          
	  {rp,{
          Description -> "First generation Leptoquark R (component 1)",
          PDG -> {999025},
          Width -> Automatic, 
          Mass -> Automatic,
          FeynArtsNr -> 201,
          ElectricCharge -> 2/3,
          LaTeX -> "R^{2/3}",
          OutputName -> "Rp" }},
          
(* ------------------------- Vector Bosons ------------------------- *)                 
                
    {VB,{
        Description -> "B-Boson",
        PDG -> {0},
        PDG . IX -> {0},
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 1,
        LaTeX -> "B",
        OutputName -> "B" }},
                                                           
    {VG,{
        Description -> "Gluon",
        PDG -> {0},
        PDG . IX ->{0},
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 5,
        LaTeX -> "g",
        ElectricCharge -> 0,
        OutputName -> "g" }},
        
    {VWB,{
        Description -> "W-Bosons",
        PDG -> {0},
        PDG . IX -> {0},
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 2,
        LaTeX -> "W",
        OutputName -> "W" }},
                 
    {gB,{
        Description -> "B-Boson Ghost",
        PDG -> {0},
        PDG . IX -> {0},
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 1,
        LaTeX -> "\\eta^B",
        OutputName -> "gB" }},  
                                                        
    {gG,{
        Description -> "Gluon Ghost",
        PDG -> {0},
        PDG . IX -> {0},
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 5,
        LaTeX -> "\\eta^G",
        ElectricCharge -> 0,
        OutputName -> "gG" }},
                  
    {gWB,{
        Description -> "W-Boson Ghost",
        PDG -> {0},
        PDG . IX -> {0},
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 2,
        LaTeX -> "\\eta^W",
        OutputName -> "gW" }},

(* ----------------------------------- Weyl fermions -----------------------------------*)

    {eL,{
        Description -> "Left Electron",
        Mass -> LesHouches,
        Width -> Automatic,
        FeynArtsNr -> 12,
        LaTeX -> "e_L",
        OutputName -> "eL" }},
        
    {vL,{
        Description -> "Left Neutrino",
        Mass -> LesHouches,
        Width -> Automatic,
        FeynArtsNr -> 23,
        LaTeX -> "\\nu_{e_L}",
        OutputName -> "vL" }},
        
     {eR,{
        Description -> "Right Electron",
        Mass -> LesHouches,
        Width -> Automatic,
        FeynArtsNr -> 14,
        LaTeX -> "e_R",
        OutputName -> "eR" }},
        
     {dL,{
        Description -> "Left Down-Quark",
        Mass -> LesHouches,
        Width -> Automatic,
        FeynArtsNr -> 7,
        LaTeX -> "d_L",
        OutputName -> "dL" }},
        
     {dR,{
        Description -> "Right Down-Quark",
        Mass -> LesHouches,
        Width -> Automatic,
        FeynArtsNr -> 8,
        LaTeX -> "d_R",
        OutputName -> "dR" }},
        
     {uL,{
        Description -> "Left Up-Quark",
        Mass -> LesHouches,
        Width -> Automatic,
        FeynArtsNr -> 19,
        LaTeX -> "u_L",
        OutputName -> "uL" }},
        
     {uR,{
        Description -> "Right Up-Quark",
        Mass -> LesHouches,
        Width -> Automatic,
        FeynArtsNr -> 21,
        LaTeX -> "u_R",
        OutputName -> "uR" }},       
(* ----------------------------------- Dirac fermions -----------------------------------*)
    {Fld,{
        Description -> "Dirac Left Down-Quarks",
        FeynArtsNr -> 121,
        LaTeX -> "\\Psi_{d}",
        Mass -> LesHouches,
        OutputName -> "dDL",
        Width -> {0, 0, 0}}},
        
     {Frd,{
        Description -> "Dirac Right Down-Quarks",
        FeynArtsNr -> 122,
        LaTeX -> "\\Chi_{d}",
        Mass -> LesHouches,
        OutputName -> "dDR",
        Width -> {0, 0, 0}}},
        
     {FLe,{
        Description -> "Dirac Left Electrons",
        FeynArtsNr -> 131,
        LaTeX -> "\\Psi_{e}",
        Mass -> LesHouches,
        OutputName -> "eDL",
        Width -> {0, 0, 0}}},
        
     {FLr,{
        Description -> "Dirac Right Electrons",
        FeynArtsNr -> 133,
        LaTeX -> "\\Chi_{e}",
        Mass -> LesHouches,
        OutputName -> "eDR",
        Width -> {0, 0, 0}}},
        
     {FLu,{
        Description -> "Dirac Left Up-Quarks",
        FeynArtsNr -> 111,
        LaTeX -> "\\Psi_{u}",
        Mass -> LesHouches,
        OutputName -> "uDL",
        Width -> {0, 0, 0}}},
        
     {FRu,{
        Description -> "Dirac Right Up-Quarks",
        FeynArtsNr -> 113,
        LaTeX -> "\\Chi_{u}",
        Mass -> LesHouches,
        OutputName -> "uDR",
        Width -> {0, 0, 0}}},
        
     {FLv,{
        Description -> "Dirac Left Neutrinos",
        FeynArtsNr -> 141,
        LaTeX -> "\\Psi_{D-L}",
        Mass -> LesHouches,
        OutputName -> "vDL",
        Width -> {0, 0, 0}}}  
      };
       
  ParticleDefinitions[EWSB] = {
(* ----------------------------------- Escalares -----------------------------------*)            
    {SS,{
        Description -> "Leptoquarks R",
        PDG -> {999014 , 999024},
        Mass -> {Automatic , Automatic},
        Width -> {Automatic , Automatic},
        FeynArtsNr -> 201,
        LaTeX -> "S",
        ElectricCharge -> 1/3,
        OutputName -> "S"  }},

    {rp,{
        Description -> "Leptoquark S",
        PDG -> {999034},
        Mass -> {Automatic},
        Width -> {Automatic},
        FeynArtsNr -> 233,
        LaTeX -> "R",
        ElectricCharge -> 2/3,
        OutputName -> "R"  }},                        
                                                                        
    {Hp,{
        Description -> "Charged Higgs",
        PDG -> {0},
        PDG . IX -> {0},
        Mass -> Automatic,
        FeynArtsNr -> 11111,
        LaTeX -> {"H^+","H^-"},
        ElectricCharge->1,
        OutputName -> {"Hp","Hm"} }},
                      
     {Ah,{  
           Description -> "Pseudo-Scalar Higgs",
           LaTeX -> "A_H",
           PDG -> {0},
           PDG . IX ->{0},
           ElectricCharge->{0},
           Mass -> {0},
           Width -> {0} }},    
            
     {hh,{
        Description -> "Higgs",
        PDG -> {25},
        PDG . IX -> {101000001},
        Width -> {0.00407},
        Mass -> {125.10},
        FeynArtsNr -> 1,
        LaTeX -> "h",
        ElectricCharge -> 0,
        OutputName -> "h" }},    
 (* ----------------------------------- Vector Bosons -----------------------------------------*)
    {VP,{
        Description -> "Photon",
        PDG -> {22},
        PDG . IX ->{121000001},
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 1,
        LaTeX -> "\\gamma",
        ElectricCharge -> 0,
        OutputName -> "A" }},  
                    
     {VZ,{
        Description -> "Z-Boson",
        PDG -> {23},
        PDG . IX ->{122000001},
        Width -> 2.44140351,
        Mass -> 91.188,
        FeynArtsNr -> 2,
        ElectricCharge -> 0,
        Goldstone -> Ah,
        LaTeX -> "Z",
        OutputName -> "Z" }},                                              
      
      {VG,{
        Description -> "Gluon",
        PDG -> {21},
        PDG . IX ->{121110001},
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 5,
        LaTeX -> "g",
        ElectricCharge -> 0,
        OutputName -> "g" }},
        
    {VWm,{
        Description -> "W-Boson",
        PDG -> {-24},
        PDG . IX ->{-120000601},
        Width -> 2.04759951,
        Mass -> 80.379,
        FeynArtsNr -> 3,
        LaTeX -> "W^-",
        ElectricCharge -> -1,
        Goldstone -> Hp,
        OutputName -> "Wm" }},
        
(* ----------------------------------- Ghosts -----------------------------------*) 

    {gP,{
        Description -> "Photon Ghost",
        PDG -> 0,
        PDG . IX -> 0,
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 1,
        ElectricCharge -> 0,
        LaTeX -> "\\eta^{\\gamma}",
        OutputName -> "gA" }},
        
     {gWm,{
         Description -> "Negative W Boson Ghost",
         PDG -> 0,
         PDG . IX -> 0,
         Mass -> Mass[VWm],
         Width -> Automatic,
         FeynArtsNr -> 3,
         ElectricCharge -> -1,
         LaTeX -> "\\eta^-",
         OutputName -> "gWm" }},
        
     {gWmC,{
          Description -> "Positive W Boson Ghost",
          PDG -> 0,
          PDG . IX -> 0,
          Mass -> Mass[VWm],
          Width -> Automatic,
          ElectricCharge -> 1,
          FeynArtsNr -> 4,
          LaTeX -> "\\eta^+",
          OutputName -> "gWpos" }},
        
     {gZ,{
        Description -> "Z-Boson Ghost",
        PDG -> 0,
        PDG . IX -> 0,
        Mass -> Mass[VZ],
        Width -> Automatic,
        FeynArtsNr -> 2,
        LaTeX -> "\\eta^Z",
        OutputName -> "gZ" }},
         
     {gG,{
        Description -> "Gluon Ghost",
        PDG -> 0,
        PDG . IX -> 0,
        Mass -> 0,
        Width -> 0,
        FeynArtsNr -> 5,
        LaTeX -> "\\eta^G",
        OutputName -> "gG" }},

(* ----------------------------------- Dirac fermions -----------------------------------*)                   
    {Fd,{
        Description -> "Down-Quarks",
        PDG -> {1,3,5},
        PDG . IX->{-110890201,-110890202,-110890203},
        Mass -> {0.0035, 0.104, 4.20},
        Width -> {Automatic, Automatic, Automatic},
        FeynArtsNr -> 4,
        LaTeX -> "d",
        ElectricCharge -> -1/3,
        OutputName -> "d" }},
        
     {Fu,{
        Description -> "Up-Quarks",
        PDG -> {2,4,6},
        Mass -> {0.0015, 1.27, 171.2},
        Width -> {Automatic, Automatic, 1.3853},
        FeynArtsNr -> 3,
        LaTeX -> "u",
        ElectricCharge -> 2/3,
        OutputName -> "u" }},
        
     {Fe,{
        Description -> "Leptons",
        PDG -> {11,13,15},
        Mass -> {0.000511, 0.105, 1.776},
        Width -> {Automatic, Automatic, Automatic},
        FeynArtsNr -> 2,
        LaTeX -> "e",
        ElectricCharge -> -1,
        OutputName -> "e" }},
            
     {Fv,{
        Description -> "Neutrinos",
        PDG -> {12,14,16},
        Mass -> {0, 0, 0},
        FeynArtsNr -> 1,
        ElectricCharge -> 0,
        LaTeX -> "\\nu",
        OutputName -> "nu" }}
                                                   
 };    
                
 WeylFermionAndIndermediate = {    
          
     {H,{
       Description -> "Higgs doublet",   
       PDG -> {0},
       Width -> 0, 
       Mass -> Automatic,
       LaTeX -> "H",
       OutputName -> "" }},
       
      {l,{
        Description -> "Left leptons",
        LaTeX -> "l",
        OutputName -> "" }},
        
      {q,{
        Description -> "Left quarks",
        LaTeX -> "q",
        OutputName -> "" }},
        
      {e,{
        Description -> "Right leptons",
        LaTeX -> "e",
        OutputName -> "" }},
        
      {u,{
        Description -> "Right u-quarks",
        LaTeX -> "u",
        OutputName -> "" }},
        
      {d,{
        Description -> "Right d-quarks",
        LaTeX -> "d",
        OutputName -> "" }},
                       
      {eL,{
        Description -> "Left Electrons",
        LaTeX -> "e_L",
        OutputName -> "" }},
        
      {vL,{
        Description -> "Left Neutrinos",
        LaTeX -> "\\nu_L",
        OutputName -> "" }},
           
      {eR,{
         Description -> "Right Electrons",
         LaTeX -> "e_R",
         OutputName -> "" }},
        
      {dL,{
         Description -> "Left Down-Quarks",
         LaTeX -> "d_L",
         OutputName -> "" }},
         
      {dR,{
         Description -> "Right Down-Quarks",
         LaTeX -> "d_R",
         OutputName -> "" }},
         
      {uL,{
         Description -> "Left Up-Quarks",
         LaTeX -> "u_L",
         OutputName -> "" }},
         
      {uR,{
         Description -> "Right Up-Quarks",
         LaTeX -> "u_R",
         OutputName -> "" }},        
     {DL,{
        Description -> "Rotated Left down-quarks",
        LaTeX -> "D_L",
        OutputName -> "" }},
        
     {DR,{
        Description -> "Rotated Right down-quarks",
        LaTeX -> "D_R",
        OutputName -> "" }},
        
     {UL,{
        Description -> "Rotated Left up-quarks",
        LaTeX -> "U_L",
        OutputName -> "" }},

     {UR,{
        Description -> "Rotated Ri,ght up-quarks",
        LaTeX -> "U_R",
        OutputName -> "" }},  
              
     {S,{
        Description -> "1st generation Leptoquark S",
        LaTeX -> "S",
        OutputName -> "" }},   
        
     {R,{
        Description -> "1st generation Leptoquark R",
        LaTeX -> "R_1",
        OutputName -> "" }}  
         
        };         


