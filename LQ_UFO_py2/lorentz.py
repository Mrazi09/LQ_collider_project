# ----------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.14.5 
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840    
# (c) Florian Staub, 2011  
# ----------------------------------------------------------------------  
# File created at 14:5 on 30.11.2022   
# ----------------------------------------------------------------------  
 
 
from __future__ import absolute_import
from object_library import all_lorentz,Lorentz 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
 
SSS1 = Lorentz(name = u'SSS1', 
	 spins = [1, 1, 1],
	 structure = u'1' ) 
 
 
SSVV1 = Lorentz(name = u'SSVV1', 
	 spins = [1, 1, 3, 3],
	 structure = u'Metric(3,4)' ) 
 
 
SSV1 = Lorentz(name = u'SSV1', 
	 spins = [1, 1, 3],
	 structure = u'P(3,1) - P(3,2)' ) 
 
 
SVV1 = Lorentz(name = u'SVV1', 
	 spins = [1, 3, 3],
	 structure = u'Metric(2,3)' ) 
 
 
FFS1 = Lorentz(name = u'FFS1', 
	 spins = [2, 2, 1],
	 structure = u'ProjP(2,1)' ) 
 
 
FFS2 = Lorentz(name = u'FFS2', 
	 spins = [2, 2, 1],
	 structure = u'ProjM(2,1)' ) 
 
 
FFV1 = Lorentz(name = u'FFV1', 
	 spins = [2, 2, 3],
	 structure = u'ProjP(2,1)' ) 
 
 
FFV2 = Lorentz(name = u'FFV2', 
	 spins = [2, 2, 3],
	 structure = u'Gamma(3,2,-1)*ProjP(-1,1)' ) 
 
 
FFV3 = Lorentz(name = u'FFV3', 
	 spins = [2, 2, 3],
	 structure = u'Gamma(3,2,-1)*ProjM(-1,1)' ) 
 
 
VVV1 = Lorentz(name = u'VVV1', 
	 spins = [3, 3, 3],
	 structure = u'-(Metric(2,3)*P(1,2)) + Metric(2,3)*P(1,3) + Metric(1,3)*P(2,1) - Metric(1,3)*P(2,3) - Metric(1,2)*P(3,1) + Metric(1,2)*P(3,2)' ) 
 
 
VVVV1 = Lorentz(name = u'VVVV1', 
	 spins = [3, 3, 3, 3],
	 structure = u'Metric(1,2)*Metric(3,4)' ) 
 
 
VVVV2 = Lorentz(name = u'VVVV2', 
	 spins = [3, 3, 3, 3],
	 structure = u'Metric(1,3)*Metric(2,4)' ) 
 
 
VVVV3 = Lorentz(name = u'VVVV3', 
	 spins = [3, 3, 3, 3],
	 structure = u'Metric(1,4)*Metric(2,3)' ) 
 
 
VVS99 = Lorentz(name=u'VVSpp', 
spins=[3,3,1], 
structure=u'P(1,2)*P(2,1)-P(-1,1)*P(-1,2)*Metric(1,2)')
