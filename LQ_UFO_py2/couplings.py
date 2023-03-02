from __future__ import absolute_import
from object_library import all_couplings,Coupling 
from cmath import exp 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
 
GC_1 = Coupling(name = u'GC_1',
	 value = u'-1*complex(0,1)*vvSM*complexconjugate(Lam)', 
	 order = {u'QED':1} ) 
 
GC_2 = Coupling(name = u'GC_2',
	 value = u'-((ZH12*complexconjugate(a1)*complexconjugate(ZH11) - a1*ZH11*complexconjugate(ZH12))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_3 = Coupling(name = u'GC_3',
	 value = u'-((ZH12*complexconjugate(a1)*complexconjugate(ZH21) - a1*ZH11*complexconjugate(ZH22))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_4 = Coupling(name = u'GC_4',
	 value = u'-((ZH22*complexconjugate(a1)*complexconjugate(ZH11) - a1*ZH21*complexconjugate(ZH12))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_5 = Coupling(name = u'GC_5',
	 value = u'-((ZH22*complexconjugate(a1)*complexconjugate(ZH21) - a1*ZH21*complexconjugate(ZH22))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_6 = Coupling(name = u'GC_6',
	 value = u'-3*complex(0,1)*vvSM*complexconjugate(Lam)', 
	 order = {u'QED':1} ) 
 
GC_7 = Coupling(name = u'GC_7',
	 value = u'-1*complex(0,1)*vvSM*complexconjugate(Lam)', 
	 order = {u'QED':1} ) 
 
GC_8 = Coupling(name = u'GC_8',
	 value = u'-1*complex(0,1)*vvSM*complexconjugate(gHR)', 
	 order = {u'QED':1} ) 
 
GC_9 = Coupling(name = u'GC_9',
	 value = u'-1./2.*complex(0,1)*(ZH11*(2*vvSM*complexconjugate(gHS)*complexconjugate(ZH11) + cmath.sqrt(2)*a1*complexconjugate(ZH12)) + ZH12*(cmath.sqrt(2)*complexconjugate(a1)*complexconjugate(ZH11) + 2*vvSM*(complexconjugate(gHR) + complexconjugate(ghrp))*complexconjugate(ZH12)))', 
	 order = {u'QED':1} ) 
 
GC_10 = Coupling(name = u'GC_10',
	 value = u'-1./2.*complex(0,1)*(ZH11*(2*vvSM*complexconjugate(gHS)*complexconjugate(ZH21) + cmath.sqrt(2)*a1*complexconjugate(ZH22)) + ZH12*(cmath.sqrt(2)*complexconjugate(a1)*complexconjugate(ZH21) + 2*vvSM*(complexconjugate(gHR) + complexconjugate(ghrp))*complexconjugate(ZH22)))', 
	 order = {u'QED':1} ) 
 
GC_11 = Coupling(name = u'GC_11',
	 value = u'-1./2.*complex(0,1)*(ZH21*(2*vvSM*complexconjugate(gHS)*complexconjugate(ZH11) + cmath.sqrt(2)*a1*complexconjugate(ZH12)) + ZH22*(cmath.sqrt(2)*complexconjugate(a1)*complexconjugate(ZH11) + 2*vvSM*(complexconjugate(gHR) + complexconjugate(ghrp))*complexconjugate(ZH12)))', 
	 order = {u'QED':1} ) 
 
GC_12 = Coupling(name = u'GC_12',
	 value = u'-1./2.*complex(0,1)*(ZH21*(2*vvSM*complexconjugate(gHS)*complexconjugate(ZH21) + cmath.sqrt(2)*a1*complexconjugate(ZH22)) + ZH22*(cmath.sqrt(2)*complexconjugate(a1)*complexconjugate(ZH21) + 2*vvSM*(complexconjugate(gHR) + complexconjugate(ghrp))*complexconjugate(ZH22)))', 
	 order = {u'QED':1} ) 
 
GC_13 = Coupling(name = u'GC_13',
	 value = u'-1./2.*complex(0,1)*(2*a1*ZH11 + cmath.sqrt(2)*vvSM*ZH12*complexconjugate(ghrp))', 
	 order = {u'QED':1} ) 
 
GC_14 = Coupling(name = u'GC_14',
	 value = u'-1./2.*complex(0,1)*(2*a1*ZH21 + cmath.sqrt(2)*vvSM*ZH22*complexconjugate(ghrp))', 
	 order = {u'QED':1} ) 
 
GC_15 = Coupling(name = u'GC_15',
	 value = u'2*complex(0,1)*(-(ZH12*ZH21) + ZH11*ZH22)*complexconjugate(lRRS)', 
	 order = {u'QED':1} ) 
 
GC_16 = Coupling(name = u'GC_16',
	 value = u'-1./2.*complex(0,1)*(2*complexconjugate(a1)*complexconjugate(ZH11) + cmath.sqrt(2)*vvSM*complexconjugate(ghrp)*complexconjugate(ZH12))', 
	 order = {u'QED':1} ) 
 
GC_17 = Coupling(name = u'GC_17',
	 value = u'-1./2.*complex(0,1)*(2*complexconjugate(a1)*complexconjugate(ZH21) + cmath.sqrt(2)*vvSM*complexconjugate(ghrp)*complexconjugate(ZH22))', 
	 order = {u'QED':1} ) 
 
GC_18 = Coupling(name = u'GC_18',
	 value = u'2*complex(0,1)*lRRS*(-(complexconjugate(ZH12)*complexconjugate(ZH21)) + complexconjugate(ZH11)*complexconjugate(ZH22))', 
	 order = {u'QED':1} ) 
 
GC_19 = Coupling(name = u'GC_19',
	 value = u'1./2.*complex(0,1)*g2**2', 
	 order = {u'QED':2} ) 
 
GC_20 = Coupling(name = u'GC_20',
	 value = u'1./2.*complex(0,1)*g2**2*cmath.cos(TW)**2 + 1*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g1**2*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_21 = Coupling(name = u'GC_21',
	 value = u'(g1*g2*cmath.cos(TW))/2.', 
	 order = {u'QED':2} ) 
 
GC_22 = Coupling(name = u'GC_22',
	 value = u'-1./2.*(g1*g2*cmath.sin(TW))', 
	 order = {u'QED':2} ) 
 
GC_23 = Coupling(name = u'GC_23',
	 value = u'-1./2.*(g1*g2*cmath.cos(TW))', 
	 order = {u'QED':2} ) 
 
GC_24 = Coupling(name = u'GC_24',
	 value = u'(g1*g2*cmath.sin(TW))/2.', 
	 order = {u'QED':2} ) 
 
GC_25 = Coupling(name = u'GC_25',
	 value = u'1./2.*complex(0,1)*g2**2', 
	 order = {u'QED':2} ) 
 
GC_26 = Coupling(name = u'GC_26',
	 value = u'1./2.*complex(0,1)*g2**2*cmath.cos(TW)**2 + 1*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g1**2*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_27 = Coupling(name = u'GC_27',
	 value = u'1./2.*complex(0,1)*g1*g2*cmath.cos(TW)', 
	 order = {u'QED':2} ) 
 
GC_28 = Coupling(name = u'GC_28',
	 value = u'-1./2.*complex(0,1)*g1*g2*cmath.sin(TW)', 
	 order = {u'QED':2} ) 
 
GC_29 = Coupling(name = u'GC_29',
	 value = u'1./2.*complex(0,1)*g1*g2*cmath.cos(TW)', 
	 order = {u'QED':2} ) 
 
GC_30 = Coupling(name = u'GC_30',
	 value = u'-1./2.*complex(0,1)*g1*g2*cmath.sin(TW)', 
	 order = {u'QED':2} ) 
 
GC_31 = Coupling(name = u'GC_31',
	 value = u'1./2.*complex(0,1)*g1**2*cmath.cos(TW)**2 + 1*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_32 = Coupling(name = u'GC_32',
	 value = u'1./2.*complex(0,1)*g1*g2*cmath.cos(2*TW) - 1./4.*complex(0,1)*g1**2*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {u'QED':2} ) 
 
GC_33 = Coupling(name = u'GC_33',
	 value = u'1./2.*complex(0,1)*g2**2', 
	 order = {u'QED':2} ) 
 
GC_34 = Coupling(name = u'GC_34',
	 value = u'1./2.*complex(0,1)*g2**2*cmath.cos(TW)**2 - 1*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g1**2*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_35 = Coupling(name = u'GC_35',
	 value = u'1*complex(0,1)*G**2', 
	 order = {u'QCD':2} ) 
 
GC_36 = Coupling(name = u'GC_36',
	 value = u'1*complex(0,1)*G**2', 
	 order = {u'QCD':2} ) 
 
GC_37 = Coupling(name = u'GC_37',
	 value = u'1./3.*complex(0,1)*G*g1*cmath.cos(TW) + 1*complex(0,1)*G*g2*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_38 = Coupling(name = u'GC_38',
	 value = u'1*complex(0,1)*cmath.sqrt(2)*G*g2*complexconjugate(ZH12)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_39 = Coupling(name = u'GC_39',
	 value = u'1*complex(0,1)*cmath.sqrt(2)*G*g2*complexconjugate(ZH22)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_40 = Coupling(name = u'GC_40',
	 value = u'1*complex(0,1)*G*g2*cmath.cos(TW) - 1./3.*complex(0,1)*G*g1*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_41 = Coupling(name = u'GC_41',
	 value = u'1./18.*complex(0,1)*g1**2*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_42 = Coupling(name = u'GC_42',
	 value = u'(1./3.*complex(0,1)*g1*g2*complexconjugate(ZH12)*cmath.cos(TW))/cmath.sqrt(2)', 
	 order = {u'QED':2} ) 
 
GC_43 = Coupling(name = u'GC_43',
	 value = u'(1./3.*complex(0,1)*g1*g2*complexconjugate(ZH22)*cmath.cos(TW))/cmath.sqrt(2)', 
	 order = {u'QED':2} ) 
 
GC_44 = Coupling(name = u'GC_44',
	 value = u'1./6.*complex(0,1)*g1*g2*cmath.cos(2*TW) - 1./36.*complex(0,1)*g1**2*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {u'QED':2} ) 
 
GC_45 = Coupling(name = u'GC_45',
	 value = u'(-1./3.*complex(0,1)*g1*g2*complexconjugate(ZH12)*cmath.sin(TW))/cmath.sqrt(2)', 
	 order = {u'QED':2} ) 
 
GC_46 = Coupling(name = u'GC_46',
	 value = u'(-1./3.*complex(0,1)*g1*g2*complexconjugate(ZH22)*cmath.sin(TW))/cmath.sqrt(2)', 
	 order = {u'QED':2} ) 
 
GC_47 = Coupling(name = u'GC_47',
	 value = u'1./2.*complex(0,1)*g2**2', 
	 order = {u'QED':2} ) 
 
GC_48 = Coupling(name = u'GC_48',
	 value = u'1./2.*complex(0,1)*g2**2*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./18.*complex(0,1)*g1**2*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_49 = Coupling(name = u'GC_49',
	 value = u'1*complex(0,1)*G**2*ZH11*complexconjugate(ZH11) + 1*complex(0,1)*G**2*ZH12*complexconjugate(ZH12)', 
	 order = {u'QCD':2} ) 
 
GC_50 = Coupling(name = u'GC_50',
	 value = u'1*complex(0,1)*G**2*ZH11*complexconjugate(ZH11) + 1*complex(0,1)*G**2*ZH12*complexconjugate(ZH12)', 
	 order = {u'QCD':2} ) 
 
GC_51 = Coupling(name = u'GC_51',
	 value = u'1*complex(0,1)*G**2*ZH11*complexconjugate(ZH21) + 1*complex(0,1)*G**2*ZH12*complexconjugate(ZH22)', 
	 order = {u'QCD':2} ) 
 
GC_52 = Coupling(name = u'GC_52',
	 value = u'1*complex(0,1)*G**2*ZH11*complexconjugate(ZH21) + 1*complex(0,1)*G**2*ZH12*complexconjugate(ZH22)', 
	 order = {u'QCD':2} ) 
 
GC_53 = Coupling(name = u'GC_53',
	 value = u'1*complex(0,1)*G**2*ZH21*complexconjugate(ZH11) + 1*complex(0,1)*G**2*ZH22*complexconjugate(ZH12)', 
	 order = {u'QCD':2} ) 
 
GC_54 = Coupling(name = u'GC_54',
	 value = u'1*complex(0,1)*G**2*ZH21*complexconjugate(ZH11) + 1*complex(0,1)*G**2*ZH22*complexconjugate(ZH12)', 
	 order = {u'QCD':2} ) 
 
GC_55 = Coupling(name = u'GC_55',
	 value = u'1*complex(0,1)*G**2*ZH21*complexconjugate(ZH21) + 1*complex(0,1)*G**2*ZH22*complexconjugate(ZH22)', 
	 order = {u'QCD':2} ) 
 
GC_56 = Coupling(name = u'GC_56',
	 value = u'1*complex(0,1)*G**2*ZH21*complexconjugate(ZH21) + 1*complex(0,1)*G**2*ZH22*complexconjugate(ZH22)', 
	 order = {u'QCD':2} ) 
 
GC_57 = Coupling(name = u'GC_57',
	 value = u'-2./3.*complex(0,1)*G*g1*ZH11*complexconjugate(ZH11)*cmath.cos(TW) + 1./3.*complex(0,1)*G*g1*ZH12*complexconjugate(ZH12)*cmath.cos(TW) - 1*complex(0,1)*G*g2*ZH12*complexconjugate(ZH12)*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_58 = Coupling(name = u'GC_58',
	 value = u'-2./3.*complex(0,1)*G*g1*ZH11*complexconjugate(ZH21)*cmath.cos(TW) + 1./3.*complex(0,1)*G*g1*ZH12*complexconjugate(ZH22)*cmath.cos(TW) - 1*complex(0,1)*G*g2*ZH12*complexconjugate(ZH22)*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_59 = Coupling(name = u'GC_59',
	 value = u'-2./3.*complex(0,1)*G*g1*ZH21*complexconjugate(ZH11)*cmath.cos(TW) + 1./3.*complex(0,1)*G*g1*ZH22*complexconjugate(ZH12)*cmath.cos(TW) - 1*complex(0,1)*G*g2*ZH22*complexconjugate(ZH12)*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_60 = Coupling(name = u'GC_60',
	 value = u'-2./3.*complex(0,1)*G*g1*ZH21*complexconjugate(ZH21)*cmath.cos(TW) + 1./3.*complex(0,1)*G*g1*ZH22*complexconjugate(ZH22)*cmath.cos(TW) - 1*complex(0,1)*G*g2*ZH22*complexconjugate(ZH22)*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_61 = Coupling(name = u'GC_61',
	 value = u'-1*complex(0,1)*G*g2*ZH12*complexconjugate(ZH12)*cmath.cos(TW) + 2./3.*complex(0,1)*G*g1*ZH11*complexconjugate(ZH11)*cmath.sin(TW) - 1./3.*complex(0,1)*G*g1*ZH12*complexconjugate(ZH12)*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_62 = Coupling(name = u'GC_62',
	 value = u'-1*complex(0,1)*G*g2*ZH12*complexconjugate(ZH22)*cmath.cos(TW) + 2./3.*complex(0,1)*G*g1*ZH11*complexconjugate(ZH21)*cmath.sin(TW) - 1./3.*complex(0,1)*G*g1*ZH12*complexconjugate(ZH22)*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_63 = Coupling(name = u'GC_63',
	 value = u'-1*complex(0,1)*G*g2*ZH22*complexconjugate(ZH12)*cmath.cos(TW) + 2./3.*complex(0,1)*G*g1*ZH21*complexconjugate(ZH11)*cmath.sin(TW) - 1./3.*complex(0,1)*G*g1*ZH22*complexconjugate(ZH12)*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_64 = Coupling(name = u'GC_64',
	 value = u'-1*complex(0,1)*G*g2*ZH22*complexconjugate(ZH22)*cmath.cos(TW) + 2./3.*complex(0,1)*G*g1*ZH21*complexconjugate(ZH21)*cmath.sin(TW) - 1./3.*complex(0,1)*G*g1*ZH22*complexconjugate(ZH22)*cmath.sin(TW)', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_65 = Coupling(name = u'GC_65',
	 value = u'1*complex(0,1)*cmath.sqrt(2)*G*g2*ZH12', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_66 = Coupling(name = u'GC_66',
	 value = u'1*complex(0,1)*cmath.sqrt(2)*G*g2*ZH22', 
	 order = {u'QED':1, u'QCD':1} ) 
 
GC_67 = Coupling(name = u'GC_67',
	 value = u'2./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH11)*cmath.cos(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH12)*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH12)*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH12)*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_68 = Coupling(name = u'GC_68',
	 value = u'2./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH21)*cmath.cos(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH22)*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH22)*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH22)*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_69 = Coupling(name = u'GC_69',
	 value = u'2./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH11)*cmath.cos(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH12)*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH12)*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH12)*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_70 = Coupling(name = u'GC_70',
	 value = u'2./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH21)*cmath.cos(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH22)*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH22)*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH22)*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_71 = Coupling(name = u'GC_71',
	 value = u'-1./6.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH12)*cmath.cos(2*TW) - 1./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH11)*cmath.sin(2*TW) - 1./36.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH12)*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH12)*cmath.sin(2*TW)', 
	 order = {u'QED':2} ) 
 
GC_72 = Coupling(name = u'GC_72',
	 value = u'-1./6.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH22)*cmath.cos(2*TW) - 1./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH21)*cmath.sin(2*TW) - 1./36.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH22)*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH22)*cmath.sin(2*TW)', 
	 order = {u'QED':2} ) 
 
GC_73 = Coupling(name = u'GC_73',
	 value = u'-1./6.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH12)*cmath.cos(2*TW) - 1./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH11)*cmath.sin(2*TW) - 1./36.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH12)*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH12)*cmath.sin(2*TW)', 
	 order = {u'QED':2} ) 
 
GC_74 = Coupling(name = u'GC_74',
	 value = u'-1./6.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH22)*cmath.cos(2*TW) - 1./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH21)*cmath.sin(2*TW) - 1./36.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH22)*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH22)*cmath.sin(2*TW)', 
	 order = {u'QED':2} ) 
 
GC_75 = Coupling(name = u'GC_75',
	 value = u'(1./3.*complex(0,1)*g1*g2*ZH12*cmath.cos(TW))/cmath.sqrt(2)', 
	 order = {u'QED':2} ) 
 
GC_76 = Coupling(name = u'GC_76',
	 value = u'(1./3.*complex(0,1)*g1*g2*ZH22*cmath.cos(TW))/cmath.sqrt(2)', 
	 order = {u'QED':2} ) 
 
GC_77 = Coupling(name = u'GC_77',
	 value = u'1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH12)', 
	 order = {u'QED':2} ) 
 
GC_78 = Coupling(name = u'GC_78',
	 value = u'1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH22)', 
	 order = {u'QED':2} ) 
 
GC_79 = Coupling(name = u'GC_79',
	 value = u'1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH12)', 
	 order = {u'QED':2} ) 
 
GC_80 = Coupling(name = u'GC_80',
	 value = u'1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH22)', 
	 order = {u'QED':2} ) 
 
GC_81 = Coupling(name = u'GC_81',
	 value = u'1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH12)*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH12)*cmath.cos(TW)*cmath.sin(TW) + 2./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH11)*cmath.sin(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH12)*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_82 = Coupling(name = u'GC_82',
	 value = u'1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH22)*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH22)*cmath.cos(TW)*cmath.sin(TW) + 2./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH21)*cmath.sin(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH22)*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_83 = Coupling(name = u'GC_83',
	 value = u'1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH12)*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH12)*cmath.cos(TW)*cmath.sin(TW) + 2./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH11)*cmath.sin(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH12)*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_84 = Coupling(name = u'GC_84',
	 value = u'1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH22)*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH22)*cmath.cos(TW)*cmath.sin(TW) + 2./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH21)*cmath.sin(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH22)*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_85 = Coupling(name = u'GC_85',
	 value = u'(-1./3.*complex(0,1)*g1*g2*ZH12*cmath.sin(TW))/cmath.sqrt(2)', 
	 order = {u'QED':2} ) 
 
GC_86 = Coupling(name = u'GC_86',
	 value = u'(-1./3.*complex(0,1)*g1*g2*ZH22*cmath.sin(TW))/cmath.sqrt(2)', 
	 order = {u'QED':2} ) 
 
GC_87 = Coupling(name = u'GC_87',
	 value = u'(g2*cmath.cos(TW) + g1*cmath.sin(TW))/2.', 
	 order = {u'QED':1} ) 
 
GC_88 = Coupling(name = u'GC_88',
	 value = u'-1./2.*g2', 
	 order = {u'QED':1} ) 
 
GC_89 = Coupling(name = u'GC_89',
	 value = u'-1./2.*g2', 
	 order = {u'QED':1} ) 
 
GC_90 = Coupling(name = u'GC_90',
	 value = u'-1./2.*complex(0,1)*g2', 
	 order = {u'QED':1} ) 
 
GC_91 = Coupling(name = u'GC_91',
	 value = u'1./2.*complex(0,1)*g2', 
	 order = {u'QED':1} ) 
 
GC_92 = Coupling(name = u'GC_92',
	 value = u'1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_93 = Coupling(name = u'GC_93',
	 value = u'1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_94 = Coupling(name = u'GC_94',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_95 = Coupling(name = u'GC_95',
	 value = u'1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_96 = Coupling(name = u'GC_96',
	 value = u'(1*complex(0,1)*g2*complexconjugate(ZH12))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_97 = Coupling(name = u'GC_97',
	 value = u'(1*complex(0,1)*g2*complexconjugate(ZH22))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_98 = Coupling(name = u'GC_98',
	 value = u'1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_99 = Coupling(name = u'GC_99',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_100 = Coupling(name = u'GC_100',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_101 = Coupling(name = u'GC_101',
	 value = u'-1./6.*complex(0,1)*(2*g1*ZH11*complexconjugate(ZH11)*cmath.cos(TW) + ZH12*complexconjugate(ZH12)*(-(g1*cmath.cos(TW)) + 3*g2*cmath.sin(TW)))', 
	 order = {u'QED':1} ) 
 
GC_102 = Coupling(name = u'GC_102',
	 value = u'-1./6.*complex(0,1)*(2*g1*ZH11*complexconjugate(ZH21)*cmath.cos(TW) + ZH12*complexconjugate(ZH22)*(-(g1*cmath.cos(TW)) + 3*g2*cmath.sin(TW)))', 
	 order = {u'QED':1} ) 
 
GC_103 = Coupling(name = u'GC_103',
	 value = u'-1./6.*complex(0,1)*(2*g1*ZH21*complexconjugate(ZH11)*cmath.cos(TW) + ZH22*complexconjugate(ZH12)*(-(g1*cmath.cos(TW)) + 3*g2*cmath.sin(TW)))', 
	 order = {u'QED':1} ) 
 
GC_104 = Coupling(name = u'GC_104',
	 value = u'-1./6.*complex(0,1)*(2*g1*ZH21*complexconjugate(ZH21)*cmath.cos(TW) + ZH22*complexconjugate(ZH22)*(-(g1*cmath.cos(TW)) + 3*g2*cmath.sin(TW)))', 
	 order = {u'QED':1} ) 
 
GC_105 = Coupling(name = u'GC_105',
	 value = u'1./6.*complex(0,1)*(2*g1*ZH11*complexconjugate(ZH11)*cmath.sin(TW) - ZH12*complexconjugate(ZH12)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW)))', 
	 order = {u'QED':1} ) 
 
GC_106 = Coupling(name = u'GC_106',
	 value = u'1./6.*complex(0,1)*(2*g1*ZH11*complexconjugate(ZH21)*cmath.sin(TW) - ZH12*complexconjugate(ZH22)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW)))', 
	 order = {u'QED':1} ) 
 
GC_107 = Coupling(name = u'GC_107',
	 value = u'1./6.*complex(0,1)*(2*g1*ZH21*complexconjugate(ZH11)*cmath.sin(TW) - ZH22*complexconjugate(ZH12)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW)))', 
	 order = {u'QED':1} ) 
 
GC_108 = Coupling(name = u'GC_108',
	 value = u'1./6.*complex(0,1)*(2*g1*ZH21*complexconjugate(ZH21)*cmath.sin(TW) - ZH22*complexconjugate(ZH22)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW)))', 
	 order = {u'QED':1} ) 
 
GC_109 = Coupling(name = u'GC_109',
	 value = u'(1*complex(0,1)*g2*ZH12)/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_110 = Coupling(name = u'GC_110',
	 value = u'(1*complex(0,1)*g2*ZH22)/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_111 = Coupling(name = u'GC_111',
	 value = u'1./2.*complex(0,1)*g2**2*vvSM', 
	 order = {u'QED':1} ) 
 
GC_112 = Coupling(name = u'GC_112',
	 value = u'1./2.*complex(0,1)*vvSM*(g2*cmath.cos(TW) + g1*cmath.sin(TW))**2', 
	 order = {u'QED':1} ) 
 
GC_113 = Coupling(name = u'GC_113',
	 value = u'1./2.*complex(0,1)*g1*g2*vvSM*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_114 = Coupling(name = u'GC_114',
	 value = u'-1./2.*complex(0,1)*g1*g2*vvSM*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_115 = Coupling(name = u'GC_115',
	 value = u'1./2.*complex(0,1)*g1*g2*vvSM*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_116 = Coupling(name = u'GC_116',
	 value = u'-1./2.*complex(0,1)*g1*g2*vvSM*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_117 = Coupling(name = u'GC_117',
	 value = u'-((complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_118 = Coupling(name = u'GC_118',
	 value = u'(ZDL11*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL12*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL13*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_119 = Coupling(name = u'GC_119',
	 value = u'-((complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_120 = Coupling(name = u'GC_120',
	 value = u'(ZDL11*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL12*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL13*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_121 = Coupling(name = u'GC_121',
	 value = u'-((complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_122 = Coupling(name = u'GC_122',
	 value = u'(ZDL11*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL12*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL13*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_123 = Coupling(name = u'GC_123',
	 value = u'-((complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_124 = Coupling(name = u'GC_124',
	 value = u'(ZDL21*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL22*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL23*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_125 = Coupling(name = u'GC_125',
	 value = u'-((complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_126 = Coupling(name = u'GC_126',
	 value = u'(ZDL21*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL22*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL23*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_127 = Coupling(name = u'GC_127',
	 value = u'-((complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_128 = Coupling(name = u'GC_128',
	 value = u'(ZDL21*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL22*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL23*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_129 = Coupling(name = u'GC_129',
	 value = u'-((complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_130 = Coupling(name = u'GC_130',
	 value = u'(ZDL31*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL32*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL33*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_131 = Coupling(name = u'GC_131',
	 value = u'-((complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_132 = Coupling(name = u'GC_132',
	 value = u'(ZDL31*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL32*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL33*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_133 = Coupling(name = u'GC_133',
	 value = u'-((complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_134 = Coupling(name = u'GC_134',
	 value = u'(ZDL31*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL32*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL33*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_135 = Coupling(name = u'GC_135',
	 value = u'-((complexconjugate(ZEL11)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_136 = Coupling(name = u'GC_136',
	 value = u'(ZEL11*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL12*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL13*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_137 = Coupling(name = u'GC_137',
	 value = u'-((complexconjugate(ZEL21)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_138 = Coupling(name = u'GC_138',
	 value = u'(ZEL11*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL12*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL13*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_139 = Coupling(name = u'GC_139',
	 value = u'-((complexconjugate(ZEL31)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_140 = Coupling(name = u'GC_140',
	 value = u'(ZEL11*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL12*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL13*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_141 = Coupling(name = u'GC_141',
	 value = u'-((complexconjugate(ZEL11)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_142 = Coupling(name = u'GC_142',
	 value = u'(ZEL21*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL22*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL23*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_143 = Coupling(name = u'GC_143',
	 value = u'-((complexconjugate(ZEL21)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_144 = Coupling(name = u'GC_144',
	 value = u'(ZEL21*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL22*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL23*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_145 = Coupling(name = u'GC_145',
	 value = u'-((complexconjugate(ZEL31)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_146 = Coupling(name = u'GC_146',
	 value = u'(ZEL21*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL22*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL23*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_147 = Coupling(name = u'GC_147',
	 value = u'-((complexconjugate(ZEL11)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_148 = Coupling(name = u'GC_148',
	 value = u'(ZEL31*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL32*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL33*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_149 = Coupling(name = u'GC_149',
	 value = u'-((complexconjugate(ZEL21)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_150 = Coupling(name = u'GC_150',
	 value = u'(ZEL31*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL32*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL33*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_151 = Coupling(name = u'GC_151',
	 value = u'-((complexconjugate(ZEL31)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_152 = Coupling(name = u'GC_152',
	 value = u'(ZEL31*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL32*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL33*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_153 = Coupling(name = u'GC_153',
	 value = u'(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_154 = Coupling(name = u'GC_154',
	 value = u'-((ZUL11*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL12*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL13*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_155 = Coupling(name = u'GC_155',
	 value = u'(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_156 = Coupling(name = u'GC_156',
	 value = u'-((ZUL11*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL12*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL13*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_157 = Coupling(name = u'GC_157',
	 value = u'(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_158 = Coupling(name = u'GC_158',
	 value = u'-((ZUL11*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL12*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL13*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_159 = Coupling(name = u'GC_159',
	 value = u'(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_160 = Coupling(name = u'GC_160',
	 value = u'-((ZUL21*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL22*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL23*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_161 = Coupling(name = u'GC_161',
	 value = u'(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_162 = Coupling(name = u'GC_162',
	 value = u'-((ZUL21*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL22*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL23*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_163 = Coupling(name = u'GC_163',
	 value = u'(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_164 = Coupling(name = u'GC_164',
	 value = u'-((ZUL21*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL22*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL23*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_165 = Coupling(name = u'GC_165',
	 value = u'(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_166 = Coupling(name = u'GC_166',
	 value = u'-((ZUL31*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL32*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL33*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_167 = Coupling(name = u'GC_167',
	 value = u'(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_168 = Coupling(name = u'GC_168',
	 value = u'-((ZUL31*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL32*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL33*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_169 = Coupling(name = u'GC_169',
	 value = u'(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_170 = Coupling(name = u'GC_170',
	 value = u'-((ZUL31*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL32*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL33*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {u'QED':1} ) 
 
GC_171 = Coupling(name = u'GC_171',
	 value = u'(2*complexconjugate(ZM11)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + 2*complexconjugate(ZM12)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + 2*complexconjugate(ZM13)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13)))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_172 = Coupling(name = u'GC_172',
	 value = u'-((2*ZM11*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + 2*ZM12*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + 2*ZM13*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)))/vvSM)', 
	 order = {u'QED':1} ) 
 
GC_173 = Coupling(name = u'GC_173',
	 value = u'((CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13))*complexconjugate(ZM21) + (CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13))*complexconjugate(ZM22) + (CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))*complexconjugate(ZM23) + complexconjugate(ZM11)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZM12)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZM13)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23)))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_174 = Coupling(name = u'GC_174',
	 value = u'-((ZM21*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM11*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM12*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)) + ZM13*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133)))/vvSM)', 
	 order = {u'QED':1} ) 
 
GC_175 = Coupling(name = u'GC_175',
	 value = u'((CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13))*complexconjugate(ZM31) + (CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13))*complexconjugate(ZM32) + (CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))*complexconjugate(ZM33) + complexconjugate(ZM11)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZM12)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZM13)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33)))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_176 = Coupling(name = u'GC_176',
	 value = u'-((ZM31*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM11*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM12*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)) + ZM13*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133)))/vvSM)', 
	 order = {u'QED':1} ) 
 
GC_177 = Coupling(name = u'GC_177',
	 value = u'(2*complexconjugate(ZM21)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + 2*complexconjugate(ZM22)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + 2*complexconjugate(ZM23)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23)))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_178 = Coupling(name = u'GC_178',
	 value = u'-((2*ZM21*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + 2*ZM22*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + 2*ZM23*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133)))/vvSM)', 
	 order = {u'QED':1} ) 
 
GC_179 = Coupling(name = u'GC_179',
	 value = u'((CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23))*complexconjugate(ZM31) + (CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23))*complexconjugate(ZM32) + (CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))*complexconjugate(ZM33) + complexconjugate(ZM21)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZM22)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZM23)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33)))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_180 = Coupling(name = u'GC_180',
	 value = u'-((ZM31*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM21*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM22*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133)) + ZM23*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133)))/vvSM)', 
	 order = {u'QED':1} ) 
 
GC_181 = Coupling(name = u'GC_181',
	 value = u'(2*complexconjugate(ZM31)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + 2*complexconjugate(ZM32)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + 2*complexconjugate(ZM33)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33)))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_182 = Coupling(name = u'GC_182',
	 value = u'-((2*ZM31*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + 2*ZM32*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + 2*ZM33*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133)))/vvSM)', 
	 order = {u'QED':1} ) 
 
GC_183 = Coupling(name = u'GC_183',
	 value = u'-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_184 = Coupling(name = u'GC_184',
	 value = u'1*complex(0,1)*(ZDR11*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR12*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR13*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {u'QED':1} ) 
 
GC_185 = Coupling(name = u'GC_185',
	 value = u'-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_186 = Coupling(name = u'GC_186',
	 value = u'1*complex(0,1)*(ZDR11*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR12*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR13*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {u'QED':1} ) 
 
GC_187 = Coupling(name = u'GC_187',
	 value = u'-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_188 = Coupling(name = u'GC_188',
	 value = u'1*complex(0,1)*(ZDR21*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR22*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR23*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {u'QED':1} ) 
 
GC_189 = Coupling(name = u'GC_189',
	 value = u'-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_190 = Coupling(name = u'GC_190',
	 value = u'1*complex(0,1)*(ZDR21*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR22*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR23*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {u'QED':1} ) 
 
GC_191 = Coupling(name = u'GC_191',
	 value = u'-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_192 = Coupling(name = u'GC_192',
	 value = u'1*complex(0,1)*(ZDR31*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR32*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR33*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {u'QED':1} ) 
 
GC_193 = Coupling(name = u'GC_193',
	 value = u'-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_194 = Coupling(name = u'GC_194',
	 value = u'1*complex(0,1)*(ZDR31*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR32*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR33*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {u'QED':1} ) 
 
GC_195 = Coupling(name = u'GC_195',
	 value = u'-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_196 = Coupling(name = u'GC_196',
	 value = u'1*complex(0,1)*(ZDR11*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR12*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR13*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {u'QED':1} ) 
 
GC_197 = Coupling(name = u'GC_197',
	 value = u'-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_198 = Coupling(name = u'GC_198',
	 value = u'1*complex(0,1)*(ZDR11*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR12*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR13*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {u'QED':1} ) 
 
GC_199 = Coupling(name = u'GC_199',
	 value = u'-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_200 = Coupling(name = u'GC_200',
	 value = u'1*complex(0,1)*(ZDR21*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR22*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR23*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {u'QED':1} ) 
 
GC_201 = Coupling(name = u'GC_201',
	 value = u'-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_202 = Coupling(name = u'GC_202',
	 value = u'1*complex(0,1)*(ZDR21*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR22*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR23*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {u'QED':1} ) 
 
GC_203 = Coupling(name = u'GC_203',
	 value = u'-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_204 = Coupling(name = u'GC_204',
	 value = u'1*complex(0,1)*(ZDR31*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR32*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR33*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {u'QED':1} ) 
 
GC_205 = Coupling(name = u'GC_205',
	 value = u'-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_206 = Coupling(name = u'GC_206',
	 value = u'1*complex(0,1)*(ZDR31*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR32*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR33*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {u'QED':1} ) 
 
GC_207 = Coupling(name = u'GC_207',
	 value = u'-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_208 = Coupling(name = u'GC_208',
	 value = u'1*complex(0,1)*(ZDR11*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR12*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR13*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {u'QED':1} ) 
 
GC_209 = Coupling(name = u'GC_209',
	 value = u'-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_210 = Coupling(name = u'GC_210',
	 value = u'1*complex(0,1)*(ZDR11*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR12*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR13*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {u'QED':1} ) 
 
GC_211 = Coupling(name = u'GC_211',
	 value = u'-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_212 = Coupling(name = u'GC_212',
	 value = u'1*complex(0,1)*(ZDR21*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR22*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR23*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {u'QED':1} ) 
 
GC_213 = Coupling(name = u'GC_213',
	 value = u'-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_214 = Coupling(name = u'GC_214',
	 value = u'1*complex(0,1)*(ZDR21*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR22*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR23*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {u'QED':1} ) 
 
GC_215 = Coupling(name = u'GC_215',
	 value = u'-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_216 = Coupling(name = u'GC_216',
	 value = u'1*complex(0,1)*(ZDR31*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR32*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR33*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {u'QED':1} ) 
 
GC_217 = Coupling(name = u'GC_217',
	 value = u'-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_218 = Coupling(name = u'GC_218',
	 value = u'1*complex(0,1)*(ZDR31*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR32*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR33*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {u'QED':1} ) 
 
GC_219 = Coupling(name = u'GC_219',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_220 = Coupling(name = u'GC_220',
	 value = u'(-1*complex(0,1)*(ZDL11*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL12*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL13*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_221 = Coupling(name = u'GC_221',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_222 = Coupling(name = u'GC_222',
	 value = u'(-1*complex(0,1)*(ZDL11*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL12*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL13*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_223 = Coupling(name = u'GC_223',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_224 = Coupling(name = u'GC_224',
	 value = u'(-1*complex(0,1)*(ZDL11*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL12*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL13*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_225 = Coupling(name = u'GC_225',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_226 = Coupling(name = u'GC_226',
	 value = u'(-1*complex(0,1)*(ZDL21*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL22*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL23*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_227 = Coupling(name = u'GC_227',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_228 = Coupling(name = u'GC_228',
	 value = u'(-1*complex(0,1)*(ZDL21*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL22*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL23*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_229 = Coupling(name = u'GC_229',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_230 = Coupling(name = u'GC_230',
	 value = u'(-1*complex(0,1)*(ZDL21*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL22*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL23*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_231 = Coupling(name = u'GC_231',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_232 = Coupling(name = u'GC_232',
	 value = u'(-1*complex(0,1)*(ZDL31*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL32*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL33*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_233 = Coupling(name = u'GC_233',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_234 = Coupling(name = u'GC_234',
	 value = u'(-1*complex(0,1)*(ZDL31*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL32*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL33*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_235 = Coupling(name = u'GC_235',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_236 = Coupling(name = u'GC_236',
	 value = u'(-1*complex(0,1)*(ZDL31*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL32*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL33*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_237 = Coupling(name = u'GC_237',
	 value = u'1*complex(0,1)*(complexconjugate(ZDL11)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZDL12)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZDL13)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))', 
	 order = {u'QED':1} ) 
 
GC_238 = Coupling(name = u'GC_238',
	 value = u'-1*complex(0,1)*(ZUL11*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZUL12*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZUL13*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))', 
	 order = {u'QED':1} ) 
 
GC_239 = Coupling(name = u'GC_239',
	 value = u'1*complex(0,1)*(complexconjugate(ZDL21)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZDL22)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZDL23)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))', 
	 order = {u'QED':1} ) 
 
GC_240 = Coupling(name = u'GC_240',
	 value = u'-1*complex(0,1)*(ZUL11*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZUL12*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZUL13*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))', 
	 order = {u'QED':1} ) 
 
GC_241 = Coupling(name = u'GC_241',
	 value = u'1*complex(0,1)*(complexconjugate(ZDL31)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZDL32)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZDL33)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))', 
	 order = {u'QED':1} ) 
 
GC_242 = Coupling(name = u'GC_242',
	 value = u'-1*complex(0,1)*(ZUL11*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZUL12*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZUL13*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))', 
	 order = {u'QED':1} ) 
 
GC_243 = Coupling(name = u'GC_243',
	 value = u'1*complex(0,1)*(complexconjugate(ZDL11)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZDL12)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZDL13)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))', 
	 order = {u'QED':1} ) 
 
GC_244 = Coupling(name = u'GC_244',
	 value = u'-1*complex(0,1)*(ZUL21*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZUL22*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZUL23*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))', 
	 order = {u'QED':1} ) 
 
GC_245 = Coupling(name = u'GC_245',
	 value = u'1*complex(0,1)*(complexconjugate(ZDL21)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZDL22)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZDL23)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))', 
	 order = {u'QED':1} ) 
 
GC_246 = Coupling(name = u'GC_246',
	 value = u'-1*complex(0,1)*(ZUL21*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZUL22*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZUL23*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))', 
	 order = {u'QED':1} ) 
 
GC_247 = Coupling(name = u'GC_247',
	 value = u'1*complex(0,1)*(complexconjugate(ZDL31)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZDL32)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZDL33)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))', 
	 order = {u'QED':1} ) 
 
GC_248 = Coupling(name = u'GC_248',
	 value = u'-1*complex(0,1)*(ZUL21*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZUL22*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZUL23*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))', 
	 order = {u'QED':1} ) 
 
GC_249 = Coupling(name = u'GC_249',
	 value = u'1*complex(0,1)*(complexconjugate(ZDL11)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZDL12)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZDL13)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))', 
	 order = {u'QED':1} ) 
 
GC_250 = Coupling(name = u'GC_250',
	 value = u'-1*complex(0,1)*(ZUL31*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZUL32*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZUL33*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))', 
	 order = {u'QED':1} ) 
 
GC_251 = Coupling(name = u'GC_251',
	 value = u'1*complex(0,1)*(complexconjugate(ZDL21)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZDL22)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZDL23)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))', 
	 order = {u'QED':1} ) 
 
GC_252 = Coupling(name = u'GC_252',
	 value = u'-1*complex(0,1)*(ZUL31*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZUL32*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZUL33*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))', 
	 order = {u'QED':1} ) 
 
GC_253 = Coupling(name = u'GC_253',
	 value = u'1*complex(0,1)*(complexconjugate(ZDL31)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZDL32)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZDL33)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))', 
	 order = {u'QED':1} ) 
 
GC_254 = Coupling(name = u'GC_254',
	 value = u'-1*complex(0,1)*(ZUL31*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZUL32*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZUL33*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))', 
	 order = {u'QED':1} ) 
 
GC_255 = Coupling(name = u'GC_255',
	 value = u'-1*complex(0,1)*(ZDR11*(ZEL11*complexconjugate(Omega11) + ZEL12*complexconjugate(Omega21) + ZEL13*complexconjugate(Omega31)) + ZDR12*(ZEL11*complexconjugate(Omega12) + ZEL12*complexconjugate(Omega22) + ZEL13*complexconjugate(Omega32)) + ZDR13*(ZEL11*complexconjugate(Omega13) + ZEL12*complexconjugate(Omega23) + ZEL13*complexconjugate(Omega33)))', 
	 order = {u'QED':1} ) 
 
GC_256 = Coupling(name = u'GC_256',
	 value = u'-1*complex(0,1)*(ZDR21*(ZEL11*complexconjugate(Omega11) + ZEL12*complexconjugate(Omega21) + ZEL13*complexconjugate(Omega31)) + ZDR22*(ZEL11*complexconjugate(Omega12) + ZEL12*complexconjugate(Omega22) + ZEL13*complexconjugate(Omega32)) + ZDR23*(ZEL11*complexconjugate(Omega13) + ZEL12*complexconjugate(Omega23) + ZEL13*complexconjugate(Omega33)))', 
	 order = {u'QED':1} ) 
 
GC_257 = Coupling(name = u'GC_257',
	 value = u'-1*complex(0,1)*(ZDR31*(ZEL11*complexconjugate(Omega11) + ZEL12*complexconjugate(Omega21) + ZEL13*complexconjugate(Omega31)) + ZDR32*(ZEL11*complexconjugate(Omega12) + ZEL12*complexconjugate(Omega22) + ZEL13*complexconjugate(Omega32)) + ZDR33*(ZEL11*complexconjugate(Omega13) + ZEL12*complexconjugate(Omega23) + ZEL13*complexconjugate(Omega33)))', 
	 order = {u'QED':1} ) 
 
GC_258 = Coupling(name = u'GC_258',
	 value = u'-1*complex(0,1)*(ZDR11*(ZEL21*complexconjugate(Omega11) + ZEL22*complexconjugate(Omega21) + ZEL23*complexconjugate(Omega31)) + ZDR12*(ZEL21*complexconjugate(Omega12) + ZEL22*complexconjugate(Omega22) + ZEL23*complexconjugate(Omega32)) + ZDR13*(ZEL21*complexconjugate(Omega13) + ZEL22*complexconjugate(Omega23) + ZEL23*complexconjugate(Omega33)))', 
	 order = {u'QED':1} ) 
 
GC_259 = Coupling(name = u'GC_259',
	 value = u'-1*complex(0,1)*(ZDR21*(ZEL21*complexconjugate(Omega11) + ZEL22*complexconjugate(Omega21) + ZEL23*complexconjugate(Omega31)) + ZDR22*(ZEL21*complexconjugate(Omega12) + ZEL22*complexconjugate(Omega22) + ZEL23*complexconjugate(Omega32)) + ZDR23*(ZEL21*complexconjugate(Omega13) + ZEL22*complexconjugate(Omega23) + ZEL23*complexconjugate(Omega33)))', 
	 order = {u'QED':1} ) 
 
GC_260 = Coupling(name = u'GC_260',
	 value = u'-1*complex(0,1)*(ZDR31*(ZEL21*complexconjugate(Omega11) + ZEL22*complexconjugate(Omega21) + ZEL23*complexconjugate(Omega31)) + ZDR32*(ZEL21*complexconjugate(Omega12) + ZEL22*complexconjugate(Omega22) + ZEL23*complexconjugate(Omega32)) + ZDR33*(ZEL21*complexconjugate(Omega13) + ZEL22*complexconjugate(Omega23) + ZEL23*complexconjugate(Omega33)))', 
	 order = {u'QED':1} ) 
 
GC_261 = Coupling(name = u'GC_261',
	 value = u'-1*complex(0,1)*(ZDR11*(ZEL31*complexconjugate(Omega11) + ZEL32*complexconjugate(Omega21) + ZEL33*complexconjugate(Omega31)) + ZDR12*(ZEL31*complexconjugate(Omega12) + ZEL32*complexconjugate(Omega22) + ZEL33*complexconjugate(Omega32)) + ZDR13*(ZEL31*complexconjugate(Omega13) + ZEL32*complexconjugate(Omega23) + ZEL33*complexconjugate(Omega33)))', 
	 order = {u'QED':1} ) 
 
GC_262 = Coupling(name = u'GC_262',
	 value = u'-1*complex(0,1)*(ZDR21*(ZEL31*complexconjugate(Omega11) + ZEL32*complexconjugate(Omega21) + ZEL33*complexconjugate(Omega31)) + ZDR22*(ZEL31*complexconjugate(Omega12) + ZEL32*complexconjugate(Omega22) + ZEL33*complexconjugate(Omega32)) + ZDR23*(ZEL31*complexconjugate(Omega13) + ZEL32*complexconjugate(Omega23) + ZEL33*complexconjugate(Omega33)))', 
	 order = {u'QED':1} ) 
 
GC_263 = Coupling(name = u'GC_263',
	 value = u'-1*complex(0,1)*(ZDR31*(ZEL31*complexconjugate(Omega11) + ZEL32*complexconjugate(Omega21) + ZEL33*complexconjugate(Omega31)) + ZDR32*(ZEL31*complexconjugate(Omega12) + ZEL32*complexconjugate(Omega22) + ZEL33*complexconjugate(Omega32)) + ZDR33*(ZEL31*complexconjugate(Omega13) + ZEL32*complexconjugate(Omega23) + ZEL33*complexconjugate(Omega33)))', 
	 order = {u'QED':1} ) 
 
GC_264 = Coupling(name = u'GC_264',
	 value = u'1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL13))', 
	 order = {u'QED':1} ) 
 
GC_265 = Coupling(name = u'GC_265',
	 value = u'-1*complex(0,1)*(ZER11*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon12) + ZUR13*complexconjugate(Upsilon13)) + ZER12*(ZUR11*complexconjugate(Upsilon21) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon23)) + ZER13*(ZUR11*complexconjugate(Upsilon31) + ZUR12*complexconjugate(Upsilon32) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {u'QED':1} ) 
 
GC_266 = Coupling(name = u'GC_266',
	 value = u'1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL13))', 
	 order = {u'QED':1} ) 
 
GC_267 = Coupling(name = u'GC_267',
	 value = u'-1*complex(0,1)*(ZER11*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon12) + ZUR13*complexconjugate(Upsilon13)) + ZER12*(ZUR11*complexconjugate(Upsilon21) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon23)) + ZER13*(ZUR11*complexconjugate(Upsilon31) + ZUR12*complexconjugate(Upsilon32) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {u'QED':1} ) 
 
GC_268 = Coupling(name = u'GC_268',
	 value = u'1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL23))', 
	 order = {u'QED':1} ) 
 
GC_269 = Coupling(name = u'GC_269',
	 value = u'-1*complex(0,1)*(ZER11*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon12) + ZUR23*complexconjugate(Upsilon13)) + ZER12*(ZUR21*complexconjugate(Upsilon21) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon23)) + ZER13*(ZUR21*complexconjugate(Upsilon31) + ZUR22*complexconjugate(Upsilon32) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {u'QED':1} ) 
 
GC_270 = Coupling(name = u'GC_270',
	 value = u'1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL23))', 
	 order = {u'QED':1} ) 
 
GC_271 = Coupling(name = u'GC_271',
	 value = u'-1*complex(0,1)*(ZER11*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon12) + ZUR23*complexconjugate(Upsilon13)) + ZER12*(ZUR21*complexconjugate(Upsilon21) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon23)) + ZER13*(ZUR21*complexconjugate(Upsilon31) + ZUR22*complexconjugate(Upsilon32) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {u'QED':1} ) 
 
GC_272 = Coupling(name = u'GC_272',
	 value = u'1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL33))', 
	 order = {u'QED':1} ) 
 
GC_273 = Coupling(name = u'GC_273',
	 value = u'-1*complex(0,1)*(ZER11*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon12) + ZUR33*complexconjugate(Upsilon13)) + ZER12*(ZUR31*complexconjugate(Upsilon21) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon23)) + ZER13*(ZUR31*complexconjugate(Upsilon31) + ZUR32*complexconjugate(Upsilon32) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {u'QED':1} ) 
 
GC_274 = Coupling(name = u'GC_274',
	 value = u'1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL33))', 
	 order = {u'QED':1} ) 
 
GC_275 = Coupling(name = u'GC_275',
	 value = u'-1*complex(0,1)*(ZER11*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon12) + ZUR33*complexconjugate(Upsilon13)) + ZER12*(ZUR31*complexconjugate(Upsilon21) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon23)) + ZER13*(ZUR31*complexconjugate(Upsilon31) + ZUR32*complexconjugate(Upsilon32) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {u'QED':1} ) 
 
GC_276 = Coupling(name = u'GC_276',
	 value = u'1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL13))', 
	 order = {u'QED':1} ) 
 
GC_277 = Coupling(name = u'GC_277',
	 value = u'-1*complex(0,1)*(ZER21*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon12) + ZUR13*complexconjugate(Upsilon13)) + ZER22*(ZUR11*complexconjugate(Upsilon21) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon23)) + ZER23*(ZUR11*complexconjugate(Upsilon31) + ZUR12*complexconjugate(Upsilon32) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {u'QED':1} ) 
 
GC_278 = Coupling(name = u'GC_278',
	 value = u'1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL13))', 
	 order = {u'QED':1} ) 
 
GC_279 = Coupling(name = u'GC_279',
	 value = u'-1*complex(0,1)*(ZER21*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon12) + ZUR13*complexconjugate(Upsilon13)) + ZER22*(ZUR11*complexconjugate(Upsilon21) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon23)) + ZER23*(ZUR11*complexconjugate(Upsilon31) + ZUR12*complexconjugate(Upsilon32) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {u'QED':1} ) 
 
GC_280 = Coupling(name = u'GC_280',
	 value = u'1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL23))', 
	 order = {u'QED':1} ) 
 
GC_281 = Coupling(name = u'GC_281',
	 value = u'-1*complex(0,1)*(ZER21*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon12) + ZUR23*complexconjugate(Upsilon13)) + ZER22*(ZUR21*complexconjugate(Upsilon21) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon23)) + ZER23*(ZUR21*complexconjugate(Upsilon31) + ZUR22*complexconjugate(Upsilon32) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {u'QED':1} ) 
 
GC_282 = Coupling(name = u'GC_282',
	 value = u'1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL23))', 
	 order = {u'QED':1} ) 
 
GC_283 = Coupling(name = u'GC_283',
	 value = u'-1*complex(0,1)*(ZER21*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon12) + ZUR23*complexconjugate(Upsilon13)) + ZER22*(ZUR21*complexconjugate(Upsilon21) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon23)) + ZER23*(ZUR21*complexconjugate(Upsilon31) + ZUR22*complexconjugate(Upsilon32) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {u'QED':1} ) 
 
GC_284 = Coupling(name = u'GC_284',
	 value = u'1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL33))', 
	 order = {u'QED':1} ) 
 
GC_285 = Coupling(name = u'GC_285',
	 value = u'-1*complex(0,1)*(ZER21*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon12) + ZUR33*complexconjugate(Upsilon13)) + ZER22*(ZUR31*complexconjugate(Upsilon21) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon23)) + ZER23*(ZUR31*complexconjugate(Upsilon31) + ZUR32*complexconjugate(Upsilon32) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {u'QED':1} ) 
 
GC_286 = Coupling(name = u'GC_286',
	 value = u'1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL33))', 
	 order = {u'QED':1} ) 
 
GC_287 = Coupling(name = u'GC_287',
	 value = u'-1*complex(0,1)*(ZER21*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon12) + ZUR33*complexconjugate(Upsilon13)) + ZER22*(ZUR31*complexconjugate(Upsilon21) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon23)) + ZER23*(ZUR31*complexconjugate(Upsilon31) + ZUR32*complexconjugate(Upsilon32) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {u'QED':1} ) 
 
GC_288 = Coupling(name = u'GC_288',
	 value = u'1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL13))', 
	 order = {u'QED':1} ) 
 
GC_289 = Coupling(name = u'GC_289',
	 value = u'-1*complex(0,1)*(ZER31*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon12) + ZUR13*complexconjugate(Upsilon13)) + ZER32*(ZUR11*complexconjugate(Upsilon21) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon23)) + ZER33*(ZUR11*complexconjugate(Upsilon31) + ZUR12*complexconjugate(Upsilon32) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {u'QED':1} ) 
 
GC_290 = Coupling(name = u'GC_290',
	 value = u'1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL13))', 
	 order = {u'QED':1} ) 
 
GC_291 = Coupling(name = u'GC_291',
	 value = u'-1*complex(0,1)*(ZER31*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon12) + ZUR13*complexconjugate(Upsilon13)) + ZER32*(ZUR11*complexconjugate(Upsilon21) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon23)) + ZER33*(ZUR11*complexconjugate(Upsilon31) + ZUR12*complexconjugate(Upsilon32) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {u'QED':1} ) 
 
GC_292 = Coupling(name = u'GC_292',
	 value = u'1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL23))', 
	 order = {u'QED':1} ) 
 
GC_293 = Coupling(name = u'GC_293',
	 value = u'-1*complex(0,1)*(ZER31*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon12) + ZUR23*complexconjugate(Upsilon13)) + ZER32*(ZUR21*complexconjugate(Upsilon21) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon23)) + ZER33*(ZUR21*complexconjugate(Upsilon31) + ZUR22*complexconjugate(Upsilon32) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {u'QED':1} ) 
 
GC_294 = Coupling(name = u'GC_294',
	 value = u'1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL23))', 
	 order = {u'QED':1} ) 
 
GC_295 = Coupling(name = u'GC_295',
	 value = u'-1*complex(0,1)*(ZER31*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon12) + ZUR23*complexconjugate(Upsilon13)) + ZER32*(ZUR21*complexconjugate(Upsilon21) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon23)) + ZER33*(ZUR21*complexconjugate(Upsilon31) + ZUR22*complexconjugate(Upsilon32) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {u'QED':1} ) 
 
GC_296 = Coupling(name = u'GC_296',
	 value = u'1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL33))', 
	 order = {u'QED':1} ) 
 
GC_297 = Coupling(name = u'GC_297',
	 value = u'-1*complex(0,1)*(ZER31*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon12) + ZUR33*complexconjugate(Upsilon13)) + ZER32*(ZUR31*complexconjugate(Upsilon21) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon23)) + ZER33*(ZUR31*complexconjugate(Upsilon31) + ZUR32*complexconjugate(Upsilon32) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {u'QED':1} ) 
 
GC_298 = Coupling(name = u'GC_298',
	 value = u'1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL33))', 
	 order = {u'QED':1} ) 
 
GC_299 = Coupling(name = u'GC_299',
	 value = u'-1*complex(0,1)*(ZER31*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon12) + ZUR33*complexconjugate(Upsilon13)) + ZER32*(ZUR31*complexconjugate(Upsilon21) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon23)) + ZER33*(ZUR31*complexconjugate(Upsilon31) + ZUR32*complexconjugate(Upsilon32) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {u'QED':1} ) 
 
GC_300 = Coupling(name = u'GC_300',
	 value = u'(1*complex(0,1)*((CW111*complexconjugate(ZEL11) + CW121*complexconjugate(ZEL12) + CW131*complexconjugate(ZEL13))*complexconjugate(ZM11) + (CW112*complexconjugate(ZEL11) + CW122*complexconjugate(ZEL12) + CW132*complexconjugate(ZEL13))*complexconjugate(ZM12) + (CW113*complexconjugate(ZEL11) + CW123*complexconjugate(ZEL12) + CW133*complexconjugate(ZEL13))*complexconjugate(ZM13) + complexconjugate(ZEL11)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + complexconjugate(ZEL12)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + complexconjugate(ZEL13)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_301 = Coupling(name = u'GC_301',
	 value = u'-1*complex(0,1)*(ZM11*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZM12*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZM13*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))', 
	 order = {u'QED':1} ) 
 
GC_302 = Coupling(name = u'GC_302',
	 value = u'(1*complex(0,1)*((CW111*complexconjugate(ZEL21) + CW121*complexconjugate(ZEL22) + CW131*complexconjugate(ZEL23))*complexconjugate(ZM11) + (CW112*complexconjugate(ZEL21) + CW122*complexconjugate(ZEL22) + CW132*complexconjugate(ZEL23))*complexconjugate(ZM12) + (CW113*complexconjugate(ZEL21) + CW123*complexconjugate(ZEL22) + CW133*complexconjugate(ZEL23))*complexconjugate(ZM13) + complexconjugate(ZEL21)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + complexconjugate(ZEL22)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + complexconjugate(ZEL23)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_303 = Coupling(name = u'GC_303',
	 value = u'-1*complex(0,1)*(ZM11*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZM12*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZM13*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))', 
	 order = {u'QED':1} ) 
 
GC_304 = Coupling(name = u'GC_304',
	 value = u'(1*complex(0,1)*((CW111*complexconjugate(ZEL31) + CW121*complexconjugate(ZEL32) + CW131*complexconjugate(ZEL33))*complexconjugate(ZM11) + (CW112*complexconjugate(ZEL31) + CW122*complexconjugate(ZEL32) + CW132*complexconjugate(ZEL33))*complexconjugate(ZM12) + (CW113*complexconjugate(ZEL31) + CW123*complexconjugate(ZEL32) + CW133*complexconjugate(ZEL33))*complexconjugate(ZM13) + complexconjugate(ZEL31)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + complexconjugate(ZEL32)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + complexconjugate(ZEL33)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_305 = Coupling(name = u'GC_305',
	 value = u'-1*complex(0,1)*(ZM11*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZM12*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZM13*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))', 
	 order = {u'QED':1} ) 
 
GC_306 = Coupling(name = u'GC_306',
	 value = u'(1*complex(0,1)*((CW111*complexconjugate(ZEL11) + CW121*complexconjugate(ZEL12) + CW131*complexconjugate(ZEL13))*complexconjugate(ZM21) + (CW112*complexconjugate(ZEL11) + CW122*complexconjugate(ZEL12) + CW132*complexconjugate(ZEL13))*complexconjugate(ZM22) + (CW113*complexconjugate(ZEL11) + CW123*complexconjugate(ZEL12) + CW133*complexconjugate(ZEL13))*complexconjugate(ZM23) + complexconjugate(ZEL11)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZEL12)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZEL13)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_307 = Coupling(name = u'GC_307',
	 value = u'-1*complex(0,1)*(ZM21*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZM22*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZM23*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))', 
	 order = {u'QED':1} ) 
 
GC_308 = Coupling(name = u'GC_308',
	 value = u'(1*complex(0,1)*((CW111*complexconjugate(ZEL21) + CW121*complexconjugate(ZEL22) + CW131*complexconjugate(ZEL23))*complexconjugate(ZM21) + (CW112*complexconjugate(ZEL21) + CW122*complexconjugate(ZEL22) + CW132*complexconjugate(ZEL23))*complexconjugate(ZM22) + (CW113*complexconjugate(ZEL21) + CW123*complexconjugate(ZEL22) + CW133*complexconjugate(ZEL23))*complexconjugate(ZM23) + complexconjugate(ZEL21)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZEL22)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZEL23)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_309 = Coupling(name = u'GC_309',
	 value = u'-1*complex(0,1)*(ZM21*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZM22*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZM23*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))', 
	 order = {u'QED':1} ) 
 
GC_310 = Coupling(name = u'GC_310',
	 value = u'(1*complex(0,1)*((CW111*complexconjugate(ZEL31) + CW121*complexconjugate(ZEL32) + CW131*complexconjugate(ZEL33))*complexconjugate(ZM21) + (CW112*complexconjugate(ZEL31) + CW122*complexconjugate(ZEL32) + CW132*complexconjugate(ZEL33))*complexconjugate(ZM22) + (CW113*complexconjugate(ZEL31) + CW123*complexconjugate(ZEL32) + CW133*complexconjugate(ZEL33))*complexconjugate(ZM23) + complexconjugate(ZEL31)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZEL32)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZEL33)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_311 = Coupling(name = u'GC_311',
	 value = u'-1*complex(0,1)*(ZM21*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZM22*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZM23*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))', 
	 order = {u'QED':1} ) 
 
GC_312 = Coupling(name = u'GC_312',
	 value = u'(1*complex(0,1)*((CW111*complexconjugate(ZEL11) + CW121*complexconjugate(ZEL12) + CW131*complexconjugate(ZEL13))*complexconjugate(ZM31) + (CW112*complexconjugate(ZEL11) + CW122*complexconjugate(ZEL12) + CW132*complexconjugate(ZEL13))*complexconjugate(ZM32) + (CW113*complexconjugate(ZEL11) + CW123*complexconjugate(ZEL12) + CW133*complexconjugate(ZEL13))*complexconjugate(ZM33) + complexconjugate(ZEL11)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZEL12)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZEL13)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_313 = Coupling(name = u'GC_313',
	 value = u'-1*complex(0,1)*(ZM31*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZM32*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZM33*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))', 
	 order = {u'QED':1} ) 
 
GC_314 = Coupling(name = u'GC_314',
	 value = u'(1*complex(0,1)*((CW111*complexconjugate(ZEL21) + CW121*complexconjugate(ZEL22) + CW131*complexconjugate(ZEL23))*complexconjugate(ZM31) + (CW112*complexconjugate(ZEL21) + CW122*complexconjugate(ZEL22) + CW132*complexconjugate(ZEL23))*complexconjugate(ZM32) + (CW113*complexconjugate(ZEL21) + CW123*complexconjugate(ZEL22) + CW133*complexconjugate(ZEL23))*complexconjugate(ZM33) + complexconjugate(ZEL21)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZEL22)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZEL23)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_315 = Coupling(name = u'GC_315',
	 value = u'-1*complex(0,1)*(ZM31*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZM32*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZM33*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))', 
	 order = {u'QED':1} ) 
 
GC_316 = Coupling(name = u'GC_316',
	 value = u'(1*complex(0,1)*((CW111*complexconjugate(ZEL31) + CW121*complexconjugate(ZEL32) + CW131*complexconjugate(ZEL33))*complexconjugate(ZM31) + (CW112*complexconjugate(ZEL31) + CW122*complexconjugate(ZEL32) + CW132*complexconjugate(ZEL33))*complexconjugate(ZM32) + (CW113*complexconjugate(ZEL31) + CW123*complexconjugate(ZEL32) + CW133*complexconjugate(ZEL33))*complexconjugate(ZM33) + complexconjugate(ZEL31)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZEL32)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZEL33)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_317 = Coupling(name = u'GC_317',
	 value = u'-1*complex(0,1)*(ZM31*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZM32*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZM33*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))', 
	 order = {u'QED':1} ) 
 
GC_318 = Coupling(name = u'GC_318',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZEL11)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_319 = Coupling(name = u'GC_319',
	 value = u'(-1*complex(0,1)*(ZEL11*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL12*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL13*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_320 = Coupling(name = u'GC_320',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZEL21)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_321 = Coupling(name = u'GC_321',
	 value = u'(-1*complex(0,1)*(ZEL11*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL12*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL13*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_322 = Coupling(name = u'GC_322',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZEL31)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_323 = Coupling(name = u'GC_323',
	 value = u'(-1*complex(0,1)*(ZEL11*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL12*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL13*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_324 = Coupling(name = u'GC_324',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZEL11)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_325 = Coupling(name = u'GC_325',
	 value = u'(-1*complex(0,1)*(ZEL21*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL22*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL23*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_326 = Coupling(name = u'GC_326',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZEL21)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_327 = Coupling(name = u'GC_327',
	 value = u'(-1*complex(0,1)*(ZEL21*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL22*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL23*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_328 = Coupling(name = u'GC_328',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZEL31)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_329 = Coupling(name = u'GC_329',
	 value = u'(-1*complex(0,1)*(ZEL21*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL22*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL23*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_330 = Coupling(name = u'GC_330',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZEL11)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_331 = Coupling(name = u'GC_331',
	 value = u'(-1*complex(0,1)*(ZEL31*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL32*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL33*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_332 = Coupling(name = u'GC_332',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZEL21)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_333 = Coupling(name = u'GC_333',
	 value = u'(-1*complex(0,1)*(ZEL31*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL32*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL33*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_334 = Coupling(name = u'GC_334',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZEL31)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_335 = Coupling(name = u'GC_335',
	 value = u'(-1*complex(0,1)*(ZEL31*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL32*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL33*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_336 = Coupling(name = u'GC_336',
	 value = u'-1*complex(0,1)*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZEL11) + Omega21*complexconjugate(ZEL12) + Omega31*complexconjugate(ZEL13)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZEL11) + Omega22*complexconjugate(ZEL12) + Omega32*complexconjugate(ZEL13)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZEL11) + Omega23*complexconjugate(ZEL12) + Omega33*complexconjugate(ZEL13)))', 
	 order = {u'QED':1} ) 
 
GC_337 = Coupling(name = u'GC_337',
	 value = u'-1*complex(0,1)*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZEL21) + Omega21*complexconjugate(ZEL22) + Omega31*complexconjugate(ZEL23)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZEL21) + Omega22*complexconjugate(ZEL22) + Omega32*complexconjugate(ZEL23)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZEL21) + Omega23*complexconjugate(ZEL22) + Omega33*complexconjugate(ZEL23)))', 
	 order = {u'QED':1} ) 
 
GC_338 = Coupling(name = u'GC_338',
	 value = u'-1*complex(0,1)*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZEL31) + Omega21*complexconjugate(ZEL32) + Omega31*complexconjugate(ZEL33)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZEL31) + Omega22*complexconjugate(ZEL32) + Omega32*complexconjugate(ZEL33)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZEL31) + Omega23*complexconjugate(ZEL32) + Omega33*complexconjugate(ZEL33)))', 
	 order = {u'QED':1} ) 
 
GC_339 = Coupling(name = u'GC_339',
	 value = u'-1*complex(0,1)*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZEL11) + Omega21*complexconjugate(ZEL12) + Omega31*complexconjugate(ZEL13)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZEL11) + Omega22*complexconjugate(ZEL12) + Omega32*complexconjugate(ZEL13)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZEL11) + Omega23*complexconjugate(ZEL12) + Omega33*complexconjugate(ZEL13)))', 
	 order = {u'QED':1} ) 
 
GC_340 = Coupling(name = u'GC_340',
	 value = u'-1*complex(0,1)*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZEL21) + Omega21*complexconjugate(ZEL22) + Omega31*complexconjugate(ZEL23)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZEL21) + Omega22*complexconjugate(ZEL22) + Omega32*complexconjugate(ZEL23)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZEL21) + Omega23*complexconjugate(ZEL22) + Omega33*complexconjugate(ZEL23)))', 
	 order = {u'QED':1} ) 
 
GC_341 = Coupling(name = u'GC_341',
	 value = u'-1*complex(0,1)*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZEL31) + Omega21*complexconjugate(ZEL32) + Omega31*complexconjugate(ZEL33)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZEL31) + Omega22*complexconjugate(ZEL32) + Omega32*complexconjugate(ZEL33)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZEL31) + Omega23*complexconjugate(ZEL32) + Omega33*complexconjugate(ZEL33)))', 
	 order = {u'QED':1} ) 
 
GC_342 = Coupling(name = u'GC_342',
	 value = u'-1*complex(0,1)*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZEL11) + Omega21*complexconjugate(ZEL12) + Omega31*complexconjugate(ZEL13)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZEL11) + Omega22*complexconjugate(ZEL12) + Omega32*complexconjugate(ZEL13)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZEL11) + Omega23*complexconjugate(ZEL12) + Omega33*complexconjugate(ZEL13)))', 
	 order = {u'QED':1} ) 
 
GC_343 = Coupling(name = u'GC_343',
	 value = u'-1*complex(0,1)*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZEL21) + Omega21*complexconjugate(ZEL22) + Omega31*complexconjugate(ZEL23)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZEL21) + Omega22*complexconjugate(ZEL22) + Omega32*complexconjugate(ZEL23)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZEL21) + Omega23*complexconjugate(ZEL22) + Omega33*complexconjugate(ZEL23)))', 
	 order = {u'QED':1} ) 
 
GC_344 = Coupling(name = u'GC_344',
	 value = u'-1*complex(0,1)*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZEL31) + Omega21*complexconjugate(ZEL32) + Omega31*complexconjugate(ZEL33)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZEL31) + Omega22*complexconjugate(ZEL32) + Omega32*complexconjugate(ZEL33)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZEL31) + Omega23*complexconjugate(ZEL32) + Omega33*complexconjugate(ZEL33)))', 
	 order = {u'QED':1} ) 
 
GC_345 = Coupling(name = u'GC_345',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_346 = Coupling(name = u'GC_346',
	 value = u'(-1*complex(0,1)*(ZUL11*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL12*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL13*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_347 = Coupling(name = u'GC_347',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_348 = Coupling(name = u'GC_348',
	 value = u'(-1*complex(0,1)*(ZUL11*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL12*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL13*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_349 = Coupling(name = u'GC_349',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_350 = Coupling(name = u'GC_350',
	 value = u'(-1*complex(0,1)*(ZUL11*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL12*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL13*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_351 = Coupling(name = u'GC_351',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_352 = Coupling(name = u'GC_352',
	 value = u'(-1*complex(0,1)*(ZUL21*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL22*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL23*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_353 = Coupling(name = u'GC_353',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_354 = Coupling(name = u'GC_354',
	 value = u'(-1*complex(0,1)*(ZUL21*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL22*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL23*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_355 = Coupling(name = u'GC_355',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_356 = Coupling(name = u'GC_356',
	 value = u'(-1*complex(0,1)*(ZUL21*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL22*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL23*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_357 = Coupling(name = u'GC_357',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_358 = Coupling(name = u'GC_358',
	 value = u'(-1*complex(0,1)*(ZUL31*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL32*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL33*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_359 = Coupling(name = u'GC_359',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_360 = Coupling(name = u'GC_360',
	 value = u'(-1*complex(0,1)*(ZUL31*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL32*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL33*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_361 = Coupling(name = u'GC_361',
	 value = u'(-1*complex(0,1)*(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_362 = Coupling(name = u'GC_362',
	 value = u'(-1*complex(0,1)*(ZUL31*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL32*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL33*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_363 = Coupling(name = u'GC_363',
	 value = u'-1*complex(0,1)*((yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13))*complexconjugate(ZUL11) + (yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13))*complexconjugate(ZUL12) + (yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))*complexconjugate(ZUL13))', 
	 order = {u'QED':1} ) 
 
GC_364 = Coupling(name = u'GC_364',
	 value = u'1*complex(0,1)*(ZDL11*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZDL12*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZDL13*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))', 
	 order = {u'QED':1} ) 
 
GC_365 = Coupling(name = u'GC_365',
	 value = u'-1*complex(0,1)*((yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13))*complexconjugate(ZUL21) + (yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13))*complexconjugate(ZUL22) + (yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))*complexconjugate(ZUL23))', 
	 order = {u'QED':1} ) 
 
GC_366 = Coupling(name = u'GC_366',
	 value = u'1*complex(0,1)*(ZDL11*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZDL12*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZDL13*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))', 
	 order = {u'QED':1} ) 
 
GC_367 = Coupling(name = u'GC_367',
	 value = u'-1*complex(0,1)*((yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13))*complexconjugate(ZUL31) + (yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13))*complexconjugate(ZUL32) + (yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))*complexconjugate(ZUL33))', 
	 order = {u'QED':1} ) 
 
GC_368 = Coupling(name = u'GC_368',
	 value = u'1*complex(0,1)*(ZDL11*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZDL12*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZDL13*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))', 
	 order = {u'QED':1} ) 
 
GC_369 = Coupling(name = u'GC_369',
	 value = u'-1*complex(0,1)*((yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23))*complexconjugate(ZUL11) + (yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23))*complexconjugate(ZUL12) + (yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))*complexconjugate(ZUL13))', 
	 order = {u'QED':1} ) 
 
GC_370 = Coupling(name = u'GC_370',
	 value = u'1*complex(0,1)*(ZDL21*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZDL22*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZDL23*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))', 
	 order = {u'QED':1} ) 
 
GC_371 = Coupling(name = u'GC_371',
	 value = u'-1*complex(0,1)*((yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23))*complexconjugate(ZUL21) + (yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23))*complexconjugate(ZUL22) + (yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))*complexconjugate(ZUL23))', 
	 order = {u'QED':1} ) 
 
GC_372 = Coupling(name = u'GC_372',
	 value = u'1*complex(0,1)*(ZDL21*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZDL22*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZDL23*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))', 
	 order = {u'QED':1} ) 
 
GC_373 = Coupling(name = u'GC_373',
	 value = u'-1*complex(0,1)*((yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23))*complexconjugate(ZUL31) + (yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23))*complexconjugate(ZUL32) + (yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))*complexconjugate(ZUL33))', 
	 order = {u'QED':1} ) 
 
GC_374 = Coupling(name = u'GC_374',
	 value = u'1*complex(0,1)*(ZDL21*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZDL22*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZDL23*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))', 
	 order = {u'QED':1} ) 
 
GC_375 = Coupling(name = u'GC_375',
	 value = u'-1*complex(0,1)*((yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33))*complexconjugate(ZUL11) + (yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33))*complexconjugate(ZUL12) + (yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))*complexconjugate(ZUL13))', 
	 order = {u'QED':1} ) 
 
GC_376 = Coupling(name = u'GC_376',
	 value = u'1*complex(0,1)*(ZDL31*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZDL32*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZDL33*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))', 
	 order = {u'QED':1} ) 
 
GC_377 = Coupling(name = u'GC_377',
	 value = u'-1*complex(0,1)*((yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33))*complexconjugate(ZUL21) + (yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33))*complexconjugate(ZUL22) + (yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))*complexconjugate(ZUL23))', 
	 order = {u'QED':1} ) 
 
GC_378 = Coupling(name = u'GC_378',
	 value = u'1*complex(0,1)*(ZDL31*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZDL32*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZDL33*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))', 
	 order = {u'QED':1} ) 
 
GC_379 = Coupling(name = u'GC_379',
	 value = u'-1*complex(0,1)*((yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33))*complexconjugate(ZUL31) + (yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33))*complexconjugate(ZUL32) + (yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))*complexconjugate(ZUL33))', 
	 order = {u'QED':1} ) 
 
GC_380 = Coupling(name = u'GC_380',
	 value = u'1*complex(0,1)*(ZDL31*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZDL32*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZDL33*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))', 
	 order = {u'QED':1} ) 
 
GC_381 = Coupling(name = u'GC_381',
	 value = u'(-1*complex(0,1)*(2*complexconjugate(ZM11)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + 2*complexconjugate(ZM12)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + 2*complexconjugate(ZM13)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_382 = Coupling(name = u'GC_382',
	 value = u'(-1*complex(0,1)*(2*ZM11*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + 2*ZM12*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + 2*ZM13*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_383 = Coupling(name = u'GC_383',
	 value = u'(-1*complex(0,1)*((CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13))*complexconjugate(ZM21) + (CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13))*complexconjugate(ZM22) + (CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))*complexconjugate(ZM23) + complexconjugate(ZM11)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZM12)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZM13)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_384 = Coupling(name = u'GC_384',
	 value = u'(-1*complex(0,1)*(ZM21*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM11*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM12*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)) + ZM13*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_385 = Coupling(name = u'GC_385',
	 value = u'(-1*complex(0,1)*((CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13))*complexconjugate(ZM31) + (CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13))*complexconjugate(ZM32) + (CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))*complexconjugate(ZM33) + complexconjugate(ZM11)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZM12)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZM13)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_386 = Coupling(name = u'GC_386',
	 value = u'(-1*complex(0,1)*(ZM31*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM11*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM12*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)) + ZM13*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_387 = Coupling(name = u'GC_387',
	 value = u'(-1*complex(0,1)*(2*complexconjugate(ZM21)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + 2*complexconjugate(ZM22)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + 2*complexconjugate(ZM23)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_388 = Coupling(name = u'GC_388',
	 value = u'(-1*complex(0,1)*(2*ZM21*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + 2*ZM22*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + 2*ZM23*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_389 = Coupling(name = u'GC_389',
	 value = u'(-1*complex(0,1)*((CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23))*complexconjugate(ZM31) + (CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23))*complexconjugate(ZM32) + (CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))*complexconjugate(ZM33) + complexconjugate(ZM21)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZM22)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZM23)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_390 = Coupling(name = u'GC_390',
	 value = u'(-1*complex(0,1)*(ZM31*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM21*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM22*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133)) + ZM23*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_391 = Coupling(name = u'GC_391',
	 value = u'(-1*complex(0,1)*(2*complexconjugate(ZM31)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + 2*complexconjugate(ZM32)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + 2*complexconjugate(ZM33)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_392 = Coupling(name = u'GC_392',
	 value = u'(-1*complex(0,1)*(2*ZM31*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + 2*ZM32*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + 2*ZM33*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/vvSM', 
	 order = {u'QED':1} ) 
 
GC_393 = Coupling(name = u'GC_393',
	 value = u'1*complex(0,1)*ZH12*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_394 = Coupling(name = u'GC_394',
	 value = u'-1*complex(0,1)*ZH11*(ZDL11*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL12*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL13*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_395 = Coupling(name = u'GC_395',
	 value = u'1*complex(0,1)*ZH22*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_396 = Coupling(name = u'GC_396',
	 value = u'-1*complex(0,1)*ZH21*(ZDL11*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL12*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL13*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_397 = Coupling(name = u'GC_397',
	 value = u'1*complex(0,1)*ZH12*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_398 = Coupling(name = u'GC_398',
	 value = u'-1*complex(0,1)*ZH11*(ZDL11*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL12*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL13*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_399 = Coupling(name = u'GC_399',
	 value = u'1*complex(0,1)*ZH22*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_400 = Coupling(name = u'GC_400',
	 value = u'-1*complex(0,1)*ZH21*(ZDL11*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL12*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL13*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_401 = Coupling(name = u'GC_401',
	 value = u'1*complex(0,1)*ZH12*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_402 = Coupling(name = u'GC_402',
	 value = u'-1*complex(0,1)*ZH11*(ZDL11*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL12*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL13*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_403 = Coupling(name = u'GC_403',
	 value = u'1*complex(0,1)*ZH22*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_404 = Coupling(name = u'GC_404',
	 value = u'-1*complex(0,1)*ZH21*(ZDL11*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL12*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL13*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_405 = Coupling(name = u'GC_405',
	 value = u'1*complex(0,1)*ZH12*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_406 = Coupling(name = u'GC_406',
	 value = u'-1*complex(0,1)*ZH11*(ZDL21*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL22*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL23*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_407 = Coupling(name = u'GC_407',
	 value = u'1*complex(0,1)*ZH22*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_408 = Coupling(name = u'GC_408',
	 value = u'-1*complex(0,1)*ZH21*(ZDL21*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL22*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL23*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_409 = Coupling(name = u'GC_409',
	 value = u'1*complex(0,1)*ZH12*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_410 = Coupling(name = u'GC_410',
	 value = u'-1*complex(0,1)*ZH11*(ZDL21*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL22*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL23*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_411 = Coupling(name = u'GC_411',
	 value = u'1*complex(0,1)*ZH22*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_412 = Coupling(name = u'GC_412',
	 value = u'-1*complex(0,1)*ZH21*(ZDL21*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL22*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL23*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_413 = Coupling(name = u'GC_413',
	 value = u'1*complex(0,1)*ZH12*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_414 = Coupling(name = u'GC_414',
	 value = u'-1*complex(0,1)*ZH11*(ZDL21*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL22*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL23*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_415 = Coupling(name = u'GC_415',
	 value = u'1*complex(0,1)*ZH22*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_416 = Coupling(name = u'GC_416',
	 value = u'-1*complex(0,1)*ZH21*(ZDL21*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL22*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL23*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_417 = Coupling(name = u'GC_417',
	 value = u'1*complex(0,1)*ZH12*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_418 = Coupling(name = u'GC_418',
	 value = u'-1*complex(0,1)*ZH11*(ZDL31*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL32*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL33*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_419 = Coupling(name = u'GC_419',
	 value = u'1*complex(0,1)*ZH22*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {u'QED':1} ) 
 
GC_420 = Coupling(name = u'GC_420',
	 value = u'-1*complex(0,1)*ZH21*(ZDL31*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL32*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL33*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_421 = Coupling(name = u'GC_421',
	 value = u'1*complex(0,1)*ZH12*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_422 = Coupling(name = u'GC_422',
	 value = u'-1*complex(0,1)*ZH11*(ZDL31*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL32*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL33*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_423 = Coupling(name = u'GC_423',
	 value = u'1*complex(0,1)*ZH22*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {u'QED':1} ) 
 
GC_424 = Coupling(name = u'GC_424',
	 value = u'-1*complex(0,1)*ZH21*(ZDL31*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL32*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL33*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_425 = Coupling(name = u'GC_425',
	 value = u'1*complex(0,1)*ZH12*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_426 = Coupling(name = u'GC_426',
	 value = u'-1*complex(0,1)*ZH11*(ZDL31*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL32*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL33*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_427 = Coupling(name = u'GC_427',
	 value = u'1*complex(0,1)*ZH22*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {u'QED':1} ) 
 
GC_428 = Coupling(name = u'GC_428',
	 value = u'-1*complex(0,1)*ZH21*(ZDL31*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL32*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL33*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_429 = Coupling(name = u'GC_429',
	 value = u'-1*complex(0,1)*((ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13))*complexconjugate(ZM11) + (ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13))*complexconjugate(ZM12) + (ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))*complexconjugate(ZM13))', 
	 order = {u'QED':1} ) 
 
GC_430 = Coupling(name = u'GC_430',
	 value = u'(1*complex(0,1)*(ZM11*(ZEL11*complexconjugate(CW111) + ZEL12*complexconjugate(CW121) + ZEL13*complexconjugate(CW131)) + ZEL11*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM12*(ZEL11*complexconjugate(CW112) + ZEL12*complexconjugate(CW122) + ZEL13*complexconjugate(CW132)) + ZEL12*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM13*(ZEL11*complexconjugate(CW113) + ZEL12*complexconjugate(CW123) + ZEL13*complexconjugate(CW133)) + ZEL13*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_431 = Coupling(name = u'GC_431',
	 value = u'-1*complex(0,1)*((ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13))*complexconjugate(ZM21) + (ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13))*complexconjugate(ZM22) + (ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))*complexconjugate(ZM23))', 
	 order = {u'QED':1} ) 
 
GC_432 = Coupling(name = u'GC_432',
	 value = u'(1*complex(0,1)*(ZM21*(ZEL11*complexconjugate(CW111) + ZEL12*complexconjugate(CW121) + ZEL13*complexconjugate(CW131)) + ZEL11*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZEL11*complexconjugate(CW112) + ZEL12*complexconjugate(CW122) + ZEL13*complexconjugate(CW132)) + ZEL12*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZEL11*complexconjugate(CW113) + ZEL12*complexconjugate(CW123) + ZEL13*complexconjugate(CW133)) + ZEL13*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_433 = Coupling(name = u'GC_433',
	 value = u'-1*complex(0,1)*((ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13))*complexconjugate(ZM31) + (ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13))*complexconjugate(ZM32) + (ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))*complexconjugate(ZM33))', 
	 order = {u'QED':1} ) 
 
GC_434 = Coupling(name = u'GC_434',
	 value = u'(1*complex(0,1)*(ZM31*(ZEL11*complexconjugate(CW111) + ZEL12*complexconjugate(CW121) + ZEL13*complexconjugate(CW131)) + ZEL11*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZEL11*complexconjugate(CW112) + ZEL12*complexconjugate(CW122) + ZEL13*complexconjugate(CW132)) + ZEL12*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZEL11*complexconjugate(CW113) + ZEL12*complexconjugate(CW123) + ZEL13*complexconjugate(CW133)) + ZEL13*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_435 = Coupling(name = u'GC_435',
	 value = u'-1*complex(0,1)*((ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23))*complexconjugate(ZM11) + (ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23))*complexconjugate(ZM12) + (ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))*complexconjugate(ZM13))', 
	 order = {u'QED':1} ) 
 
GC_436 = Coupling(name = u'GC_436',
	 value = u'(1*complex(0,1)*(ZM11*(ZEL21*complexconjugate(CW111) + ZEL22*complexconjugate(CW121) + ZEL23*complexconjugate(CW131)) + ZEL21*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM12*(ZEL21*complexconjugate(CW112) + ZEL22*complexconjugate(CW122) + ZEL23*complexconjugate(CW132)) + ZEL22*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM13*(ZEL21*complexconjugate(CW113) + ZEL22*complexconjugate(CW123) + ZEL23*complexconjugate(CW133)) + ZEL23*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_437 = Coupling(name = u'GC_437',
	 value = u'-1*complex(0,1)*((ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23))*complexconjugate(ZM21) + (ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23))*complexconjugate(ZM22) + (ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))*complexconjugate(ZM23))', 
	 order = {u'QED':1} ) 
 
GC_438 = Coupling(name = u'GC_438',
	 value = u'(1*complex(0,1)*(ZM21*(ZEL21*complexconjugate(CW111) + ZEL22*complexconjugate(CW121) + ZEL23*complexconjugate(CW131)) + ZEL21*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZEL21*complexconjugate(CW112) + ZEL22*complexconjugate(CW122) + ZEL23*complexconjugate(CW132)) + ZEL22*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZEL21*complexconjugate(CW113) + ZEL22*complexconjugate(CW123) + ZEL23*complexconjugate(CW133)) + ZEL23*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_439 = Coupling(name = u'GC_439',
	 value = u'-1*complex(0,1)*((ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23))*complexconjugate(ZM31) + (ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23))*complexconjugate(ZM32) + (ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))*complexconjugate(ZM33))', 
	 order = {u'QED':1} ) 
 
GC_440 = Coupling(name = u'GC_440',
	 value = u'(1*complex(0,1)*(ZM31*(ZEL21*complexconjugate(CW111) + ZEL22*complexconjugate(CW121) + ZEL23*complexconjugate(CW131)) + ZEL21*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZEL21*complexconjugate(CW112) + ZEL22*complexconjugate(CW122) + ZEL23*complexconjugate(CW132)) + ZEL22*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZEL21*complexconjugate(CW113) + ZEL22*complexconjugate(CW123) + ZEL23*complexconjugate(CW133)) + ZEL23*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_441 = Coupling(name = u'GC_441',
	 value = u'-1*complex(0,1)*((ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33))*complexconjugate(ZM11) + (ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33))*complexconjugate(ZM12) + (ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))*complexconjugate(ZM13))', 
	 order = {u'QED':1} ) 
 
GC_442 = Coupling(name = u'GC_442',
	 value = u'(1*complex(0,1)*(ZM11*(ZEL31*complexconjugate(CW111) + ZEL32*complexconjugate(CW121) + ZEL33*complexconjugate(CW131)) + ZEL31*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM12*(ZEL31*complexconjugate(CW112) + ZEL32*complexconjugate(CW122) + ZEL33*complexconjugate(CW132)) + ZEL32*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM13*(ZEL31*complexconjugate(CW113) + ZEL32*complexconjugate(CW123) + ZEL33*complexconjugate(CW133)) + ZEL33*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_443 = Coupling(name = u'GC_443',
	 value = u'-1*complex(0,1)*((ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33))*complexconjugate(ZM21) + (ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33))*complexconjugate(ZM22) + (ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))*complexconjugate(ZM23))', 
	 order = {u'QED':1} ) 
 
GC_444 = Coupling(name = u'GC_444',
	 value = u'(1*complex(0,1)*(ZM21*(ZEL31*complexconjugate(CW111) + ZEL32*complexconjugate(CW121) + ZEL33*complexconjugate(CW131)) + ZEL31*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZEL31*complexconjugate(CW112) + ZEL32*complexconjugate(CW122) + ZEL33*complexconjugate(CW132)) + ZEL32*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZEL31*complexconjugate(CW113) + ZEL32*complexconjugate(CW123) + ZEL33*complexconjugate(CW133)) + ZEL33*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_445 = Coupling(name = u'GC_445',
	 value = u'-1*complex(0,1)*((ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33))*complexconjugate(ZM31) + (ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33))*complexconjugate(ZM32) + (ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))*complexconjugate(ZM33))', 
	 order = {u'QED':1} ) 
 
GC_446 = Coupling(name = u'GC_446',
	 value = u'(1*complex(0,1)*(ZM31*(ZEL31*complexconjugate(CW111) + ZEL32*complexconjugate(CW121) + ZEL33*complexconjugate(CW131)) + ZEL31*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZEL31*complexconjugate(CW112) + ZEL32*complexconjugate(CW122) + ZEL33*complexconjugate(CW132)) + ZEL32*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZEL31*complexconjugate(CW113) + ZEL32*complexconjugate(CW123) + ZEL33*complexconjugate(CW133)) + ZEL33*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {u'QED':1} ) 
 
GC_447 = Coupling(name = u'GC_447',
	 value = u'-1*complex(0,1)*ZH11*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR11) + Upsilon12*complexconjugate(ZUR12) + Upsilon13*complexconjugate(ZUR13)) + complexconjugate(ZER12)*(Upsilon21*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon23*complexconjugate(ZUR13)) + complexconjugate(ZER13)*(Upsilon31*complexconjugate(ZUR11) + Upsilon32*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {u'QED':1} ) 
 
GC_448 = Coupling(name = u'GC_448',
	 value = u'1*complex(0,1)*ZH11*(ZUL11*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL12*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL13*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_449 = Coupling(name = u'GC_449',
	 value = u'-1*complex(0,1)*ZH21*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR11) + Upsilon12*complexconjugate(ZUR12) + Upsilon13*complexconjugate(ZUR13)) + complexconjugate(ZER12)*(Upsilon21*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon23*complexconjugate(ZUR13)) + complexconjugate(ZER13)*(Upsilon31*complexconjugate(ZUR11) + Upsilon32*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {u'QED':1} ) 
 
GC_450 = Coupling(name = u'GC_450',
	 value = u'1*complex(0,1)*ZH21*(ZUL11*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL12*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL13*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_451 = Coupling(name = u'GC_451',
	 value = u'-1*complex(0,1)*ZH11*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR21) + Upsilon12*complexconjugate(ZUR22) + Upsilon13*complexconjugate(ZUR23)) + complexconjugate(ZER12)*(Upsilon21*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon23*complexconjugate(ZUR23)) + complexconjugate(ZER13)*(Upsilon31*complexconjugate(ZUR21) + Upsilon32*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {u'QED':1} ) 
 
GC_452 = Coupling(name = u'GC_452',
	 value = u'1*complex(0,1)*ZH11*(ZUL21*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL22*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL23*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_453 = Coupling(name = u'GC_453',
	 value = u'-1*complex(0,1)*ZH21*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR21) + Upsilon12*complexconjugate(ZUR22) + Upsilon13*complexconjugate(ZUR23)) + complexconjugate(ZER12)*(Upsilon21*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon23*complexconjugate(ZUR23)) + complexconjugate(ZER13)*(Upsilon31*complexconjugate(ZUR21) + Upsilon32*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {u'QED':1} ) 
 
GC_454 = Coupling(name = u'GC_454',
	 value = u'1*complex(0,1)*ZH21*(ZUL21*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL22*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL23*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_455 = Coupling(name = u'GC_455',
	 value = u'-1*complex(0,1)*ZH11*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR31) + Upsilon12*complexconjugate(ZUR32) + Upsilon13*complexconjugate(ZUR33)) + complexconjugate(ZER12)*(Upsilon21*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon23*complexconjugate(ZUR33)) + complexconjugate(ZER13)*(Upsilon31*complexconjugate(ZUR31) + Upsilon32*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {u'QED':1} ) 
 
GC_456 = Coupling(name = u'GC_456',
	 value = u'1*complex(0,1)*ZH11*(ZUL31*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL32*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL33*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_457 = Coupling(name = u'GC_457',
	 value = u'-1*complex(0,1)*ZH21*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR31) + Upsilon12*complexconjugate(ZUR32) + Upsilon13*complexconjugate(ZUR33)) + complexconjugate(ZER12)*(Upsilon21*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon23*complexconjugate(ZUR33)) + complexconjugate(ZER13)*(Upsilon31*complexconjugate(ZUR31) + Upsilon32*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {u'QED':1} ) 
 
GC_458 = Coupling(name = u'GC_458',
	 value = u'1*complex(0,1)*ZH21*(ZUL31*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL32*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL33*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_459 = Coupling(name = u'GC_459',
	 value = u'-1*complex(0,1)*ZH11*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR11) + Upsilon12*complexconjugate(ZUR12) + Upsilon13*complexconjugate(ZUR13)) + complexconjugate(ZER22)*(Upsilon21*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon23*complexconjugate(ZUR13)) + complexconjugate(ZER23)*(Upsilon31*complexconjugate(ZUR11) + Upsilon32*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {u'QED':1} ) 
 
GC_460 = Coupling(name = u'GC_460',
	 value = u'1*complex(0,1)*ZH11*(ZUL11*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL12*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL13*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_461 = Coupling(name = u'GC_461',
	 value = u'-1*complex(0,1)*ZH21*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR11) + Upsilon12*complexconjugate(ZUR12) + Upsilon13*complexconjugate(ZUR13)) + complexconjugate(ZER22)*(Upsilon21*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon23*complexconjugate(ZUR13)) + complexconjugate(ZER23)*(Upsilon31*complexconjugate(ZUR11) + Upsilon32*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {u'QED':1} ) 
 
GC_462 = Coupling(name = u'GC_462',
	 value = u'1*complex(0,1)*ZH21*(ZUL11*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL12*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL13*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_463 = Coupling(name = u'GC_463',
	 value = u'-1*complex(0,1)*ZH11*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR21) + Upsilon12*complexconjugate(ZUR22) + Upsilon13*complexconjugate(ZUR23)) + complexconjugate(ZER22)*(Upsilon21*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon23*complexconjugate(ZUR23)) + complexconjugate(ZER23)*(Upsilon31*complexconjugate(ZUR21) + Upsilon32*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {u'QED':1} ) 
 
GC_464 = Coupling(name = u'GC_464',
	 value = u'1*complex(0,1)*ZH11*(ZUL21*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL22*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL23*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_465 = Coupling(name = u'GC_465',
	 value = u'-1*complex(0,1)*ZH21*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR21) + Upsilon12*complexconjugate(ZUR22) + Upsilon13*complexconjugate(ZUR23)) + complexconjugate(ZER22)*(Upsilon21*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon23*complexconjugate(ZUR23)) + complexconjugate(ZER23)*(Upsilon31*complexconjugate(ZUR21) + Upsilon32*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {u'QED':1} ) 
 
GC_466 = Coupling(name = u'GC_466',
	 value = u'1*complex(0,1)*ZH21*(ZUL21*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL22*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL23*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_467 = Coupling(name = u'GC_467',
	 value = u'-1*complex(0,1)*ZH11*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR31) + Upsilon12*complexconjugate(ZUR32) + Upsilon13*complexconjugate(ZUR33)) + complexconjugate(ZER22)*(Upsilon21*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon23*complexconjugate(ZUR33)) + complexconjugate(ZER23)*(Upsilon31*complexconjugate(ZUR31) + Upsilon32*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {u'QED':1} ) 
 
GC_468 = Coupling(name = u'GC_468',
	 value = u'1*complex(0,1)*ZH11*(ZUL31*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL32*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL33*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_469 = Coupling(name = u'GC_469',
	 value = u'-1*complex(0,1)*ZH21*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR31) + Upsilon12*complexconjugate(ZUR32) + Upsilon13*complexconjugate(ZUR33)) + complexconjugate(ZER22)*(Upsilon21*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon23*complexconjugate(ZUR33)) + complexconjugate(ZER23)*(Upsilon31*complexconjugate(ZUR31) + Upsilon32*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {u'QED':1} ) 
 
GC_470 = Coupling(name = u'GC_470',
	 value = u'1*complex(0,1)*ZH21*(ZUL31*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL32*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL33*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_471 = Coupling(name = u'GC_471',
	 value = u'-1*complex(0,1)*ZH11*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR11) + Upsilon12*complexconjugate(ZUR12) + Upsilon13*complexconjugate(ZUR13)) + complexconjugate(ZER32)*(Upsilon21*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon23*complexconjugate(ZUR13)) + complexconjugate(ZER33)*(Upsilon31*complexconjugate(ZUR11) + Upsilon32*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {u'QED':1} ) 
 
GC_472 = Coupling(name = u'GC_472',
	 value = u'1*complex(0,1)*ZH11*(ZUL11*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL12*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL13*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_473 = Coupling(name = u'GC_473',
	 value = u'-1*complex(0,1)*ZH21*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR11) + Upsilon12*complexconjugate(ZUR12) + Upsilon13*complexconjugate(ZUR13)) + complexconjugate(ZER32)*(Upsilon21*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon23*complexconjugate(ZUR13)) + complexconjugate(ZER33)*(Upsilon31*complexconjugate(ZUR11) + Upsilon32*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {u'QED':1} ) 
 
GC_474 = Coupling(name = u'GC_474',
	 value = u'1*complex(0,1)*ZH21*(ZUL11*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL12*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL13*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_475 = Coupling(name = u'GC_475',
	 value = u'-1*complex(0,1)*ZH11*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR21) + Upsilon12*complexconjugate(ZUR22) + Upsilon13*complexconjugate(ZUR23)) + complexconjugate(ZER32)*(Upsilon21*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon23*complexconjugate(ZUR23)) + complexconjugate(ZER33)*(Upsilon31*complexconjugate(ZUR21) + Upsilon32*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {u'QED':1} ) 
 
GC_476 = Coupling(name = u'GC_476',
	 value = u'1*complex(0,1)*ZH11*(ZUL21*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL22*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL23*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_477 = Coupling(name = u'GC_477',
	 value = u'-1*complex(0,1)*ZH21*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR21) + Upsilon12*complexconjugate(ZUR22) + Upsilon13*complexconjugate(ZUR23)) + complexconjugate(ZER32)*(Upsilon21*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon23*complexconjugate(ZUR23)) + complexconjugate(ZER33)*(Upsilon31*complexconjugate(ZUR21) + Upsilon32*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {u'QED':1} ) 
 
GC_478 = Coupling(name = u'GC_478',
	 value = u'1*complex(0,1)*ZH21*(ZUL21*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL22*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL23*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_479 = Coupling(name = u'GC_479',
	 value = u'-1*complex(0,1)*ZH11*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR31) + Upsilon12*complexconjugate(ZUR32) + Upsilon13*complexconjugate(ZUR33)) + complexconjugate(ZER32)*(Upsilon21*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon23*complexconjugate(ZUR33)) + complexconjugate(ZER33)*(Upsilon31*complexconjugate(ZUR31) + Upsilon32*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {u'QED':1} ) 
 
GC_480 = Coupling(name = u'GC_480',
	 value = u'1*complex(0,1)*ZH11*(ZUL31*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL32*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL33*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_481 = Coupling(name = u'GC_481',
	 value = u'-1*complex(0,1)*ZH21*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR31) + Upsilon12*complexconjugate(ZUR32) + Upsilon13*complexconjugate(ZUR33)) + complexconjugate(ZER32)*(Upsilon21*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon23*complexconjugate(ZUR33)) + complexconjugate(ZER33)*(Upsilon31*complexconjugate(ZUR31) + Upsilon32*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {u'QED':1} ) 
 
GC_482 = Coupling(name = u'GC_482',
	 value = u'1*complex(0,1)*ZH21*(ZUL31*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL32*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL33*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {u'QED':1} ) 
 
GC_483 = Coupling(name = u'GC_483',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_484 = Coupling(name = u'GC_484',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_485 = Coupling(name = u'GC_485',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_486 = Coupling(name = u'GC_486',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_487 = Coupling(name = u'GC_487',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_488 = Coupling(name = u'GC_488',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_489 = Coupling(name = u'GC_489',
	 value = u'1./6.*complex(0,1)*(g1*cmath.cos(TW) - 3*g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_490 = Coupling(name = u'GC_490',
	 value = u'-1./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_491 = Coupling(name = u'GC_491',
	 value = u'1./6.*complex(0,1)*(g1*cmath.cos(TW) - 3*g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_492 = Coupling(name = u'GC_492',
	 value = u'-1./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_493 = Coupling(name = u'GC_493',
	 value = u'1./6.*complex(0,1)*(g1*cmath.cos(TW) - 3*g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_494 = Coupling(name = u'GC_494',
	 value = u'-1./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_495 = Coupling(name = u'GC_495',
	 value = u'-1./6.*complex(0,1)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_496 = Coupling(name = u'GC_496',
	 value = u'1./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_497 = Coupling(name = u'GC_497',
	 value = u'-1./6.*complex(0,1)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_498 = Coupling(name = u'GC_498',
	 value = u'1./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_499 = Coupling(name = u'GC_499',
	 value = u'-1./6.*complex(0,1)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_500 = Coupling(name = u'GC_500',
	 value = u'1./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_501 = Coupling(name = u'GC_501',
	 value = u'(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL11) + ZUL12*complexconjugate(ZDL12) + ZUL13*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_502 = Coupling(name = u'GC_502',
	 value = u'(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL21) + ZUL12*complexconjugate(ZDL22) + ZUL13*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_503 = Coupling(name = u'GC_503',
	 value = u'(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL31) + ZUL12*complexconjugate(ZDL32) + ZUL13*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_504 = Coupling(name = u'GC_504',
	 value = u'(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL11) + ZUL22*complexconjugate(ZDL12) + ZUL23*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_505 = Coupling(name = u'GC_505',
	 value = u'(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL21) + ZUL22*complexconjugate(ZDL22) + ZUL23*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_506 = Coupling(name = u'GC_506',
	 value = u'(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL31) + ZUL22*complexconjugate(ZDL32) + ZUL23*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_507 = Coupling(name = u'GC_507',
	 value = u'(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL11) + ZUL32*complexconjugate(ZDL12) + ZUL33*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_508 = Coupling(name = u'GC_508',
	 value = u'(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL21) + ZUL32*complexconjugate(ZDL22) + ZUL33*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_509 = Coupling(name = u'GC_509',
	 value = u'(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL31) + ZUL32*complexconjugate(ZDL32) + ZUL33*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_510 = Coupling(name = u'GC_510',
	 value = u'(1*complex(0,1)*g2*(ZM11*complexconjugate(ZEL11) + ZM12*complexconjugate(ZEL12) + ZM13*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_511 = Coupling(name = u'GC_511',
	 value = u'(1*complex(0,1)*g2*(ZM11*complexconjugate(ZEL21) + ZM12*complexconjugate(ZEL22) + ZM13*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_512 = Coupling(name = u'GC_512',
	 value = u'(1*complex(0,1)*g2*(ZM11*complexconjugate(ZEL31) + ZM12*complexconjugate(ZEL32) + ZM13*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_513 = Coupling(name = u'GC_513',
	 value = u'(1*complex(0,1)*g2*(ZM21*complexconjugate(ZEL11) + ZM22*complexconjugate(ZEL12) + ZM23*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_514 = Coupling(name = u'GC_514',
	 value = u'(1*complex(0,1)*g2*(ZM21*complexconjugate(ZEL21) + ZM22*complexconjugate(ZEL22) + ZM23*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_515 = Coupling(name = u'GC_515',
	 value = u'(1*complex(0,1)*g2*(ZM21*complexconjugate(ZEL31) + ZM22*complexconjugate(ZEL32) + ZM23*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_516 = Coupling(name = u'GC_516',
	 value = u'(1*complex(0,1)*g2*(ZM31*complexconjugate(ZEL11) + ZM32*complexconjugate(ZEL12) + ZM33*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_517 = Coupling(name = u'GC_517',
	 value = u'(1*complex(0,1)*g2*(ZM31*complexconjugate(ZEL21) + ZM32*complexconjugate(ZEL22) + ZM33*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_518 = Coupling(name = u'GC_518',
	 value = u'(1*complex(0,1)*g2*(ZM31*complexconjugate(ZEL31) + ZM32*complexconjugate(ZEL32) + ZM33*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_519 = Coupling(name = u'GC_519',
	 value = u'-1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_520 = Coupling(name = u'GC_520',
	 value = u'-1*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_521 = Coupling(name = u'GC_521',
	 value = u'-1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_522 = Coupling(name = u'GC_522',
	 value = u'-1*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_523 = Coupling(name = u'GC_523',
	 value = u'-1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_524 = Coupling(name = u'GC_524',
	 value = u'-1*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_525 = Coupling(name = u'GC_525',
	 value = u'-1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_526 = Coupling(name = u'GC_526',
	 value = u'1*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_527 = Coupling(name = u'GC_527',
	 value = u'-1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_528 = Coupling(name = u'GC_528',
	 value = u'1*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_529 = Coupling(name = u'GC_529',
	 value = u'-1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_530 = Coupling(name = u'GC_530',
	 value = u'1*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_531 = Coupling(name = u'GC_531',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_532 = Coupling(name = u'GC_532',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_533 = Coupling(name = u'GC_533',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_534 = Coupling(name = u'GC_534',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_535 = Coupling(name = u'GC_535',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_536 = Coupling(name = u'GC_536',
	 value = u'1*complex(0,1)*G', 
	 order = {u'QCD':1} ) 
 
GC_537 = Coupling(name = u'GC_537',
	 value = u'1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_538 = Coupling(name = u'GC_538',
	 value = u'2./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_539 = Coupling(name = u'GC_539',
	 value = u'1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_540 = Coupling(name = u'GC_540',
	 value = u'2./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_541 = Coupling(name = u'GC_541',
	 value = u'1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_542 = Coupling(name = u'GC_542',
	 value = u'2./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_543 = Coupling(name = u'GC_543',
	 value = u'(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL11) + ZDL12*complexconjugate(ZUL12) + ZDL13*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_544 = Coupling(name = u'GC_544',
	 value = u'(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL21) + ZDL12*complexconjugate(ZUL22) + ZDL13*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_545 = Coupling(name = u'GC_545',
	 value = u'(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL31) + ZDL12*complexconjugate(ZUL32) + ZDL13*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_546 = Coupling(name = u'GC_546',
	 value = u'(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL11) + ZDL22*complexconjugate(ZUL12) + ZDL23*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_547 = Coupling(name = u'GC_547',
	 value = u'(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL21) + ZDL22*complexconjugate(ZUL22) + ZDL23*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_548 = Coupling(name = u'GC_548',
	 value = u'(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL31) + ZDL22*complexconjugate(ZUL32) + ZDL23*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_549 = Coupling(name = u'GC_549',
	 value = u'(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL11) + ZDL32*complexconjugate(ZUL12) + ZDL33*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_550 = Coupling(name = u'GC_550',
	 value = u'(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL21) + ZDL32*complexconjugate(ZUL22) + ZDL33*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_551 = Coupling(name = u'GC_551',
	 value = u'(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL31) + ZDL32*complexconjugate(ZUL32) + ZDL33*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_552 = Coupling(name = u'GC_552',
	 value = u'1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_553 = Coupling(name = u'GC_553',
	 value = u'-2./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_554 = Coupling(name = u'GC_554',
	 value = u'1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_555 = Coupling(name = u'GC_555',
	 value = u'-2./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_556 = Coupling(name = u'GC_556',
	 value = u'1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_557 = Coupling(name = u'GC_557',
	 value = u'-2./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_558 = Coupling(name = u'GC_558',
	 value = u'1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_559 = Coupling(name = u'GC_559',
	 value = u'-1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_560 = Coupling(name = u'GC_560',
	 value = u'1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_561 = Coupling(name = u'GC_561',
	 value = u'-1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_562 = Coupling(name = u'GC_562',
	 value = u'1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_563 = Coupling(name = u'GC_563',
	 value = u'-1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {u'QED':1} ) 
 
GC_564 = Coupling(name = u'GC_564',
	 value = u'(1*complex(0,1)*g2*(ZEL11*complexconjugate(ZM11) + ZEL12*complexconjugate(ZM12) + ZEL13*complexconjugate(ZM13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_565 = Coupling(name = u'GC_565',
	 value = u'(1*complex(0,1)*g2*(ZEL11*complexconjugate(ZM21) + ZEL12*complexconjugate(ZM22) + ZEL13*complexconjugate(ZM23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_566 = Coupling(name = u'GC_566',
	 value = u'(1*complex(0,1)*g2*(ZEL11*complexconjugate(ZM31) + ZEL12*complexconjugate(ZM32) + ZEL13*complexconjugate(ZM33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_567 = Coupling(name = u'GC_567',
	 value = u'(1*complex(0,1)*g2*(ZEL21*complexconjugate(ZM11) + ZEL22*complexconjugate(ZM12) + ZEL23*complexconjugate(ZM13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_568 = Coupling(name = u'GC_568',
	 value = u'(1*complex(0,1)*g2*(ZEL21*complexconjugate(ZM21) + ZEL22*complexconjugate(ZM22) + ZEL23*complexconjugate(ZM23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_569 = Coupling(name = u'GC_569',
	 value = u'(1*complex(0,1)*g2*(ZEL21*complexconjugate(ZM31) + ZEL22*complexconjugate(ZM32) + ZEL23*complexconjugate(ZM33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_570 = Coupling(name = u'GC_570',
	 value = u'(1*complex(0,1)*g2*(ZEL31*complexconjugate(ZM11) + ZEL32*complexconjugate(ZM12) + ZEL33*complexconjugate(ZM13)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_571 = Coupling(name = u'GC_571',
	 value = u'(1*complex(0,1)*g2*(ZEL31*complexconjugate(ZM21) + ZEL32*complexconjugate(ZM22) + ZEL33*complexconjugate(ZM23)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_572 = Coupling(name = u'GC_572',
	 value = u'(1*complex(0,1)*g2*(ZEL31*complexconjugate(ZM31) + ZEL32*complexconjugate(ZM32) + ZEL33*complexconjugate(ZM33)))/cmath.sqrt(2)', 
	 order = {u'QED':1} ) 
 
GC_573 = Coupling(name = u'GC_573',
	 value = u'G', 
	 order = {u'QCD':1} ) 
 
GC_574 = Coupling(name = u'GC_574',
	 value = u'-1*complex(0,1)*g2*cmath.sin(TW)', 
	 order = {u'QED':1} ) 
 
GC_575 = Coupling(name = u'GC_575',
	 value = u'1*complex(0,1)*g2*cmath.cos(TW)', 
	 order = {u'QED':1} ) 
 
GC_576 = Coupling(name = u'GC_576',
	 value = u'-1*complex(0,1)*G**2', 
	 order = {u'QCD':2} ) 
 
GC_577 = Coupling(name = u'GC_577',
	 value = u'-1*complex(0,1)*G**2', 
	 order = {u'QCD':2} ) 
 
GC_578 = Coupling(name = u'GC_578',
	 value = u'1*complex(0,1)*G**2', 
	 order = {u'QCD':2} ) 
 
GC_579 = Coupling(name = u'GC_579',
	 value = u'-1*complex(0,1)*G**2', 
	 order = {u'QCD':2} ) 
 
GC_580 = Coupling(name = u'GC_580',
	 value = u'1*complex(0,1)*G**2', 
	 order = {u'QCD':2} ) 
 
GC_581 = Coupling(name = u'GC_581',
	 value = u'1*complex(0,1)*G**2', 
	 order = {u'QCD':2} ) 
 
GC_582 = Coupling(name = u'GC_582',
	 value = u'1*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_583 = Coupling(name = u'GC_583',
	 value = u'1*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_584 = Coupling(name = u'GC_584',
	 value = u'-2*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_585 = Coupling(name = u'GC_585',
	 value = u'1./2.*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {u'QED':2} ) 
 
GC_586 = Coupling(name = u'GC_586',
	 value = u'-1*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {u'QED':2} ) 
 
GC_587 = Coupling(name = u'GC_587',
	 value = u'1./2.*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {u'QED':2} ) 
 
GC_588 = Coupling(name = u'GC_588',
	 value = u'2*complex(0,1)*g2**2', 
	 order = {u'QED':2} ) 
 
GC_589 = Coupling(name = u'GC_589',
	 value = u'-1*complex(0,1)*g2**2', 
	 order = {u'QED':2} ) 
 
GC_590 = Coupling(name = u'GC_590',
	 value = u'-1*complex(0,1)*g2**2', 
	 order = {u'QED':2} ) 
 
GC_591 = Coupling(name = u'GC_591',
	 value = u'-2*complex(0,1)*g2**2*cmath.cos(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_592 = Coupling(name = u'GC_592',
	 value = u'1*complex(0,1)*g2**2*cmath.cos(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_593 = Coupling(name = u'GC_593',
	 value = u'1*complex(0,1)*g2**2*cmath.cos(TW)**2', 
	 order = {u'QED':2} ) 
 
GC_594=Coupling(name=u'GC_594',
	 value=u'-(HPP1*complex(0,1))', 
	 order={u'HIW':1})

GC_595=Coupling(name=u'GC_595',
	 value=u'-(HGG1*complex(0,1))', 
	 order={u'HIG':1})

