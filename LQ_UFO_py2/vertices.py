# ------------------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.14.5 
# SARAH References: arXiv:0806.0538, 0909.2863, 1002.0840, 1207.0906, 1309.7223   
# (c) Florian Staub, 2013  
# -------------------------------------------------------------------------------  
# File created at 14:05 on 30.11.2022   
# ----------------------------------------------------------------------  
 
 
from __future__ import absolute_import
from object_library import all_vertices,Vertex 
import particles as P 
import couplings as C 
import lorentz as L 
 
 
V_1 = Vertex(name = u'V_1', 
	 particles = [P.Ah, P.Ah, P.h], 
	 color = [u'1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_1}) 
 
 
V_2 = Vertex(name = u'V_2', 
	 particles = [P.Ah, P.S1, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_2}) 
 
 
V_3 = Vertex(name = u'V_3', 
	 particles = [P.Ah, P.S1, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_3}) 
 
 
V_4 = Vertex(name = u'V_4', 
	 particles = [P.Ah, P.S2, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_4}) 
 
 
V_5 = Vertex(name = u'V_5', 
	 particles = [P.Ah, P.S2, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_5}) 
 
 
V_6 = Vertex(name = u'V_6', 
	 particles = [P.h, P.h, P.h], 
	 color = [u'1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_6}) 
 
 
V_7 = Vertex(name = u'V_7', 
	 particles = [P.h, P.Hp, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_7}) 
 
 
V_8 = Vertex(name = u'V_8', 
	 particles = [P.h, P.R, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_8}) 
 
 
V_9 = Vertex(name = u'V_9', 
	 particles = [P.h, P.S1, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_9}) 
 
 
V_10 = Vertex(name = u'V_10', 
	 particles = [P.h, P.S1, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_10}) 
 
 
V_11 = Vertex(name = u'V_11', 
	 particles = [P.h, P.S2, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_11}) 
 
 
V_12 = Vertex(name = u'V_12', 
	 particles = [P.h, P.S2, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_12}) 
 
 
V_13 = Vertex(name = u'V_13', 
	 particles = [P.Hp, P.S1, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_13}) 
 
 
V_14 = Vertex(name = u'V_14', 
	 particles = [P.Hp, P.S2, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_14}) 
 
 
V_15 = Vertex(name = u'V_15', 
	 particles = [P.R, P.S1, P.S2], 
	 color = [u'Epsilon(1,2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_15}) 
 
 
V_16 = Vertex(name = u'V_16', 
	 particles = [P.R, P.Hpc, P.S1c], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_16}) 
 
 
V_17 = Vertex(name = u'V_17', 
	 particles = [P.R, P.Hpc, P.S2c], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_17}) 
 
 
V_18 = Vertex(name = u'V_18', 
	 particles = [P.Rc, P.S1c, P.S2c], 
	 color = [u'EpsilonBar(1,2,3)'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_18}) 
 
 
V_19 = Vertex(name = u'V_19', 
	 particles = [P.Ah, P.Ah, P.Wmc, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_19}) 
 
 
V_20 = Vertex(name = u'V_20', 
	 particles = [P.Ah, P.Ah, P.Z, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_20}) 
 
 
V_21 = Vertex(name = u'V_21', 
	 particles = [P.Ah, P.Hp, P.A, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_21}) 
 
 
V_22 = Vertex(name = u'V_22', 
	 particles = [P.Ah, P.Hp, P.Wm, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_22}) 
 
 
V_23 = Vertex(name = u'V_23', 
	 particles = [P.Ah, P.Hpc, P.Wmc, P.A], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_23}) 
 
 
V_24 = Vertex(name = u'V_24', 
	 particles = [P.Ah, P.Hpc, P.Wmc, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_24}) 
 
 
V_25 = Vertex(name = u'V_25', 
	 particles = [P.h, P.h, P.Wmc, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_25}) 
 
 
V_26 = Vertex(name = u'V_26', 
	 particles = [P.h, P.h, P.Z, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_26}) 
 
 
V_27 = Vertex(name = u'V_27', 
	 particles = [P.h, P.Hp, P.A, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_27}) 
 
 
V_28 = Vertex(name = u'V_28', 
	 particles = [P.h, P.Hp, P.Wm, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_28}) 
 
 
V_29 = Vertex(name = u'V_29', 
	 particles = [P.h, P.Hpc, P.Wmc, P.A], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_29}) 
 
 
V_30 = Vertex(name = u'V_30', 
	 particles = [P.h, P.Hpc, P.Wmc, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_30}) 
 
 
V_31 = Vertex(name = u'V_31', 
	 particles = [P.Hp, P.Hpc, P.A, P.A], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_31}) 
 
 
V_32 = Vertex(name = u'V_32', 
	 particles = [P.Hp, P.Hpc, P.A, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_32}) 
 
 
V_33 = Vertex(name = u'V_33', 
	 particles = [P.Hp, P.Hpc, P.Wmc, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_33}) 
 
 
V_34 = Vertex(name = u'V_34', 
	 particles = [P.Hp, P.Hpc, P.Z, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_34}) 
 
 
V_35 = Vertex(name = u'V_35', 
	 particles = [P.R, P.Rc, P.g, P.g], 
	 color = [u'T(3,-1,2)*T(4,1,-1)', u'T(3,1,-1)*T(4,-1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_35,(1,0):C.GC_36}) 
 
 
V_36 = Vertex(name = u'V_36', 
	 particles = [P.R, P.Rc, P.g, P.A], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_37}) 
 
 
V_37 = Vertex(name = u'V_37', 
	 particles = [P.R, P.S1c, P.g, P.Wm], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_38}) 
 
 
V_38 = Vertex(name = u'V_38', 
	 particles = [P.R, P.S2c, P.g, P.Wm], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_39}) 
 
 
V_39 = Vertex(name = u'V_39', 
	 particles = [P.R, P.Rc, P.g, P.Z], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_40}) 
 
 
V_40 = Vertex(name = u'V_40', 
	 particles = [P.R, P.Rc, P.A, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_41}) 
 
 
V_41 = Vertex(name = u'V_41', 
	 particles = [P.R, P.S1c, P.A, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_42}) 
 
 
V_42 = Vertex(name = u'V_42', 
	 particles = [P.R, P.S2c, P.A, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_43}) 
 
 
V_43 = Vertex(name = u'V_43', 
	 particles = [P.R, P.Rc, P.A, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_44}) 
 
 
V_44 = Vertex(name = u'V_44', 
	 particles = [P.R, P.S1c, P.Wm, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_45}) 
 
 
V_45 = Vertex(name = u'V_45', 
	 particles = [P.R, P.S2c, P.Wm, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_46}) 
 
 
V_46 = Vertex(name = u'V_46', 
	 particles = [P.R, P.Rc, P.Wmc, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_47}) 
 
 
V_47 = Vertex(name = u'V_47', 
	 particles = [P.R, P.Rc, P.Z, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_48}) 
 
 
V_48 = Vertex(name = u'V_48', 
	 particles = [P.S1, P.S1c, P.g, P.g], 
	 color = [u'T(3,-1,2)*T(4,1,-1)', u'T(3,1,-1)*T(4,-1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_49,(1,0):C.GC_50}) 
 
 
V_49 = Vertex(name = u'V_49', 
	 particles = [P.S1, P.S2c, P.g, P.g], 
	 color = [u'T(3,-1,2)*T(4,1,-1)', u'T(3,1,-1)*T(4,-1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_51,(1,0):C.GC_52}) 
 
 
V_50 = Vertex(name = u'V_50', 
	 particles = [P.S2, P.S1c, P.g, P.g], 
	 color = [u'T(3,-1,2)*T(4,1,-1)', u'T(3,1,-1)*T(4,-1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_53,(1,0):C.GC_54}) 
 
 
V_51 = Vertex(name = u'V_51', 
	 particles = [P.S2, P.S2c, P.g, P.g], 
	 color = [u'T(3,-1,2)*T(4,1,-1)', u'T(3,1,-1)*T(4,-1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_55,(1,0):C.GC_56}) 
 
 
V_52 = Vertex(name = u'V_52', 
	 particles = [P.S1, P.S1c, P.g, P.A], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_57}) 
 
 
V_53 = Vertex(name = u'V_53', 
	 particles = [P.S1, P.S2c, P.g, P.A], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_58}) 
 
 
V_54 = Vertex(name = u'V_54', 
	 particles = [P.S2, P.S1c, P.g, P.A], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_59}) 
 
 
V_55 = Vertex(name = u'V_55', 
	 particles = [P.S2, P.S2c, P.g, P.A], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_60}) 
 
 
V_56 = Vertex(name = u'V_56', 
	 particles = [P.S1, P.S1c, P.g, P.Z], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_61}) 
 
 
V_57 = Vertex(name = u'V_57', 
	 particles = [P.S1, P.S2c, P.g, P.Z], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_62}) 
 
 
V_58 = Vertex(name = u'V_58', 
	 particles = [P.S2, P.S1c, P.g, P.Z], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_63}) 
 
 
V_59 = Vertex(name = u'V_59', 
	 particles = [P.S2, P.S2c, P.g, P.Z], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_64}) 
 
 
V_60 = Vertex(name = u'V_60', 
	 particles = [P.S1, P.Rc, P.Wmc, P.g], 
	 color = [u'T(4,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_65}) 
 
 
V_61 = Vertex(name = u'V_61', 
	 particles = [P.S2, P.Rc, P.Wmc, P.g], 
	 color = [u'T(4,1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_66}) 
 
 
V_62 = Vertex(name = u'V_62', 
	 particles = [P.S1, P.S1c, P.A, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_67}) 
 
 
V_63 = Vertex(name = u'V_63', 
	 particles = [P.S1, P.S2c, P.A, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_68}) 
 
 
V_64 = Vertex(name = u'V_64', 
	 particles = [P.S2, P.S1c, P.A, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_69}) 
 
 
V_65 = Vertex(name = u'V_65', 
	 particles = [P.S2, P.S2c, P.A, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_70}) 
 
 
V_66 = Vertex(name = u'V_66', 
	 particles = [P.S1, P.S1c, P.A, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_71}) 
 
 
V_67 = Vertex(name = u'V_67', 
	 particles = [P.S1, P.S2c, P.A, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_72}) 
 
 
V_68 = Vertex(name = u'V_68', 
	 particles = [P.S2, P.S1c, P.A, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_73}) 
 
 
V_69 = Vertex(name = u'V_69', 
	 particles = [P.S2, P.S2c, P.A, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_74}) 
 
 
V_70 = Vertex(name = u'V_70', 
	 particles = [P.S1, P.Rc, P.Wmc, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_75}) 
 
 
V_71 = Vertex(name = u'V_71', 
	 particles = [P.S2, P.Rc, P.Wmc, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_76}) 
 
 
V_72 = Vertex(name = u'V_72', 
	 particles = [P.S1, P.S1c, P.Wmc, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_77}) 
 
 
V_73 = Vertex(name = u'V_73', 
	 particles = [P.S1, P.S2c, P.Wmc, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_78}) 
 
 
V_74 = Vertex(name = u'V_74', 
	 particles = [P.S2, P.S1c, P.Wmc, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_79}) 
 
 
V_75 = Vertex(name = u'V_75', 
	 particles = [P.S2, P.S2c, P.Wmc, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_80}) 
 
 
V_76 = Vertex(name = u'V_76', 
	 particles = [P.S1, P.S1c, P.Z, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_81}) 
 
 
V_77 = Vertex(name = u'V_77', 
	 particles = [P.S1, P.S2c, P.Z, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_82}) 
 
 
V_78 = Vertex(name = u'V_78', 
	 particles = [P.S2, P.S1c, P.Z, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_83}) 
 
 
V_79 = Vertex(name = u'V_79', 
	 particles = [P.S2, P.S2c, P.Z, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_84}) 
 
 
V_80 = Vertex(name = u'V_80', 
	 particles = [P.S1, P.Rc, P.Wmc, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_85}) 
 
 
V_81 = Vertex(name = u'V_81', 
	 particles = [P.S2, P.Rc, P.Wmc, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_86}) 
 
 
V_82 = Vertex(name = u'V_82', 
	 particles = [P.Ah, P.h, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_87}) 
 
 
V_83 = Vertex(name = u'V_83', 
	 particles = [P.Ah, P.Hp, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_88}) 
 
 
V_84 = Vertex(name = u'V_84', 
	 particles = [P.Ah, P.Hpc, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_89}) 
 
 
V_85 = Vertex(name = u'V_85', 
	 particles = [P.h, P.Hp, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_90}) 
 
 
V_86 = Vertex(name = u'V_86', 
	 particles = [P.h, P.Hpc, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_91}) 
 
 
V_87 = Vertex(name = u'V_87', 
	 particles = [P.Hp, P.Hpc, P.A], 
	 color = [u'1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_92}) 
 
 
V_88 = Vertex(name = u'V_88', 
	 particles = [P.Hp, P.Hpc, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_93}) 
 
 
V_89 = Vertex(name = u'V_89', 
	 particles = [P.R, P.Rc, P.g], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_94}) 
 
 
V_90 = Vertex(name = u'V_90', 
	 particles = [P.R, P.Rc, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_95}) 
 
 
V_91 = Vertex(name = u'V_91', 
	 particles = [P.R, P.S1c, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_96}) 
 
 
V_92 = Vertex(name = u'V_92', 
	 particles = [P.R, P.S2c, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_97}) 
 
 
V_93 = Vertex(name = u'V_93', 
	 particles = [P.R, P.Rc, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_98}) 
 
 
V_94 = Vertex(name = u'V_94', 
	 particles = [P.S1, P.S1c, P.g], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_99}) 
 
 
V_95 = Vertex(name = u'V_95', 
	 particles = [P.S2, P.S2c, P.g], 
	 color = [u'T(3,1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_100}) 
 
 
V_96 = Vertex(name = u'V_96', 
	 particles = [P.S1, P.S1c, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_101}) 
 
 
V_97 = Vertex(name = u'V_97', 
	 particles = [P.S1, P.S2c, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_102}) 
 
 
V_98 = Vertex(name = u'V_98', 
	 particles = [P.S2, P.S1c, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_103}) 
 
 
V_99 = Vertex(name = u'V_99', 
	 particles = [P.S2, P.S2c, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_104}) 
 
 
V_100 = Vertex(name = u'V_100', 
	 particles = [P.S1, P.S1c, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_105}) 
 
 
V_101 = Vertex(name = u'V_101', 
	 particles = [P.S1, P.S2c, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_106}) 
 
 
V_102 = Vertex(name = u'V_102', 
	 particles = [P.S2, P.S1c, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_107}) 
 
 
V_103 = Vertex(name = u'V_103', 
	 particles = [P.S2, P.S2c, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_108}) 
 
 
V_104 = Vertex(name = u'V_104', 
	 particles = [P.S1, P.Rc, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_109}) 
 
 
V_105 = Vertex(name = u'V_105', 
	 particles = [P.S2, P.Rc, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_110}) 
 
 
V_106 = Vertex(name = u'V_106', 
	 particles = [P.h, P.Wmc, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_111}) 
 
 
V_107 = Vertex(name = u'V_107', 
	 particles = [P.h, P.Z, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_112}) 
 
 
V_108 = Vertex(name = u'V_108', 
	 particles = [P.Hp, P.A, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_113}) 
 
 
V_109 = Vertex(name = u'V_109', 
	 particles = [P.Hp, P.Wm, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_114}) 
 
 
V_110 = Vertex(name = u'V_110', 
	 particles = [P.Hpc, P.Wmc, P.A], 
	 color = [u'1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_115}) 
 
 
V_111 = Vertex(name = u'V_111', 
	 particles = [P.Hpc, P.Wmc, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_116}) 
 
 
V_112 = Vertex(name = u'V_112', 
	 particles = [P.d1bar, P.d1, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_117,(0,1):C.GC_118}) 
 
 
V_113 = Vertex(name = u'V_113', 
	 particles = [P.d1bar, P.d2, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_119,(0,1):C.GC_120}) 
 
 
V_114 = Vertex(name = u'V_114', 
	 particles = [P.d1bar, P.d3, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_121,(0,1):C.GC_122}) 
 
 
V_115 = Vertex(name = u'V_115', 
	 particles = [P.d2bar, P.d1, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_123,(0,1):C.GC_124}) 
 
 
V_116 = Vertex(name = u'V_116', 
	 particles = [P.d2bar, P.d2, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_125,(0,1):C.GC_126}) 
 
 
V_117 = Vertex(name = u'V_117', 
	 particles = [P.d2bar, P.d3, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_127,(0,1):C.GC_128}) 
 
 
V_118 = Vertex(name = u'V_118', 
	 particles = [P.d3bar, P.d1, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_129,(0,1):C.GC_130}) 
 
 
V_119 = Vertex(name = u'V_119', 
	 particles = [P.d3bar, P.d2, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_131,(0,1):C.GC_132}) 
 
 
V_120 = Vertex(name = u'V_120', 
	 particles = [P.d3bar, P.d3, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_133,(0,1):C.GC_134}) 
 
 
V_121 = Vertex(name = u'V_121', 
	 particles = [P.e1bar, P.e1, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_135,(0,1):C.GC_136}) 
 
 
V_122 = Vertex(name = u'V_122', 
	 particles = [P.e1bar, P.e2, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_137,(0,1):C.GC_138}) 
 
 
V_123 = Vertex(name = u'V_123', 
	 particles = [P.e1bar, P.e3, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_139,(0,1):C.GC_140}) 
 
 
V_124 = Vertex(name = u'V_124', 
	 particles = [P.e2bar, P.e1, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_141,(0,1):C.GC_142}) 
 
 
V_125 = Vertex(name = u'V_125', 
	 particles = [P.e2bar, P.e2, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_143,(0,1):C.GC_144}) 
 
 
V_126 = Vertex(name = u'V_126', 
	 particles = [P.e2bar, P.e3, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_145,(0,1):C.GC_146}) 
 
 
V_127 = Vertex(name = u'V_127', 
	 particles = [P.e3bar, P.e1, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_147,(0,1):C.GC_148}) 
 
 
V_128 = Vertex(name = u'V_128', 
	 particles = [P.e3bar, P.e2, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_149,(0,1):C.GC_150}) 
 
 
V_129 = Vertex(name = u'V_129', 
	 particles = [P.e3bar, P.e3, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_151,(0,1):C.GC_152}) 
 
 
V_130 = Vertex(name = u'V_130', 
	 particles = [P.u1bar, P.u1, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_153,(0,1):C.GC_154}) 
 
 
V_131 = Vertex(name = u'V_131', 
	 particles = [P.u1bar, P.u2, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_155,(0,1):C.GC_156}) 
 
 
V_132 = Vertex(name = u'V_132', 
	 particles = [P.u1bar, P.u3, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_157,(0,1):C.GC_158}) 
 
 
V_133 = Vertex(name = u'V_133', 
	 particles = [P.u2bar, P.u1, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_159,(0,1):C.GC_160}) 
 
 
V_134 = Vertex(name = u'V_134', 
	 particles = [P.u2bar, P.u2, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_161,(0,1):C.GC_162}) 
 
 
V_135 = Vertex(name = u'V_135', 
	 particles = [P.u2bar, P.u3, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_163,(0,1):C.GC_164}) 
 
 
V_136 = Vertex(name = u'V_136', 
	 particles = [P.u3bar, P.u1, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_165,(0,1):C.GC_166}) 
 
 
V_137 = Vertex(name = u'V_137', 
	 particles = [P.u3bar, P.u2, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_167,(0,1):C.GC_168}) 
 
 
V_138 = Vertex(name = u'V_138', 
	 particles = [P.u3bar, P.u3, P.Ah], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_169,(0,1):C.GC_170}) 
 
 
V_139 = Vertex(name = u'V_139', 
	 particles = [P.nu1, P.nu1, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_171,(0,1):C.GC_172}) 
 
 
V_140 = Vertex(name = u'V_140', 
	 particles = [P.nu1, P.nu2, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_173,(0,1):C.GC_174}) 
 
 
V_141 = Vertex(name = u'V_141', 
	 particles = [P.nu1, P.nu3, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_175,(0,1):C.GC_176}) 
 
 
V_142 = Vertex(name = u'V_142', 
	 particles = [P.nu2, P.nu2, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_177,(0,1):C.GC_178}) 
 
 
V_143 = Vertex(name = u'V_143', 
	 particles = [P.nu2, P.nu3, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_179,(0,1):C.GC_180}) 
 
 
V_144 = Vertex(name = u'V_144', 
	 particles = [P.nu3, P.nu3, P.Ah], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_181,(0,1):C.GC_182}) 
 
 
V_145 = Vertex(name = u'V_145', 
	 particles = [P.nu1, P.d1, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_183,(0,1):C.GC_184}) 
 
 
V_146 = Vertex(name = u'V_146', 
	 particles = [P.nu1, P.d1, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_185,(0,1):C.GC_186}) 
 
 
V_147 = Vertex(name = u'V_147', 
	 particles = [P.nu1, P.d2, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_187,(0,1):C.GC_188}) 
 
 
V_148 = Vertex(name = u'V_148', 
	 particles = [P.nu1, P.d2, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_189,(0,1):C.GC_190}) 
 
 
V_149 = Vertex(name = u'V_149', 
	 particles = [P.nu1, P.d3, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_191,(0,1):C.GC_192}) 
 
 
V_150 = Vertex(name = u'V_150', 
	 particles = [P.nu1, P.d3, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_193,(0,1):C.GC_194}) 
 
 
V_151 = Vertex(name = u'V_151', 
	 particles = [P.nu2, P.d1, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_195,(0,1):C.GC_196}) 
 
 
V_152 = Vertex(name = u'V_152', 
	 particles = [P.nu2, P.d1, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_197,(0,1):C.GC_198}) 
 
 
V_153 = Vertex(name = u'V_153', 
	 particles = [P.nu2, P.d2, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_199,(0,1):C.GC_200}) 
 
 
V_154 = Vertex(name = u'V_154', 
	 particles = [P.nu2, P.d2, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_201,(0,1):C.GC_202}) 
 
 
V_155 = Vertex(name = u'V_155', 
	 particles = [P.nu2, P.d3, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_203,(0,1):C.GC_204}) 
 
 
V_156 = Vertex(name = u'V_156', 
	 particles = [P.nu2, P.d3, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_205,(0,1):C.GC_206}) 
 
 
V_157 = Vertex(name = u'V_157', 
	 particles = [P.nu3, P.d1, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_207,(0,1):C.GC_208}) 
 
 
V_158 = Vertex(name = u'V_158', 
	 particles = [P.nu3, P.d1, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_209,(0,1):C.GC_210}) 
 
 
V_159 = Vertex(name = u'V_159', 
	 particles = [P.nu3, P.d2, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_211,(0,1):C.GC_212}) 
 
 
V_160 = Vertex(name = u'V_160', 
	 particles = [P.nu3, P.d2, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_213,(0,1):C.GC_214}) 
 
 
V_161 = Vertex(name = u'V_161', 
	 particles = [P.nu3, P.d3, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_215,(0,1):C.GC_216}) 
 
 
V_162 = Vertex(name = u'V_162', 
	 particles = [P.nu3, P.d3, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_217,(0,1):C.GC_218}) 
 
 
V_163 = Vertex(name = u'V_163', 
	 particles = [P.d1bar, P.d1, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_219,(0,1):C.GC_220}) 
 
 
V_164 = Vertex(name = u'V_164', 
	 particles = [P.d1bar, P.d2, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_221,(0,1):C.GC_222}) 
 
 
V_165 = Vertex(name = u'V_165', 
	 particles = [P.d1bar, P.d3, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_223,(0,1):C.GC_224}) 
 
 
V_166 = Vertex(name = u'V_166', 
	 particles = [P.d2bar, P.d1, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_225,(0,1):C.GC_226}) 
 
 
V_167 = Vertex(name = u'V_167', 
	 particles = [P.d2bar, P.d2, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_227,(0,1):C.GC_228}) 
 
 
V_168 = Vertex(name = u'V_168', 
	 particles = [P.d2bar, P.d3, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_229,(0,1):C.GC_230}) 
 
 
V_169 = Vertex(name = u'V_169', 
	 particles = [P.d3bar, P.d1, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_231,(0,1):C.GC_232}) 
 
 
V_170 = Vertex(name = u'V_170', 
	 particles = [P.d3bar, P.d2, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_233,(0,1):C.GC_234}) 
 
 
V_171 = Vertex(name = u'V_171', 
	 particles = [P.d3bar, P.d3, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_235,(0,1):C.GC_236}) 
 
 
V_172 = Vertex(name = u'V_172', 
	 particles = [P.u1bar, P.d1, P.Hp], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_237,(0,1):C.GC_238}) 
 
 
V_173 = Vertex(name = u'V_173', 
	 particles = [P.u1bar, P.d2, P.Hp], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_239,(0,1):C.GC_240}) 
 
 
V_174 = Vertex(name = u'V_174', 
	 particles = [P.u1bar, P.d3, P.Hp], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_241,(0,1):C.GC_242}) 
 
 
V_175 = Vertex(name = u'V_175', 
	 particles = [P.u2bar, P.d1, P.Hp], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_243,(0,1):C.GC_244}) 
 
 
V_176 = Vertex(name = u'V_176', 
	 particles = [P.u2bar, P.d2, P.Hp], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_245,(0,1):C.GC_246}) 
 
 
V_177 = Vertex(name = u'V_177', 
	 particles = [P.u2bar, P.d3, P.Hp], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_247,(0,1):C.GC_248}) 
 
 
V_178 = Vertex(name = u'V_178', 
	 particles = [P.u3bar, P.d1, P.Hp], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_249,(0,1):C.GC_250}) 
 
 
V_179 = Vertex(name = u'V_179', 
	 particles = [P.u3bar, P.d2, P.Hp], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_251,(0,1):C.GC_252}) 
 
 
V_180 = Vertex(name = u'V_180', 
	 particles = [P.u3bar, P.d3, P.Hp], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_253,(0,1):C.GC_254}) 
 
 
V_181 = Vertex(name = u'V_181', 
	 particles = [P.e1bar, P.d1, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS2], 
	 couplings = {(0,0):C.GC_255}) 
 
 
V_182 = Vertex(name = u'V_182', 
	 particles = [P.e1bar, P.d2, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS2], 
	 couplings = {(0,0):C.GC_256}) 
 
 
V_183 = Vertex(name = u'V_183', 
	 particles = [P.e1bar, P.d3, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS2], 
	 couplings = {(0,0):C.GC_257}) 
 
 
V_184 = Vertex(name = u'V_184', 
	 particles = [P.e2bar, P.d1, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS2], 
	 couplings = {(0,0):C.GC_258}) 
 
 
V_185 = Vertex(name = u'V_185', 
	 particles = [P.e2bar, P.d2, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS2], 
	 couplings = {(0,0):C.GC_259}) 
 
 
V_186 = Vertex(name = u'V_186', 
	 particles = [P.e2bar, P.d3, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS2], 
	 couplings = {(0,0):C.GC_260}) 
 
 
V_187 = Vertex(name = u'V_187', 
	 particles = [P.e3bar, P.d1, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS2], 
	 couplings = {(0,0):C.GC_261}) 
 
 
V_188 = Vertex(name = u'V_188', 
	 particles = [P.e3bar, P.d2, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS2], 
	 couplings = {(0,0):C.GC_262}) 
 
 
V_189 = Vertex(name = u'V_189', 
	 particles = [P.e3bar, P.d3, P.Rc], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS2], 
	 couplings = {(0,0):C.GC_263}) 
 
 
V_190 = Vertex(name = u'V_190', 
	 particles = [P.e1, P.u1, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_264,(0,1):C.GC_265}) 
 
 
V_191 = Vertex(name = u'V_191', 
	 particles = [P.e1, P.u1, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_266,(0,1):C.GC_267}) 
 
 
V_192 = Vertex(name = u'V_192', 
	 particles = [P.e1, P.u2, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_268,(0,1):C.GC_269}) 
 
 
V_193 = Vertex(name = u'V_193', 
	 particles = [P.e1, P.u2, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_270,(0,1):C.GC_271}) 
 
 
V_194 = Vertex(name = u'V_194', 
	 particles = [P.e1, P.u3, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_272,(0,1):C.GC_273}) 
 
 
V_195 = Vertex(name = u'V_195', 
	 particles = [P.e1, P.u3, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_274,(0,1):C.GC_275}) 
 
 
V_196 = Vertex(name = u'V_196', 
	 particles = [P.e2, P.u1, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_276,(0,1):C.GC_277}) 
 
 
V_197 = Vertex(name = u'V_197', 
	 particles = [P.e2, P.u1, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_278,(0,1):C.GC_279}) 
 
 
V_198 = Vertex(name = u'V_198', 
	 particles = [P.e2, P.u2, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_280,(0,1):C.GC_281}) 
 
 
V_199 = Vertex(name = u'V_199', 
	 particles = [P.e2, P.u2, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_282,(0,1):C.GC_283}) 
 
 
V_200 = Vertex(name = u'V_200', 
	 particles = [P.e2, P.u3, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_284,(0,1):C.GC_285}) 
 
 
V_201 = Vertex(name = u'V_201', 
	 particles = [P.e2, P.u3, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_286,(0,1):C.GC_287}) 
 
 
V_202 = Vertex(name = u'V_202', 
	 particles = [P.e3, P.u1, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_288,(0,1):C.GC_289}) 
 
 
V_203 = Vertex(name = u'V_203', 
	 particles = [P.e3, P.u1, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_290,(0,1):C.GC_291}) 
 
 
V_204 = Vertex(name = u'V_204', 
	 particles = [P.e3, P.u2, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_292,(0,1):C.GC_293}) 
 
 
V_205 = Vertex(name = u'V_205', 
	 particles = [P.e3, P.u2, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_294,(0,1):C.GC_295}) 
 
 
V_206 = Vertex(name = u'V_206', 
	 particles = [P.e3, P.u3, P.S1c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_296,(0,1):C.GC_297}) 
 
 
V_207 = Vertex(name = u'V_207', 
	 particles = [P.e3, P.u3, P.S2c], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_298,(0,1):C.GC_299}) 
 
 
V_208 = Vertex(name = u'V_208', 
	 particles = [P.nu1, P.e1, P.Hp], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_300,(0,1):C.GC_301}) 
 
 
V_209 = Vertex(name = u'V_209', 
	 particles = [P.nu1, P.e2, P.Hp], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_302,(0,1):C.GC_303}) 
 
 
V_210 = Vertex(name = u'V_210', 
	 particles = [P.nu1, P.e3, P.Hp], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_304,(0,1):C.GC_305}) 
 
 
V_211 = Vertex(name = u'V_211', 
	 particles = [P.nu2, P.e1, P.Hp], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_306,(0,1):C.GC_307}) 
 
 
V_212 = Vertex(name = u'V_212', 
	 particles = [P.nu2, P.e2, P.Hp], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_308,(0,1):C.GC_309}) 
 
 
V_213 = Vertex(name = u'V_213', 
	 particles = [P.nu2, P.e3, P.Hp], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_310,(0,1):C.GC_311}) 
 
 
V_214 = Vertex(name = u'V_214', 
	 particles = [P.nu3, P.e1, P.Hp], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_312,(0,1):C.GC_313}) 
 
 
V_215 = Vertex(name = u'V_215', 
	 particles = [P.nu3, P.e2, P.Hp], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_314,(0,1):C.GC_315}) 
 
 
V_216 = Vertex(name = u'V_216', 
	 particles = [P.nu3, P.e3, P.Hp], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_316,(0,1):C.GC_317}) 
 
 
V_217 = Vertex(name = u'V_217', 
	 particles = [P.e1bar, P.e1, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_318,(0,1):C.GC_319}) 
 
 
V_218 = Vertex(name = u'V_218', 
	 particles = [P.e1bar, P.e2, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_320,(0,1):C.GC_321}) 
 
 
V_219 = Vertex(name = u'V_219', 
	 particles = [P.e1bar, P.e3, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_322,(0,1):C.GC_323}) 
 
 
V_220 = Vertex(name = u'V_220', 
	 particles = [P.e2bar, P.e1, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_324,(0,1):C.GC_325}) 
 
 
V_221 = Vertex(name = u'V_221', 
	 particles = [P.e2bar, P.e2, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_326,(0,1):C.GC_327}) 
 
 
V_222 = Vertex(name = u'V_222', 
	 particles = [P.e2bar, P.e3, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_328,(0,1):C.GC_329}) 
 
 
V_223 = Vertex(name = u'V_223', 
	 particles = [P.e3bar, P.e1, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_330,(0,1):C.GC_331}) 
 
 
V_224 = Vertex(name = u'V_224', 
	 particles = [P.e3bar, P.e2, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_332,(0,1):C.GC_333}) 
 
 
V_225 = Vertex(name = u'V_225', 
	 particles = [P.e3bar, P.e3, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_334,(0,1):C.GC_335}) 
 
 
V_226 = Vertex(name = u'V_226', 
	 particles = [P.d1bar, P.e1, P.R], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1], 
	 couplings = {(0,0):C.GC_336}) 
 
 
V_227 = Vertex(name = u'V_227', 
	 particles = [P.d1bar, P.e2, P.R], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1], 
	 couplings = {(0,0):C.GC_337}) 
 
 
V_228 = Vertex(name = u'V_228', 
	 particles = [P.d1bar, P.e3, P.R], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1], 
	 couplings = {(0,0):C.GC_338}) 
 
 
V_229 = Vertex(name = u'V_229', 
	 particles = [P.d2bar, P.e1, P.R], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1], 
	 couplings = {(0,0):C.GC_339}) 
 
 
V_230 = Vertex(name = u'V_230', 
	 particles = [P.d2bar, P.e2, P.R], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1], 
	 couplings = {(0,0):C.GC_340}) 
 
 
V_231 = Vertex(name = u'V_231', 
	 particles = [P.d2bar, P.e3, P.R], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1], 
	 couplings = {(0,0):C.GC_341}) 
 
 
V_232 = Vertex(name = u'V_232', 
	 particles = [P.d3bar, P.e1, P.R], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1], 
	 couplings = {(0,0):C.GC_342}) 
 
 
V_233 = Vertex(name = u'V_233', 
	 particles = [P.d3bar, P.e2, P.R], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1], 
	 couplings = {(0,0):C.GC_343}) 
 
 
V_234 = Vertex(name = u'V_234', 
	 particles = [P.d3bar, P.e3, P.R], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1], 
	 couplings = {(0,0):C.GC_344}) 
 
 
V_235 = Vertex(name = u'V_235', 
	 particles = [P.u1bar, P.u1, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_345,(0,1):C.GC_346}) 
 
 
V_236 = Vertex(name = u'V_236', 
	 particles = [P.u1bar, P.u2, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_347,(0,1):C.GC_348}) 
 
 
V_237 = Vertex(name = u'V_237', 
	 particles = [P.u1bar, P.u3, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_349,(0,1):C.GC_350}) 
 
 
V_238 = Vertex(name = u'V_238', 
	 particles = [P.u2bar, P.u1, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_351,(0,1):C.GC_352}) 
 
 
V_239 = Vertex(name = u'V_239', 
	 particles = [P.u2bar, P.u2, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_353,(0,1):C.GC_354}) 
 
 
V_240 = Vertex(name = u'V_240', 
	 particles = [P.u2bar, P.u3, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_355,(0,1):C.GC_356}) 
 
 
V_241 = Vertex(name = u'V_241', 
	 particles = [P.u3bar, P.u1, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_357,(0,1):C.GC_358}) 
 
 
V_242 = Vertex(name = u'V_242', 
	 particles = [P.u3bar, P.u2, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_359,(0,1):C.GC_360}) 
 
 
V_243 = Vertex(name = u'V_243', 
	 particles = [P.u3bar, P.u3, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_361,(0,1):C.GC_362}) 
 
 
V_244 = Vertex(name = u'V_244', 
	 particles = [P.d1bar, P.u1, P.Hpc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_363,(0,1):C.GC_364}) 
 
 
V_245 = Vertex(name = u'V_245', 
	 particles = [P.d1bar, P.u2, P.Hpc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_365,(0,1):C.GC_366}) 
 
 
V_246 = Vertex(name = u'V_246', 
	 particles = [P.d1bar, P.u3, P.Hpc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_367,(0,1):C.GC_368}) 
 
 
V_247 = Vertex(name = u'V_247', 
	 particles = [P.d2bar, P.u1, P.Hpc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_369,(0,1):C.GC_370}) 
 
 
V_248 = Vertex(name = u'V_248', 
	 particles = [P.d2bar, P.u2, P.Hpc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_371,(0,1):C.GC_372}) 
 
 
V_249 = Vertex(name = u'V_249', 
	 particles = [P.d2bar, P.u3, P.Hpc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_373,(0,1):C.GC_374}) 
 
 
V_250 = Vertex(name = u'V_250', 
	 particles = [P.d3bar, P.u1, P.Hpc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_375,(0,1):C.GC_376}) 
 
 
V_251 = Vertex(name = u'V_251', 
	 particles = [P.d3bar, P.u2, P.Hpc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_377,(0,1):C.GC_378}) 
 
 
V_252 = Vertex(name = u'V_252', 
	 particles = [P.d3bar, P.u3, P.Hpc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_379,(0,1):C.GC_380}) 
 
 
V_253 = Vertex(name = u'V_253', 
	 particles = [P.nu1, P.nu1, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_381,(0,1):C.GC_382}) 
 
 
V_254 = Vertex(name = u'V_254', 
	 particles = [P.nu1, P.nu2, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_383,(0,1):C.GC_384}) 
 
 
V_255 = Vertex(name = u'V_255', 
	 particles = [P.nu1, P.nu3, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_385,(0,1):C.GC_386}) 
 
 
V_256 = Vertex(name = u'V_256', 
	 particles = [P.nu2, P.nu2, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_387,(0,1):C.GC_388}) 
 
 
V_257 = Vertex(name = u'V_257', 
	 particles = [P.nu2, P.nu3, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_389,(0,1):C.GC_390}) 
 
 
V_258 = Vertex(name = u'V_258', 
	 particles = [P.nu3, P.nu3, P.h], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_391,(0,1):C.GC_392}) 
 
 
V_259 = Vertex(name = u'V_259', 
	 particles = [P.d1bar, P.nu1, P.S1], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_393,(0,1):C.GC_394}) 
 
 
V_260 = Vertex(name = u'V_260', 
	 particles = [P.d1bar, P.nu1, P.S2], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_395,(0,1):C.GC_396}) 
 
 
V_261 = Vertex(name = u'V_261', 
	 particles = [P.d1bar, P.nu2, P.S1], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_397,(0,1):C.GC_398}) 
 
 
V_262 = Vertex(name = u'V_262', 
	 particles = [P.d1bar, P.nu2, P.S2], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_399,(0,1):C.GC_400}) 
 
 
V_263 = Vertex(name = u'V_263', 
	 particles = [P.d1bar, P.nu3, P.S1], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_401,(0,1):C.GC_402}) 
 
 
V_264 = Vertex(name = u'V_264', 
	 particles = [P.d1bar, P.nu3, P.S2], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_403,(0,1):C.GC_404}) 
 
 
V_265 = Vertex(name = u'V_265', 
	 particles = [P.d2bar, P.nu1, P.S1], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_405,(0,1):C.GC_406}) 
 
 
V_266 = Vertex(name = u'V_266', 
	 particles = [P.d2bar, P.nu1, P.S2], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_407,(0,1):C.GC_408}) 
 
 
V_267 = Vertex(name = u'V_267', 
	 particles = [P.d2bar, P.nu2, P.S1], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_409,(0,1):C.GC_410}) 
 
 
V_268 = Vertex(name = u'V_268', 
	 particles = [P.d2bar, P.nu2, P.S2], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_411,(0,1):C.GC_412}) 
 
 
V_269 = Vertex(name = u'V_269', 
	 particles = [P.d2bar, P.nu3, P.S1], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_413,(0,1):C.GC_414}) 
 
 
V_270 = Vertex(name = u'V_270', 
	 particles = [P.d2bar, P.nu3, P.S2], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_415,(0,1):C.GC_416}) 
 
 
V_271 = Vertex(name = u'V_271', 
	 particles = [P.d3bar, P.nu1, P.S1], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_417,(0,1):C.GC_418}) 
 
 
V_272 = Vertex(name = u'V_272', 
	 particles = [P.d3bar, P.nu1, P.S2], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_419,(0,1):C.GC_420}) 
 
 
V_273 = Vertex(name = u'V_273', 
	 particles = [P.d3bar, P.nu2, P.S1], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_421,(0,1):C.GC_422}) 
 
 
V_274 = Vertex(name = u'V_274', 
	 particles = [P.d3bar, P.nu2, P.S2], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_423,(0,1):C.GC_424}) 
 
 
V_275 = Vertex(name = u'V_275', 
	 particles = [P.d3bar, P.nu3, P.S1], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_425,(0,1):C.GC_426}) 
 
 
V_276 = Vertex(name = u'V_276', 
	 particles = [P.d3bar, P.nu3, P.S2], 
	 color = [u'Identity(1,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_427,(0,1):C.GC_428}) 
 
 
V_277 = Vertex(name = u'V_277', 
	 particles = [P.e1bar, P.nu1, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_429,(0,1):C.GC_430}) 
 
 
V_278 = Vertex(name = u'V_278', 
	 particles = [P.e1bar, P.nu2, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_431,(0,1):C.GC_432}) 
 
 
V_279 = Vertex(name = u'V_279', 
	 particles = [P.e1bar, P.nu3, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_433,(0,1):C.GC_434}) 
 
 
V_280 = Vertex(name = u'V_280', 
	 particles = [P.e2bar, P.nu1, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_435,(0,1):C.GC_436}) 
 
 
V_281 = Vertex(name = u'V_281', 
	 particles = [P.e2bar, P.nu2, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_437,(0,1):C.GC_438}) 
 
 
V_282 = Vertex(name = u'V_282', 
	 particles = [P.e2bar, P.nu3, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_439,(0,1):C.GC_440}) 
 
 
V_283 = Vertex(name = u'V_283', 
	 particles = [P.e3bar, P.nu1, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_441,(0,1):C.GC_442}) 
 
 
V_284 = Vertex(name = u'V_284', 
	 particles = [P.e3bar, P.nu2, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_443,(0,1):C.GC_444}) 
 
 
V_285 = Vertex(name = u'V_285', 
	 particles = [P.e3bar, P.nu3, P.Hpc], 
	 color = [u'1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_445,(0,1):C.GC_446}) 
 
 
V_286 = Vertex(name = u'V_286', 
	 particles = [P.e1bar, P.u1bar, P.S1], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_447,(0,1):C.GC_448}) 
 
 
V_287 = Vertex(name = u'V_287', 
	 particles = [P.e1bar, P.u1bar, P.S2], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_449,(0,1):C.GC_450}) 
 
 
V_288 = Vertex(name = u'V_288', 
	 particles = [P.e1bar, P.u2bar, P.S1], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_451,(0,1):C.GC_452}) 
 
 
V_289 = Vertex(name = u'V_289', 
	 particles = [P.e1bar, P.u2bar, P.S2], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_453,(0,1):C.GC_454}) 
 
 
V_290 = Vertex(name = u'V_290', 
	 particles = [P.e1bar, P.u3bar, P.S1], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_455,(0,1):C.GC_456}) 
 
 
V_291 = Vertex(name = u'V_291', 
	 particles = [P.e1bar, P.u3bar, P.S2], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_457,(0,1):C.GC_458}) 
 
 
V_292 = Vertex(name = u'V_292', 
	 particles = [P.e2bar, P.u1bar, P.S1], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_459,(0,1):C.GC_460}) 
 
 
V_293 = Vertex(name = u'V_293', 
	 particles = [P.e2bar, P.u1bar, P.S2], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_461,(0,1):C.GC_462}) 
 
 
V_294 = Vertex(name = u'V_294', 
	 particles = [P.e2bar, P.u2bar, P.S1], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_463,(0,1):C.GC_464}) 
 
 
V_295 = Vertex(name = u'V_295', 
	 particles = [P.e2bar, P.u2bar, P.S2], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_465,(0,1):C.GC_466}) 
 
 
V_296 = Vertex(name = u'V_296', 
	 particles = [P.e2bar, P.u3bar, P.S1], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_467,(0,1):C.GC_468}) 
 
 
V_297 = Vertex(name = u'V_297', 
	 particles = [P.e2bar, P.u3bar, P.S2], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_469,(0,1):C.GC_470}) 
 
 
V_298 = Vertex(name = u'V_298', 
	 particles = [P.e3bar, P.u1bar, P.S1], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_471,(0,1):C.GC_472}) 
 
 
V_299 = Vertex(name = u'V_299', 
	 particles = [P.e3bar, P.u1bar, P.S2], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_473,(0,1):C.GC_474}) 
 
 
V_300 = Vertex(name = u'V_300', 
	 particles = [P.e3bar, P.u2bar, P.S1], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_475,(0,1):C.GC_476}) 
 
 
V_301 = Vertex(name = u'V_301', 
	 particles = [P.e3bar, P.u2bar, P.S2], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_477,(0,1):C.GC_478}) 
 
 
V_302 = Vertex(name = u'V_302', 
	 particles = [P.e3bar, P.u3bar, P.S1], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_479,(0,1):C.GC_480}) 
 
 
V_303 = Vertex(name = u'V_303', 
	 particles = [P.e3bar, P.u3bar, P.S2], 
	 color = [u'Identity(2,3)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_481,(0,1):C.GC_482}) 
 
 
V_304 = Vertex(name = u'V_304', 
	 particles = [P.d1bar, P.d1, P.g], 
	 color = [u'T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_483,(0,0):C.GC_484}) 
 
 
V_305 = Vertex(name = u'V_305', 
	 particles = [P.d2bar, P.d2, P.g], 
	 color = [u'T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_485,(0,0):C.GC_486}) 
 
 
V_306 = Vertex(name = u'V_306', 
	 particles = [P.d3bar, P.d3, P.g], 
	 color = [u'T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_487,(0,0):C.GC_488}) 
 
 
V_307 = Vertex(name = u'V_307', 
	 particles = [P.d1bar, P.d1, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_489,(0,0):C.GC_490}) 
 
 
V_308 = Vertex(name = u'V_308', 
	 particles = [P.d2bar, P.d2, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_491,(0,0):C.GC_492}) 
 
 
V_309 = Vertex(name = u'V_309', 
	 particles = [P.d3bar, P.d3, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_493,(0,0):C.GC_494}) 
 
 
V_310 = Vertex(name = u'V_310', 
	 particles = [P.d1bar, P.d1, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_495,(0,0):C.GC_496}) 
 
 
V_311 = Vertex(name = u'V_311', 
	 particles = [P.d2bar, P.d2, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_497,(0,0):C.GC_498}) 
 
 
V_312 = Vertex(name = u'V_312', 
	 particles = [P.d3bar, P.d3, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_499,(0,0):C.GC_500}) 
 
 
V_313 = Vertex(name = u'V_313', 
	 particles = [P.u1bar, P.d1, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_501}) 
 
 
V_314 = Vertex(name = u'V_314', 
	 particles = [P.u1bar, P.d2, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_502}) 
 
 
V_315 = Vertex(name = u'V_315', 
	 particles = [P.u1bar, P.d3, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_503}) 
 
 
V_316 = Vertex(name = u'V_316', 
	 particles = [P.u2bar, P.d1, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_504}) 
 
 
V_317 = Vertex(name = u'V_317', 
	 particles = [P.u2bar, P.d2, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_505}) 
 
 
V_318 = Vertex(name = u'V_318', 
	 particles = [P.u2bar, P.d3, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_506}) 
 
 
V_319 = Vertex(name = u'V_319', 
	 particles = [P.u3bar, P.d1, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_507}) 
 
 
V_320 = Vertex(name = u'V_320', 
	 particles = [P.u3bar, P.d2, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_508}) 
 
 
V_321 = Vertex(name = u'V_321', 
	 particles = [P.u3bar, P.d3, P.Wmc], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_509}) 
 
 
V_322 = Vertex(name = u'V_322', 
	 particles = [P.nu1, P.e1, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_510}) 
 
 
V_323 = Vertex(name = u'V_323', 
	 particles = [P.nu1, P.e2, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_511}) 
 
 
V_324 = Vertex(name = u'V_324', 
	 particles = [P.nu1, P.e3, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_512}) 
 
 
V_325 = Vertex(name = u'V_325', 
	 particles = [P.nu2, P.e1, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_513}) 
 
 
V_326 = Vertex(name = u'V_326', 
	 particles = [P.nu2, P.e2, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_514}) 
 
 
V_327 = Vertex(name = u'V_327', 
	 particles = [P.nu2, P.e3, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_515}) 
 
 
V_328 = Vertex(name = u'V_328', 
	 particles = [P.nu3, P.e1, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_516}) 
 
 
V_329 = Vertex(name = u'V_329', 
	 particles = [P.nu3, P.e2, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_517}) 
 
 
V_330 = Vertex(name = u'V_330', 
	 particles = [P.nu3, P.e3, P.Wmc], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_518}) 
 
 
V_331 = Vertex(name = u'V_331', 
	 particles = [P.e1bar, P.e1, P.A], 
	 color = [u'1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_519,(0,0):C.GC_520}) 
 
 
V_332 = Vertex(name = u'V_332', 
	 particles = [P.e2bar, P.e2, P.A], 
	 color = [u'1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_521,(0,0):C.GC_522}) 
 
 
V_333 = Vertex(name = u'V_333', 
	 particles = [P.e3bar, P.e3, P.A], 
	 color = [u'1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_523,(0,0):C.GC_524}) 
 
 
V_334 = Vertex(name = u'V_334', 
	 particles = [P.e1bar, P.e1, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_525,(0,0):C.GC_526}) 
 
 
V_335 = Vertex(name = u'V_335', 
	 particles = [P.e2bar, P.e2, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_527,(0,0):C.GC_528}) 
 
 
V_336 = Vertex(name = u'V_336', 
	 particles = [P.e3bar, P.e3, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_529,(0,0):C.GC_530}) 
 
 
V_337 = Vertex(name = u'V_337', 
	 particles = [P.u1bar, P.u1, P.g], 
	 color = [u'T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_531,(0,0):C.GC_532}) 
 
 
V_338 = Vertex(name = u'V_338', 
	 particles = [P.u2bar, P.u2, P.g], 
	 color = [u'T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_533,(0,0):C.GC_534}) 
 
 
V_339 = Vertex(name = u'V_339', 
	 particles = [P.u3bar, P.u3, P.g], 
	 color = [u'T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_535,(0,0):C.GC_536}) 
 
 
V_340 = Vertex(name = u'V_340', 
	 particles = [P.u1bar, P.u1, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_537,(0,0):C.GC_538}) 
 
 
V_341 = Vertex(name = u'V_341', 
	 particles = [P.u2bar, P.u2, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_539,(0,0):C.GC_540}) 
 
 
V_342 = Vertex(name = u'V_342', 
	 particles = [P.u3bar, P.u3, P.A], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_541,(0,0):C.GC_542}) 
 
 
V_343 = Vertex(name = u'V_343', 
	 particles = [P.d1bar, P.u1, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_543}) 
 
 
V_344 = Vertex(name = u'V_344', 
	 particles = [P.d1bar, P.u2, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_544}) 
 
 
V_345 = Vertex(name = u'V_345', 
	 particles = [P.d1bar, P.u3, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_545}) 
 
 
V_346 = Vertex(name = u'V_346', 
	 particles = [P.d2bar, P.u1, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_546}) 
 
 
V_347 = Vertex(name = u'V_347', 
	 particles = [P.d2bar, P.u2, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_547}) 
 
 
V_348 = Vertex(name = u'V_348', 
	 particles = [P.d2bar, P.u3, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_548}) 
 
 
V_349 = Vertex(name = u'V_349', 
	 particles = [P.d3bar, P.u1, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_549}) 
 
 
V_350 = Vertex(name = u'V_350', 
	 particles = [P.d3bar, P.u2, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_550}) 
 
 
V_351 = Vertex(name = u'V_351', 
	 particles = [P.d3bar, P.u3, P.Wm], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_551}) 
 
 
V_352 = Vertex(name = u'V_352', 
	 particles = [P.u1bar, P.u1, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_552,(0,0):C.GC_553}) 
 
 
V_353 = Vertex(name = u'V_353', 
	 particles = [P.u2bar, P.u2, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_554,(0,0):C.GC_555}) 
 
 
V_354 = Vertex(name = u'V_354', 
	 particles = [P.u3bar, P.u3, P.Z], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_556,(0,0):C.GC_557}) 
 
 
V_355 = Vertex(name = u'V_355', 
	 particles = [P.nu1, P.nu1, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_558,(0,0):C.GC_559}) 
 
 
V_356 = Vertex(name = u'V_356', 
	 particles = [P.nu2, P.nu2, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_560,(0,0):C.GC_561}) 
 
 
V_357 = Vertex(name = u'V_357', 
	 particles = [P.nu3, P.nu3, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_562,(0,0):C.GC_563}) 
 
 
V_358 = Vertex(name = u'V_358', 
	 particles = [P.e1bar, P.nu1, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_564}) 
 
 
V_359 = Vertex(name = u'V_359', 
	 particles = [P.e1bar, P.nu2, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_565}) 
 
 
V_360 = Vertex(name = u'V_360', 
	 particles = [P.e1bar, P.nu3, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_566}) 
 
 
V_361 = Vertex(name = u'V_361', 
	 particles = [P.e2bar, P.nu1, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_567}) 
 
 
V_362 = Vertex(name = u'V_362', 
	 particles = [P.e2bar, P.nu2, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_568}) 
 
 
V_363 = Vertex(name = u'V_363', 
	 particles = [P.e2bar, P.nu3, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_569}) 
 
 
V_364 = Vertex(name = u'V_364', 
	 particles = [P.e3bar, P.nu1, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_570}) 
 
 
V_365 = Vertex(name = u'V_365', 
	 particles = [P.e3bar, P.nu2, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_571}) 
 
 
V_366 = Vertex(name = u'V_366', 
	 particles = [P.e3bar, P.nu3, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_572}) 
 
 
V_367 = Vertex(name = u'V_367', 
	 particles = [P.g, P.g, P.g], 
	 color = [u'f(1,2,3)'], 
	 lorentz = [L.VVV1], 
	 couplings = {(0,0):C.GC_573}) 
 
 
V_368 = Vertex(name = u'V_368', 
	 particles = [P.Wmc, P.A, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.VVV1], 
	 couplings = {(0,0):C.GC_574}) 
 
 
V_369 = Vertex(name = u'V_369', 
	 particles = [P.Wmc, P.Wm, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.VVV1], 
	 couplings = {(0,0):C.GC_575}) 
 
 
V_370 = Vertex(name = u'V_370', 
	 particles = [P.g, P.g, P.g, P.g], 
	 color = [u'f(-1,1,4)*f(-1,2,3)', u'f(-1,1,3)*f(-1,2,4)', u'f(-1,1,2)*f(-1,3,4)'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_576,(1,0):C.GC_577,(0,1):C.GC_578,(2,1):C.GC_579,(1,2):C.GC_580,(2,2):C.GC_581}) 
 
 
V_371 = Vertex(name = u'V_371', 
	 particles = [P.Wmc, P.A, P.A, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_582,(0,1):C.GC_583,(0,2):C.GC_584}) 
 
 
V_372 = Vertex(name = u'V_372', 
	 particles = [P.Wmc, P.A, P.Wm, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_585,(0,1):C.GC_586,(0,2):C.GC_587}) 
 
 
V_373 = Vertex(name = u'V_373', 
	 particles = [P.Wmc, P.Wmc, P.Wm, P.Wm], 
	 color = [u'1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_588,(0,1):C.GC_589,(0,2):C.GC_590}) 
 
 
V_374 = Vertex(name = u'V_374', 
	 particles = [P.Wmc, P.Wm, P.Z, P.Z], 
	 color = [u'1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_591,(0,1):C.GC_592,(0,2):C.GC_593}) 
 
 
V_375 = Vertex(name = u'V_375', 
	 particles = [P.A, P.A, P.h], 
	 color = [u'1'], 
	 lorentz = [L.VVS99], 
	 couplings = {(0,0):C.GC_594}) 
 
 
V_376 = Vertex(name = u'V_376', 
	 particles = [P.g, P.g, P.h], 
	 color = [u'Identity(1,2)'], 
	 lorentz = [L.VVS99], 
	 couplings = {(0,0):C.GC_595}) 
 
 
