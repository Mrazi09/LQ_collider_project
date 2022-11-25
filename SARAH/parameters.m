(* ::Package:: *)

ParameterDefinitions = { 

    {aEWinv,{
        Description -> "inverse weak coupling constant at mZ",
        Dependence -> None,
        DependenceNum -> None,
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> True,
        Value -> 137.035999679,
        LesHouches -> {SMINPUTS, 1},
        LaTeX -> "\\alpha^{-1}",
        OutputName -> aEWinv}},
    
    {Gf,{
        Description -> "Fermi constant",
        Dependence -> None,
        DependenceNum -> None,
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> True,
        Value -> 0.0000116639,
        LesHouches -> {SMINPUTS, 2},
        LaTeX -> "G_f",
        OutputName -> Gf}},

    {AlphaS,{
        Description -> "Alpha Strong",
        Dependence -> None,
        DependenceNum -> None,
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> True,
        Value -> 0.119,
        LesHouches -> {SMINPUTS, 3},
        LaTeX -> "\\alpha_S",
        OutputName -> aS}},
    
    {e,{
        Description -> "electric charge",
        Dependence -> None,
        DependenceNum -> 2*Sqrt[aEWinv^(-1)]*Sqrt[Pi],
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> True,
        LaTeX -> "e",
        OutputName -> el}},
        
     {ThetaW,{
        Description -> "Weinberg-Angle",
        DependenceNum -> ArcSin[Sqrt[1 - Mass[VWm]^2/Mass[VZ]^2]],
        Real -> True,
        LesHouches -> ThetaW,
        LaTeX -> "\\Theta_W",
        OutputName -> TW}},

    {g1,{
        Description -> "Hypercharge-Coupling",
        Dependence -> None,
        DependenceNum -> e*Sec[ThetaW],
        DependenceOptional -> e*Sec[ThetaW],
        DependenceSPheno -> None,
        Real -> True,
        LesHouches -> {GAUGE, 1},
        LaTeX -> "g_1",
        OutputName -> g1}},
     
    {g2,{
        Description -> "Left-Coupling",
        Dependence -> None,
        DependenceNum -> e*Csc[ThetaW],
        DependenceOptional -> e*Csc[ThetaW],
        DependenceSPheno -> None,
        Real -> True,
        LesHouches -> {GAUGE, 2},
        LaTeX -> "g_2",
        OutputName -> g2}},
        
    {g3,{
        Description -> "Strong-Coupling",
        Dependence -> None,
        DependenceNum -> 2*Sqrt[AlphaS]*Sqrt[Pi],
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> True,
        LesHouches -> {GAUGE, 3},
        LaTeX -> "g_3",
        OutputName -> g3}},
                    									
    {Yu,{
        Description -> "Up-Yukawa-Coupling",
        Real -> False,
        LaTeX -> "y_u",
        LesHouches -> YU,
        OutputName -> yu}},
        
     {Yd,{
        Description -> "Down-Yukawa-Coupling",
        Real -> False,
        LaTeX -> "y_d",
        LesHouches -> YD,
        OutputName -> yd}},
       
     {Ye,{
        Description -> "Lepton-Yukawa-Coupling",
        Real -> False,
        LaTeX -> "y_e",
        LesHouches -> YE,
        OutputName -> ye}},       
                                                                          
      {mu2,{ 
           Description -> "SM Mu Parameter",
		   LaTeX -> "\\mu",
           OutputName->m2SM}},     
                                                   
      {Lambd,{ 
         Description -> "SM Higgs Selfcouplings",
         LaTeX -> "\\lambda",
         DependenceNum -> Mass[hh]^2/(v^2)}},
               
               
      {v,{ 
         Description -> "EW-VEV",
               DependenceNum -> 2*Sqrt[Mass[VWm]^2/(g2^2)],
               DependenceSPheno -> None,
               Real -> True,
               LaTeX -> "v",
               OutputName -> vvSM}},
               
      {ZZ,{
          Description -> "Photon-Z Mixing Matrix",
          DependenceNum -> None,
          DependenceOptional -> None,
          DependenceSPheno -> None,
          LesHouches -> ZZMIX,
          LaTeX -> "Z^{\\gamma Z}",
          OutputName -> ZZ}},
          
       {ZW,{
           Description -> "W Mixing Matrix",
           DependenceNum -> None,
           DependenceOptional -> None,
           DependenceSPheno -> None,
           Real -> False,
           LesHouches -> ZWMIX,
           LaTeX -> "Z^W",
           OutputName -> ZW}},
           
        {ZH,{
           Description -> "Leptoquark Mixing Matrix (R's)",
           DependenceNum -> None,
           DependenceOptional -> None,
           DependenceSPheno -> None,
           Real -> False,
           LesHouches -> ZHMIX,
           LaTeX -> "Z^H",
           OutputName -> ZH}},
                              
        {ZM,{
           Description -> "Neutrino Mixing Matrix",
           DependenceNum -> None,
           DependenceOptional -> None,
           DependenceSPheno -> None,
           Real -> False,
           LesHouches -> ZMMIX,
           LaTeX -> "Z^M",
           OutputName -> ZM}},

(* Parametros para os Leptoquarks *)


(* Parameters for LagLQ *)

	  {cw1,{
             Description -> "Wilson for (H.l).(l.H)", 
             LaTeX -> "C_{W,1}", 
             LesHouches -> cw1,
	         OutputName -> CW1 }},   

       {Theta,{
             Description -> "Quark-Lepton-1stGenLQS Yukawa",
             LaTeX -> "\\Theta", 
             Real -> False,
             LesHouches -> THETA,
	         OutputName -> Theta }},
	         
	   {Upsilon,{
             Description -> "UpQuark-Lepton-1stGenLQS Yukawa", 
             LaTeX -> "\\Upsilon", 
             LesHouches -> UPSILON,
	         OutputName -> Upsilon }},
	         
	   {Omega,{
             Description -> "Lepton-DownQuarkRight-1stGenLQR Yukawa", 
             LaTeX -> "\\Omega", 
             LesHouches -> OMEGA,
	         OutputName -> Omega }},
	         
(* Parameters for LagNoHc *)

	   {muS,{
             Description -> "Quadratic term S.S", 
             LaTeX -> "M_{S}", 
             LesHouches -> muS,
	         OutputName -> MUS }},
	         
	   {muR,{
             Description -> "Quadratic term R.R", 
             LaTeX -> "mu_{R}", 
             LesHouches -> mur,
	         OutputName -> muR }},
	         
	   {gHS,{
             Description -> "Quartic term H.H.S.S", 
             LaTeX -> "g_{H,S}", 
             LesHouches -> GHS,
	         OutputName -> gHS }},
	         
	   {gHR,{
             Description -> "Quartic term H.H.R.R", 
             LaTeX -> "g_{H,R}", 
             LesHouches -> GHR,
	         OutputName -> gHR }},
	         
	   {gHRp,{
             Description -> "Quartic term H.R.H.R", 
             LaTeX -> "g_{H,R}^\\prime", 
             LesHouches -> GHRP,
	         OutputName -> ghrp }},        

	   {lambS,{
             Description -> "Quartic term S.S^2", 
             LaTeX -> "\\lambda_{S}", 
             LesHouches -> LAMBS,
	         OutputName -> lambS }},

	   {lambR,{
             Description -> "Quartic term R.R^2", 
             LaTeX -> "\\lambda_{R}", 
             LesHouches -> LAMBR,
	         OutputName -> lambR }},
	         	         
(* Parameters for LagLQV *)
	         
	   {lRRRH,{
             Description -> "Quartic term R.R.R.conj{H}", 
             LaTeX -> "\\lambda_{R, R, R, H}", 
             LesHouches -> LRRRH,
	         OutputName -> lRRRH }},
	         
	   {lRRS,{
             Description -> "Cubic term R.R.bar{S}", 
             LaTeX -> "\\lambda_{R,R,S}", 
             LesHouches -> LRRS,
	         OutputName -> lRRS }},
	         
	   {a1,{
             Description -> "Cubic term R.S.bar{H}", 
             LaTeX -> "a_{1}", 
             LesHouches -> A1,
	         OutputName -> a1 }},

	   {RRSS,{
             Description -> "Quartic term R.S.conj{R}.conj{S}", 
             LaTeX -> "\\lambda_{R,S,R,S}", 
             LesHouches -> RRSS,
	         OutputName -> RRSS }},
	         
	   {lSSHR,{
             Description -> "Cubic term S.S.conj{H}.conj{R}", 
             LaTeX -> "\\lambda_{S,S,H,R}", 
             LesHouches -> LSSHR,
	         OutputName -> lSSHR }},
	         
    {Vu,{
        Description -> "Left-Up-Mixing-Matrix",
        Dependence -> None,
        DependenceNum -> None,
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> False,
        LesHouches -> UULMIX,
        LaTeX -> "U^u_L",
        OutputName -> ZUL}},
        
    {Vd,{
        Description -> "Left-Down-Mixing-Matrix",
        Dependence -> None,
        DependenceNum -> None,
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> False,
        LesHouches -> UDLMIX,
        LaTeX -> "U^d_L",
        OutputName -> ZDL}},
        
    {Uu,{
        Description -> "Right-Up-Mixing-Matrix",
        Dependence -> None,
        DependenceNum -> None,
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> False,
        LesHouches -> UURMIX,
        LaTeX -> "U^u_R",
        OutputName -> ZUR}},
        
    {Ud,{
        Description -> "Right-Down-Mixing-Matrix",
        Dependence -> None,
        DependenceNum -> None,
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> False,
        LesHouches -> UDRMIX,
        LaTeX -> "U^d_R",
        OutputName -> ZDR}},
        
    {Ve,{
        Description -> "Left-Lepton-Mixing-Matrix",
        Dependence -> None,
        DependenceNum -> None,
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> False,
        LesHouches -> UELMIX,
        LaTeX -> "U^e_L",
        OutputName -> ZEL}},
        
    {Ue,{
        Description -> "Right-Lepton-Mixing-Matrix",
        Dependence -> None,
        DependenceNum -> None,
        DependenceOptional -> None,
        DependenceSPheno -> None,
        Real -> False,
        LesHouches -> UERMIX,
        LaTeX -> "U^e_R",
        OutputName -> ZER}}

 }; 
 

