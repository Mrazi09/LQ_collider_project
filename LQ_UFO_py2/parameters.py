# ----------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.14.5 
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840    
# (c) Florian Staub, 2011  
# ----------------------------------------------------------------------  
# File created at 14:5 on 30.11.2022   
# ----------------------------------------------------------------------  
 
 
from __future__ import absolute_import
from object_library import all_parameters,Parameter 
 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
ZERO=Parameter(name=u'ZERO', 
                      nature=u'internal', 
                      type=u'real', 
                      value=u'0.0', 
                      texname=u'0') 
 
Md1 = 	 Parameter(name = u'Md1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0.0035, 
	 texname = u'\\text{Md1}', 
	 lhablock = u'MASS', 
	 lhacode = [1]) 
 
Wd1 = 	 Parameter(name = u'Wd1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Wd1}', 
	 lhablock = u'DECAY', 
	 lhacode = [1]) 
 
Md2 = 	 Parameter(name = u'Md2', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0.104, 
	 texname = u'\\text{Md2}', 
	 lhablock = u'MASS', 
	 lhacode = [3]) 
 
Wd2 = 	 Parameter(name = u'Wd2', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Wd2}', 
	 lhablock = u'DECAY', 
	 lhacode = [3]) 
 
Md3 = 	 Parameter(name = u'Md3', 
	 nature = u'external', 
	 type = u'real', 
	 value = 4.2, 
	 texname = u'\\text{Md3}', 
	 lhablock = u'MASS', 
	 lhacode = [5]) 
 
Wd3 = 	 Parameter(name = u'Wd3', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Wd3}', 
	 lhablock = u'DECAY', 
	 lhacode = [5]) 
 
Mu1 = 	 Parameter(name = u'Mu1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0.0015, 
	 texname = u'\\text{Mu1}', 
	 lhablock = u'MASS', 
	 lhacode = [2]) 
 
Wu1 = 	 Parameter(name = u'Wu1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Wu1}', 
	 lhablock = u'DECAY', 
	 lhacode = [2]) 
 
Mu2 = 	 Parameter(name = u'Mu2', 
	 nature = u'external', 
	 type = u'real', 
	 value = 1.27, 
	 texname = u'\\text{Mu2}', 
	 lhablock = u'MASS', 
	 lhacode = [4]) 
 
Wu2 = 	 Parameter(name = u'Wu2', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Wu2}', 
	 lhablock = u'DECAY', 
	 lhacode = [4]) 
 
Mu3 = 	 Parameter(name = u'Mu3', 
	 nature = u'external', 
	 type = u'real', 
	 value = 171.2, 
	 texname = u'\\text{Mu3}', 
	 lhablock = u'MASS', 
	 lhacode = [6]) 
 
Wu3 = 	 Parameter(name = u'Wu3', 
	 nature = u'external', 
	 type = u'real', 
	 value = 1.3853, 
	 texname = u'\\text{Wu3}', 
	 lhablock = u'DECAY', 
	 lhacode = [6]) 
 
Me1 = 	 Parameter(name = u'Me1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0.000511, 
	 texname = u'\\text{Me1}', 
	 lhablock = u'MASS', 
	 lhacode = [11]) 
 
We1 = 	 Parameter(name = u'We1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{We1}', 
	 lhablock = u'DECAY', 
	 lhacode = [11]) 
 
Me2 = 	 Parameter(name = u'Me2', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0.105, 
	 texname = u'\\text{Me2}', 
	 lhablock = u'MASS', 
	 lhacode = [13]) 
 
We2 = 	 Parameter(name = u'We2', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{We2}', 
	 lhablock = u'DECAY', 
	 lhacode = [13]) 
 
Me3 = 	 Parameter(name = u'Me3', 
	 nature = u'external', 
	 type = u'real', 
	 value = 1.776, 
	 texname = u'\\text{Me3}', 
	 lhablock = u'MASS', 
	 lhacode = [15]) 
 
We3 = 	 Parameter(name = u'We3', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{We3}', 
	 lhablock = u'DECAY', 
	 lhacode = [15]) 
 
MR = 	 Parameter(name = u'MR', 
	 nature = u'external', 
	 type = u'real', 
	 value = 100., 
	 texname = u'\\text{MR}', 
	 lhablock = u'MASS', 
	 lhacode = [999034]) 
 
WR = 	 Parameter(name = u'WR', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{WR}', 
	 lhablock = u'DECAY', 
	 lhacode = [999034]) 
 
Mh = 	 Parameter(name = u'Mh', 
	 nature = u'external', 
	 type = u'real', 
	 value = 100., 
	 texname = u'\\text{Mh}', 
	 lhablock = u'MASS', 
	 lhacode = [25]) 
 
Wh = 	 Parameter(name = u'Wh', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Wh}', 
	 lhablock = u'DECAY', 
	 lhacode = [25]) 
 
MS1 = 	 Parameter(name = u'MS1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 100., 
	 texname = u'\\text{MS1}', 
	 lhablock = u'MASS', 
	 lhacode = [999014]) 
 
WS1 = 	 Parameter(name = u'WS1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{WS1}', 
	 lhablock = u'DECAY', 
	 lhacode = [999014]) 
 
MS2 = 	 Parameter(name = u'MS2', 
	 nature = u'external', 
	 type = u'real', 
	 value = 100., 
	 texname = u'\\text{MS2}', 
	 lhablock = u'MASS', 
	 lhacode = [999024]) 
 
WS2 = 	 Parameter(name = u'WS2', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{WS2}', 
	 lhablock = u'DECAY', 
	 lhacode = [999024]) 
 
MZ = 	 Parameter(name = u'MZ', 
	 nature = u'external', 
	 type = u'real', 
	 value = 91.188, 
	 texname = u'\\text{MZ}', 
	 lhablock = u'MASS', 
	 lhacode = [23]) 
 
WZ = 	 Parameter(name = u'WZ', 
	 nature = u'external', 
	 type = u'real', 
	 value = 2.4414, 
	 texname = u'\\text{WZ}', 
	 lhablock = u'DECAY', 
	 lhacode = [23]) 
 
MWm = 	 Parameter(name = u'MWm', 
	 nature = u'external', 
	 type = u'real', 
	 value = 80.379, 
	 texname = u'\\text{MWm}', 
	 lhablock = u'MASS', 
	 lhacode = [24]) 
 
WWm = 	 Parameter(name = u'WWm', 
	 nature = u'external', 
	 type = u'real', 
	 value = 2.0476, 
	 texname = u'\\text{WWm}', 
	 lhablock = u'DECAY', 
	 lhacode = [24]) 
 
ryu11 = 	 Parameter(name=u'ryu11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu11}', 
	 lhablock = u'YU', 
	 lhacode = [1, 1] ) 
 
iyu11 = 	 Parameter(name=u'iyu11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu11}', 
	 lhablock = u'IMYU', 
	 lhacode = [1, 1] ) 
 
ryu12 = 	 Parameter(name=u'ryu12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu12}', 
	 lhablock = u'YU', 
	 lhacode = [1, 2] ) 
 
iyu12 = 	 Parameter(name=u'iyu12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu12}', 
	 lhablock = u'IMYU', 
	 lhacode = [1, 2] ) 
 
ryu13 = 	 Parameter(name=u'ryu13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu13}', 
	 lhablock = u'YU', 
	 lhacode = [1, 3] ) 
 
iyu13 = 	 Parameter(name=u'iyu13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu13}', 
	 lhablock = u'IMYU', 
	 lhacode = [1, 3] ) 
 
ryu21 = 	 Parameter(name=u'ryu21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu21}', 
	 lhablock = u'YU', 
	 lhacode = [2, 1] ) 
 
iyu21 = 	 Parameter(name=u'iyu21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu21}', 
	 lhablock = u'IMYU', 
	 lhacode = [2, 1] ) 
 
ryu22 = 	 Parameter(name=u'ryu22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu22}', 
	 lhablock = u'YU', 
	 lhacode = [2, 2] ) 
 
iyu22 = 	 Parameter(name=u'iyu22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu22}', 
	 lhablock = u'IMYU', 
	 lhacode = [2, 2] ) 
 
ryu23 = 	 Parameter(name=u'ryu23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu23}', 
	 lhablock = u'YU', 
	 lhacode = [2, 3] ) 
 
iyu23 = 	 Parameter(name=u'iyu23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu23}', 
	 lhablock = u'IMYU', 
	 lhacode = [2, 3] ) 
 
ryu31 = 	 Parameter(name=u'ryu31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu31}', 
	 lhablock = u'YU', 
	 lhacode = [3, 1] ) 
 
iyu31 = 	 Parameter(name=u'iyu31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu31}', 
	 lhablock = u'IMYU', 
	 lhacode = [3, 1] ) 
 
ryu32 = 	 Parameter(name=u'ryu32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu32}', 
	 lhablock = u'YU', 
	 lhacode = [3, 2] ) 
 
iyu32 = 	 Parameter(name=u'iyu32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu32}', 
	 lhablock = u'IMYU', 
	 lhacode = [3, 2] ) 
 
ryu33 = 	 Parameter(name=u'ryu33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu33}', 
	 lhablock = u'YU', 
	 lhacode = [3, 3] ) 
 
iyu33 = 	 Parameter(name=u'iyu33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yu33}', 
	 lhablock = u'IMYU', 
	 lhacode = [3, 3] ) 
 
ryd11 = 	 Parameter(name=u'ryd11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd11}', 
	 lhablock = u'YD', 
	 lhacode = [1, 1] ) 
 
iyd11 = 	 Parameter(name=u'iyd11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd11}', 
	 lhablock = u'IMYD', 
	 lhacode = [1, 1] ) 
 
ryd12 = 	 Parameter(name=u'ryd12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd12}', 
	 lhablock = u'YD', 
	 lhacode = [1, 2] ) 
 
iyd12 = 	 Parameter(name=u'iyd12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd12}', 
	 lhablock = u'IMYD', 
	 lhacode = [1, 2] ) 
 
ryd13 = 	 Parameter(name=u'ryd13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd13}', 
	 lhablock = u'YD', 
	 lhacode = [1, 3] ) 
 
iyd13 = 	 Parameter(name=u'iyd13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd13}', 
	 lhablock = u'IMYD', 
	 lhacode = [1, 3] ) 
 
ryd21 = 	 Parameter(name=u'ryd21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd21}', 
	 lhablock = u'YD', 
	 lhacode = [2, 1] ) 
 
iyd21 = 	 Parameter(name=u'iyd21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd21}', 
	 lhablock = u'IMYD', 
	 lhacode = [2, 1] ) 
 
ryd22 = 	 Parameter(name=u'ryd22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd22}', 
	 lhablock = u'YD', 
	 lhacode = [2, 2] ) 
 
iyd22 = 	 Parameter(name=u'iyd22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd22}', 
	 lhablock = u'IMYD', 
	 lhacode = [2, 2] ) 
 
ryd23 = 	 Parameter(name=u'ryd23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd23}', 
	 lhablock = u'YD', 
	 lhacode = [2, 3] ) 
 
iyd23 = 	 Parameter(name=u'iyd23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd23}', 
	 lhablock = u'IMYD', 
	 lhacode = [2, 3] ) 
 
ryd31 = 	 Parameter(name=u'ryd31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd31}', 
	 lhablock = u'YD', 
	 lhacode = [3, 1] ) 
 
iyd31 = 	 Parameter(name=u'iyd31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd31}', 
	 lhablock = u'IMYD', 
	 lhacode = [3, 1] ) 
 
ryd32 = 	 Parameter(name=u'ryd32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd32}', 
	 lhablock = u'YD', 
	 lhacode = [3, 2] ) 
 
iyd32 = 	 Parameter(name=u'iyd32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd32}', 
	 lhablock = u'IMYD', 
	 lhacode = [3, 2] ) 
 
ryd33 = 	 Parameter(name=u'ryd33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd33}', 
	 lhablock = u'YD', 
	 lhacode = [3, 3] ) 
 
iyd33 = 	 Parameter(name=u'iyd33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{yd33}', 
	 lhablock = u'IMYD', 
	 lhacode = [3, 3] ) 
 
rye11 = 	 Parameter(name=u'rye11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye11}', 
	 lhablock = u'YE', 
	 lhacode = [1, 1] ) 
 
iye11 = 	 Parameter(name=u'iye11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye11}', 
	 lhablock = u'IMYE', 
	 lhacode = [1, 1] ) 
 
rye12 = 	 Parameter(name=u'rye12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye12}', 
	 lhablock = u'YE', 
	 lhacode = [1, 2] ) 
 
iye12 = 	 Parameter(name=u'iye12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye12}', 
	 lhablock = u'IMYE', 
	 lhacode = [1, 2] ) 
 
rye13 = 	 Parameter(name=u'rye13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye13}', 
	 lhablock = u'YE', 
	 lhacode = [1, 3] ) 
 
iye13 = 	 Parameter(name=u'iye13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye13}', 
	 lhablock = u'IMYE', 
	 lhacode = [1, 3] ) 
 
rye21 = 	 Parameter(name=u'rye21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye21}', 
	 lhablock = u'YE', 
	 lhacode = [2, 1] ) 
 
iye21 = 	 Parameter(name=u'iye21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye21}', 
	 lhablock = u'IMYE', 
	 lhacode = [2, 1] ) 
 
rye22 = 	 Parameter(name=u'rye22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye22}', 
	 lhablock = u'YE', 
	 lhacode = [2, 2] ) 
 
iye22 = 	 Parameter(name=u'iye22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye22}', 
	 lhablock = u'IMYE', 
	 lhacode = [2, 2] ) 
 
rye23 = 	 Parameter(name=u'rye23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye23}', 
	 lhablock = u'YE', 
	 lhacode = [2, 3] ) 
 
iye23 = 	 Parameter(name=u'iye23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye23}', 
	 lhablock = u'IMYE', 
	 lhacode = [2, 3] ) 
 
rye31 = 	 Parameter(name=u'rye31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye31}', 
	 lhablock = u'YE', 
	 lhacode = [3, 1] ) 
 
iye31 = 	 Parameter(name=u'iye31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye31}', 
	 lhablock = u'IMYE', 
	 lhacode = [3, 1] ) 
 
rye32 = 	 Parameter(name=u'rye32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye32}', 
	 lhablock = u'YE', 
	 lhacode = [3, 2] ) 
 
iye32 = 	 Parameter(name=u'iye32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye32}', 
	 lhablock = u'IMYE', 
	 lhacode = [3, 2] ) 
 
rye33 = 	 Parameter(name=u'rye33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye33}', 
	 lhablock = u'YE', 
	 lhacode = [3, 3] ) 
 
iye33 = 	 Parameter(name=u'iye33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ye33}', 
	 lhablock = u'IMYE', 
	 lhacode = [3, 3] ) 
 
rCW111 = 	 Parameter(name=u'rCW111', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW111}', 
	 lhablock = u'CW1', 
	 lhacode = [1, 1] ) 
 
iCW111 = 	 Parameter(name=u'iCW111', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW111}', 
	 lhablock = u'IMCW1', 
	 lhacode = [1, 1] ) 
 
rCW112 = 	 Parameter(name=u'rCW112', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW112}', 
	 lhablock = u'CW1', 
	 lhacode = [1, 2] ) 
 
iCW112 = 	 Parameter(name=u'iCW112', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW112}', 
	 lhablock = u'IMCW1', 
	 lhacode = [1, 2] ) 
 
rCW113 = 	 Parameter(name=u'rCW113', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW113}', 
	 lhablock = u'CW1', 
	 lhacode = [1, 3] ) 
 
iCW113 = 	 Parameter(name=u'iCW113', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW113}', 
	 lhablock = u'IMCW1', 
	 lhacode = [1, 3] ) 
 
rCW121 = 	 Parameter(name=u'rCW121', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW121}', 
	 lhablock = u'CW1', 
	 lhacode = [2, 1] ) 
 
iCW121 = 	 Parameter(name=u'iCW121', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW121}', 
	 lhablock = u'IMCW1', 
	 lhacode = [2, 1] ) 
 
rCW122 = 	 Parameter(name=u'rCW122', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW122}', 
	 lhablock = u'CW1', 
	 lhacode = [2, 2] ) 
 
iCW122 = 	 Parameter(name=u'iCW122', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW122}', 
	 lhablock = u'IMCW1', 
	 lhacode = [2, 2] ) 
 
rCW123 = 	 Parameter(name=u'rCW123', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW123}', 
	 lhablock = u'CW1', 
	 lhacode = [2, 3] ) 
 
iCW123 = 	 Parameter(name=u'iCW123', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW123}', 
	 lhablock = u'IMCW1', 
	 lhacode = [2, 3] ) 
 
rCW131 = 	 Parameter(name=u'rCW131', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW131}', 
	 lhablock = u'CW1', 
	 lhacode = [3, 1] ) 
 
iCW131 = 	 Parameter(name=u'iCW131', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW131}', 
	 lhablock = u'IMCW1', 
	 lhacode = [3, 1] ) 
 
rCW132 = 	 Parameter(name=u'rCW132', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW132}', 
	 lhablock = u'CW1', 
	 lhacode = [3, 2] ) 
 
iCW132 = 	 Parameter(name=u'iCW132', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW132}', 
	 lhablock = u'IMCW1', 
	 lhacode = [3, 2] ) 
 
rCW133 = 	 Parameter(name=u'rCW133', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW133}', 
	 lhablock = u'CW1', 
	 lhacode = [3, 3] ) 
 
iCW133 = 	 Parameter(name=u'iCW133', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{CW133}', 
	 lhablock = u'IMCW1', 
	 lhacode = [3, 3] ) 
 
rgHR = 	 Parameter(name=u'rgHR', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{gHR}', 
	 lhablock = u'GHR', 
	 lhacode = [1] ) 
 
igHR = 	 Parameter(name=u'igHR', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{gHR}', 
	 lhablock = u'IMGHR', 
	 lhacode = [1] ) 
 
rgHS = 	 Parameter(name=u'rgHS', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{gHS}', 
	 lhablock = u'GHS', 
	 lhacode = [1] ) 
 
igHS = 	 Parameter(name=u'igHS', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{gHS}', 
	 lhablock = u'IMGHS', 
	 lhacode = [1] ) 
 
rghrp = 	 Parameter(name=u'rghrp', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ghrp}', 
	 lhablock = u'GHRP', 
	 lhacode = [1] ) 
 
ighrp = 	 Parameter(name=u'ighrp', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ghrp}', 
	 lhablock = u'IMGHRP', 
	 lhacode = [1] ) 
 
rlambR = 	 Parameter(name=u'rlambR', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{lambR}', 
	 lhablock = u'LAMBR', 
	 lhacode = [1] ) 
 
ilambR = 	 Parameter(name=u'ilambR', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{lambR}', 
	 lhablock = u'IMLAMBR', 
	 lhacode = [1] ) 
 
rlambS = 	 Parameter(name=u'rlambS', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{lambS}', 
	 lhablock = u'LAMBS', 
	 lhacode = [1] ) 
 
ilambS = 	 Parameter(name=u'ilambS', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{lambS}', 
	 lhablock = u'IMLAMBS', 
	 lhacode = [1] ) 
 
rTheta11 = 	 Parameter(name=u'rTheta11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta11}', 
	 lhablock = u'THETA', 
	 lhacode = [1, 1] ) 
 
iTheta11 = 	 Parameter(name=u'iTheta11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta11}', 
	 lhablock = u'IMTHETA', 
	 lhacode = [1, 1] ) 
 
rTheta12 = 	 Parameter(name=u'rTheta12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta12}', 
	 lhablock = u'THETA', 
	 lhacode = [1, 2] ) 
 
iTheta12 = 	 Parameter(name=u'iTheta12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta12}', 
	 lhablock = u'IMTHETA', 
	 lhacode = [1, 2] ) 
 
rTheta13 = 	 Parameter(name=u'rTheta13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta13}', 
	 lhablock = u'THETA', 
	 lhacode = [1, 3] ) 
 
iTheta13 = 	 Parameter(name=u'iTheta13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta13}', 
	 lhablock = u'IMTHETA', 
	 lhacode = [1, 3] ) 
 
rTheta21 = 	 Parameter(name=u'rTheta21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta21}', 
	 lhablock = u'THETA', 
	 lhacode = [2, 1] ) 
 
iTheta21 = 	 Parameter(name=u'iTheta21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta21}', 
	 lhablock = u'IMTHETA', 
	 lhacode = [2, 1] ) 
 
rTheta22 = 	 Parameter(name=u'rTheta22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta22}', 
	 lhablock = u'THETA', 
	 lhacode = [2, 2] ) 
 
iTheta22 = 	 Parameter(name=u'iTheta22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta22}', 
	 lhablock = u'IMTHETA', 
	 lhacode = [2, 2] ) 
 
rTheta23 = 	 Parameter(name=u'rTheta23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta23}', 
	 lhablock = u'THETA', 
	 lhacode = [2, 3] ) 
 
iTheta23 = 	 Parameter(name=u'iTheta23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta23}', 
	 lhablock = u'IMTHETA', 
	 lhacode = [2, 3] ) 
 
rTheta31 = 	 Parameter(name=u'rTheta31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta31}', 
	 lhablock = u'THETA', 
	 lhacode = [3, 1] ) 
 
iTheta31 = 	 Parameter(name=u'iTheta31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta31}', 
	 lhablock = u'IMTHETA', 
	 lhacode = [3, 1] ) 
 
rTheta32 = 	 Parameter(name=u'rTheta32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta32}', 
	 lhablock = u'THETA', 
	 lhacode = [3, 2] ) 
 
iTheta32 = 	 Parameter(name=u'iTheta32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta32}', 
	 lhablock = u'IMTHETA', 
	 lhacode = [3, 2] ) 
 
rTheta33 = 	 Parameter(name=u'rTheta33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta33}', 
	 lhablock = u'THETA', 
	 lhacode = [3, 3] ) 
 
iTheta33 = 	 Parameter(name=u'iTheta33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Theta33}', 
	 lhablock = u'IMTHETA', 
	 lhacode = [3, 3] ) 
 
rOmega11 = 	 Parameter(name=u'rOmega11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega11}', 
	 lhablock = u'OMEGA', 
	 lhacode = [1, 1] ) 
 
iOmega11 = 	 Parameter(name=u'iOmega11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega11}', 
	 lhablock = u'IMOMEGA', 
	 lhacode = [1, 1] ) 
 
rOmega12 = 	 Parameter(name=u'rOmega12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega12}', 
	 lhablock = u'OMEGA', 
	 lhacode = [1, 2] ) 
 
iOmega12 = 	 Parameter(name=u'iOmega12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega12}', 
	 lhablock = u'IMOMEGA', 
	 lhacode = [1, 2] ) 
 
rOmega13 = 	 Parameter(name=u'rOmega13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega13}', 
	 lhablock = u'OMEGA', 
	 lhacode = [1, 3] ) 
 
iOmega13 = 	 Parameter(name=u'iOmega13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega13}', 
	 lhablock = u'IMOMEGA', 
	 lhacode = [1, 3] ) 
 
rOmega21 = 	 Parameter(name=u'rOmega21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega21}', 
	 lhablock = u'OMEGA', 
	 lhacode = [2, 1] ) 
 
iOmega21 = 	 Parameter(name=u'iOmega21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega21}', 
	 lhablock = u'IMOMEGA', 
	 lhacode = [2, 1] ) 
 
rOmega22 = 	 Parameter(name=u'rOmega22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega22}', 
	 lhablock = u'OMEGA', 
	 lhacode = [2, 2] ) 
 
iOmega22 = 	 Parameter(name=u'iOmega22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega22}', 
	 lhablock = u'IMOMEGA', 
	 lhacode = [2, 2] ) 
 
rOmega23 = 	 Parameter(name=u'rOmega23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega23}', 
	 lhablock = u'OMEGA', 
	 lhacode = [2, 3] ) 
 
iOmega23 = 	 Parameter(name=u'iOmega23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega23}', 
	 lhablock = u'IMOMEGA', 
	 lhacode = [2, 3] ) 
 
rOmega31 = 	 Parameter(name=u'rOmega31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega31}', 
	 lhablock = u'OMEGA', 
	 lhacode = [3, 1] ) 
 
iOmega31 = 	 Parameter(name=u'iOmega31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega31}', 
	 lhablock = u'IMOMEGA', 
	 lhacode = [3, 1] ) 
 
rOmega32 = 	 Parameter(name=u'rOmega32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega32}', 
	 lhablock = u'OMEGA', 
	 lhacode = [3, 2] ) 
 
iOmega32 = 	 Parameter(name=u'iOmega32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega32}', 
	 lhablock = u'IMOMEGA', 
	 lhacode = [3, 2] ) 
 
rOmega33 = 	 Parameter(name=u'rOmega33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega33}', 
	 lhablock = u'OMEGA', 
	 lhacode = [3, 3] ) 
 
iOmega33 = 	 Parameter(name=u'iOmega33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Omega33}', 
	 lhablock = u'IMOMEGA', 
	 lhacode = [3, 3] ) 
 
rUpsilon11 = 	 Parameter(name=u'rUpsilon11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon11}', 
	 lhablock = u'UPSILON', 
	 lhacode = [1, 1] ) 
 
iUpsilon11 = 	 Parameter(name=u'iUpsilon11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon11}', 
	 lhablock = u'IMUPSILON', 
	 lhacode = [1, 1] ) 
 
rUpsilon12 = 	 Parameter(name=u'rUpsilon12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon12}', 
	 lhablock = u'UPSILON', 
	 lhacode = [1, 2] ) 
 
iUpsilon12 = 	 Parameter(name=u'iUpsilon12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon12}', 
	 lhablock = u'IMUPSILON', 
	 lhacode = [1, 2] ) 
 
rUpsilon13 = 	 Parameter(name=u'rUpsilon13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon13}', 
	 lhablock = u'UPSILON', 
	 lhacode = [1, 3] ) 
 
iUpsilon13 = 	 Parameter(name=u'iUpsilon13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon13}', 
	 lhablock = u'IMUPSILON', 
	 lhacode = [1, 3] ) 
 
rUpsilon21 = 	 Parameter(name=u'rUpsilon21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon21}', 
	 lhablock = u'UPSILON', 
	 lhacode = [2, 1] ) 
 
iUpsilon21 = 	 Parameter(name=u'iUpsilon21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon21}', 
	 lhablock = u'IMUPSILON', 
	 lhacode = [2, 1] ) 
 
rUpsilon22 = 	 Parameter(name=u'rUpsilon22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon22}', 
	 lhablock = u'UPSILON', 
	 lhacode = [2, 2] ) 
 
iUpsilon22 = 	 Parameter(name=u'iUpsilon22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon22}', 
	 lhablock = u'IMUPSILON', 
	 lhacode = [2, 2] ) 
 
rUpsilon23 = 	 Parameter(name=u'rUpsilon23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon23}', 
	 lhablock = u'UPSILON', 
	 lhacode = [2, 3] ) 
 
iUpsilon23 = 	 Parameter(name=u'iUpsilon23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon23}', 
	 lhablock = u'IMUPSILON', 
	 lhacode = [2, 3] ) 
 
rUpsilon31 = 	 Parameter(name=u'rUpsilon31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon31}', 
	 lhablock = u'UPSILON', 
	 lhacode = [3, 1] ) 
 
iUpsilon31 = 	 Parameter(name=u'iUpsilon31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon31}', 
	 lhablock = u'IMUPSILON', 
	 lhacode = [3, 1] ) 
 
rUpsilon32 = 	 Parameter(name=u'rUpsilon32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon32}', 
	 lhablock = u'UPSILON', 
	 lhacode = [3, 2] ) 
 
iUpsilon32 = 	 Parameter(name=u'iUpsilon32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon32}', 
	 lhablock = u'IMUPSILON', 
	 lhacode = [3, 2] ) 
 
rUpsilon33 = 	 Parameter(name=u'rUpsilon33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon33}', 
	 lhablock = u'UPSILON', 
	 lhacode = [3, 3] ) 
 
iUpsilon33 = 	 Parameter(name=u'iUpsilon33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{Upsilon33}', 
	 lhablock = u'IMUPSILON', 
	 lhacode = [3, 3] ) 
 
rlRRS = 	 Parameter(name=u'rlRRS', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{lRRS}', 
	 lhablock = u'LRRS', 
	 lhacode = [1] ) 
 
ilRRS = 	 Parameter(name=u'ilRRS', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{lRRS}', 
	 lhablock = u'IMLRRS', 
	 lhacode = [1] ) 
 
ra1 = 	 Parameter(name=u'ra1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{a1}', 
	 lhablock = u'A1', 
	 lhacode = [1] ) 
 
ia1 = 	 Parameter(name=u'ia1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{a1}', 
	 lhablock = u'IMA1', 
	 lhacode = [1] ) 
 
rRRSS = 	 Parameter(name=u'rRRSS', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{RRSS}', 
	 lhablock = u'RRSS', 
	 lhacode = [1] ) 
 
iRRSS = 	 Parameter(name=u'iRRSS', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{RRSS}', 
	 lhablock = u'IMRRSS', 
	 lhacode = [1] ) 
 
rZH11 = 	 Parameter(name=u'rZH11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZH11}', 
	 lhablock = u'ZHMIX', 
	 lhacode = [1, 1] ) 
 
iZH11 = 	 Parameter(name=u'iZH11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZH11}', 
	 lhablock = u'IMZHMIX', 
	 lhacode = [1, 1] ) 
 
rZH12 = 	 Parameter(name=u'rZH12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZH12}', 
	 lhablock = u'ZHMIX', 
	 lhacode = [1, 2] ) 
 
iZH12 = 	 Parameter(name=u'iZH12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZH12}', 
	 lhablock = u'IMZHMIX', 
	 lhacode = [1, 2] ) 
 
rZH21 = 	 Parameter(name=u'rZH21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZH21}', 
	 lhablock = u'ZHMIX', 
	 lhacode = [2, 1] ) 
 
iZH21 = 	 Parameter(name=u'iZH21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZH21}', 
	 lhablock = u'IMZHMIX', 
	 lhacode = [2, 1] ) 
 
rZH22 = 	 Parameter(name=u'rZH22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZH22}', 
	 lhablock = u'ZHMIX', 
	 lhacode = [2, 2] ) 
 
iZH22 = 	 Parameter(name=u'iZH22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZH22}', 
	 lhablock = u'IMZHMIX', 
	 lhacode = [2, 2] ) 
 
rZDL11 = 	 Parameter(name=u'rZDL11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL11}', 
	 lhablock = u'UDLMIX', 
	 lhacode = [1, 1] ) 
 
iZDL11 = 	 Parameter(name=u'iZDL11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL11}', 
	 lhablock = u'IMUDLMIX', 
	 lhacode = [1, 1] ) 
 
rZDL12 = 	 Parameter(name=u'rZDL12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL12}', 
	 lhablock = u'UDLMIX', 
	 lhacode = [1, 2] ) 
 
iZDL12 = 	 Parameter(name=u'iZDL12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL12}', 
	 lhablock = u'IMUDLMIX', 
	 lhacode = [1, 2] ) 
 
rZDL13 = 	 Parameter(name=u'rZDL13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL13}', 
	 lhablock = u'UDLMIX', 
	 lhacode = [1, 3] ) 
 
iZDL13 = 	 Parameter(name=u'iZDL13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL13}', 
	 lhablock = u'IMUDLMIX', 
	 lhacode = [1, 3] ) 
 
rZDL21 = 	 Parameter(name=u'rZDL21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL21}', 
	 lhablock = u'UDLMIX', 
	 lhacode = [2, 1] ) 
 
iZDL21 = 	 Parameter(name=u'iZDL21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL21}', 
	 lhablock = u'IMUDLMIX', 
	 lhacode = [2, 1] ) 
 
rZDL22 = 	 Parameter(name=u'rZDL22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL22}', 
	 lhablock = u'UDLMIX', 
	 lhacode = [2, 2] ) 
 
iZDL22 = 	 Parameter(name=u'iZDL22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL22}', 
	 lhablock = u'IMUDLMIX', 
	 lhacode = [2, 2] ) 
 
rZDL23 = 	 Parameter(name=u'rZDL23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL23}', 
	 lhablock = u'UDLMIX', 
	 lhacode = [2, 3] ) 
 
iZDL23 = 	 Parameter(name=u'iZDL23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL23}', 
	 lhablock = u'IMUDLMIX', 
	 lhacode = [2, 3] ) 
 
rZDL31 = 	 Parameter(name=u'rZDL31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL31}', 
	 lhablock = u'UDLMIX', 
	 lhacode = [3, 1] ) 
 
iZDL31 = 	 Parameter(name=u'iZDL31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL31}', 
	 lhablock = u'IMUDLMIX', 
	 lhacode = [3, 1] ) 
 
rZDL32 = 	 Parameter(name=u'rZDL32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL32}', 
	 lhablock = u'UDLMIX', 
	 lhacode = [3, 2] ) 
 
iZDL32 = 	 Parameter(name=u'iZDL32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL32}', 
	 lhablock = u'IMUDLMIX', 
	 lhacode = [3, 2] ) 
 
rZDL33 = 	 Parameter(name=u'rZDL33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL33}', 
	 lhablock = u'UDLMIX', 
	 lhacode = [3, 3] ) 
 
iZDL33 = 	 Parameter(name=u'iZDL33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDL33}', 
	 lhablock = u'IMUDLMIX', 
	 lhacode = [3, 3] ) 
 
rZDR11 = 	 Parameter(name=u'rZDR11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR11}', 
	 lhablock = u'UDRMIX', 
	 lhacode = [1, 1] ) 
 
iZDR11 = 	 Parameter(name=u'iZDR11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR11}', 
	 lhablock = u'IMUDRMIX', 
	 lhacode = [1, 1] ) 
 
rZDR12 = 	 Parameter(name=u'rZDR12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR12}', 
	 lhablock = u'UDRMIX', 
	 lhacode = [1, 2] ) 
 
iZDR12 = 	 Parameter(name=u'iZDR12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR12}', 
	 lhablock = u'IMUDRMIX', 
	 lhacode = [1, 2] ) 
 
rZDR13 = 	 Parameter(name=u'rZDR13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR13}', 
	 lhablock = u'UDRMIX', 
	 lhacode = [1, 3] ) 
 
iZDR13 = 	 Parameter(name=u'iZDR13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR13}', 
	 lhablock = u'IMUDRMIX', 
	 lhacode = [1, 3] ) 
 
rZDR21 = 	 Parameter(name=u'rZDR21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR21}', 
	 lhablock = u'UDRMIX', 
	 lhacode = [2, 1] ) 
 
iZDR21 = 	 Parameter(name=u'iZDR21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR21}', 
	 lhablock = u'IMUDRMIX', 
	 lhacode = [2, 1] ) 
 
rZDR22 = 	 Parameter(name=u'rZDR22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR22}', 
	 lhablock = u'UDRMIX', 
	 lhacode = [2, 2] ) 
 
iZDR22 = 	 Parameter(name=u'iZDR22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR22}', 
	 lhablock = u'IMUDRMIX', 
	 lhacode = [2, 2] ) 
 
rZDR23 = 	 Parameter(name=u'rZDR23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR23}', 
	 lhablock = u'UDRMIX', 
	 lhacode = [2, 3] ) 
 
iZDR23 = 	 Parameter(name=u'iZDR23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR23}', 
	 lhablock = u'IMUDRMIX', 
	 lhacode = [2, 3] ) 
 
rZDR31 = 	 Parameter(name=u'rZDR31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR31}', 
	 lhablock = u'UDRMIX', 
	 lhacode = [3, 1] ) 
 
iZDR31 = 	 Parameter(name=u'iZDR31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR31}', 
	 lhablock = u'IMUDRMIX', 
	 lhacode = [3, 1] ) 
 
rZDR32 = 	 Parameter(name=u'rZDR32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR32}', 
	 lhablock = u'UDRMIX', 
	 lhacode = [3, 2] ) 
 
iZDR32 = 	 Parameter(name=u'iZDR32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR32}', 
	 lhablock = u'IMUDRMIX', 
	 lhacode = [3, 2] ) 
 
rZDR33 = 	 Parameter(name=u'rZDR33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR33}', 
	 lhablock = u'UDRMIX', 
	 lhacode = [3, 3] ) 
 
iZDR33 = 	 Parameter(name=u'iZDR33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZDR33}', 
	 lhablock = u'IMUDRMIX', 
	 lhacode = [3, 3] ) 
 
rZUL11 = 	 Parameter(name=u'rZUL11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL11}', 
	 lhablock = u'UULMIX', 
	 lhacode = [1, 1] ) 
 
iZUL11 = 	 Parameter(name=u'iZUL11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL11}', 
	 lhablock = u'IMUULMIX', 
	 lhacode = [1, 1] ) 
 
rZUL12 = 	 Parameter(name=u'rZUL12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL12}', 
	 lhablock = u'UULMIX', 
	 lhacode = [1, 2] ) 
 
iZUL12 = 	 Parameter(name=u'iZUL12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL12}', 
	 lhablock = u'IMUULMIX', 
	 lhacode = [1, 2] ) 
 
rZUL13 = 	 Parameter(name=u'rZUL13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL13}', 
	 lhablock = u'UULMIX', 
	 lhacode = [1, 3] ) 
 
iZUL13 = 	 Parameter(name=u'iZUL13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL13}', 
	 lhablock = u'IMUULMIX', 
	 lhacode = [1, 3] ) 
 
rZUL21 = 	 Parameter(name=u'rZUL21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL21}', 
	 lhablock = u'UULMIX', 
	 lhacode = [2, 1] ) 
 
iZUL21 = 	 Parameter(name=u'iZUL21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL21}', 
	 lhablock = u'IMUULMIX', 
	 lhacode = [2, 1] ) 
 
rZUL22 = 	 Parameter(name=u'rZUL22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL22}', 
	 lhablock = u'UULMIX', 
	 lhacode = [2, 2] ) 
 
iZUL22 = 	 Parameter(name=u'iZUL22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL22}', 
	 lhablock = u'IMUULMIX', 
	 lhacode = [2, 2] ) 
 
rZUL23 = 	 Parameter(name=u'rZUL23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL23}', 
	 lhablock = u'UULMIX', 
	 lhacode = [2, 3] ) 
 
iZUL23 = 	 Parameter(name=u'iZUL23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL23}', 
	 lhablock = u'IMUULMIX', 
	 lhacode = [2, 3] ) 
 
rZUL31 = 	 Parameter(name=u'rZUL31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL31}', 
	 lhablock = u'UULMIX', 
	 lhacode = [3, 1] ) 
 
iZUL31 = 	 Parameter(name=u'iZUL31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL31}', 
	 lhablock = u'IMUULMIX', 
	 lhacode = [3, 1] ) 
 
rZUL32 = 	 Parameter(name=u'rZUL32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL32}', 
	 lhablock = u'UULMIX', 
	 lhacode = [3, 2] ) 
 
iZUL32 = 	 Parameter(name=u'iZUL32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL32}', 
	 lhablock = u'IMUULMIX', 
	 lhacode = [3, 2] ) 
 
rZUL33 = 	 Parameter(name=u'rZUL33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL33}', 
	 lhablock = u'UULMIX', 
	 lhacode = [3, 3] ) 
 
iZUL33 = 	 Parameter(name=u'iZUL33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUL33}', 
	 lhablock = u'IMUULMIX', 
	 lhacode = [3, 3] ) 
 
rZUR11 = 	 Parameter(name=u'rZUR11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR11}', 
	 lhablock = u'UURMIX', 
	 lhacode = [1, 1] ) 
 
iZUR11 = 	 Parameter(name=u'iZUR11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR11}', 
	 lhablock = u'IMUURMIX', 
	 lhacode = [1, 1] ) 
 
rZUR12 = 	 Parameter(name=u'rZUR12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR12}', 
	 lhablock = u'UURMIX', 
	 lhacode = [1, 2] ) 
 
iZUR12 = 	 Parameter(name=u'iZUR12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR12}', 
	 lhablock = u'IMUURMIX', 
	 lhacode = [1, 2] ) 
 
rZUR13 = 	 Parameter(name=u'rZUR13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR13}', 
	 lhablock = u'UURMIX', 
	 lhacode = [1, 3] ) 
 
iZUR13 = 	 Parameter(name=u'iZUR13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR13}', 
	 lhablock = u'IMUURMIX', 
	 lhacode = [1, 3] ) 
 
rZUR21 = 	 Parameter(name=u'rZUR21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR21}', 
	 lhablock = u'UURMIX', 
	 lhacode = [2, 1] ) 
 
iZUR21 = 	 Parameter(name=u'iZUR21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR21}', 
	 lhablock = u'IMUURMIX', 
	 lhacode = [2, 1] ) 
 
rZUR22 = 	 Parameter(name=u'rZUR22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR22}', 
	 lhablock = u'UURMIX', 
	 lhacode = [2, 2] ) 
 
iZUR22 = 	 Parameter(name=u'iZUR22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR22}', 
	 lhablock = u'IMUURMIX', 
	 lhacode = [2, 2] ) 
 
rZUR23 = 	 Parameter(name=u'rZUR23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR23}', 
	 lhablock = u'UURMIX', 
	 lhacode = [2, 3] ) 
 
iZUR23 = 	 Parameter(name=u'iZUR23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR23}', 
	 lhablock = u'IMUURMIX', 
	 lhacode = [2, 3] ) 
 
rZUR31 = 	 Parameter(name=u'rZUR31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR31}', 
	 lhablock = u'UURMIX', 
	 lhacode = [3, 1] ) 
 
iZUR31 = 	 Parameter(name=u'iZUR31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR31}', 
	 lhablock = u'IMUURMIX', 
	 lhacode = [3, 1] ) 
 
rZUR32 = 	 Parameter(name=u'rZUR32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR32}', 
	 lhablock = u'UURMIX', 
	 lhacode = [3, 2] ) 
 
iZUR32 = 	 Parameter(name=u'iZUR32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR32}', 
	 lhablock = u'IMUURMIX', 
	 lhacode = [3, 2] ) 
 
rZUR33 = 	 Parameter(name=u'rZUR33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR33}', 
	 lhablock = u'UURMIX', 
	 lhacode = [3, 3] ) 
 
iZUR33 = 	 Parameter(name=u'iZUR33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZUR33}', 
	 lhablock = u'IMUURMIX', 
	 lhacode = [3, 3] ) 
 
rZEL11 = 	 Parameter(name=u'rZEL11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL11}', 
	 lhablock = u'UELMIX', 
	 lhacode = [1, 1] ) 
 
iZEL11 = 	 Parameter(name=u'iZEL11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL11}', 
	 lhablock = u'IMUELMIX', 
	 lhacode = [1, 1] ) 
 
rZEL12 = 	 Parameter(name=u'rZEL12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL12}', 
	 lhablock = u'UELMIX', 
	 lhacode = [1, 2] ) 
 
iZEL12 = 	 Parameter(name=u'iZEL12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL12}', 
	 lhablock = u'IMUELMIX', 
	 lhacode = [1, 2] ) 
 
rZEL13 = 	 Parameter(name=u'rZEL13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL13}', 
	 lhablock = u'UELMIX', 
	 lhacode = [1, 3] ) 
 
iZEL13 = 	 Parameter(name=u'iZEL13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL13}', 
	 lhablock = u'IMUELMIX', 
	 lhacode = [1, 3] ) 
 
rZEL21 = 	 Parameter(name=u'rZEL21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL21}', 
	 lhablock = u'UELMIX', 
	 lhacode = [2, 1] ) 
 
iZEL21 = 	 Parameter(name=u'iZEL21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL21}', 
	 lhablock = u'IMUELMIX', 
	 lhacode = [2, 1] ) 
 
rZEL22 = 	 Parameter(name=u'rZEL22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL22}', 
	 lhablock = u'UELMIX', 
	 lhacode = [2, 2] ) 
 
iZEL22 = 	 Parameter(name=u'iZEL22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL22}', 
	 lhablock = u'IMUELMIX', 
	 lhacode = [2, 2] ) 
 
rZEL23 = 	 Parameter(name=u'rZEL23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL23}', 
	 lhablock = u'UELMIX', 
	 lhacode = [2, 3] ) 
 
iZEL23 = 	 Parameter(name=u'iZEL23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL23}', 
	 lhablock = u'IMUELMIX', 
	 lhacode = [2, 3] ) 
 
rZEL31 = 	 Parameter(name=u'rZEL31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL31}', 
	 lhablock = u'UELMIX', 
	 lhacode = [3, 1] ) 
 
iZEL31 = 	 Parameter(name=u'iZEL31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL31}', 
	 lhablock = u'IMUELMIX', 
	 lhacode = [3, 1] ) 
 
rZEL32 = 	 Parameter(name=u'rZEL32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL32}', 
	 lhablock = u'UELMIX', 
	 lhacode = [3, 2] ) 
 
iZEL32 = 	 Parameter(name=u'iZEL32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL32}', 
	 lhablock = u'IMUELMIX', 
	 lhacode = [3, 2] ) 
 
rZEL33 = 	 Parameter(name=u'rZEL33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL33}', 
	 lhablock = u'UELMIX', 
	 lhacode = [3, 3] ) 
 
iZEL33 = 	 Parameter(name=u'iZEL33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZEL33}', 
	 lhablock = u'IMUELMIX', 
	 lhacode = [3, 3] ) 
 
rZER11 = 	 Parameter(name=u'rZER11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER11}', 
	 lhablock = u'UERMIX', 
	 lhacode = [1, 1] ) 
 
iZER11 = 	 Parameter(name=u'iZER11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER11}', 
	 lhablock = u'IMUERMIX', 
	 lhacode = [1, 1] ) 
 
rZER12 = 	 Parameter(name=u'rZER12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER12}', 
	 lhablock = u'UERMIX', 
	 lhacode = [1, 2] ) 
 
iZER12 = 	 Parameter(name=u'iZER12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER12}', 
	 lhablock = u'IMUERMIX', 
	 lhacode = [1, 2] ) 
 
rZER13 = 	 Parameter(name=u'rZER13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER13}', 
	 lhablock = u'UERMIX', 
	 lhacode = [1, 3] ) 
 
iZER13 = 	 Parameter(name=u'iZER13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER13}', 
	 lhablock = u'IMUERMIX', 
	 lhacode = [1, 3] ) 
 
rZER21 = 	 Parameter(name=u'rZER21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER21}', 
	 lhablock = u'UERMIX', 
	 lhacode = [2, 1] ) 
 
iZER21 = 	 Parameter(name=u'iZER21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER21}', 
	 lhablock = u'IMUERMIX', 
	 lhacode = [2, 1] ) 
 
rZER22 = 	 Parameter(name=u'rZER22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER22}', 
	 lhablock = u'UERMIX', 
	 lhacode = [2, 2] ) 
 
iZER22 = 	 Parameter(name=u'iZER22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER22}', 
	 lhablock = u'IMUERMIX', 
	 lhacode = [2, 2] ) 
 
rZER23 = 	 Parameter(name=u'rZER23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER23}', 
	 lhablock = u'UERMIX', 
	 lhacode = [2, 3] ) 
 
iZER23 = 	 Parameter(name=u'iZER23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER23}', 
	 lhablock = u'IMUERMIX', 
	 lhacode = [2, 3] ) 
 
rZER31 = 	 Parameter(name=u'rZER31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER31}', 
	 lhablock = u'UERMIX', 
	 lhacode = [3, 1] ) 
 
iZER31 = 	 Parameter(name=u'iZER31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER31}', 
	 lhablock = u'IMUERMIX', 
	 lhacode = [3, 1] ) 
 
rZER32 = 	 Parameter(name=u'rZER32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER32}', 
	 lhablock = u'UERMIX', 
	 lhacode = [3, 2] ) 
 
iZER32 = 	 Parameter(name=u'iZER32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER32}', 
	 lhablock = u'IMUERMIX', 
	 lhacode = [3, 2] ) 
 
rZER33 = 	 Parameter(name=u'rZER33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER33}', 
	 lhablock = u'UERMIX', 
	 lhacode = [3, 3] ) 
 
iZER33 = 	 Parameter(name=u'iZER33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZER33}', 
	 lhablock = u'IMUERMIX', 
	 lhacode = [3, 3] ) 
 
rZM11 = 	 Parameter(name=u'rZM11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM11}', 
	 lhablock = u'ZMMIX', 
	 lhacode = [1, 1] ) 
 
iZM11 = 	 Parameter(name=u'iZM11', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM11}', 
	 lhablock = u'IMZMMIX', 
	 lhacode = [1, 1] ) 
 
rZM12 = 	 Parameter(name=u'rZM12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM12}', 
	 lhablock = u'ZMMIX', 
	 lhacode = [1, 2] ) 
 
iZM12 = 	 Parameter(name=u'iZM12', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM12}', 
	 lhablock = u'IMZMMIX', 
	 lhacode = [1, 2] ) 
 
rZM13 = 	 Parameter(name=u'rZM13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM13}', 
	 lhablock = u'ZMMIX', 
	 lhacode = [1, 3] ) 
 
iZM13 = 	 Parameter(name=u'iZM13', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM13}', 
	 lhablock = u'IMZMMIX', 
	 lhacode = [1, 3] ) 
 
rZM21 = 	 Parameter(name=u'rZM21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM21}', 
	 lhablock = u'ZMMIX', 
	 lhacode = [2, 1] ) 
 
iZM21 = 	 Parameter(name=u'iZM21', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM21}', 
	 lhablock = u'IMZMMIX', 
	 lhacode = [2, 1] ) 
 
rZM22 = 	 Parameter(name=u'rZM22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM22}', 
	 lhablock = u'ZMMIX', 
	 lhacode = [2, 2] ) 
 
iZM22 = 	 Parameter(name=u'iZM22', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM22}', 
	 lhablock = u'IMZMMIX', 
	 lhacode = [2, 2] ) 
 
rZM23 = 	 Parameter(name=u'rZM23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM23}', 
	 lhablock = u'ZMMIX', 
	 lhacode = [2, 3] ) 
 
iZM23 = 	 Parameter(name=u'iZM23', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM23}', 
	 lhablock = u'IMZMMIX', 
	 lhacode = [2, 3] ) 
 
rZM31 = 	 Parameter(name=u'rZM31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM31}', 
	 lhablock = u'ZMMIX', 
	 lhacode = [3, 1] ) 
 
iZM31 = 	 Parameter(name=u'iZM31', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM31}', 
	 lhablock = u'IMZMMIX', 
	 lhacode = [3, 1] ) 
 
rZM32 = 	 Parameter(name=u'rZM32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM32}', 
	 lhablock = u'ZMMIX', 
	 lhacode = [3, 2] ) 
 
iZM32 = 	 Parameter(name=u'iZM32', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM32}', 
	 lhablock = u'IMZMMIX', 
	 lhacode = [3, 2] ) 
 
rZM33 = 	 Parameter(name=u'rZM33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM33}', 
	 lhablock = u'ZMMIX', 
	 lhacode = [3, 3] ) 
 
iZM33 = 	 Parameter(name=u'iZM33', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{ZM33}', 
	 lhablock = u'IMZMMIX', 
	 lhacode = [3, 3] ) 
 
aEWM1 = 	 Parameter(name=u'aEWM1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 137.035999679, 
	 texname = u'\\text{aEWM1}', 
	 lhablock = u'SMINPUTS', 
	 lhacode = [1] ) 
 
aS = 	 Parameter(name=u'aS', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0.119, 
	 texname = u'\\text{aS}', 
	 lhablock = u'SMINPUTS', 
	 lhacode = [3] ) 
 
yu11 = 	 Parameter(name=u'yu11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryu11 + complex(0,1)*iyu11', 
	 texname = u'\\text{yu11}' ) 
 
yu12 = 	 Parameter(name=u'yu12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryu12 + complex(0,1)*iyu12', 
	 texname = u'\\text{yu12}' ) 
 
yu13 = 	 Parameter(name=u'yu13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryu13 + complex(0,1)*iyu13', 
	 texname = u'\\text{yu13}' ) 
 
yu21 = 	 Parameter(name=u'yu21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryu21 + complex(0,1)*iyu21', 
	 texname = u'\\text{yu21}' ) 
 
yu22 = 	 Parameter(name=u'yu22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryu22 + complex(0,1)*iyu22', 
	 texname = u'\\text{yu22}' ) 
 
yu23 = 	 Parameter(name=u'yu23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryu23 + complex(0,1)*iyu23', 
	 texname = u'\\text{yu23}' ) 
 
yu31 = 	 Parameter(name=u'yu31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryu31 + complex(0,1)*iyu31', 
	 texname = u'\\text{yu31}' ) 
 
yu32 = 	 Parameter(name=u'yu32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryu32 + complex(0,1)*iyu32', 
	 texname = u'\\text{yu32}' ) 
 
yu33 = 	 Parameter(name=u'yu33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryu33 + complex(0,1)*iyu33', 
	 texname = u'\\text{yu33}' ) 
 
yd11 = 	 Parameter(name=u'yd11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryd11 + complex(0,1)*iyd11', 
	 texname = u'\\text{yd11}' ) 
 
yd12 = 	 Parameter(name=u'yd12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryd12 + complex(0,1)*iyd12', 
	 texname = u'\\text{yd12}' ) 
 
yd13 = 	 Parameter(name=u'yd13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryd13 + complex(0,1)*iyd13', 
	 texname = u'\\text{yd13}' ) 
 
yd21 = 	 Parameter(name=u'yd21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryd21 + complex(0,1)*iyd21', 
	 texname = u'\\text{yd21}' ) 
 
yd22 = 	 Parameter(name=u'yd22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryd22 + complex(0,1)*iyd22', 
	 texname = u'\\text{yd22}' ) 
 
yd23 = 	 Parameter(name=u'yd23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryd23 + complex(0,1)*iyd23', 
	 texname = u'\\text{yd23}' ) 
 
yd31 = 	 Parameter(name=u'yd31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryd31 + complex(0,1)*iyd31', 
	 texname = u'\\text{yd31}' ) 
 
yd32 = 	 Parameter(name=u'yd32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryd32 + complex(0,1)*iyd32', 
	 texname = u'\\text{yd32}' ) 
 
yd33 = 	 Parameter(name=u'yd33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ryd33 + complex(0,1)*iyd33', 
	 texname = u'\\text{yd33}' ) 
 
ye11 = 	 Parameter(name=u'ye11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rye11 + complex(0,1)*iye11', 
	 texname = u'\\text{ye11}' ) 
 
ye12 = 	 Parameter(name=u'ye12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rye12 + complex(0,1)*iye12', 
	 texname = u'\\text{ye12}' ) 
 
ye13 = 	 Parameter(name=u'ye13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rye13 + complex(0,1)*iye13', 
	 texname = u'\\text{ye13}' ) 
 
ye21 = 	 Parameter(name=u'ye21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rye21 + complex(0,1)*iye21', 
	 texname = u'\\text{ye21}' ) 
 
ye22 = 	 Parameter(name=u'ye22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rye22 + complex(0,1)*iye22', 
	 texname = u'\\text{ye22}' ) 
 
ye23 = 	 Parameter(name=u'ye23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rye23 + complex(0,1)*iye23', 
	 texname = u'\\text{ye23}' ) 
 
ye31 = 	 Parameter(name=u'ye31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rye31 + complex(0,1)*iye31', 
	 texname = u'\\text{ye31}' ) 
 
ye32 = 	 Parameter(name=u'ye32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rye32 + complex(0,1)*iye32', 
	 texname = u'\\text{ye32}' ) 
 
ye33 = 	 Parameter(name=u'ye33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rye33 + complex(0,1)*iye33', 
	 texname = u'\\text{ye33}' ) 
 
CW111 = 	 Parameter(name=u'CW111', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rCW111 + complex(0,1)*iCW111', 
	 texname = u'\\text{CW111}' ) 
 
CW112 = 	 Parameter(name=u'CW112', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rCW112 + complex(0,1)*iCW112', 
	 texname = u'\\text{CW112}' ) 
 
CW113 = 	 Parameter(name=u'CW113', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rCW113 + complex(0,1)*iCW113', 
	 texname = u'\\text{CW113}' ) 
 
CW121 = 	 Parameter(name=u'CW121', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rCW121 + complex(0,1)*iCW121', 
	 texname = u'\\text{CW121}' ) 
 
CW122 = 	 Parameter(name=u'CW122', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rCW122 + complex(0,1)*iCW122', 
	 texname = u'\\text{CW122}' ) 
 
CW123 = 	 Parameter(name=u'CW123', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rCW123 + complex(0,1)*iCW123', 
	 texname = u'\\text{CW123}' ) 
 
CW131 = 	 Parameter(name=u'CW131', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rCW131 + complex(0,1)*iCW131', 
	 texname = u'\\text{CW131}' ) 
 
CW132 = 	 Parameter(name=u'CW132', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rCW132 + complex(0,1)*iCW132', 
	 texname = u'\\text{CW132}' ) 
 
CW133 = 	 Parameter(name=u'CW133', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rCW133 + complex(0,1)*iCW133', 
	 texname = u'\\text{CW133}' ) 
 
gHR = 	 Parameter(name=u'gHR', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rgHR + complex(0,1)*igHR', 
	 texname = u'\\text{gHR}' ) 
 
gHS = 	 Parameter(name=u'gHS', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rgHS + complex(0,1)*igHS', 
	 texname = u'\\text{gHS}' ) 
 
ghrp = 	 Parameter(name=u'ghrp', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rghrp + complex(0,1)*ighrp', 
	 texname = u'\\text{ghrp}' ) 
 
lambR = 	 Parameter(name=u'lambR', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rlambR + complex(0,1)*ilambR', 
	 texname = u'\\text{lambR}' ) 
 
lambS = 	 Parameter(name=u'lambS', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rlambS + complex(0,1)*ilambS', 
	 texname = u'\\text{lambS}' ) 
 
Theta11 = 	 Parameter(name=u'Theta11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rTheta11 + complex(0,1)*iTheta11', 
	 texname = u'\\text{Theta11}' ) 
 
Theta12 = 	 Parameter(name=u'Theta12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rTheta12 + complex(0,1)*iTheta12', 
	 texname = u'\\text{Theta12}' ) 
 
Theta13 = 	 Parameter(name=u'Theta13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rTheta13 + complex(0,1)*iTheta13', 
	 texname = u'\\text{Theta13}' ) 
 
Theta21 = 	 Parameter(name=u'Theta21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rTheta21 + complex(0,1)*iTheta21', 
	 texname = u'\\text{Theta21}' ) 
 
Theta22 = 	 Parameter(name=u'Theta22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rTheta22 + complex(0,1)*iTheta22', 
	 texname = u'\\text{Theta22}' ) 
 
Theta23 = 	 Parameter(name=u'Theta23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rTheta23 + complex(0,1)*iTheta23', 
	 texname = u'\\text{Theta23}' ) 
 
Theta31 = 	 Parameter(name=u'Theta31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rTheta31 + complex(0,1)*iTheta31', 
	 texname = u'\\text{Theta31}' ) 
 
Theta32 = 	 Parameter(name=u'Theta32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rTheta32 + complex(0,1)*iTheta32', 
	 texname = u'\\text{Theta32}' ) 
 
Theta33 = 	 Parameter(name=u'Theta33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rTheta33 + complex(0,1)*iTheta33', 
	 texname = u'\\text{Theta33}' ) 
 
Omega11 = 	 Parameter(name=u'Omega11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rOmega11 + complex(0,1)*iOmega11', 
	 texname = u'\\text{Omega11}' ) 
 
Omega12 = 	 Parameter(name=u'Omega12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rOmega12 + complex(0,1)*iOmega12', 
	 texname = u'\\text{Omega12}' ) 
 
Omega13 = 	 Parameter(name=u'Omega13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rOmega13 + complex(0,1)*iOmega13', 
	 texname = u'\\text{Omega13}' ) 
 
Omega21 = 	 Parameter(name=u'Omega21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rOmega21 + complex(0,1)*iOmega21', 
	 texname = u'\\text{Omega21}' ) 
 
Omega22 = 	 Parameter(name=u'Omega22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rOmega22 + complex(0,1)*iOmega22', 
	 texname = u'\\text{Omega22}' ) 
 
Omega23 = 	 Parameter(name=u'Omega23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rOmega23 + complex(0,1)*iOmega23', 
	 texname = u'\\text{Omega23}' ) 
 
Omega31 = 	 Parameter(name=u'Omega31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rOmega31 + complex(0,1)*iOmega31', 
	 texname = u'\\text{Omega31}' ) 
 
Omega32 = 	 Parameter(name=u'Omega32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rOmega32 + complex(0,1)*iOmega32', 
	 texname = u'\\text{Omega32}' ) 
 
Omega33 = 	 Parameter(name=u'Omega33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rOmega33 + complex(0,1)*iOmega33', 
	 texname = u'\\text{Omega33}' ) 
 
Upsilon11 = 	 Parameter(name=u'Upsilon11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rUpsilon11 + complex(0,1)*iUpsilon11', 
	 texname = u'\\text{Upsilon11}' ) 
 
Upsilon12 = 	 Parameter(name=u'Upsilon12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rUpsilon12 + complex(0,1)*iUpsilon12', 
	 texname = u'\\text{Upsilon12}' ) 
 
Upsilon13 = 	 Parameter(name=u'Upsilon13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rUpsilon13 + complex(0,1)*iUpsilon13', 
	 texname = u'\\text{Upsilon13}' ) 
 
Upsilon21 = 	 Parameter(name=u'Upsilon21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rUpsilon21 + complex(0,1)*iUpsilon21', 
	 texname = u'\\text{Upsilon21}' ) 
 
Upsilon22 = 	 Parameter(name=u'Upsilon22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rUpsilon22 + complex(0,1)*iUpsilon22', 
	 texname = u'\\text{Upsilon22}' ) 
 
Upsilon23 = 	 Parameter(name=u'Upsilon23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rUpsilon23 + complex(0,1)*iUpsilon23', 
	 texname = u'\\text{Upsilon23}' ) 
 
Upsilon31 = 	 Parameter(name=u'Upsilon31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rUpsilon31 + complex(0,1)*iUpsilon31', 
	 texname = u'\\text{Upsilon31}' ) 
 
Upsilon32 = 	 Parameter(name=u'Upsilon32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rUpsilon32 + complex(0,1)*iUpsilon32', 
	 texname = u'\\text{Upsilon32}' ) 
 
Upsilon33 = 	 Parameter(name=u'Upsilon33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rUpsilon33 + complex(0,1)*iUpsilon33', 
	 texname = u'\\text{Upsilon33}' ) 
 
lRRS = 	 Parameter(name=u'lRRS', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rlRRS + complex(0,1)*ilRRS', 
	 texname = u'\\text{lRRS}' ) 
 
a1 = 	 Parameter(name=u'a1', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'ra1 + complex(0,1)*ia1', 
	 texname = u'\\text{a1}' ) 
 
RRSS = 	 Parameter(name=u'RRSS', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rRRSS + complex(0,1)*iRRSS', 
	 texname = u'\\text{RRSS}' ) 
 
ZH11 = 	 Parameter(name=u'ZH11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZH11 + complex(0,1)*iZH11', 
	 texname = u'\\text{ZH11}' ) 
 
ZH12 = 	 Parameter(name=u'ZH12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZH12 + complex(0,1)*iZH12', 
	 texname = u'\\text{ZH12}' ) 
 
ZH21 = 	 Parameter(name=u'ZH21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZH21 + complex(0,1)*iZH21', 
	 texname = u'\\text{ZH21}' ) 
 
ZH22 = 	 Parameter(name=u'ZH22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZH22 + complex(0,1)*iZH22', 
	 texname = u'\\text{ZH22}' ) 
 
ZDL11 = 	 Parameter(name=u'ZDL11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDL11 + complex(0,1)*iZDL11', 
	 texname = u'\\text{ZDL11}' ) 
 
ZDL12 = 	 Parameter(name=u'ZDL12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDL12 + complex(0,1)*iZDL12', 
	 texname = u'\\text{ZDL12}' ) 
 
ZDL13 = 	 Parameter(name=u'ZDL13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDL13 + complex(0,1)*iZDL13', 
	 texname = u'\\text{ZDL13}' ) 
 
ZDL21 = 	 Parameter(name=u'ZDL21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDL21 + complex(0,1)*iZDL21', 
	 texname = u'\\text{ZDL21}' ) 
 
ZDL22 = 	 Parameter(name=u'ZDL22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDL22 + complex(0,1)*iZDL22', 
	 texname = u'\\text{ZDL22}' ) 
 
ZDL23 = 	 Parameter(name=u'ZDL23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDL23 + complex(0,1)*iZDL23', 
	 texname = u'\\text{ZDL23}' ) 
 
ZDL31 = 	 Parameter(name=u'ZDL31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDL31 + complex(0,1)*iZDL31', 
	 texname = u'\\text{ZDL31}' ) 
 
ZDL32 = 	 Parameter(name=u'ZDL32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDL32 + complex(0,1)*iZDL32', 
	 texname = u'\\text{ZDL32}' ) 
 
ZDL33 = 	 Parameter(name=u'ZDL33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDL33 + complex(0,1)*iZDL33', 
	 texname = u'\\text{ZDL33}' ) 
 
ZDR11 = 	 Parameter(name=u'ZDR11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDR11 + complex(0,1)*iZDR11', 
	 texname = u'\\text{ZDR11}' ) 
 
ZDR12 = 	 Parameter(name=u'ZDR12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDR12 + complex(0,1)*iZDR12', 
	 texname = u'\\text{ZDR12}' ) 
 
ZDR13 = 	 Parameter(name=u'ZDR13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDR13 + complex(0,1)*iZDR13', 
	 texname = u'\\text{ZDR13}' ) 
 
ZDR21 = 	 Parameter(name=u'ZDR21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDR21 + complex(0,1)*iZDR21', 
	 texname = u'\\text{ZDR21}' ) 
 
ZDR22 = 	 Parameter(name=u'ZDR22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDR22 + complex(0,1)*iZDR22', 
	 texname = u'\\text{ZDR22}' ) 
 
ZDR23 = 	 Parameter(name=u'ZDR23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDR23 + complex(0,1)*iZDR23', 
	 texname = u'\\text{ZDR23}' ) 
 
ZDR31 = 	 Parameter(name=u'ZDR31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDR31 + complex(0,1)*iZDR31', 
	 texname = u'\\text{ZDR31}' ) 
 
ZDR32 = 	 Parameter(name=u'ZDR32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDR32 + complex(0,1)*iZDR32', 
	 texname = u'\\text{ZDR32}' ) 
 
ZDR33 = 	 Parameter(name=u'ZDR33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZDR33 + complex(0,1)*iZDR33', 
	 texname = u'\\text{ZDR33}' ) 
 
ZUL11 = 	 Parameter(name=u'ZUL11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUL11 + complex(0,1)*iZUL11', 
	 texname = u'\\text{ZUL11}' ) 
 
ZUL12 = 	 Parameter(name=u'ZUL12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUL12 + complex(0,1)*iZUL12', 
	 texname = u'\\text{ZUL12}' ) 
 
ZUL13 = 	 Parameter(name=u'ZUL13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUL13 + complex(0,1)*iZUL13', 
	 texname = u'\\text{ZUL13}' ) 
 
ZUL21 = 	 Parameter(name=u'ZUL21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUL21 + complex(0,1)*iZUL21', 
	 texname = u'\\text{ZUL21}' ) 
 
ZUL22 = 	 Parameter(name=u'ZUL22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUL22 + complex(0,1)*iZUL22', 
	 texname = u'\\text{ZUL22}' ) 
 
ZUL23 = 	 Parameter(name=u'ZUL23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUL23 + complex(0,1)*iZUL23', 
	 texname = u'\\text{ZUL23}' ) 
 
ZUL31 = 	 Parameter(name=u'ZUL31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUL31 + complex(0,1)*iZUL31', 
	 texname = u'\\text{ZUL31}' ) 
 
ZUL32 = 	 Parameter(name=u'ZUL32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUL32 + complex(0,1)*iZUL32', 
	 texname = u'\\text{ZUL32}' ) 
 
ZUL33 = 	 Parameter(name=u'ZUL33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUL33 + complex(0,1)*iZUL33', 
	 texname = u'\\text{ZUL33}' ) 
 
ZUR11 = 	 Parameter(name=u'ZUR11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUR11 + complex(0,1)*iZUR11', 
	 texname = u'\\text{ZUR11}' ) 
 
ZUR12 = 	 Parameter(name=u'ZUR12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUR12 + complex(0,1)*iZUR12', 
	 texname = u'\\text{ZUR12}' ) 
 
ZUR13 = 	 Parameter(name=u'ZUR13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUR13 + complex(0,1)*iZUR13', 
	 texname = u'\\text{ZUR13}' ) 
 
ZUR21 = 	 Parameter(name=u'ZUR21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUR21 + complex(0,1)*iZUR21', 
	 texname = u'\\text{ZUR21}' ) 
 
ZUR22 = 	 Parameter(name=u'ZUR22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUR22 + complex(0,1)*iZUR22', 
	 texname = u'\\text{ZUR22}' ) 
 
ZUR23 = 	 Parameter(name=u'ZUR23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUR23 + complex(0,1)*iZUR23', 
	 texname = u'\\text{ZUR23}' ) 
 
ZUR31 = 	 Parameter(name=u'ZUR31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUR31 + complex(0,1)*iZUR31', 
	 texname = u'\\text{ZUR31}' ) 
 
ZUR32 = 	 Parameter(name=u'ZUR32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUR32 + complex(0,1)*iZUR32', 
	 texname = u'\\text{ZUR32}' ) 
 
ZUR33 = 	 Parameter(name=u'ZUR33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZUR33 + complex(0,1)*iZUR33', 
	 texname = u'\\text{ZUR33}' ) 
 
ZEL11 = 	 Parameter(name=u'ZEL11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZEL11 + complex(0,1)*iZEL11', 
	 texname = u'\\text{ZEL11}' ) 
 
ZEL12 = 	 Parameter(name=u'ZEL12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZEL12 + complex(0,1)*iZEL12', 
	 texname = u'\\text{ZEL12}' ) 
 
ZEL13 = 	 Parameter(name=u'ZEL13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZEL13 + complex(0,1)*iZEL13', 
	 texname = u'\\text{ZEL13}' ) 
 
ZEL21 = 	 Parameter(name=u'ZEL21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZEL21 + complex(0,1)*iZEL21', 
	 texname = u'\\text{ZEL21}' ) 
 
ZEL22 = 	 Parameter(name=u'ZEL22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZEL22 + complex(0,1)*iZEL22', 
	 texname = u'\\text{ZEL22}' ) 
 
ZEL23 = 	 Parameter(name=u'ZEL23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZEL23 + complex(0,1)*iZEL23', 
	 texname = u'\\text{ZEL23}' ) 
 
ZEL31 = 	 Parameter(name=u'ZEL31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZEL31 + complex(0,1)*iZEL31', 
	 texname = u'\\text{ZEL31}' ) 
 
ZEL32 = 	 Parameter(name=u'ZEL32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZEL32 + complex(0,1)*iZEL32', 
	 texname = u'\\text{ZEL32}' ) 
 
ZEL33 = 	 Parameter(name=u'ZEL33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZEL33 + complex(0,1)*iZEL33', 
	 texname = u'\\text{ZEL33}' ) 
 
ZER11 = 	 Parameter(name=u'ZER11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZER11 + complex(0,1)*iZER11', 
	 texname = u'\\text{ZER11}' ) 
 
ZER12 = 	 Parameter(name=u'ZER12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZER12 + complex(0,1)*iZER12', 
	 texname = u'\\text{ZER12}' ) 
 
ZER13 = 	 Parameter(name=u'ZER13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZER13 + complex(0,1)*iZER13', 
	 texname = u'\\text{ZER13}' ) 
 
ZER21 = 	 Parameter(name=u'ZER21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZER21 + complex(0,1)*iZER21', 
	 texname = u'\\text{ZER21}' ) 
 
ZER22 = 	 Parameter(name=u'ZER22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZER22 + complex(0,1)*iZER22', 
	 texname = u'\\text{ZER22}' ) 
 
ZER23 = 	 Parameter(name=u'ZER23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZER23 + complex(0,1)*iZER23', 
	 texname = u'\\text{ZER23}' ) 
 
ZER31 = 	 Parameter(name=u'ZER31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZER31 + complex(0,1)*iZER31', 
	 texname = u'\\text{ZER31}' ) 
 
ZER32 = 	 Parameter(name=u'ZER32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZER32 + complex(0,1)*iZER32', 
	 texname = u'\\text{ZER32}' ) 
 
ZER33 = 	 Parameter(name=u'ZER33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZER33 + complex(0,1)*iZER33', 
	 texname = u'\\text{ZER33}' ) 
 
ZM11 = 	 Parameter(name=u'ZM11', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZM11 + complex(0,1)*iZM11', 
	 texname = u'\\text{ZM11}' ) 
 
ZM12 = 	 Parameter(name=u'ZM12', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZM12 + complex(0,1)*iZM12', 
	 texname = u'\\text{ZM12}' ) 
 
ZM13 = 	 Parameter(name=u'ZM13', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZM13 + complex(0,1)*iZM13', 
	 texname = u'\\text{ZM13}' ) 
 
ZM21 = 	 Parameter(name=u'ZM21', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZM21 + complex(0,1)*iZM21', 
	 texname = u'\\text{ZM21}' ) 
 
ZM22 = 	 Parameter(name=u'ZM22', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZM22 + complex(0,1)*iZM22', 
	 texname = u'\\text{ZM22}' ) 
 
ZM23 = 	 Parameter(name=u'ZM23', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZM23 + complex(0,1)*iZM23', 
	 texname = u'\\text{ZM23}' ) 
 
ZM31 = 	 Parameter(name=u'ZM31', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZM31 + complex(0,1)*iZM31', 
	 texname = u'\\text{ZM31}' ) 
 
ZM32 = 	 Parameter(name=u'ZM32', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZM32 + complex(0,1)*iZM32', 
	 texname = u'\\text{ZM32}' ) 
 
ZM33 = 	 Parameter(name=u'ZM33', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'rZM33 + complex(0,1)*iZM33', 
	 texname = u'\\text{ZM33}' ) 
 
G = 	 Parameter(name=u'G', 
	 nature = u'internal', 
	 type = u'real', 
	 value = u'2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)', 
	 texname = u'G') 
 
el = 	 Parameter(name=u'el', 
	 nature = u'internal', 
	 type = u'real', 
	 value = u'2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)', 
	 texname = u'el') 
 
TW = 	 Parameter(name=u'TW', 
	 nature = u'internal', 
	 type = u'real', 
	 value = u'cmath.asin(cmath.sqrt(1 - MWm**2/MZ**2))', 
	 texname = u'TW') 
 
g1 = 	 Parameter(name=u'g1', 
	 nature = u'internal', 
	 type = u'real', 
	 value = u'el*1./cmath.cos(TW)', 
	 texname = u'g1') 
 
g2 = 	 Parameter(name=u'g2', 
	 nature = u'internal', 
	 type = u'real', 
	 value = u'el*1./cmath.sin(TW)', 
	 texname = u'g2') 
 
vvSM = 	 Parameter(name=u'vvSM', 
	 nature = u'internal', 
	 type = u'real', 
	 value = u'2*cmath.sqrt(MWm**2/g2**2)', 
	 texname = u'vvSM') 
 
Lam = 	 Parameter(name=u'Lam', 
	 nature = u'internal', 
	 type = u'complex', 
	 value = u'Mh**2/vvSM**2', 
	 texname = u'Lam') 
 
RXiWm = 	 Parameter(name=u'RXiWm', 
	 nature = u'internal', 
	 type = u'real', 
	 value = u'1.', 
	 texname = u'RXiWm') 
 
RXiZ = 	 Parameter(name=u'RXiZ', 
	 nature = u'internal', 
	 type = u'real', 
	 value = u'1.', 
	 texname = u'RXiZ') 
 
HPP1 = 	 Parameter(name=u'HPP1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{HPP1}', 
	 lhablock = u'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,22,22] ) 
 
HGG1 = 	 Parameter(name=u'HGG1', 
	 nature = u'external', 
	 type = u'real', 
	 value = 0., 
	 texname = u'\\text{HGG1}', 
	 lhablock = u'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,21,21] ) 
 
