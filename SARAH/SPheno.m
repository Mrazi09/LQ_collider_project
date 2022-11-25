(* ::Package:: *)

OnlyLowEnergySPheno = True;

MINPAR={
 {1, Lambdainput},
 {2,   muSinput}, 
 {3,   gHSinput},
 {4, lambSinput},
 {5,   muRinput}, 
 {6,   gHRinput},
 {7, lambRinput},
 {8, lRRRHinput},
 {9,  lRRSinput},
 {10,  lRSHinput},
 {11,  RRSSinput},
 {12, lSSHRinput}
 };


ParametersToSolveTadpoles = {mu2};

DEFINITION[MatchingConditions]= {
 {v, vSM},
 {Ye, YeSM},
 {Yd, YdSM},
 {Yu, YuSM},
 {g1, g1SM},
 {g2, g2SM},
 {g3, g3SM}
 };

BoundaryLowScaleInput={
 {Lambd, Lambdainput},
 {muS,   muSinput}, 
 {gHS,   gHSinput},
 {lambS, lambSinput},
 {muR,   muRinput}, 
 {gHR,   gHRinput},
 {lambR, lambRinput},
 {Yd,LHInput[Yd]},
 {Ye,LHInput[Ye]}, 
 {Yu,LHInput[Yu]}, 
 {Theta,LHInput[Theta]},
 {Upsilon,LHInput[Upsilon]},
 {Omega,LHInput[Omega,]},
 {lRRRH, lRRRHinput},
 {lRRS,  lRRSinput},
 {lRSH,  lRSHinput},
 {RRSS,  RRSSinput},
 {lSSHR, lSSHRinput},
 {cw1, LHInput[cw1]}
 };



ListDecayParticles = {Fu,Fe,Fd,hh,SS,rp,VZ,VWm};
ListDecayParticles3B = {{Fu,"Fu.f90"},{Fe,"Fe.f90"},{Fd,"Fd.f90"},{SS,"R_LQs.f90"},{rp,"S_LQs.f90"}};

AddTreeLevelUnitarityLimits=True;

(*RenConditionsDecays={
{dCosTW, 1/2*Cos[ThetaW] * (PiVWm/(MVWm^2) - PiVZ/(mVZ^2)) },
{dSinTW, -dCosTW/Tan[ThetaW]},
{dg2, 1/2*g2*(derPiVPheavy0 + PiVPlightMZ/MVZ^2 - (-(PiVWm/MVWm^2) + PiVZ/MVZ^2)/Tan[ThetaW]^2 + (2*PiVZVP*Tan[ThetaW])/MVZ^2)  },
{dg1, dg2*Tan[ThetaW]+g2*dSinTW/Cos[ThetaW]- dCosTW*g2*Tan[ThetaW]/Cos[ThetaW]}
};*)


(* loop decays not working as long as neutrinos in the model are not mixed *)                     
SA`AddOneLoopDecay = False;
