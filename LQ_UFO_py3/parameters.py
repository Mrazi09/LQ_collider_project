# ----------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.14.5 
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840    
# (c) Florian Staub, 2011  
# ----------------------------------------------------------------------  
# File created at 15:13 on 25.11.2022   
# ----------------------------------------------------------------------  
 
 
from object_library import all_parameters,Parameter 
 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
ZERO=Parameter(name='ZERO', 
                      nature='internal', 
                      type='real', 
                      value='0.0', 
                      texname='0') 
 
Md1 = 	 Parameter(name = 'Md1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0035, 
	 texname = '\\text{Md1}', 
	 lhablock = 'MASS', 
	 lhacode = [1]) 
 
Wd1 = 	 Parameter(name = 'Wd1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wd1}', 
	 lhablock = 'DECAY', 
	 lhacode = [1]) 
 
Md2 = 	 Parameter(name = 'Md2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.104, 
	 texname = '\\text{Md2}', 
	 lhablock = 'MASS', 
	 lhacode = [3]) 
 
Wd2 = 	 Parameter(name = 'Wd2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wd2}', 
	 lhablock = 'DECAY', 
	 lhacode = [3]) 
 
Md3 = 	 Parameter(name = 'Md3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 4.2, 
	 texname = '\\text{Md3}', 
	 lhablock = 'MASS', 
	 lhacode = [5]) 
 
Wd3 = 	 Parameter(name = 'Wd3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wd3}', 
	 lhablock = 'DECAY', 
	 lhacode = [5]) 
 
Mu1 = 	 Parameter(name = 'Mu1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0015, 
	 texname = '\\text{Mu1}', 
	 lhablock = 'MASS', 
	 lhacode = [2]) 
 
Wu1 = 	 Parameter(name = 'Wu1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wu1}', 
	 lhablock = 'DECAY', 
	 lhacode = [2]) 
 
Mu2 = 	 Parameter(name = 'Mu2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.27, 
	 texname = '\\text{Mu2}', 
	 lhablock = 'MASS', 
	 lhacode = [4]) 
 
Wu2 = 	 Parameter(name = 'Wu2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wu2}', 
	 lhablock = 'DECAY', 
	 lhacode = [4]) 
 
Mu3 = 	 Parameter(name = 'Mu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 171.2, 
	 texname = '\\text{Mu3}', 
	 lhablock = 'MASS', 
	 lhacode = [6]) 
 
Wu3 = 	 Parameter(name = 'Wu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.3853, 
	 texname = '\\text{Wu3}', 
	 lhablock = 'DECAY', 
	 lhacode = [6]) 
 
Me1 = 	 Parameter(name = 'Me1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.000511, 
	 texname = '\\text{Me1}', 
	 lhablock = 'MASS', 
	 lhacode = [11]) 
 
We1 = 	 Parameter(name = 'We1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{We1}', 
	 lhablock = 'DECAY', 
	 lhacode = [11]) 
 
Me2 = 	 Parameter(name = 'Me2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.105, 
	 texname = '\\text{Me2}', 
	 lhablock = 'MASS', 
	 lhacode = [13]) 
 
We2 = 	 Parameter(name = 'We2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{We2}', 
	 lhablock = 'DECAY', 
	 lhacode = [13]) 
 
Me3 = 	 Parameter(name = 'Me3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.776, 
	 texname = '\\text{Me3}', 
	 lhablock = 'MASS', 
	 lhacode = [15]) 
 
We3 = 	 Parameter(name = 'We3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{We3}', 
	 lhablock = 'DECAY', 
	 lhacode = [15]) 
 
MR = 	 Parameter(name = 'MR', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MR}', 
	 lhablock = 'MASS', 
	 lhacode = [999034]) 
 
WR = 	 Parameter(name = 'WR', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WR}', 
	 lhablock = 'DECAY', 
	 lhacode = [999034]) 
 
Mh = 	 Parameter(name = 'Mh', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mh}', 
	 lhablock = 'MASS', 
	 lhacode = [25]) 
 
Wh = 	 Parameter(name = 'Wh', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wh}', 
	 lhablock = 'DECAY', 
	 lhacode = [25]) 
 
MS1 = 	 Parameter(name = 'MS1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MS1}', 
	 lhablock = 'MASS', 
	 lhacode = [999014]) 
 
WS1 = 	 Parameter(name = 'WS1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WS1}', 
	 lhablock = 'DECAY', 
	 lhacode = [999014]) 
 
MS2 = 	 Parameter(name = 'MS2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MS2}', 
	 lhablock = 'MASS', 
	 lhacode = [999024]) 
 
WS2 = 	 Parameter(name = 'WS2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WS2}', 
	 lhablock = 'DECAY', 
	 lhacode = [999024]) 
 
MZ = 	 Parameter(name = 'MZ', 
	 nature = 'external', 
	 type = 'real', 
	 value = 91.188, 
	 texname = '\\text{MZ}', 
	 lhablock = 'MASS', 
	 lhacode = [23]) 
 
WZ = 	 Parameter(name = 'WZ', 
	 nature = 'external', 
	 type = 'real', 
	 value = 2.4414, 
	 texname = '\\text{WZ}', 
	 lhablock = 'DECAY', 
	 lhacode = [23]) 
 
MWm = 	 Parameter(name = 'MWm', 
	 nature = 'external', 
	 type = 'real', 
	 value = 80.379, 
	 texname = '\\text{MWm}', 
	 lhablock = 'MASS', 
	 lhacode = [24]) 
 
WWm = 	 Parameter(name = 'WWm', 
	 nature = 'external', 
	 type = 'real', 
	 value = 2.0476, 
	 texname = '\\text{WWm}', 
	 lhablock = 'DECAY', 
	 lhacode = [24]) 
 
ryu11 = 	 Parameter(name='ryu11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu11}', 
	 lhablock = 'YU', 
	 lhacode = [1, 1] ) 
 
iyu11 = 	 Parameter(name='iyu11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu11}', 
	 lhablock = 'IMYU', 
	 lhacode = [1, 1] ) 
 
ryu12 = 	 Parameter(name='ryu12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu12}', 
	 lhablock = 'YU', 
	 lhacode = [1, 2] ) 
 
iyu12 = 	 Parameter(name='iyu12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu12}', 
	 lhablock = 'IMYU', 
	 lhacode = [1, 2] ) 
 
ryu13 = 	 Parameter(name='ryu13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu13}', 
	 lhablock = 'YU', 
	 lhacode = [1, 3] ) 
 
iyu13 = 	 Parameter(name='iyu13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu13}', 
	 lhablock = 'IMYU', 
	 lhacode = [1, 3] ) 
 
ryu21 = 	 Parameter(name='ryu21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu21}', 
	 lhablock = 'YU', 
	 lhacode = [2, 1] ) 
 
iyu21 = 	 Parameter(name='iyu21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu21}', 
	 lhablock = 'IMYU', 
	 lhacode = [2, 1] ) 
 
ryu22 = 	 Parameter(name='ryu22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu22}', 
	 lhablock = 'YU', 
	 lhacode = [2, 2] ) 
 
iyu22 = 	 Parameter(name='iyu22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu22}', 
	 lhablock = 'IMYU', 
	 lhacode = [2, 2] ) 
 
ryu23 = 	 Parameter(name='ryu23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu23}', 
	 lhablock = 'YU', 
	 lhacode = [2, 3] ) 
 
iyu23 = 	 Parameter(name='iyu23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu23}', 
	 lhablock = 'IMYU', 
	 lhacode = [2, 3] ) 
 
ryu31 = 	 Parameter(name='ryu31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu31}', 
	 lhablock = 'YU', 
	 lhacode = [3, 1] ) 
 
iyu31 = 	 Parameter(name='iyu31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu31}', 
	 lhablock = 'IMYU', 
	 lhacode = [3, 1] ) 
 
ryu32 = 	 Parameter(name='ryu32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu32}', 
	 lhablock = 'YU', 
	 lhacode = [3, 2] ) 
 
iyu32 = 	 Parameter(name='iyu32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu32}', 
	 lhablock = 'IMYU', 
	 lhacode = [3, 2] ) 
 
ryu33 = 	 Parameter(name='ryu33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu33}', 
	 lhablock = 'YU', 
	 lhacode = [3, 3] ) 
 
iyu33 = 	 Parameter(name='iyu33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yu33}', 
	 lhablock = 'IMYU', 
	 lhacode = [3, 3] ) 
 
ryd11 = 	 Parameter(name='ryd11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd11}', 
	 lhablock = 'YD', 
	 lhacode = [1, 1] ) 
 
iyd11 = 	 Parameter(name='iyd11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd11}', 
	 lhablock = 'IMYD', 
	 lhacode = [1, 1] ) 
 
ryd12 = 	 Parameter(name='ryd12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd12}', 
	 lhablock = 'YD', 
	 lhacode = [1, 2] ) 
 
iyd12 = 	 Parameter(name='iyd12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd12}', 
	 lhablock = 'IMYD', 
	 lhacode = [1, 2] ) 
 
ryd13 = 	 Parameter(name='ryd13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd13}', 
	 lhablock = 'YD', 
	 lhacode = [1, 3] ) 
 
iyd13 = 	 Parameter(name='iyd13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd13}', 
	 lhablock = 'IMYD', 
	 lhacode = [1, 3] ) 
 
ryd21 = 	 Parameter(name='ryd21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd21}', 
	 lhablock = 'YD', 
	 lhacode = [2, 1] ) 
 
iyd21 = 	 Parameter(name='iyd21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd21}', 
	 lhablock = 'IMYD', 
	 lhacode = [2, 1] ) 
 
ryd22 = 	 Parameter(name='ryd22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd22}', 
	 lhablock = 'YD', 
	 lhacode = [2, 2] ) 
 
iyd22 = 	 Parameter(name='iyd22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd22}', 
	 lhablock = 'IMYD', 
	 lhacode = [2, 2] ) 
 
ryd23 = 	 Parameter(name='ryd23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd23}', 
	 lhablock = 'YD', 
	 lhacode = [2, 3] ) 
 
iyd23 = 	 Parameter(name='iyd23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd23}', 
	 lhablock = 'IMYD', 
	 lhacode = [2, 3] ) 
 
ryd31 = 	 Parameter(name='ryd31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd31}', 
	 lhablock = 'YD', 
	 lhacode = [3, 1] ) 
 
iyd31 = 	 Parameter(name='iyd31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd31}', 
	 lhablock = 'IMYD', 
	 lhacode = [3, 1] ) 
 
ryd32 = 	 Parameter(name='ryd32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd32}', 
	 lhablock = 'YD', 
	 lhacode = [3, 2] ) 
 
iyd32 = 	 Parameter(name='iyd32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd32}', 
	 lhablock = 'IMYD', 
	 lhacode = [3, 2] ) 
 
ryd33 = 	 Parameter(name='ryd33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd33}', 
	 lhablock = 'YD', 
	 lhacode = [3, 3] ) 
 
iyd33 = 	 Parameter(name='iyd33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{yd33}', 
	 lhablock = 'IMYD', 
	 lhacode = [3, 3] ) 
 
rye11 = 	 Parameter(name='rye11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye11}', 
	 lhablock = 'YE', 
	 lhacode = [1, 1] ) 
 
iye11 = 	 Parameter(name='iye11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye11}', 
	 lhablock = 'IMYE', 
	 lhacode = [1, 1] ) 
 
rye12 = 	 Parameter(name='rye12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye12}', 
	 lhablock = 'YE', 
	 lhacode = [1, 2] ) 
 
iye12 = 	 Parameter(name='iye12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye12}', 
	 lhablock = 'IMYE', 
	 lhacode = [1, 2] ) 
 
rye13 = 	 Parameter(name='rye13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye13}', 
	 lhablock = 'YE', 
	 lhacode = [1, 3] ) 
 
iye13 = 	 Parameter(name='iye13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye13}', 
	 lhablock = 'IMYE', 
	 lhacode = [1, 3] ) 
 
rye21 = 	 Parameter(name='rye21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye21}', 
	 lhablock = 'YE', 
	 lhacode = [2, 1] ) 
 
iye21 = 	 Parameter(name='iye21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye21}', 
	 lhablock = 'IMYE', 
	 lhacode = [2, 1] ) 
 
rye22 = 	 Parameter(name='rye22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye22}', 
	 lhablock = 'YE', 
	 lhacode = [2, 2] ) 
 
iye22 = 	 Parameter(name='iye22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye22}', 
	 lhablock = 'IMYE', 
	 lhacode = [2, 2] ) 
 
rye23 = 	 Parameter(name='rye23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye23}', 
	 lhablock = 'YE', 
	 lhacode = [2, 3] ) 
 
iye23 = 	 Parameter(name='iye23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye23}', 
	 lhablock = 'IMYE', 
	 lhacode = [2, 3] ) 
 
rye31 = 	 Parameter(name='rye31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye31}', 
	 lhablock = 'YE', 
	 lhacode = [3, 1] ) 
 
iye31 = 	 Parameter(name='iye31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye31}', 
	 lhablock = 'IMYE', 
	 lhacode = [3, 1] ) 
 
rye32 = 	 Parameter(name='rye32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye32}', 
	 lhablock = 'YE', 
	 lhacode = [3, 2] ) 
 
iye32 = 	 Parameter(name='iye32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye32}', 
	 lhablock = 'IMYE', 
	 lhacode = [3, 2] ) 
 
rye33 = 	 Parameter(name='rye33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye33}', 
	 lhablock = 'YE', 
	 lhacode = [3, 3] ) 
 
iye33 = 	 Parameter(name='iye33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ye33}', 
	 lhablock = 'IMYE', 
	 lhacode = [3, 3] ) 
 
rCW111 = 	 Parameter(name='rCW111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW111}', 
	 lhablock = 'CW1', 
	 lhacode = [1, 1] ) 
 
iCW111 = 	 Parameter(name='iCW111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW111}', 
	 lhablock = 'IMCW1', 
	 lhacode = [1, 1] ) 
 
rCW112 = 	 Parameter(name='rCW112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW112}', 
	 lhablock = 'CW1', 
	 lhacode = [1, 2] ) 
 
iCW112 = 	 Parameter(name='iCW112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW112}', 
	 lhablock = 'IMCW1', 
	 lhacode = [1, 2] ) 
 
rCW113 = 	 Parameter(name='rCW113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW113}', 
	 lhablock = 'CW1', 
	 lhacode = [1, 3] ) 
 
iCW113 = 	 Parameter(name='iCW113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW113}', 
	 lhablock = 'IMCW1', 
	 lhacode = [1, 3] ) 
 
rCW121 = 	 Parameter(name='rCW121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW121}', 
	 lhablock = 'CW1', 
	 lhacode = [2, 1] ) 
 
iCW121 = 	 Parameter(name='iCW121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW121}', 
	 lhablock = 'IMCW1', 
	 lhacode = [2, 1] ) 
 
rCW122 = 	 Parameter(name='rCW122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW122}', 
	 lhablock = 'CW1', 
	 lhacode = [2, 2] ) 
 
iCW122 = 	 Parameter(name='iCW122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW122}', 
	 lhablock = 'IMCW1', 
	 lhacode = [2, 2] ) 
 
rCW123 = 	 Parameter(name='rCW123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW123}', 
	 lhablock = 'CW1', 
	 lhacode = [2, 3] ) 
 
iCW123 = 	 Parameter(name='iCW123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW123}', 
	 lhablock = 'IMCW1', 
	 lhacode = [2, 3] ) 
 
rCW131 = 	 Parameter(name='rCW131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW131}', 
	 lhablock = 'CW1', 
	 lhacode = [3, 1] ) 
 
iCW131 = 	 Parameter(name='iCW131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW131}', 
	 lhablock = 'IMCW1', 
	 lhacode = [3, 1] ) 
 
rCW132 = 	 Parameter(name='rCW132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW132}', 
	 lhablock = 'CW1', 
	 lhacode = [3, 2] ) 
 
iCW132 = 	 Parameter(name='iCW132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW132}', 
	 lhablock = 'IMCW1', 
	 lhacode = [3, 2] ) 
 
rCW133 = 	 Parameter(name='rCW133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW133}', 
	 lhablock = 'CW1', 
	 lhacode = [3, 3] ) 
 
iCW133 = 	 Parameter(name='iCW133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{CW133}', 
	 lhablock = 'IMCW1', 
	 lhacode = [3, 3] ) 
 
rgHR = 	 Parameter(name='rgHR', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{gHR}', 
	 lhablock = 'GHR', 
	 lhacode = [1] ) 
 
igHR = 	 Parameter(name='igHR', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{gHR}', 
	 lhablock = 'IMGHR', 
	 lhacode = [1] ) 
 
rgHS = 	 Parameter(name='rgHS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{gHS}', 
	 lhablock = 'GHS', 
	 lhacode = [1] ) 
 
igHS = 	 Parameter(name='igHS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{gHS}', 
	 lhablock = 'IMGHS', 
	 lhacode = [1] ) 
 
rghrp = 	 Parameter(name='rghrp', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ghrp}', 
	 lhablock = 'GHRP', 
	 lhacode = [1] ) 
 
ighrp = 	 Parameter(name='ighrp', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ghrp}', 
	 lhablock = 'IMGHRP', 
	 lhacode = [1] ) 
 
rlambR = 	 Parameter(name='rlambR', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lambR}', 
	 lhablock = 'LAMBR', 
	 lhacode = [1] ) 
 
ilambR = 	 Parameter(name='ilambR', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lambR}', 
	 lhablock = 'IMLAMBR', 
	 lhacode = [1] ) 
 
rlambS = 	 Parameter(name='rlambS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lambS}', 
	 lhablock = 'LAMBS', 
	 lhacode = [1] ) 
 
ilambS = 	 Parameter(name='ilambS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lambS}', 
	 lhablock = 'IMLAMBS', 
	 lhacode = [1] ) 
 
rTheta11 = 	 Parameter(name='rTheta11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta11}', 
	 lhablock = 'THETA', 
	 lhacode = [1, 1] ) 
 
iTheta11 = 	 Parameter(name='iTheta11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta11}', 
	 lhablock = 'IMTHETA', 
	 lhacode = [1, 1] ) 
 
rTheta12 = 	 Parameter(name='rTheta12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta12}', 
	 lhablock = 'THETA', 
	 lhacode = [1, 2] ) 
 
iTheta12 = 	 Parameter(name='iTheta12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta12}', 
	 lhablock = 'IMTHETA', 
	 lhacode = [1, 2] ) 
 
rTheta13 = 	 Parameter(name='rTheta13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta13}', 
	 lhablock = 'THETA', 
	 lhacode = [1, 3] ) 
 
iTheta13 = 	 Parameter(name='iTheta13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta13}', 
	 lhablock = 'IMTHETA', 
	 lhacode = [1, 3] ) 
 
rTheta21 = 	 Parameter(name='rTheta21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta21}', 
	 lhablock = 'THETA', 
	 lhacode = [2, 1] ) 
 
iTheta21 = 	 Parameter(name='iTheta21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta21}', 
	 lhablock = 'IMTHETA', 
	 lhacode = [2, 1] ) 
 
rTheta22 = 	 Parameter(name='rTheta22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta22}', 
	 lhablock = 'THETA', 
	 lhacode = [2, 2] ) 
 
iTheta22 = 	 Parameter(name='iTheta22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta22}', 
	 lhablock = 'IMTHETA', 
	 lhacode = [2, 2] ) 
 
rTheta23 = 	 Parameter(name='rTheta23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta23}', 
	 lhablock = 'THETA', 
	 lhacode = [2, 3] ) 
 
iTheta23 = 	 Parameter(name='iTheta23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta23}', 
	 lhablock = 'IMTHETA', 
	 lhacode = [2, 3] ) 
 
rTheta31 = 	 Parameter(name='rTheta31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta31}', 
	 lhablock = 'THETA', 
	 lhacode = [3, 1] ) 
 
iTheta31 = 	 Parameter(name='iTheta31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta31}', 
	 lhablock = 'IMTHETA', 
	 lhacode = [3, 1] ) 
 
rTheta32 = 	 Parameter(name='rTheta32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta32}', 
	 lhablock = 'THETA', 
	 lhacode = [3, 2] ) 
 
iTheta32 = 	 Parameter(name='iTheta32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta32}', 
	 lhablock = 'IMTHETA', 
	 lhacode = [3, 2] ) 
 
rTheta33 = 	 Parameter(name='rTheta33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta33}', 
	 lhablock = 'THETA', 
	 lhacode = [3, 3] ) 
 
iTheta33 = 	 Parameter(name='iTheta33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Theta33}', 
	 lhablock = 'IMTHETA', 
	 lhacode = [3, 3] ) 
 
rOmega11 = 	 Parameter(name='rOmega11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega11}', 
	 lhablock = 'OMEGA', 
	 lhacode = [1, 1] ) 
 
iOmega11 = 	 Parameter(name='iOmega11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega11}', 
	 lhablock = 'IMOMEGA', 
	 lhacode = [1, 1] ) 
 
rOmega12 = 	 Parameter(name='rOmega12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega12}', 
	 lhablock = 'OMEGA', 
	 lhacode = [1, 2] ) 
 
iOmega12 = 	 Parameter(name='iOmega12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega12}', 
	 lhablock = 'IMOMEGA', 
	 lhacode = [1, 2] ) 
 
rOmega13 = 	 Parameter(name='rOmega13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega13}', 
	 lhablock = 'OMEGA', 
	 lhacode = [1, 3] ) 
 
iOmega13 = 	 Parameter(name='iOmega13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega13}', 
	 lhablock = 'IMOMEGA', 
	 lhacode = [1, 3] ) 
 
rOmega21 = 	 Parameter(name='rOmega21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega21}', 
	 lhablock = 'OMEGA', 
	 lhacode = [2, 1] ) 
 
iOmega21 = 	 Parameter(name='iOmega21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega21}', 
	 lhablock = 'IMOMEGA', 
	 lhacode = [2, 1] ) 
 
rOmega22 = 	 Parameter(name='rOmega22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega22}', 
	 lhablock = 'OMEGA', 
	 lhacode = [2, 2] ) 
 
iOmega22 = 	 Parameter(name='iOmega22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega22}', 
	 lhablock = 'IMOMEGA', 
	 lhacode = [2, 2] ) 
 
rOmega23 = 	 Parameter(name='rOmega23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega23}', 
	 lhablock = 'OMEGA', 
	 lhacode = [2, 3] ) 
 
iOmega23 = 	 Parameter(name='iOmega23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega23}', 
	 lhablock = 'IMOMEGA', 
	 lhacode = [2, 3] ) 
 
rOmega31 = 	 Parameter(name='rOmega31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega31}', 
	 lhablock = 'OMEGA', 
	 lhacode = [3, 1] ) 
 
iOmega31 = 	 Parameter(name='iOmega31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega31}', 
	 lhablock = 'IMOMEGA', 
	 lhacode = [3, 1] ) 
 
rOmega32 = 	 Parameter(name='rOmega32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega32}', 
	 lhablock = 'OMEGA', 
	 lhacode = [3, 2] ) 
 
iOmega32 = 	 Parameter(name='iOmega32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega32}', 
	 lhablock = 'IMOMEGA', 
	 lhacode = [3, 2] ) 
 
rOmega33 = 	 Parameter(name='rOmega33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega33}', 
	 lhablock = 'OMEGA', 
	 lhacode = [3, 3] ) 
 
iOmega33 = 	 Parameter(name='iOmega33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Omega33}', 
	 lhablock = 'IMOMEGA', 
	 lhacode = [3, 3] ) 
 
rUpsilon11 = 	 Parameter(name='rUpsilon11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon11}', 
	 lhablock = 'UPSILON', 
	 lhacode = [1, 1] ) 
 
iUpsilon11 = 	 Parameter(name='iUpsilon11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon11}', 
	 lhablock = 'IMUPSILON', 
	 lhacode = [1, 1] ) 
 
rUpsilon12 = 	 Parameter(name='rUpsilon12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon12}', 
	 lhablock = 'UPSILON', 
	 lhacode = [1, 2] ) 
 
iUpsilon12 = 	 Parameter(name='iUpsilon12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon12}', 
	 lhablock = 'IMUPSILON', 
	 lhacode = [1, 2] ) 
 
rUpsilon13 = 	 Parameter(name='rUpsilon13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon13}', 
	 lhablock = 'UPSILON', 
	 lhacode = [1, 3] ) 
 
iUpsilon13 = 	 Parameter(name='iUpsilon13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon13}', 
	 lhablock = 'IMUPSILON', 
	 lhacode = [1, 3] ) 
 
rUpsilon21 = 	 Parameter(name='rUpsilon21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon21}', 
	 lhablock = 'UPSILON', 
	 lhacode = [2, 1] ) 
 
iUpsilon21 = 	 Parameter(name='iUpsilon21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon21}', 
	 lhablock = 'IMUPSILON', 
	 lhacode = [2, 1] ) 
 
rUpsilon22 = 	 Parameter(name='rUpsilon22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon22}', 
	 lhablock = 'UPSILON', 
	 lhacode = [2, 2] ) 
 
iUpsilon22 = 	 Parameter(name='iUpsilon22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon22}', 
	 lhablock = 'IMUPSILON', 
	 lhacode = [2, 2] ) 
 
rUpsilon23 = 	 Parameter(name='rUpsilon23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon23}', 
	 lhablock = 'UPSILON', 
	 lhacode = [2, 3] ) 
 
iUpsilon23 = 	 Parameter(name='iUpsilon23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon23}', 
	 lhablock = 'IMUPSILON', 
	 lhacode = [2, 3] ) 
 
rUpsilon31 = 	 Parameter(name='rUpsilon31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon31}', 
	 lhablock = 'UPSILON', 
	 lhacode = [3, 1] ) 
 
iUpsilon31 = 	 Parameter(name='iUpsilon31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon31}', 
	 lhablock = 'IMUPSILON', 
	 lhacode = [3, 1] ) 
 
rUpsilon32 = 	 Parameter(name='rUpsilon32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon32}', 
	 lhablock = 'UPSILON', 
	 lhacode = [3, 2] ) 
 
iUpsilon32 = 	 Parameter(name='iUpsilon32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon32}', 
	 lhablock = 'IMUPSILON', 
	 lhacode = [3, 2] ) 
 
rUpsilon33 = 	 Parameter(name='rUpsilon33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon33}', 
	 lhablock = 'UPSILON', 
	 lhacode = [3, 3] ) 
 
iUpsilon33 = 	 Parameter(name='iUpsilon33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Upsilon33}', 
	 lhablock = 'IMUPSILON', 
	 lhacode = [3, 3] ) 
 
rlRRS = 	 Parameter(name='rlRRS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lRRS}', 
	 lhablock = 'LRRS', 
	 lhacode = [1] ) 
 
ilRRS = 	 Parameter(name='ilRRS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lRRS}', 
	 lhablock = 'IMLRRS', 
	 lhacode = [1] ) 
 
ra1 = 	 Parameter(name='ra1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{a1}', 
	 lhablock = 'A1', 
	 lhacode = [1] ) 
 
ia1 = 	 Parameter(name='ia1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{a1}', 
	 lhablock = 'IMA1', 
	 lhacode = [1] ) 
 
rRRSS = 	 Parameter(name='rRRSS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RRSS}', 
	 lhablock = 'RRSS', 
	 lhacode = [1] ) 
 
iRRSS = 	 Parameter(name='iRRSS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RRSS}', 
	 lhablock = 'IMRRSS', 
	 lhacode = [1] ) 
 
rZH11 = 	 Parameter(name='rZH11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH11}', 
	 lhablock = 'ZHMIX', 
	 lhacode = [1, 1] ) 
 
iZH11 = 	 Parameter(name='iZH11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH11}', 
	 lhablock = 'IMZHMIX', 
	 lhacode = [1, 1] ) 
 
rZH12 = 	 Parameter(name='rZH12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH12}', 
	 lhablock = 'ZHMIX', 
	 lhacode = [1, 2] ) 
 
iZH12 = 	 Parameter(name='iZH12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH12}', 
	 lhablock = 'IMZHMIX', 
	 lhacode = [1, 2] ) 
 
rZH21 = 	 Parameter(name='rZH21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH21}', 
	 lhablock = 'ZHMIX', 
	 lhacode = [2, 1] ) 
 
iZH21 = 	 Parameter(name='iZH21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH21}', 
	 lhablock = 'IMZHMIX', 
	 lhacode = [2, 1] ) 
 
rZH22 = 	 Parameter(name='rZH22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH22}', 
	 lhablock = 'ZHMIX', 
	 lhacode = [2, 2] ) 
 
iZH22 = 	 Parameter(name='iZH22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH22}', 
	 lhablock = 'IMZHMIX', 
	 lhacode = [2, 2] ) 
 
rZDL11 = 	 Parameter(name='rZDL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL11}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 1] ) 
 
iZDL11 = 	 Parameter(name='iZDL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL11}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 1] ) 
 
rZDL12 = 	 Parameter(name='rZDL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL12}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 2] ) 
 
iZDL12 = 	 Parameter(name='iZDL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL12}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 2] ) 
 
rZDL13 = 	 Parameter(name='rZDL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL13}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 3] ) 
 
iZDL13 = 	 Parameter(name='iZDL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL13}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 3] ) 
 
rZDL21 = 	 Parameter(name='rZDL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL21}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 1] ) 
 
iZDL21 = 	 Parameter(name='iZDL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL21}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 1] ) 
 
rZDL22 = 	 Parameter(name='rZDL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL22}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 2] ) 
 
iZDL22 = 	 Parameter(name='iZDL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL22}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 2] ) 
 
rZDL23 = 	 Parameter(name='rZDL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL23}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 3] ) 
 
iZDL23 = 	 Parameter(name='iZDL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL23}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 3] ) 
 
rZDL31 = 	 Parameter(name='rZDL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL31}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 1] ) 
 
iZDL31 = 	 Parameter(name='iZDL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL31}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 1] ) 
 
rZDL32 = 	 Parameter(name='rZDL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL32}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 2] ) 
 
iZDL32 = 	 Parameter(name='iZDL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL32}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 2] ) 
 
rZDL33 = 	 Parameter(name='rZDL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL33}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 3] ) 
 
iZDL33 = 	 Parameter(name='iZDL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL33}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 3] ) 
 
rZDR11 = 	 Parameter(name='rZDR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR11}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 1] ) 
 
iZDR11 = 	 Parameter(name='iZDR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR11}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 1] ) 
 
rZDR12 = 	 Parameter(name='rZDR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR12}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 2] ) 
 
iZDR12 = 	 Parameter(name='iZDR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR12}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 2] ) 
 
rZDR13 = 	 Parameter(name='rZDR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR13}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 3] ) 
 
iZDR13 = 	 Parameter(name='iZDR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR13}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 3] ) 
 
rZDR21 = 	 Parameter(name='rZDR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR21}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 1] ) 
 
iZDR21 = 	 Parameter(name='iZDR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR21}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 1] ) 
 
rZDR22 = 	 Parameter(name='rZDR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR22}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 2] ) 
 
iZDR22 = 	 Parameter(name='iZDR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR22}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 2] ) 
 
rZDR23 = 	 Parameter(name='rZDR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR23}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 3] ) 
 
iZDR23 = 	 Parameter(name='iZDR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR23}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 3] ) 
 
rZDR31 = 	 Parameter(name='rZDR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR31}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 1] ) 
 
iZDR31 = 	 Parameter(name='iZDR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR31}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 1] ) 
 
rZDR32 = 	 Parameter(name='rZDR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR32}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 2] ) 
 
iZDR32 = 	 Parameter(name='iZDR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR32}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 2] ) 
 
rZDR33 = 	 Parameter(name='rZDR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR33}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 3] ) 
 
iZDR33 = 	 Parameter(name='iZDR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR33}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 3] ) 
 
rZUL11 = 	 Parameter(name='rZUL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL11}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 1] ) 
 
iZUL11 = 	 Parameter(name='iZUL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL11}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 1] ) 
 
rZUL12 = 	 Parameter(name='rZUL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL12}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 2] ) 
 
iZUL12 = 	 Parameter(name='iZUL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL12}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 2] ) 
 
rZUL13 = 	 Parameter(name='rZUL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL13}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 3] ) 
 
iZUL13 = 	 Parameter(name='iZUL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL13}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 3] ) 
 
rZUL21 = 	 Parameter(name='rZUL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL21}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 1] ) 
 
iZUL21 = 	 Parameter(name='iZUL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL21}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 1] ) 
 
rZUL22 = 	 Parameter(name='rZUL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL22}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 2] ) 
 
iZUL22 = 	 Parameter(name='iZUL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL22}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 2] ) 
 
rZUL23 = 	 Parameter(name='rZUL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL23}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 3] ) 
 
iZUL23 = 	 Parameter(name='iZUL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL23}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 3] ) 
 
rZUL31 = 	 Parameter(name='rZUL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL31}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 1] ) 
 
iZUL31 = 	 Parameter(name='iZUL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL31}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 1] ) 
 
rZUL32 = 	 Parameter(name='rZUL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL32}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 2] ) 
 
iZUL32 = 	 Parameter(name='iZUL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL32}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 2] ) 
 
rZUL33 = 	 Parameter(name='rZUL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL33}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 3] ) 
 
iZUL33 = 	 Parameter(name='iZUL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL33}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 3] ) 
 
rZUR11 = 	 Parameter(name='rZUR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR11}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 1] ) 
 
iZUR11 = 	 Parameter(name='iZUR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR11}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 1] ) 
 
rZUR12 = 	 Parameter(name='rZUR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR12}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 2] ) 
 
iZUR12 = 	 Parameter(name='iZUR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR12}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 2] ) 
 
rZUR13 = 	 Parameter(name='rZUR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR13}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 3] ) 
 
iZUR13 = 	 Parameter(name='iZUR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR13}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 3] ) 
 
rZUR21 = 	 Parameter(name='rZUR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR21}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 1] ) 
 
iZUR21 = 	 Parameter(name='iZUR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR21}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 1] ) 
 
rZUR22 = 	 Parameter(name='rZUR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR22}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 2] ) 
 
iZUR22 = 	 Parameter(name='iZUR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR22}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 2] ) 
 
rZUR23 = 	 Parameter(name='rZUR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR23}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 3] ) 
 
iZUR23 = 	 Parameter(name='iZUR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR23}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 3] ) 
 
rZUR31 = 	 Parameter(name='rZUR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR31}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 1] ) 
 
iZUR31 = 	 Parameter(name='iZUR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR31}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 1] ) 
 
rZUR32 = 	 Parameter(name='rZUR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR32}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 2] ) 
 
iZUR32 = 	 Parameter(name='iZUR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR32}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 2] ) 
 
rZUR33 = 	 Parameter(name='rZUR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR33}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 3] ) 
 
iZUR33 = 	 Parameter(name='iZUR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR33}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 3] ) 
 
rZEL11 = 	 Parameter(name='rZEL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL11}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 1] ) 
 
iZEL11 = 	 Parameter(name='iZEL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL11}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 1] ) 
 
rZEL12 = 	 Parameter(name='rZEL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL12}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 2] ) 
 
iZEL12 = 	 Parameter(name='iZEL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL12}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 2] ) 
 
rZEL13 = 	 Parameter(name='rZEL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL13}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 3] ) 
 
iZEL13 = 	 Parameter(name='iZEL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL13}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 3] ) 
 
rZEL21 = 	 Parameter(name='rZEL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL21}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 1] ) 
 
iZEL21 = 	 Parameter(name='iZEL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL21}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 1] ) 
 
rZEL22 = 	 Parameter(name='rZEL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL22}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 2] ) 
 
iZEL22 = 	 Parameter(name='iZEL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL22}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 2] ) 
 
rZEL23 = 	 Parameter(name='rZEL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL23}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 3] ) 
 
iZEL23 = 	 Parameter(name='iZEL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL23}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 3] ) 
 
rZEL31 = 	 Parameter(name='rZEL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL31}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 1] ) 
 
iZEL31 = 	 Parameter(name='iZEL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL31}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 1] ) 
 
rZEL32 = 	 Parameter(name='rZEL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL32}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 2] ) 
 
iZEL32 = 	 Parameter(name='iZEL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL32}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 2] ) 
 
rZEL33 = 	 Parameter(name='rZEL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL33}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 3] ) 
 
iZEL33 = 	 Parameter(name='iZEL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL33}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 3] ) 
 
rZER11 = 	 Parameter(name='rZER11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER11}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 1] ) 
 
iZER11 = 	 Parameter(name='iZER11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER11}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 1] ) 
 
rZER12 = 	 Parameter(name='rZER12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER12}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 2] ) 
 
iZER12 = 	 Parameter(name='iZER12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER12}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 2] ) 
 
rZER13 = 	 Parameter(name='rZER13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER13}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 3] ) 
 
iZER13 = 	 Parameter(name='iZER13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER13}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 3] ) 
 
rZER21 = 	 Parameter(name='rZER21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER21}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 1] ) 
 
iZER21 = 	 Parameter(name='iZER21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER21}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 1] ) 
 
rZER22 = 	 Parameter(name='rZER22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER22}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 2] ) 
 
iZER22 = 	 Parameter(name='iZER22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER22}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 2] ) 
 
rZER23 = 	 Parameter(name='rZER23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER23}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 3] ) 
 
iZER23 = 	 Parameter(name='iZER23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER23}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 3] ) 
 
rZER31 = 	 Parameter(name='rZER31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER31}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 1] ) 
 
iZER31 = 	 Parameter(name='iZER31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER31}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 1] ) 
 
rZER32 = 	 Parameter(name='rZER32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER32}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 2] ) 
 
iZER32 = 	 Parameter(name='iZER32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER32}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 2] ) 
 
rZER33 = 	 Parameter(name='rZER33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER33}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 3] ) 
 
iZER33 = 	 Parameter(name='iZER33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER33}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 3] ) 
 
rZM11 = 	 Parameter(name='rZM11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM11}', 
	 lhablock = 'ZMMIX', 
	 lhacode = [1, 1] ) 
 
iZM11 = 	 Parameter(name='iZM11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM11}', 
	 lhablock = 'IMZMMIX', 
	 lhacode = [1, 1] ) 
 
rZM12 = 	 Parameter(name='rZM12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM12}', 
	 lhablock = 'ZMMIX', 
	 lhacode = [1, 2] ) 
 
iZM12 = 	 Parameter(name='iZM12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM12}', 
	 lhablock = 'IMZMMIX', 
	 lhacode = [1, 2] ) 
 
rZM13 = 	 Parameter(name='rZM13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM13}', 
	 lhablock = 'ZMMIX', 
	 lhacode = [1, 3] ) 
 
iZM13 = 	 Parameter(name='iZM13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM13}', 
	 lhablock = 'IMZMMIX', 
	 lhacode = [1, 3] ) 
 
rZM21 = 	 Parameter(name='rZM21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM21}', 
	 lhablock = 'ZMMIX', 
	 lhacode = [2, 1] ) 
 
iZM21 = 	 Parameter(name='iZM21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM21}', 
	 lhablock = 'IMZMMIX', 
	 lhacode = [2, 1] ) 
 
rZM22 = 	 Parameter(name='rZM22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM22}', 
	 lhablock = 'ZMMIX', 
	 lhacode = [2, 2] ) 
 
iZM22 = 	 Parameter(name='iZM22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM22}', 
	 lhablock = 'IMZMMIX', 
	 lhacode = [2, 2] ) 
 
rZM23 = 	 Parameter(name='rZM23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM23}', 
	 lhablock = 'ZMMIX', 
	 lhacode = [2, 3] ) 
 
iZM23 = 	 Parameter(name='iZM23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM23}', 
	 lhablock = 'IMZMMIX', 
	 lhacode = [2, 3] ) 
 
rZM31 = 	 Parameter(name='rZM31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM31}', 
	 lhablock = 'ZMMIX', 
	 lhacode = [3, 1] ) 
 
iZM31 = 	 Parameter(name='iZM31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM31}', 
	 lhablock = 'IMZMMIX', 
	 lhacode = [3, 1] ) 
 
rZM32 = 	 Parameter(name='rZM32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM32}', 
	 lhablock = 'ZMMIX', 
	 lhacode = [3, 2] ) 
 
iZM32 = 	 Parameter(name='iZM32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM32}', 
	 lhablock = 'IMZMMIX', 
	 lhacode = [3, 2] ) 
 
rZM33 = 	 Parameter(name='rZM33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM33}', 
	 lhablock = 'ZMMIX', 
	 lhacode = [3, 3] ) 
 
iZM33 = 	 Parameter(name='iZM33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZM33}', 
	 lhablock = 'IMZMMIX', 
	 lhacode = [3, 3] ) 
 
aEWM1 = 	 Parameter(name='aEWM1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 137.035999679, 
	 texname = '\\text{aEWM1}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [1] ) 
 
aS = 	 Parameter(name='aS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.119, 
	 texname = '\\text{aS}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [3] ) 
 
yu11 = 	 Parameter(name='yu11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryu11 + complex(0,1)*iyu11', 
	 texname = '\\text{yu11}' ) 
 
yu12 = 	 Parameter(name='yu12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryu12 + complex(0,1)*iyu12', 
	 texname = '\\text{yu12}' ) 
 
yu13 = 	 Parameter(name='yu13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryu13 + complex(0,1)*iyu13', 
	 texname = '\\text{yu13}' ) 
 
yu21 = 	 Parameter(name='yu21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryu21 + complex(0,1)*iyu21', 
	 texname = '\\text{yu21}' ) 
 
yu22 = 	 Parameter(name='yu22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryu22 + complex(0,1)*iyu22', 
	 texname = '\\text{yu22}' ) 
 
yu23 = 	 Parameter(name='yu23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryu23 + complex(0,1)*iyu23', 
	 texname = '\\text{yu23}' ) 
 
yu31 = 	 Parameter(name='yu31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryu31 + complex(0,1)*iyu31', 
	 texname = '\\text{yu31}' ) 
 
yu32 = 	 Parameter(name='yu32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryu32 + complex(0,1)*iyu32', 
	 texname = '\\text{yu32}' ) 
 
yu33 = 	 Parameter(name='yu33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryu33 + complex(0,1)*iyu33', 
	 texname = '\\text{yu33}' ) 
 
yd11 = 	 Parameter(name='yd11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryd11 + complex(0,1)*iyd11', 
	 texname = '\\text{yd11}' ) 
 
yd12 = 	 Parameter(name='yd12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryd12 + complex(0,1)*iyd12', 
	 texname = '\\text{yd12}' ) 
 
yd13 = 	 Parameter(name='yd13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryd13 + complex(0,1)*iyd13', 
	 texname = '\\text{yd13}' ) 
 
yd21 = 	 Parameter(name='yd21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryd21 + complex(0,1)*iyd21', 
	 texname = '\\text{yd21}' ) 
 
yd22 = 	 Parameter(name='yd22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryd22 + complex(0,1)*iyd22', 
	 texname = '\\text{yd22}' ) 
 
yd23 = 	 Parameter(name='yd23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryd23 + complex(0,1)*iyd23', 
	 texname = '\\text{yd23}' ) 
 
yd31 = 	 Parameter(name='yd31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryd31 + complex(0,1)*iyd31', 
	 texname = '\\text{yd31}' ) 
 
yd32 = 	 Parameter(name='yd32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryd32 + complex(0,1)*iyd32', 
	 texname = '\\text{yd32}' ) 
 
yd33 = 	 Parameter(name='yd33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ryd33 + complex(0,1)*iyd33', 
	 texname = '\\text{yd33}' ) 
 
ye11 = 	 Parameter(name='ye11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rye11 + complex(0,1)*iye11', 
	 texname = '\\text{ye11}' ) 
 
ye12 = 	 Parameter(name='ye12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rye12 + complex(0,1)*iye12', 
	 texname = '\\text{ye12}' ) 
 
ye13 = 	 Parameter(name='ye13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rye13 + complex(0,1)*iye13', 
	 texname = '\\text{ye13}' ) 
 
ye21 = 	 Parameter(name='ye21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rye21 + complex(0,1)*iye21', 
	 texname = '\\text{ye21}' ) 
 
ye22 = 	 Parameter(name='ye22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rye22 + complex(0,1)*iye22', 
	 texname = '\\text{ye22}' ) 
 
ye23 = 	 Parameter(name='ye23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rye23 + complex(0,1)*iye23', 
	 texname = '\\text{ye23}' ) 
 
ye31 = 	 Parameter(name='ye31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rye31 + complex(0,1)*iye31', 
	 texname = '\\text{ye31}' ) 
 
ye32 = 	 Parameter(name='ye32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rye32 + complex(0,1)*iye32', 
	 texname = '\\text{ye32}' ) 
 
ye33 = 	 Parameter(name='ye33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rye33 + complex(0,1)*iye33', 
	 texname = '\\text{ye33}' ) 
 
CW111 = 	 Parameter(name='CW111', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rCW111 + complex(0,1)*iCW111', 
	 texname = '\\text{CW111}' ) 
 
CW112 = 	 Parameter(name='CW112', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rCW112 + complex(0,1)*iCW112', 
	 texname = '\\text{CW112}' ) 
 
CW113 = 	 Parameter(name='CW113', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rCW113 + complex(0,1)*iCW113', 
	 texname = '\\text{CW113}' ) 
 
CW121 = 	 Parameter(name='CW121', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rCW121 + complex(0,1)*iCW121', 
	 texname = '\\text{CW121}' ) 
 
CW122 = 	 Parameter(name='CW122', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rCW122 + complex(0,1)*iCW122', 
	 texname = '\\text{CW122}' ) 
 
CW123 = 	 Parameter(name='CW123', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rCW123 + complex(0,1)*iCW123', 
	 texname = '\\text{CW123}' ) 
 
CW131 = 	 Parameter(name='CW131', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rCW131 + complex(0,1)*iCW131', 
	 texname = '\\text{CW131}' ) 
 
CW132 = 	 Parameter(name='CW132', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rCW132 + complex(0,1)*iCW132', 
	 texname = '\\text{CW132}' ) 
 
CW133 = 	 Parameter(name='CW133', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rCW133 + complex(0,1)*iCW133', 
	 texname = '\\text{CW133}' ) 
 
gHR = 	 Parameter(name='gHR', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rgHR + complex(0,1)*igHR', 
	 texname = '\\text{gHR}' ) 
 
gHS = 	 Parameter(name='gHS', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rgHS + complex(0,1)*igHS', 
	 texname = '\\text{gHS}' ) 
 
ghrp = 	 Parameter(name='ghrp', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rghrp + complex(0,1)*ighrp', 
	 texname = '\\text{ghrp}' ) 
 
lambR = 	 Parameter(name='lambR', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlambR + complex(0,1)*ilambR', 
	 texname = '\\text{lambR}' ) 
 
lambS = 	 Parameter(name='lambS', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlambS + complex(0,1)*ilambS', 
	 texname = '\\text{lambS}' ) 
 
Theta11 = 	 Parameter(name='Theta11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTheta11 + complex(0,1)*iTheta11', 
	 texname = '\\text{Theta11}' ) 
 
Theta12 = 	 Parameter(name='Theta12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTheta12 + complex(0,1)*iTheta12', 
	 texname = '\\text{Theta12}' ) 
 
Theta13 = 	 Parameter(name='Theta13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTheta13 + complex(0,1)*iTheta13', 
	 texname = '\\text{Theta13}' ) 
 
Theta21 = 	 Parameter(name='Theta21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTheta21 + complex(0,1)*iTheta21', 
	 texname = '\\text{Theta21}' ) 
 
Theta22 = 	 Parameter(name='Theta22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTheta22 + complex(0,1)*iTheta22', 
	 texname = '\\text{Theta22}' ) 
 
Theta23 = 	 Parameter(name='Theta23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTheta23 + complex(0,1)*iTheta23', 
	 texname = '\\text{Theta23}' ) 
 
Theta31 = 	 Parameter(name='Theta31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTheta31 + complex(0,1)*iTheta31', 
	 texname = '\\text{Theta31}' ) 
 
Theta32 = 	 Parameter(name='Theta32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTheta32 + complex(0,1)*iTheta32', 
	 texname = '\\text{Theta32}' ) 
 
Theta33 = 	 Parameter(name='Theta33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTheta33 + complex(0,1)*iTheta33', 
	 texname = '\\text{Theta33}' ) 
 
Omega11 = 	 Parameter(name='Omega11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rOmega11 + complex(0,1)*iOmega11', 
	 texname = '\\text{Omega11}' ) 
 
Omega12 = 	 Parameter(name='Omega12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rOmega12 + complex(0,1)*iOmega12', 
	 texname = '\\text{Omega12}' ) 
 
Omega13 = 	 Parameter(name='Omega13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rOmega13 + complex(0,1)*iOmega13', 
	 texname = '\\text{Omega13}' ) 
 
Omega21 = 	 Parameter(name='Omega21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rOmega21 + complex(0,1)*iOmega21', 
	 texname = '\\text{Omega21}' ) 
 
Omega22 = 	 Parameter(name='Omega22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rOmega22 + complex(0,1)*iOmega22', 
	 texname = '\\text{Omega22}' ) 
 
Omega23 = 	 Parameter(name='Omega23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rOmega23 + complex(0,1)*iOmega23', 
	 texname = '\\text{Omega23}' ) 
 
Omega31 = 	 Parameter(name='Omega31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rOmega31 + complex(0,1)*iOmega31', 
	 texname = '\\text{Omega31}' ) 
 
Omega32 = 	 Parameter(name='Omega32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rOmega32 + complex(0,1)*iOmega32', 
	 texname = '\\text{Omega32}' ) 
 
Omega33 = 	 Parameter(name='Omega33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rOmega33 + complex(0,1)*iOmega33', 
	 texname = '\\text{Omega33}' ) 
 
Upsilon11 = 	 Parameter(name='Upsilon11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUpsilon11 + complex(0,1)*iUpsilon11', 
	 texname = '\\text{Upsilon11}' ) 
 
Upsilon12 = 	 Parameter(name='Upsilon12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUpsilon12 + complex(0,1)*iUpsilon12', 
	 texname = '\\text{Upsilon12}' ) 
 
Upsilon13 = 	 Parameter(name='Upsilon13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUpsilon13 + complex(0,1)*iUpsilon13', 
	 texname = '\\text{Upsilon13}' ) 
 
Upsilon21 = 	 Parameter(name='Upsilon21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUpsilon21 + complex(0,1)*iUpsilon21', 
	 texname = '\\text{Upsilon21}' ) 
 
Upsilon22 = 	 Parameter(name='Upsilon22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUpsilon22 + complex(0,1)*iUpsilon22', 
	 texname = '\\text{Upsilon22}' ) 
 
Upsilon23 = 	 Parameter(name='Upsilon23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUpsilon23 + complex(0,1)*iUpsilon23', 
	 texname = '\\text{Upsilon23}' ) 
 
Upsilon31 = 	 Parameter(name='Upsilon31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUpsilon31 + complex(0,1)*iUpsilon31', 
	 texname = '\\text{Upsilon31}' ) 
 
Upsilon32 = 	 Parameter(name='Upsilon32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUpsilon32 + complex(0,1)*iUpsilon32', 
	 texname = '\\text{Upsilon32}' ) 
 
Upsilon33 = 	 Parameter(name='Upsilon33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUpsilon33 + complex(0,1)*iUpsilon33', 
	 texname = '\\text{Upsilon33}' ) 
 
lRRS = 	 Parameter(name='lRRS', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlRRS + complex(0,1)*ilRRS', 
	 texname = '\\text{lRRS}' ) 
 
a1 = 	 Parameter(name='a1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'ra1 + complex(0,1)*ia1', 
	 texname = '\\text{a1}' ) 
 
RRSS = 	 Parameter(name='RRSS', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rRRSS + complex(0,1)*iRRSS', 
	 texname = '\\text{RRSS}' ) 
 
ZH11 = 	 Parameter(name='ZH11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZH11 + complex(0,1)*iZH11', 
	 texname = '\\text{ZH11}' ) 
 
ZH12 = 	 Parameter(name='ZH12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZH12 + complex(0,1)*iZH12', 
	 texname = '\\text{ZH12}' ) 
 
ZH21 = 	 Parameter(name='ZH21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZH21 + complex(0,1)*iZH21', 
	 texname = '\\text{ZH21}' ) 
 
ZH22 = 	 Parameter(name='ZH22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZH22 + complex(0,1)*iZH22', 
	 texname = '\\text{ZH22}' ) 
 
ZDL11 = 	 Parameter(name='ZDL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL11 + complex(0,1)*iZDL11', 
	 texname = '\\text{ZDL11}' ) 
 
ZDL12 = 	 Parameter(name='ZDL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL12 + complex(0,1)*iZDL12', 
	 texname = '\\text{ZDL12}' ) 
 
ZDL13 = 	 Parameter(name='ZDL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL13 + complex(0,1)*iZDL13', 
	 texname = '\\text{ZDL13}' ) 
 
ZDL21 = 	 Parameter(name='ZDL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL21 + complex(0,1)*iZDL21', 
	 texname = '\\text{ZDL21}' ) 
 
ZDL22 = 	 Parameter(name='ZDL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL22 + complex(0,1)*iZDL22', 
	 texname = '\\text{ZDL22}' ) 
 
ZDL23 = 	 Parameter(name='ZDL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL23 + complex(0,1)*iZDL23', 
	 texname = '\\text{ZDL23}' ) 
 
ZDL31 = 	 Parameter(name='ZDL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL31 + complex(0,1)*iZDL31', 
	 texname = '\\text{ZDL31}' ) 
 
ZDL32 = 	 Parameter(name='ZDL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL32 + complex(0,1)*iZDL32', 
	 texname = '\\text{ZDL32}' ) 
 
ZDL33 = 	 Parameter(name='ZDL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL33 + complex(0,1)*iZDL33', 
	 texname = '\\text{ZDL33}' ) 
 
ZDR11 = 	 Parameter(name='ZDR11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR11 + complex(0,1)*iZDR11', 
	 texname = '\\text{ZDR11}' ) 
 
ZDR12 = 	 Parameter(name='ZDR12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR12 + complex(0,1)*iZDR12', 
	 texname = '\\text{ZDR12}' ) 
 
ZDR13 = 	 Parameter(name='ZDR13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR13 + complex(0,1)*iZDR13', 
	 texname = '\\text{ZDR13}' ) 
 
ZDR21 = 	 Parameter(name='ZDR21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR21 + complex(0,1)*iZDR21', 
	 texname = '\\text{ZDR21}' ) 
 
ZDR22 = 	 Parameter(name='ZDR22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR22 + complex(0,1)*iZDR22', 
	 texname = '\\text{ZDR22}' ) 
 
ZDR23 = 	 Parameter(name='ZDR23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR23 + complex(0,1)*iZDR23', 
	 texname = '\\text{ZDR23}' ) 
 
ZDR31 = 	 Parameter(name='ZDR31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR31 + complex(0,1)*iZDR31', 
	 texname = '\\text{ZDR31}' ) 
 
ZDR32 = 	 Parameter(name='ZDR32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR32 + complex(0,1)*iZDR32', 
	 texname = '\\text{ZDR32}' ) 
 
ZDR33 = 	 Parameter(name='ZDR33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR33 + complex(0,1)*iZDR33', 
	 texname = '\\text{ZDR33}' ) 
 
ZUL11 = 	 Parameter(name='ZUL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL11 + complex(0,1)*iZUL11', 
	 texname = '\\text{ZUL11}' ) 
 
ZUL12 = 	 Parameter(name='ZUL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL12 + complex(0,1)*iZUL12', 
	 texname = '\\text{ZUL12}' ) 
 
ZUL13 = 	 Parameter(name='ZUL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL13 + complex(0,1)*iZUL13', 
	 texname = '\\text{ZUL13}' ) 
 
ZUL21 = 	 Parameter(name='ZUL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL21 + complex(0,1)*iZUL21', 
	 texname = '\\text{ZUL21}' ) 
 
ZUL22 = 	 Parameter(name='ZUL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL22 + complex(0,1)*iZUL22', 
	 texname = '\\text{ZUL22}' ) 
 
ZUL23 = 	 Parameter(name='ZUL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL23 + complex(0,1)*iZUL23', 
	 texname = '\\text{ZUL23}' ) 
 
ZUL31 = 	 Parameter(name='ZUL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL31 + complex(0,1)*iZUL31', 
	 texname = '\\text{ZUL31}' ) 
 
ZUL32 = 	 Parameter(name='ZUL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL32 + complex(0,1)*iZUL32', 
	 texname = '\\text{ZUL32}' ) 
 
ZUL33 = 	 Parameter(name='ZUL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL33 + complex(0,1)*iZUL33', 
	 texname = '\\text{ZUL33}' ) 
 
ZUR11 = 	 Parameter(name='ZUR11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR11 + complex(0,1)*iZUR11', 
	 texname = '\\text{ZUR11}' ) 
 
ZUR12 = 	 Parameter(name='ZUR12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR12 + complex(0,1)*iZUR12', 
	 texname = '\\text{ZUR12}' ) 
 
ZUR13 = 	 Parameter(name='ZUR13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR13 + complex(0,1)*iZUR13', 
	 texname = '\\text{ZUR13}' ) 
 
ZUR21 = 	 Parameter(name='ZUR21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR21 + complex(0,1)*iZUR21', 
	 texname = '\\text{ZUR21}' ) 
 
ZUR22 = 	 Parameter(name='ZUR22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR22 + complex(0,1)*iZUR22', 
	 texname = '\\text{ZUR22}' ) 
 
ZUR23 = 	 Parameter(name='ZUR23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR23 + complex(0,1)*iZUR23', 
	 texname = '\\text{ZUR23}' ) 
 
ZUR31 = 	 Parameter(name='ZUR31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR31 + complex(0,1)*iZUR31', 
	 texname = '\\text{ZUR31}' ) 
 
ZUR32 = 	 Parameter(name='ZUR32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR32 + complex(0,1)*iZUR32', 
	 texname = '\\text{ZUR32}' ) 
 
ZUR33 = 	 Parameter(name='ZUR33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR33 + complex(0,1)*iZUR33', 
	 texname = '\\text{ZUR33}' ) 
 
ZEL11 = 	 Parameter(name='ZEL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL11 + complex(0,1)*iZEL11', 
	 texname = '\\text{ZEL11}' ) 
 
ZEL12 = 	 Parameter(name='ZEL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL12 + complex(0,1)*iZEL12', 
	 texname = '\\text{ZEL12}' ) 
 
ZEL13 = 	 Parameter(name='ZEL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL13 + complex(0,1)*iZEL13', 
	 texname = '\\text{ZEL13}' ) 
 
ZEL21 = 	 Parameter(name='ZEL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL21 + complex(0,1)*iZEL21', 
	 texname = '\\text{ZEL21}' ) 
 
ZEL22 = 	 Parameter(name='ZEL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL22 + complex(0,1)*iZEL22', 
	 texname = '\\text{ZEL22}' ) 
 
ZEL23 = 	 Parameter(name='ZEL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL23 + complex(0,1)*iZEL23', 
	 texname = '\\text{ZEL23}' ) 
 
ZEL31 = 	 Parameter(name='ZEL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL31 + complex(0,1)*iZEL31', 
	 texname = '\\text{ZEL31}' ) 
 
ZEL32 = 	 Parameter(name='ZEL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL32 + complex(0,1)*iZEL32', 
	 texname = '\\text{ZEL32}' ) 
 
ZEL33 = 	 Parameter(name='ZEL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL33 + complex(0,1)*iZEL33', 
	 texname = '\\text{ZEL33}' ) 
 
ZER11 = 	 Parameter(name='ZER11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER11 + complex(0,1)*iZER11', 
	 texname = '\\text{ZER11}' ) 
 
ZER12 = 	 Parameter(name='ZER12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER12 + complex(0,1)*iZER12', 
	 texname = '\\text{ZER12}' ) 
 
ZER13 = 	 Parameter(name='ZER13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER13 + complex(0,1)*iZER13', 
	 texname = '\\text{ZER13}' ) 
 
ZER21 = 	 Parameter(name='ZER21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER21 + complex(0,1)*iZER21', 
	 texname = '\\text{ZER21}' ) 
 
ZER22 = 	 Parameter(name='ZER22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER22 + complex(0,1)*iZER22', 
	 texname = '\\text{ZER22}' ) 
 
ZER23 = 	 Parameter(name='ZER23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER23 + complex(0,1)*iZER23', 
	 texname = '\\text{ZER23}' ) 
 
ZER31 = 	 Parameter(name='ZER31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER31 + complex(0,1)*iZER31', 
	 texname = '\\text{ZER31}' ) 
 
ZER32 = 	 Parameter(name='ZER32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER32 + complex(0,1)*iZER32', 
	 texname = '\\text{ZER32}' ) 
 
ZER33 = 	 Parameter(name='ZER33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER33 + complex(0,1)*iZER33', 
	 texname = '\\text{ZER33}' ) 
 
ZM11 = 	 Parameter(name='ZM11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZM11 + complex(0,1)*iZM11', 
	 texname = '\\text{ZM11}' ) 
 
ZM12 = 	 Parameter(name='ZM12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZM12 + complex(0,1)*iZM12', 
	 texname = '\\text{ZM12}' ) 
 
ZM13 = 	 Parameter(name='ZM13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZM13 + complex(0,1)*iZM13', 
	 texname = '\\text{ZM13}' ) 
 
ZM21 = 	 Parameter(name='ZM21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZM21 + complex(0,1)*iZM21', 
	 texname = '\\text{ZM21}' ) 
 
ZM22 = 	 Parameter(name='ZM22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZM22 + complex(0,1)*iZM22', 
	 texname = '\\text{ZM22}' ) 
 
ZM23 = 	 Parameter(name='ZM23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZM23 + complex(0,1)*iZM23', 
	 texname = '\\text{ZM23}' ) 
 
ZM31 = 	 Parameter(name='ZM31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZM31 + complex(0,1)*iZM31', 
	 texname = '\\text{ZM31}' ) 
 
ZM32 = 	 Parameter(name='ZM32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZM32 + complex(0,1)*iZM32', 
	 texname = '\\text{ZM32}' ) 
 
ZM33 = 	 Parameter(name='ZM33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZM33 + complex(0,1)*iZM33', 
	 texname = '\\text{ZM33}' ) 
 
G = 	 Parameter(name='G', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)', 
	 texname = 'G') 
 
el = 	 Parameter(name='el', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)', 
	 texname = 'el') 
 
TW = 	 Parameter(name='TW', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'cmath.asin(cmath.sqrt(1 - MWm**2/MZ**2))', 
	 texname = 'TW') 
 
g1 = 	 Parameter(name='g1', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'el*1./cmath.cos(TW)', 
	 texname = 'g1') 
 
g2 = 	 Parameter(name='g2', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'el*1./cmath.sin(TW)', 
	 texname = 'g2') 
 
vvSM = 	 Parameter(name='vvSM', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(MWm**2/g2**2)', 
	 texname = 'vvSM') 
 
Lam = 	 Parameter(name='Lam', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'Mh**2/vvSM**2', 
	 texname = 'Lam') 
 
RXiWm = 	 Parameter(name='RXiWm', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiWm') 
 
RXiZ = 	 Parameter(name='RXiZ', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiZ') 
 
HPP1 = 	 Parameter(name='HPP1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP1}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,22,22] ) 
 
HGG1 = 	 Parameter(name='HGG1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG1}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,21,21] ) 
 
