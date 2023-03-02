# ----------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.14.5 
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840    
# (c) Florian Staub, 2011  
# ----------------------------------------------------------------------  
# File created at 14:5 on 30.11.2022   
# ----------------------------------------------------------------------  
 
 
from __future__ import absolute_import
from __future__ import division 
from object_library import all_particles,Particle 
import parameters as Param 


d1 = Particle(pdg_code =1, 
	 name = u'd1' ,
	 antiname = u'd1bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Md1 ,
	 width = Param.Wd1 ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = -1/3 ,
	 texname = u'd1' ,
	 antitexname = u'd1bar' ) 
 
d1bar = d1.anti() 
 
 
d2 = Particle(pdg_code =3, 
	 name = u'd2' ,
	 antiname = u'd2bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Md2 ,
	 width = Param.Wd2 ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = -1/3 ,
	 texname = u'd2' ,
	 antitexname = u'd2bar' ) 
 
d2bar = d2.anti() 
 
 
d3 = Particle(pdg_code =5, 
	 name = u'd3' ,
	 antiname = u'd3bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Md3 ,
	 width = Param.Wd3 ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = -1/3 ,
	 texname = u'd3' ,
	 antitexname = u'd3bar' ) 
 
d3bar = d3.anti() 
 
 
u1 = Particle(pdg_code =2, 
	 name = u'u1' ,
	 antiname = u'u1bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Mu1 ,
	 width = Param.Wu1 ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = 2/3 ,
	 texname = u'u1' ,
	 antitexname = u'u1bar' ) 
 
u1bar = u1.anti() 
 
 
u2 = Particle(pdg_code =4, 
	 name = u'u2' ,
	 antiname = u'u2bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Mu2 ,
	 width = Param.Wu2 ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = 2/3 ,
	 texname = u'u2' ,
	 antitexname = u'u2bar' ) 
 
u2bar = u2.anti() 
 
 
u3 = Particle(pdg_code =6, 
	 name = u'u3' ,
	 antiname = u'u3bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Mu3 ,
	 width = Param.Wu3 ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = 2/3 ,
	 texname = u'u3' ,
	 antitexname = u'u3bar' ) 
 
u3bar = u3.anti() 
 
 
e1 = Particle(pdg_code =11, 
	 name = u'e1' ,
	 antiname = u'e1bar' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.Me1 ,
	 width = Param.We1 ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = -1 ,
	 texname = u'e1' ,
	 antitexname = u'e1bar' ) 
 
e1bar = e1.anti() 
 
 
e2 = Particle(pdg_code =13, 
	 name = u'e2' ,
	 antiname = u'e2bar' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.Me2 ,
	 width = Param.We2 ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = -1 ,
	 texname = u'e2' ,
	 antitexname = u'e2bar' ) 
 
e2bar = e2.anti() 
 
 
e3 = Particle(pdg_code =15, 
	 name = u'e3' ,
	 antiname = u'e3bar' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.Me3 ,
	 width = Param.We3 ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = -1 ,
	 texname = u'e3' ,
	 antitexname = u'e3bar' ) 
 
e3bar = e3.anti() 
 
 
nu1 = Particle(pdg_code =12, 
	 name = u'nu1' ,
	 antiname = u'nu1' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = 0 ,
	 texname = u'nu1' ,
	 antitexname = u'nu1' ) 
 
nu2 = Particle(pdg_code =14, 
	 name = u'nu2' ,
	 antiname = u'nu2' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = 0 ,
	 texname = u'nu2' ,
	 antitexname = u'nu2' ) 
 
nu3 = Particle(pdg_code =16, 
	 name = u'nu3' ,
	 antiname = u'nu3' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = u'swavy' ,
	 charge = 0 ,
	 texname = u'nu3' ,
	 antitexname = u'nu3' ) 
 
Hp = Particle(pdg_code =999900, 
	 name = u'Hp' ,
	 antiname = u'Hpc' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = u'dashed' ,
	 charge = 1 ,
	 GoldstoneBoson = True ,
	 texname = u'Hp' ,
	 antitexname = u'Hpc' ) 
 
Hpc = Hp.anti() 
 
 
R = Particle(pdg_code =999034, 
	 name = u'R' ,
	 antiname = u'Rc' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.MR ,
	 width = Param.WR ,
	 GhostNumber = 0, 
	 line = u'dashed' ,
	 charge = 2/3 ,
	 texname = u'R' ,
	 antitexname = u'Rc' ) 
 
Rc = R.anti() 
 
 
Ah = Particle(pdg_code =999901, 
	 name = u'Ah' ,
	 antiname = u'Ah' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = u'dashed' ,
	 charge = 0 ,
	 GoldstoneBoson = True ,
	 texname = u'Ah' ,
	 antitexname = u'Ah' ) 
 
h = Particle(pdg_code =25, 
	 name = u'h' ,
	 antiname = u'h' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mh ,
	 width = Param.Wh ,
	 GhostNumber = 0, 
	 line = u'dashed' ,
	 charge = 0 ,
	 texname = u'h' ,
	 antitexname = u'h' ) 
 
S1 = Particle(pdg_code =999014, 
	 name = u'S1' ,
	 antiname = u'S1c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.MS1 ,
	 width = Param.WS1 ,
	 GhostNumber = 0, 
	 line = u'dashed' ,
	 charge = -1/3 ,
	 texname = u'S1' ,
	 antitexname = u'S1c' ) 
 
S1c = S1.anti() 
 
 
S2 = Particle(pdg_code =999024, 
	 name = u'S2' ,
	 antiname = u'S2c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.MS2 ,
	 width = Param.WS2 ,
	 GhostNumber = 0, 
	 line = u'dashed' ,
	 charge = -1/3 ,
	 texname = u'S2' ,
	 antitexname = u'S2c' ) 
 
S2c = S2.anti() 
 
 
g = Particle(pdg_code =21, 
	 name = u'g' ,
	 antiname = u'g' ,
	 spin = 3 ,
	 color = 8 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = u'wavy' ,
	 charge = 0 ,
	 texname = u'g' ,
	 antitexname = u'g' ) 
 
A = Particle(pdg_code =22, 
	 name = u'A' ,
	 antiname = u'A' ,
	 spin = 3 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = u'wavy' ,
	 charge = 0 ,
	 texname = u'A' ,
	 antitexname = u'A' ) 
 
Z = Particle(pdg_code =23, 
	 name = u'Z' ,
	 antiname = u'Z' ,
	 spin = 3 ,
	 color = 1 ,
	 mass = Param.MZ ,
	 width = Param.WZ ,
	 GhostNumber = 0, 
	 line = u'wavy' ,
	 charge = 0 ,
	 texname = u'Z' ,
	 antitexname = u'Z' ) 
 
Wm = Particle(pdg_code =-24, 
	 name = u'Wm' ,
	 antiname = u'Wmc' ,
	 spin = 3 ,
	 color = 1 ,
	 mass = Param.MWm ,
	 width = Param.WWm ,
	 GhostNumber = 0, 
	 line = u'wavy' ,
	 charge = -1 ,
	 texname = u'Wm' ,
	 antitexname = u'Wmc' ) 
 
Wmc = Wm.anti() 
 
 
gG = Particle(pdg_code =999902, 
	 name = u'gG' ,
	 antiname = u'gGc' ,
	 spin = -1 ,
	 color = 8 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 1, 
	 line = u'dotted' ,
	 charge = 0 ,
	 texname = u'gG' ,
	 antitexname = u'gGc' ) 
 
gGc = gG.anti() 
 
 
gA = Particle(pdg_code =999903, 
	 name = u'gA' ,
	 antiname = u'gAc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 1, 
	 line = u'dotted' ,
	 charge = 0 ,
	 texname = u'gA' ,
	 antitexname = u'gAc' ) 
 
gAc = gA.anti() 
 
 
gZ = Particle(pdg_code =999904, 
	 name = u'gZ' ,
	 antiname = u'gZc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.MZ ,
	 width = Param.WZ ,
	 GhostNumber = 1, 
	 line = u'dotted' ,
	 charge = 0 ,
	 texname = u'gZ' ,
	 antitexname = u'gZc' ) 
 
gZc = gZ.anti() 
 
 
gWm = Particle(pdg_code =999905, 
	 name = u'gWm' ,
	 antiname = u'gWmc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.MWm ,
	 width = Param.WWm ,
	 GhostNumber = 1, 
	 line = u'dotted' ,
	 charge = -1 ,
	 texname = u'gWm' ,
	 antitexname = u'gWmc' ) 
 
gWmc = gWm.anti() 
 
 
gWpos = Particle(pdg_code =999906, 
	 name = u'gWpos' ,
	 antiname = u'gWposc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.MWm ,
	 width = Param.WWm ,
	 GhostNumber = 1, 
	 line = u'dotted' ,
	 charge = 1 ,
	 texname = u'gWpos' ,
	 antitexname = u'gWposc' ) 
 
gWposc = gWpos.anti() 
 
 
