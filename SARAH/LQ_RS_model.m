(* ::Package:: *)

Off[General::spell]

Model`Name = "LQ_RS_model";
Model`NameLaTeX ="Two leptoquarks";
Model`Authors = "Joao Pino";
Model`Date = "2022-11-25";



(*-------------------------------------------*)
(*   Particle Content*)
(*-------------------------------------------*)

(* Gauge Groups *)

Gauge[[1]]={B,   U[1], hypercharge, g1,False};
Gauge[[2]]={WB, SU[2], left,        g2,True};
Gauge[[3]]={G,  SU[3], color,       g3,False};


(* Matter Fields *)

FermionFields[[1]] = {q, 3, {uL, dL},     1/6, 2,  3};  
FermionFields[[2]] = {l, 3, {vL, eL},    -1/2, 2,  1};
FermionFields[[3]] = {d, 3, conj[dR],     1/3, 1, -3};
FermionFields[[4]] = {u, 3, conj[uR],    -2/3, 1, -3};
FermionFields[[5]] = {e, 3, conj[eR],       1, 1,  1};


ScalarFields[[1]] =  {H, 1, {Hp, H0},     1/2, 2,  1};
ScalarFields[[2]] =  {S, 1, s,            -1/3, 1, 3};
ScalarFields[[3]] =  {R, 1, {rp, rm},     1/6, 2,  3};


        
(*----------------------------------------------*)
(*   DEFINITION                                 *)
(*----------------------------------------------*)

NameOfStates={GaugeES, EWSB};

(* ----- Before EWSB ----- *)

DEFINITION[GaugeES][LagrangianInput]= {
	{LagHC, {AddHC->True}},
	{LagNoHC,{AddHC->False}},
	{LagLQ,{AddHC->True}},
	{LagLQV,{AddHC-> True}}
};


LagNoHC = - mu2 conj[H] . H - 1/2 Lambd conj[H] . H . conj[H] . H -\
	        muS conj[S] . S - gHS conj[H] . H . conj[S] . S - 1/2 lambS conj[S] . S . conj[S] . S -\
            muR conj[R] . R - gHR conj[H] . H . conj[R] . R - gHRp conj[H] . R . H . conj[R] -\
            1/2 lambR conj[R] . R . conj[R] . R;

LagHC   = - (Yd conj[H] . d . q + Ye conj[H] . e . l + Yu u . q . H - (cw1/(v^2))(H . l) . (l . H));

(*Z2 symmetry protects against di-quark interactions*)
LagLQ   = - (Theta l . q . conj[S] + Upsilon e . u . S + Omega R . l . d);

LagLQV  = - lRRRH R . R . R . conj[H] - lRRS R . R . S - a1 R . conj[S] . conj[H] - RRSS R . conj[S] . conj[R] . S -\
			lSSHR conj[S] . conj[S] . conj[H] . conj[R];


(* Gauge Sector *)

DEFINITION[EWSB][GaugeSector] =
{
  {{VB,VWB[3]},{VP,VZ},ZZ},
  {{VWB[1],VWB[2]},{VWm,conj[VWm]},ZW}
};     
        
(* ----- VEVs ---- *)

(*DEFINITION[EWSB][VEVs]={{H0,{v,1/Sqrt[2]},{Ah,\[ImaginaryI]/Sqrt[2]},{hh,1/Sqrt[2]}}};*)

(*DEFINITION[EWSB][VEVs] ={{H10, {v, 1/Sqrt[2]}, {Ah, I/Sqrt[2]},{hh, 1/Sqrt[2]}}};*)

DEFINITION[EWSB][VEVs]= 
{    {H0, {v, 1/Sqrt[2]}, {Ah, I/Sqrt[2]}, {hh, 1/Sqrt[2]}}
};
 

DEFINITION[EWSB][MatterSector]=   
    {
     {{s, rm}, {SS,ZH}},
     {{{dL}, {conj[dR]}}, {{DL,Vd}, {DR,Ud}}},
     {{{uL}, {conj[uR]}}, {{UL,Vu}, {UR,Uu}}},
     {{{eL}, {conj[eR]}}, {{EL,Ve}, {ER,Ue}}},
     {{vL}, {VL,ZM}}
    };  


(*------------------------------------------------------*)
(* Dirac-Spinors *)
(*------------------------------------------------------*)

(*o GaugeES e DiracSpinores estavam trocados. O nome das vari\[AAcute]veis tamb\[EAcute]m n\[ATilde]o
estava totalmente correcta*)
DEFINITION[GaugeES][DiracSpinors]=
{
 Fld -> { dL, 0 },
 Frd -> { 0, dR },
 FLu -> { uL, 0 },
 FRu -> { 0, uR },
 FLe -> { eL, 0 },
 FLr -> { 0, eR },
 FLv -> { vL, 0 }
 };
DEFINITION[EWSB][DiracSpinors]=
{
 Fd -> { DL, conj[DR] },
 Fe -> { EL, conj[ER] },
 Fu -> { UL, conj[UR] },
 Fv -> { VL, conj[VL] }
 };



