from object_library import all_couplings,Coupling 
from cmath import exp 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
 
GC_1 = Coupling(name = 'GC_1',
	 value = '-1*complex(0,1)*vvSM*complexconjugate(Lam)', 
	 order = {'QED':1} ) 
 
GC_2 = Coupling(name = 'GC_2',
	 value = '-((ZH12*complexconjugate(a1)*complexconjugate(ZH11) - a1*ZH11*complexconjugate(ZH12))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_3 = Coupling(name = 'GC_3',
	 value = '-((ZH12*complexconjugate(a1)*complexconjugate(ZH21) - a1*ZH11*complexconjugate(ZH22))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_4 = Coupling(name = 'GC_4',
	 value = '-((ZH22*complexconjugate(a1)*complexconjugate(ZH11) - a1*ZH21*complexconjugate(ZH12))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_5 = Coupling(name = 'GC_5',
	 value = '-((ZH22*complexconjugate(a1)*complexconjugate(ZH21) - a1*ZH21*complexconjugate(ZH22))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_6 = Coupling(name = 'GC_6',
	 value = '-3*complex(0,1)*vvSM*complexconjugate(Lam)', 
	 order = {'QED':1} ) 
 
GC_7 = Coupling(name = 'GC_7',
	 value = '-1*complex(0,1)*vvSM*complexconjugate(Lam)', 
	 order = {'QED':1} ) 
 
GC_8 = Coupling(name = 'GC_8',
	 value = '-1*complex(0,1)*vvSM*complexconjugate(gHR)', 
	 order = {'QED':1} ) 
 
GC_9 = Coupling(name = 'GC_9',
	 value = '-1./2.*complex(0,1)*(ZH11*(2*vvSM*complexconjugate(gHS)*complexconjugate(ZH11) + cmath.sqrt(2)*a1*complexconjugate(ZH12)) + ZH12*(cmath.sqrt(2)*complexconjugate(a1)*complexconjugate(ZH11) + 2*vvSM*(complexconjugate(gHR) + complexconjugate(ghrp))*complexconjugate(ZH12)))', 
	 order = {'QED':1} ) 
 
GC_10 = Coupling(name = 'GC_10',
	 value = '-1./2.*complex(0,1)*(ZH11*(2*vvSM*complexconjugate(gHS)*complexconjugate(ZH21) + cmath.sqrt(2)*a1*complexconjugate(ZH22)) + ZH12*(cmath.sqrt(2)*complexconjugate(a1)*complexconjugate(ZH21) + 2*vvSM*(complexconjugate(gHR) + complexconjugate(ghrp))*complexconjugate(ZH22)))', 
	 order = {'QED':1} ) 
 
GC_11 = Coupling(name = 'GC_11',
	 value = '-1./2.*complex(0,1)*(ZH21*(2*vvSM*complexconjugate(gHS)*complexconjugate(ZH11) + cmath.sqrt(2)*a1*complexconjugate(ZH12)) + ZH22*(cmath.sqrt(2)*complexconjugate(a1)*complexconjugate(ZH11) + 2*vvSM*(complexconjugate(gHR) + complexconjugate(ghrp))*complexconjugate(ZH12)))', 
	 order = {'QED':1} ) 
 
GC_12 = Coupling(name = 'GC_12',
	 value = '-1./2.*complex(0,1)*(ZH21*(2*vvSM*complexconjugate(gHS)*complexconjugate(ZH21) + cmath.sqrt(2)*a1*complexconjugate(ZH22)) + ZH22*(cmath.sqrt(2)*complexconjugate(a1)*complexconjugate(ZH21) + 2*vvSM*(complexconjugate(gHR) + complexconjugate(ghrp))*complexconjugate(ZH22)))', 
	 order = {'QED':1} ) 
 
GC_13 = Coupling(name = 'GC_13',
	 value = '-1./2.*complex(0,1)*(2*a1*ZH11 + cmath.sqrt(2)*vvSM*ZH12*complexconjugate(ghrp))', 
	 order = {'QED':1} ) 
 
GC_14 = Coupling(name = 'GC_14',
	 value = '-1./2.*complex(0,1)*(2*a1*ZH21 + cmath.sqrt(2)*vvSM*ZH22*complexconjugate(ghrp))', 
	 order = {'QED':1} ) 
 
GC_15 = Coupling(name = 'GC_15',
	 value = '2*complex(0,1)*(-(ZH12*ZH21) + ZH11*ZH22)*complexconjugate(lRRS)', 
	 order = {'QED':1} ) 
 
GC_16 = Coupling(name = 'GC_16',
	 value = '-1./2.*complex(0,1)*(2*complexconjugate(a1)*complexconjugate(ZH11) + cmath.sqrt(2)*vvSM*complexconjugate(ghrp)*complexconjugate(ZH12))', 
	 order = {'QED':1} ) 
 
GC_17 = Coupling(name = 'GC_17',
	 value = '-1./2.*complex(0,1)*(2*complexconjugate(a1)*complexconjugate(ZH21) + cmath.sqrt(2)*vvSM*complexconjugate(ghrp)*complexconjugate(ZH22))', 
	 order = {'QED':1} ) 
 
GC_18 = Coupling(name = 'GC_18',
	 value = '2*complex(0,1)*lRRS*(-(complexconjugate(ZH12)*complexconjugate(ZH21)) + complexconjugate(ZH11)*complexconjugate(ZH22))', 
	 order = {'QED':1} ) 
 
GC_19 = Coupling(name = 'GC_19',
	 value = '1./2.*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_20 = Coupling(name = 'GC_20',
	 value = '1./2.*complex(0,1)*g2**2*cmath.cos(TW)**2 + 1*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g1**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_21 = Coupling(name = 'GC_21',
	 value = '(g1*g2*cmath.cos(TW))/2.', 
	 order = {'QED':2} ) 
 
GC_22 = Coupling(name = 'GC_22',
	 value = '-1./2.*(g1*g2*cmath.sin(TW))', 
	 order = {'QED':2} ) 
 
GC_23 = Coupling(name = 'GC_23',
	 value = '-1./2.*(g1*g2*cmath.cos(TW))', 
	 order = {'QED':2} ) 
 
GC_24 = Coupling(name = 'GC_24',
	 value = '(g1*g2*cmath.sin(TW))/2.', 
	 order = {'QED':2} ) 
 
GC_25 = Coupling(name = 'GC_25',
	 value = '1./2.*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_26 = Coupling(name = 'GC_26',
	 value = '1./2.*complex(0,1)*g2**2*cmath.cos(TW)**2 + 1*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g1**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_27 = Coupling(name = 'GC_27',
	 value = '1./2.*complex(0,1)*g1*g2*cmath.cos(TW)', 
	 order = {'QED':2} ) 
 
GC_28 = Coupling(name = 'GC_28',
	 value = '-1./2.*complex(0,1)*g1*g2*cmath.sin(TW)', 
	 order = {'QED':2} ) 
 
GC_29 = Coupling(name = 'GC_29',
	 value = '1./2.*complex(0,1)*g1*g2*cmath.cos(TW)', 
	 order = {'QED':2} ) 
 
GC_30 = Coupling(name = 'GC_30',
	 value = '-1./2.*complex(0,1)*g1*g2*cmath.sin(TW)', 
	 order = {'QED':2} ) 
 
GC_31 = Coupling(name = 'GC_31',
	 value = '1./2.*complex(0,1)*g1**2*cmath.cos(TW)**2 + 1*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_32 = Coupling(name = 'GC_32',
	 value = '1./2.*complex(0,1)*g1*g2*cmath.cos(2*TW) - 1./4.*complex(0,1)*g1**2*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_33 = Coupling(name = 'GC_33',
	 value = '1./2.*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_34 = Coupling(name = 'GC_34',
	 value = '1./2.*complex(0,1)*g2**2*cmath.cos(TW)**2 - 1*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g1**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_35 = Coupling(name = 'GC_35',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_36 = Coupling(name = 'GC_36',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_37 = Coupling(name = 'GC_37',
	 value = '1./3.*complex(0,1)*G*g1*cmath.cos(TW) + 1*complex(0,1)*G*g2*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_38 = Coupling(name = 'GC_38',
	 value = '1*complex(0,1)*cmath.sqrt(2)*G*g2*complexconjugate(ZH12)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_39 = Coupling(name = 'GC_39',
	 value = '1*complex(0,1)*cmath.sqrt(2)*G*g2*complexconjugate(ZH22)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_40 = Coupling(name = 'GC_40',
	 value = '1*complex(0,1)*G*g2*cmath.cos(TW) - 1./3.*complex(0,1)*G*g1*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_41 = Coupling(name = 'GC_41',
	 value = '1./18.*complex(0,1)*g1**2*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_42 = Coupling(name = 'GC_42',
	 value = '(1./3.*complex(0,1)*g1*g2*complexconjugate(ZH12)*cmath.cos(TW))/cmath.sqrt(2)', 
	 order = {'QED':2} ) 
 
GC_43 = Coupling(name = 'GC_43',
	 value = '(1./3.*complex(0,1)*g1*g2*complexconjugate(ZH22)*cmath.cos(TW))/cmath.sqrt(2)', 
	 order = {'QED':2} ) 
 
GC_44 = Coupling(name = 'GC_44',
	 value = '1./6.*complex(0,1)*g1*g2*cmath.cos(2*TW) - 1./36.*complex(0,1)*g1**2*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_45 = Coupling(name = 'GC_45',
	 value = '(-1./3.*complex(0,1)*g1*g2*complexconjugate(ZH12)*cmath.sin(TW))/cmath.sqrt(2)', 
	 order = {'QED':2} ) 
 
GC_46 = Coupling(name = 'GC_46',
	 value = '(-1./3.*complex(0,1)*g1*g2*complexconjugate(ZH22)*cmath.sin(TW))/cmath.sqrt(2)', 
	 order = {'QED':2} ) 
 
GC_47 = Coupling(name = 'GC_47',
	 value = '1./2.*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_48 = Coupling(name = 'GC_48',
	 value = '1./2.*complex(0,1)*g2**2*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*cmath.cos(TW)*cmath.sin(TW) + 1./18.*complex(0,1)*g1**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_49 = Coupling(name = 'GC_49',
	 value = '1*complex(0,1)*G**2*ZH11*complexconjugate(ZH11) + 1*complex(0,1)*G**2*ZH12*complexconjugate(ZH12)', 
	 order = {'QCD':2} ) 
 
GC_50 = Coupling(name = 'GC_50',
	 value = '1*complex(0,1)*G**2*ZH11*complexconjugate(ZH11) + 1*complex(0,1)*G**2*ZH12*complexconjugate(ZH12)', 
	 order = {'QCD':2} ) 
 
GC_51 = Coupling(name = 'GC_51',
	 value = '1*complex(0,1)*G**2*ZH11*complexconjugate(ZH21) + 1*complex(0,1)*G**2*ZH12*complexconjugate(ZH22)', 
	 order = {'QCD':2} ) 
 
GC_52 = Coupling(name = 'GC_52',
	 value = '1*complex(0,1)*G**2*ZH11*complexconjugate(ZH21) + 1*complex(0,1)*G**2*ZH12*complexconjugate(ZH22)', 
	 order = {'QCD':2} ) 
 
GC_53 = Coupling(name = 'GC_53',
	 value = '1*complex(0,1)*G**2*ZH21*complexconjugate(ZH11) + 1*complex(0,1)*G**2*ZH22*complexconjugate(ZH12)', 
	 order = {'QCD':2} ) 
 
GC_54 = Coupling(name = 'GC_54',
	 value = '1*complex(0,1)*G**2*ZH21*complexconjugate(ZH11) + 1*complex(0,1)*G**2*ZH22*complexconjugate(ZH12)', 
	 order = {'QCD':2} ) 
 
GC_55 = Coupling(name = 'GC_55',
	 value = '1*complex(0,1)*G**2*ZH21*complexconjugate(ZH21) + 1*complex(0,1)*G**2*ZH22*complexconjugate(ZH22)', 
	 order = {'QCD':2} ) 
 
GC_56 = Coupling(name = 'GC_56',
	 value = '1*complex(0,1)*G**2*ZH21*complexconjugate(ZH21) + 1*complex(0,1)*G**2*ZH22*complexconjugate(ZH22)', 
	 order = {'QCD':2} ) 
 
GC_57 = Coupling(name = 'GC_57',
	 value = '-2./3.*complex(0,1)*G*g1*ZH11*complexconjugate(ZH11)*cmath.cos(TW) + 1./3.*complex(0,1)*G*g1*ZH12*complexconjugate(ZH12)*cmath.cos(TW) - 1*complex(0,1)*G*g2*ZH12*complexconjugate(ZH12)*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_58 = Coupling(name = 'GC_58',
	 value = '-2./3.*complex(0,1)*G*g1*ZH11*complexconjugate(ZH21)*cmath.cos(TW) + 1./3.*complex(0,1)*G*g1*ZH12*complexconjugate(ZH22)*cmath.cos(TW) - 1*complex(0,1)*G*g2*ZH12*complexconjugate(ZH22)*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_59 = Coupling(name = 'GC_59',
	 value = '-2./3.*complex(0,1)*G*g1*ZH21*complexconjugate(ZH11)*cmath.cos(TW) + 1./3.*complex(0,1)*G*g1*ZH22*complexconjugate(ZH12)*cmath.cos(TW) - 1*complex(0,1)*G*g2*ZH22*complexconjugate(ZH12)*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_60 = Coupling(name = 'GC_60',
	 value = '-2./3.*complex(0,1)*G*g1*ZH21*complexconjugate(ZH21)*cmath.cos(TW) + 1./3.*complex(0,1)*G*g1*ZH22*complexconjugate(ZH22)*cmath.cos(TW) - 1*complex(0,1)*G*g2*ZH22*complexconjugate(ZH22)*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_61 = Coupling(name = 'GC_61',
	 value = '-1*complex(0,1)*G*g2*ZH12*complexconjugate(ZH12)*cmath.cos(TW) + 2./3.*complex(0,1)*G*g1*ZH11*complexconjugate(ZH11)*cmath.sin(TW) - 1./3.*complex(0,1)*G*g1*ZH12*complexconjugate(ZH12)*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_62 = Coupling(name = 'GC_62',
	 value = '-1*complex(0,1)*G*g2*ZH12*complexconjugate(ZH22)*cmath.cos(TW) + 2./3.*complex(0,1)*G*g1*ZH11*complexconjugate(ZH21)*cmath.sin(TW) - 1./3.*complex(0,1)*G*g1*ZH12*complexconjugate(ZH22)*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_63 = Coupling(name = 'GC_63',
	 value = '-1*complex(0,1)*G*g2*ZH22*complexconjugate(ZH12)*cmath.cos(TW) + 2./3.*complex(0,1)*G*g1*ZH21*complexconjugate(ZH11)*cmath.sin(TW) - 1./3.*complex(0,1)*G*g1*ZH22*complexconjugate(ZH12)*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_64 = Coupling(name = 'GC_64',
	 value = '-1*complex(0,1)*G*g2*ZH22*complexconjugate(ZH22)*cmath.cos(TW) + 2./3.*complex(0,1)*G*g1*ZH21*complexconjugate(ZH21)*cmath.sin(TW) - 1./3.*complex(0,1)*G*g1*ZH22*complexconjugate(ZH22)*cmath.sin(TW)', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_65 = Coupling(name = 'GC_65',
	 value = '1*complex(0,1)*cmath.sqrt(2)*G*g2*ZH12', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_66 = Coupling(name = 'GC_66',
	 value = '1*complex(0,1)*cmath.sqrt(2)*G*g2*ZH22', 
	 order = {'QED':1, 'QCD':1} ) 
 
GC_67 = Coupling(name = 'GC_67',
	 value = '2./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH11)*cmath.cos(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH12)*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH12)*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH12)*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_68 = Coupling(name = 'GC_68',
	 value = '2./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH21)*cmath.cos(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH22)*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH22)*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH22)*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_69 = Coupling(name = 'GC_69',
	 value = '2./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH11)*cmath.cos(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH12)*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH12)*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH12)*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_70 = Coupling(name = 'GC_70',
	 value = '2./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH21)*cmath.cos(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH22)*cmath.cos(TW)**2 - 1./3.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH22)*cmath.cos(TW)*cmath.sin(TW) + 1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH22)*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_71 = Coupling(name = 'GC_71',
	 value = '-1./6.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH12)*cmath.cos(2*TW) - 1./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH11)*cmath.sin(2*TW) - 1./36.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH12)*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH12)*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_72 = Coupling(name = 'GC_72',
	 value = '-1./6.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH22)*cmath.cos(2*TW) - 1./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH21)*cmath.sin(2*TW) - 1./36.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH22)*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH22)*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_73 = Coupling(name = 'GC_73',
	 value = '-1./6.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH12)*cmath.cos(2*TW) - 1./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH11)*cmath.sin(2*TW) - 1./36.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH12)*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH12)*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_74 = Coupling(name = 'GC_74',
	 value = '-1./6.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH22)*cmath.cos(2*TW) - 1./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH21)*cmath.sin(2*TW) - 1./36.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH22)*cmath.sin(2*TW) + 1./4.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH22)*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_75 = Coupling(name = 'GC_75',
	 value = '(1./3.*complex(0,1)*g1*g2*ZH12*cmath.cos(TW))/cmath.sqrt(2)', 
	 order = {'QED':2} ) 
 
GC_76 = Coupling(name = 'GC_76',
	 value = '(1./3.*complex(0,1)*g1*g2*ZH22*cmath.cos(TW))/cmath.sqrt(2)', 
	 order = {'QED':2} ) 
 
GC_77 = Coupling(name = 'GC_77',
	 value = '1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH12)', 
	 order = {'QED':2} ) 
 
GC_78 = Coupling(name = 'GC_78',
	 value = '1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH22)', 
	 order = {'QED':2} ) 
 
GC_79 = Coupling(name = 'GC_79',
	 value = '1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH12)', 
	 order = {'QED':2} ) 
 
GC_80 = Coupling(name = 'GC_80',
	 value = '1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH22)', 
	 order = {'QED':2} ) 
 
GC_81 = Coupling(name = 'GC_81',
	 value = '1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH12)*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH12)*cmath.cos(TW)*cmath.sin(TW) + 2./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH11)*cmath.sin(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH12)*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_82 = Coupling(name = 'GC_82',
	 value = '1./2.*complex(0,1)*g2**2*ZH12*complexconjugate(ZH22)*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZH22)*cmath.cos(TW)*cmath.sin(TW) + 2./9.*complex(0,1)*g1**2*ZH11*complexconjugate(ZH21)*cmath.sin(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH12*complexconjugate(ZH22)*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_83 = Coupling(name = 'GC_83',
	 value = '1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH12)*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH12)*cmath.cos(TW)*cmath.sin(TW) + 2./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH11)*cmath.sin(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH12)*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_84 = Coupling(name = 'GC_84',
	 value = '1./2.*complex(0,1)*g2**2*ZH22*complexconjugate(ZH22)*cmath.cos(TW)**2 + 1./3.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZH22)*cmath.cos(TW)*cmath.sin(TW) + 2./9.*complex(0,1)*g1**2*ZH21*complexconjugate(ZH21)*cmath.sin(TW)**2 + 1./18.*complex(0,1)*g1**2*ZH22*complexconjugate(ZH22)*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_85 = Coupling(name = 'GC_85',
	 value = '(-1./3.*complex(0,1)*g1*g2*ZH12*cmath.sin(TW))/cmath.sqrt(2)', 
	 order = {'QED':2} ) 
 
GC_86 = Coupling(name = 'GC_86',
	 value = '(-1./3.*complex(0,1)*g1*g2*ZH22*cmath.sin(TW))/cmath.sqrt(2)', 
	 order = {'QED':2} ) 
 
GC_87 = Coupling(name = 'GC_87',
	 value = '(g2*cmath.cos(TW) + g1*cmath.sin(TW))/2.', 
	 order = {'QED':1} ) 
 
GC_88 = Coupling(name = 'GC_88',
	 value = '-1./2.*g2', 
	 order = {'QED':1} ) 
 
GC_89 = Coupling(name = 'GC_89',
	 value = '-1./2.*g2', 
	 order = {'QED':1} ) 
 
GC_90 = Coupling(name = 'GC_90',
	 value = '-1./2.*complex(0,1)*g2', 
	 order = {'QED':1} ) 
 
GC_91 = Coupling(name = 'GC_91',
	 value = '1./2.*complex(0,1)*g2', 
	 order = {'QED':1} ) 
 
GC_92 = Coupling(name = 'GC_92',
	 value = '1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_93 = Coupling(name = 'GC_93',
	 value = '1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_94 = Coupling(name = 'GC_94',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_95 = Coupling(name = 'GC_95',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_96 = Coupling(name = 'GC_96',
	 value = '(1*complex(0,1)*g2*complexconjugate(ZH12))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_97 = Coupling(name = 'GC_97',
	 value = '(1*complex(0,1)*g2*complexconjugate(ZH22))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_98 = Coupling(name = 'GC_98',
	 value = '1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_99 = Coupling(name = 'GC_99',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_100 = Coupling(name = 'GC_100',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_101 = Coupling(name = 'GC_101',
	 value = '-1./6.*complex(0,1)*(2*g1*ZH11*complexconjugate(ZH11)*cmath.cos(TW) + ZH12*complexconjugate(ZH12)*(-(g1*cmath.cos(TW)) + 3*g2*cmath.sin(TW)))', 
	 order = {'QED':1} ) 
 
GC_102 = Coupling(name = 'GC_102',
	 value = '-1./6.*complex(0,1)*(2*g1*ZH11*complexconjugate(ZH21)*cmath.cos(TW) + ZH12*complexconjugate(ZH22)*(-(g1*cmath.cos(TW)) + 3*g2*cmath.sin(TW)))', 
	 order = {'QED':1} ) 
 
GC_103 = Coupling(name = 'GC_103',
	 value = '-1./6.*complex(0,1)*(2*g1*ZH21*complexconjugate(ZH11)*cmath.cos(TW) + ZH22*complexconjugate(ZH12)*(-(g1*cmath.cos(TW)) + 3*g2*cmath.sin(TW)))', 
	 order = {'QED':1} ) 
 
GC_104 = Coupling(name = 'GC_104',
	 value = '-1./6.*complex(0,1)*(2*g1*ZH21*complexconjugate(ZH21)*cmath.cos(TW) + ZH22*complexconjugate(ZH22)*(-(g1*cmath.cos(TW)) + 3*g2*cmath.sin(TW)))', 
	 order = {'QED':1} ) 
 
GC_105 = Coupling(name = 'GC_105',
	 value = '1./6.*complex(0,1)*(2*g1*ZH11*complexconjugate(ZH11)*cmath.sin(TW) - ZH12*complexconjugate(ZH12)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW)))', 
	 order = {'QED':1} ) 
 
GC_106 = Coupling(name = 'GC_106',
	 value = '1./6.*complex(0,1)*(2*g1*ZH11*complexconjugate(ZH21)*cmath.sin(TW) - ZH12*complexconjugate(ZH22)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW)))', 
	 order = {'QED':1} ) 
 
GC_107 = Coupling(name = 'GC_107',
	 value = '1./6.*complex(0,1)*(2*g1*ZH21*complexconjugate(ZH11)*cmath.sin(TW) - ZH22*complexconjugate(ZH12)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW)))', 
	 order = {'QED':1} ) 
 
GC_108 = Coupling(name = 'GC_108',
	 value = '1./6.*complex(0,1)*(2*g1*ZH21*complexconjugate(ZH21)*cmath.sin(TW) - ZH22*complexconjugate(ZH22)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW)))', 
	 order = {'QED':1} ) 
 
GC_109 = Coupling(name = 'GC_109',
	 value = '(1*complex(0,1)*g2*ZH12)/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_110 = Coupling(name = 'GC_110',
	 value = '(1*complex(0,1)*g2*ZH22)/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_111 = Coupling(name = 'GC_111',
	 value = '1./2.*complex(0,1)*g2**2*vvSM', 
	 order = {'QED':1} ) 
 
GC_112 = Coupling(name = 'GC_112',
	 value = '1./2.*complex(0,1)*vvSM*(g2*cmath.cos(TW) + g1*cmath.sin(TW))**2', 
	 order = {'QED':1} ) 
 
GC_113 = Coupling(name = 'GC_113',
	 value = '1./2.*complex(0,1)*g1*g2*vvSM*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_114 = Coupling(name = 'GC_114',
	 value = '-1./2.*complex(0,1)*g1*g2*vvSM*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_115 = Coupling(name = 'GC_115',
	 value = '1./2.*complex(0,1)*g1*g2*vvSM*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_116 = Coupling(name = 'GC_116',
	 value = '-1./2.*complex(0,1)*g1*g2*vvSM*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_117 = Coupling(name = 'GC_117',
	 value = '-((complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_118 = Coupling(name = 'GC_118',
	 value = '(ZDL11*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL12*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL13*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_119 = Coupling(name = 'GC_119',
	 value = '-((complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_120 = Coupling(name = 'GC_120',
	 value = '(ZDL11*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL12*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL13*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_121 = Coupling(name = 'GC_121',
	 value = '-((complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_122 = Coupling(name = 'GC_122',
	 value = '(ZDL11*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL12*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL13*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_123 = Coupling(name = 'GC_123',
	 value = '-((complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_124 = Coupling(name = 'GC_124',
	 value = '(ZDL21*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL22*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL23*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_125 = Coupling(name = 'GC_125',
	 value = '-((complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_126 = Coupling(name = 'GC_126',
	 value = '(ZDL21*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL22*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL23*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_127 = Coupling(name = 'GC_127',
	 value = '-((complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_128 = Coupling(name = 'GC_128',
	 value = '(ZDL21*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL22*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL23*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_129 = Coupling(name = 'GC_129',
	 value = '-((complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_130 = Coupling(name = 'GC_130',
	 value = '(ZDL31*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL32*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL33*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_131 = Coupling(name = 'GC_131',
	 value = '-((complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_132 = Coupling(name = 'GC_132',
	 value = '(ZDL31*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL32*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL33*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_133 = Coupling(name = 'GC_133',
	 value = '-((complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_134 = Coupling(name = 'GC_134',
	 value = '(ZDL31*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL32*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL33*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_135 = Coupling(name = 'GC_135',
	 value = '-((complexconjugate(ZEL11)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_136 = Coupling(name = 'GC_136',
	 value = '(ZEL11*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL12*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL13*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_137 = Coupling(name = 'GC_137',
	 value = '-((complexconjugate(ZEL21)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_138 = Coupling(name = 'GC_138',
	 value = '(ZEL11*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL12*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL13*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_139 = Coupling(name = 'GC_139',
	 value = '-((complexconjugate(ZEL31)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_140 = Coupling(name = 'GC_140',
	 value = '(ZEL11*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL12*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL13*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_141 = Coupling(name = 'GC_141',
	 value = '-((complexconjugate(ZEL11)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_142 = Coupling(name = 'GC_142',
	 value = '(ZEL21*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL22*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL23*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_143 = Coupling(name = 'GC_143',
	 value = '-((complexconjugate(ZEL21)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_144 = Coupling(name = 'GC_144',
	 value = '(ZEL21*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL22*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL23*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_145 = Coupling(name = 'GC_145',
	 value = '-((complexconjugate(ZEL31)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_146 = Coupling(name = 'GC_146',
	 value = '(ZEL21*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL22*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL23*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_147 = Coupling(name = 'GC_147',
	 value = '-((complexconjugate(ZEL11)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_148 = Coupling(name = 'GC_148',
	 value = '(ZEL31*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL32*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL33*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_149 = Coupling(name = 'GC_149',
	 value = '-((complexconjugate(ZEL21)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_150 = Coupling(name = 'GC_150',
	 value = '(ZEL31*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL32*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL33*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_151 = Coupling(name = 'GC_151',
	 value = '-((complexconjugate(ZEL31)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_152 = Coupling(name = 'GC_152',
	 value = '(ZEL31*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL32*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL33*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_153 = Coupling(name = 'GC_153',
	 value = '(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_154 = Coupling(name = 'GC_154',
	 value = '-((ZUL11*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL12*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL13*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_155 = Coupling(name = 'GC_155',
	 value = '(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_156 = Coupling(name = 'GC_156',
	 value = '-((ZUL11*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL12*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL13*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_157 = Coupling(name = 'GC_157',
	 value = '(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_158 = Coupling(name = 'GC_158',
	 value = '-((ZUL11*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL12*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL13*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_159 = Coupling(name = 'GC_159',
	 value = '(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_160 = Coupling(name = 'GC_160',
	 value = '-((ZUL21*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL22*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL23*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_161 = Coupling(name = 'GC_161',
	 value = '(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_162 = Coupling(name = 'GC_162',
	 value = '-((ZUL21*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL22*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL23*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_163 = Coupling(name = 'GC_163',
	 value = '(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_164 = Coupling(name = 'GC_164',
	 value = '-((ZUL21*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL22*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL23*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_165 = Coupling(name = 'GC_165',
	 value = '(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_166 = Coupling(name = 'GC_166',
	 value = '-((ZUL31*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL32*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL33*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_167 = Coupling(name = 'GC_167',
	 value = '(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_168 = Coupling(name = 'GC_168',
	 value = '-((ZUL31*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL32*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL33*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_169 = Coupling(name = 'GC_169',
	 value = '(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_170 = Coupling(name = 'GC_170',
	 value = '-((ZUL31*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL32*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL33*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_171 = Coupling(name = 'GC_171',
	 value = '(2*complexconjugate(ZM11)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + 2*complexconjugate(ZM12)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + 2*complexconjugate(ZM13)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13)))/vvSM', 
	 order = {'QED':1} ) 
 
GC_172 = Coupling(name = 'GC_172',
	 value = '-((2*ZM11*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + 2*ZM12*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + 2*ZM13*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)))/vvSM)', 
	 order = {'QED':1} ) 
 
GC_173 = Coupling(name = 'GC_173',
	 value = '((CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13))*complexconjugate(ZM21) + (CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13))*complexconjugate(ZM22) + (CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))*complexconjugate(ZM23) + complexconjugate(ZM11)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZM12)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZM13)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23)))/vvSM', 
	 order = {'QED':1} ) 
 
GC_174 = Coupling(name = 'GC_174',
	 value = '-((ZM21*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM11*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM12*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)) + ZM13*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133)))/vvSM)', 
	 order = {'QED':1} ) 
 
GC_175 = Coupling(name = 'GC_175',
	 value = '((CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13))*complexconjugate(ZM31) + (CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13))*complexconjugate(ZM32) + (CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))*complexconjugate(ZM33) + complexconjugate(ZM11)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZM12)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZM13)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33)))/vvSM', 
	 order = {'QED':1} ) 
 
GC_176 = Coupling(name = 'GC_176',
	 value = '-((ZM31*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM11*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM12*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)) + ZM13*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133)))/vvSM)', 
	 order = {'QED':1} ) 
 
GC_177 = Coupling(name = 'GC_177',
	 value = '(2*complexconjugate(ZM21)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + 2*complexconjugate(ZM22)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + 2*complexconjugate(ZM23)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23)))/vvSM', 
	 order = {'QED':1} ) 
 
GC_178 = Coupling(name = 'GC_178',
	 value = '-((2*ZM21*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + 2*ZM22*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + 2*ZM23*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133)))/vvSM)', 
	 order = {'QED':1} ) 
 
GC_179 = Coupling(name = 'GC_179',
	 value = '((CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23))*complexconjugate(ZM31) + (CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23))*complexconjugate(ZM32) + (CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))*complexconjugate(ZM33) + complexconjugate(ZM21)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZM22)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZM23)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33)))/vvSM', 
	 order = {'QED':1} ) 
 
GC_180 = Coupling(name = 'GC_180',
	 value = '-((ZM31*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM21*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM22*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133)) + ZM23*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133)))/vvSM)', 
	 order = {'QED':1} ) 
 
GC_181 = Coupling(name = 'GC_181',
	 value = '(2*complexconjugate(ZM31)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + 2*complexconjugate(ZM32)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + 2*complexconjugate(ZM33)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33)))/vvSM', 
	 order = {'QED':1} ) 
 
GC_182 = Coupling(name = 'GC_182',
	 value = '-((2*ZM31*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + 2*ZM32*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + 2*ZM33*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133)))/vvSM)', 
	 order = {'QED':1} ) 
 
GC_183 = Coupling(name = 'GC_183',
	 value = '-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_184 = Coupling(name = 'GC_184',
	 value = '1*complex(0,1)*(ZDR11*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR12*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR13*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {'QED':1} ) 
 
GC_185 = Coupling(name = 'GC_185',
	 value = '-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_186 = Coupling(name = 'GC_186',
	 value = '1*complex(0,1)*(ZDR11*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR12*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR13*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {'QED':1} ) 
 
GC_187 = Coupling(name = 'GC_187',
	 value = '-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_188 = Coupling(name = 'GC_188',
	 value = '1*complex(0,1)*(ZDR21*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR22*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR23*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {'QED':1} ) 
 
GC_189 = Coupling(name = 'GC_189',
	 value = '-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_190 = Coupling(name = 'GC_190',
	 value = '1*complex(0,1)*(ZDR21*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR22*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR23*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {'QED':1} ) 
 
GC_191 = Coupling(name = 'GC_191',
	 value = '-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_192 = Coupling(name = 'GC_192',
	 value = '1*complex(0,1)*(ZDR31*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR32*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR33*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {'QED':1} ) 
 
GC_193 = Coupling(name = 'GC_193',
	 value = '-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM11) + Theta21*complexconjugate(ZM12) + Theta31*complexconjugate(ZM13)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM11) + Theta22*complexconjugate(ZM12) + Theta32*complexconjugate(ZM13)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM11) + Theta23*complexconjugate(ZM12) + Theta33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_194 = Coupling(name = 'GC_194',
	 value = '1*complex(0,1)*(ZDR31*(ZM11*complexconjugate(Omega11) + ZM12*complexconjugate(Omega21) + ZM13*complexconjugate(Omega31)) + ZDR32*(ZM11*complexconjugate(Omega12) + ZM12*complexconjugate(Omega22) + ZM13*complexconjugate(Omega32)) + ZDR33*(ZM11*complexconjugate(Omega13) + ZM12*complexconjugate(Omega23) + ZM13*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {'QED':1} ) 
 
GC_195 = Coupling(name = 'GC_195',
	 value = '-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_196 = Coupling(name = 'GC_196',
	 value = '1*complex(0,1)*(ZDR11*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR12*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR13*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {'QED':1} ) 
 
GC_197 = Coupling(name = 'GC_197',
	 value = '-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_198 = Coupling(name = 'GC_198',
	 value = '1*complex(0,1)*(ZDR11*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR12*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR13*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {'QED':1} ) 
 
GC_199 = Coupling(name = 'GC_199',
	 value = '-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_200 = Coupling(name = 'GC_200',
	 value = '1*complex(0,1)*(ZDR21*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR22*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR23*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {'QED':1} ) 
 
GC_201 = Coupling(name = 'GC_201',
	 value = '-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_202 = Coupling(name = 'GC_202',
	 value = '1*complex(0,1)*(ZDR21*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR22*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR23*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {'QED':1} ) 
 
GC_203 = Coupling(name = 'GC_203',
	 value = '-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_204 = Coupling(name = 'GC_204',
	 value = '1*complex(0,1)*(ZDR31*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR32*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR33*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {'QED':1} ) 
 
GC_205 = Coupling(name = 'GC_205',
	 value = '-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM21) + Theta21*complexconjugate(ZM22) + Theta31*complexconjugate(ZM23)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM21) + Theta22*complexconjugate(ZM22) + Theta32*complexconjugate(ZM23)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM21) + Theta23*complexconjugate(ZM22) + Theta33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_206 = Coupling(name = 'GC_206',
	 value = '1*complex(0,1)*(ZDR31*(ZM21*complexconjugate(Omega11) + ZM22*complexconjugate(Omega21) + ZM23*complexconjugate(Omega31)) + ZDR32*(ZM21*complexconjugate(Omega12) + ZM22*complexconjugate(Omega22) + ZM23*complexconjugate(Omega32)) + ZDR33*(ZM21*complexconjugate(Omega13) + ZM22*complexconjugate(Omega23) + ZM23*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {'QED':1} ) 
 
GC_207 = Coupling(name = 'GC_207',
	 value = '-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_208 = Coupling(name = 'GC_208',
	 value = '1*complex(0,1)*(ZDR11*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR12*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR13*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {'QED':1} ) 
 
GC_209 = Coupling(name = 'GC_209',
	 value = '-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL11)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL12)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL13)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_210 = Coupling(name = 'GC_210',
	 value = '1*complex(0,1)*(ZDR11*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR12*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR13*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {'QED':1} ) 
 
GC_211 = Coupling(name = 'GC_211',
	 value = '-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_212 = Coupling(name = 'GC_212',
	 value = '1*complex(0,1)*(ZDR21*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR22*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR23*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {'QED':1} ) 
 
GC_213 = Coupling(name = 'GC_213',
	 value = '-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL21)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL22)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL23)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_214 = Coupling(name = 'GC_214',
	 value = '1*complex(0,1)*(ZDR21*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR22*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR23*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {'QED':1} ) 
 
GC_215 = Coupling(name = 'GC_215',
	 value = '-1*complex(0,1)*complexconjugate(ZH11)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_216 = Coupling(name = 'GC_216',
	 value = '1*complex(0,1)*(ZDR31*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR32*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR33*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH12)', 
	 order = {'QED':1} ) 
 
GC_217 = Coupling(name = 'GC_217',
	 value = '-1*complex(0,1)*complexconjugate(ZH21)*(complexconjugate(ZDL31)*(Theta11*complexconjugate(ZM31) + Theta21*complexconjugate(ZM32) + Theta31*complexconjugate(ZM33)) + complexconjugate(ZDL32)*(Theta12*complexconjugate(ZM31) + Theta22*complexconjugate(ZM32) + Theta32*complexconjugate(ZM33)) + complexconjugate(ZDL33)*(Theta13*complexconjugate(ZM31) + Theta23*complexconjugate(ZM32) + Theta33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_218 = Coupling(name = 'GC_218',
	 value = '1*complex(0,1)*(ZDR31*(ZM31*complexconjugate(Omega11) + ZM32*complexconjugate(Omega21) + ZM33*complexconjugate(Omega31)) + ZDR32*(ZM31*complexconjugate(Omega12) + ZM32*complexconjugate(Omega22) + ZM33*complexconjugate(Omega32)) + ZDR33*(ZM31*complexconjugate(Omega13) + ZM32*complexconjugate(Omega23) + ZM33*complexconjugate(Omega33)))*complexconjugate(ZH22)', 
	 order = {'QED':1} ) 
 
GC_219 = Coupling(name = 'GC_219',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_220 = Coupling(name = 'GC_220',
	 value = '(-1*complex(0,1)*(ZDL11*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL12*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL13*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_221 = Coupling(name = 'GC_221',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_222 = Coupling(name = 'GC_222',
	 value = '(-1*complex(0,1)*(ZDL11*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL12*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL13*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_223 = Coupling(name = 'GC_223',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_224 = Coupling(name = 'GC_224',
	 value = '(-1*complex(0,1)*(ZDL11*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL12*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL13*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_225 = Coupling(name = 'GC_225',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_226 = Coupling(name = 'GC_226',
	 value = '(-1*complex(0,1)*(ZDL21*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL22*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL23*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_227 = Coupling(name = 'GC_227',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_228 = Coupling(name = 'GC_228',
	 value = '(-1*complex(0,1)*(ZDL21*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL22*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL23*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_229 = Coupling(name = 'GC_229',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_230 = Coupling(name = 'GC_230',
	 value = '(-1*complex(0,1)*(ZDL21*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL22*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL23*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_231 = Coupling(name = 'GC_231',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL11)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL12)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL13)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_232 = Coupling(name = 'GC_232',
	 value = '(-1*complex(0,1)*(ZDL31*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZDL32*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZDL33*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_233 = Coupling(name = 'GC_233',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL21)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL22)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL23)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_234 = Coupling(name = 'GC_234',
	 value = '(-1*complex(0,1)*(ZDL31*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZDL32*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZDL33*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_235 = Coupling(name = 'GC_235',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL31)*(yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL32)*(yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL33)*(yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_236 = Coupling(name = 'GC_236',
	 value = '(-1*complex(0,1)*(ZDL31*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZDL32*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZDL33*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_237 = Coupling(name = 'GC_237',
	 value = '1*complex(0,1)*(complexconjugate(ZDL11)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZDL12)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZDL13)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_238 = Coupling(name = 'GC_238',
	 value = '-1*complex(0,1)*(ZUL11*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZUL12*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZUL13*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))', 
	 order = {'QED':1} ) 
 
GC_239 = Coupling(name = 'GC_239',
	 value = '1*complex(0,1)*(complexconjugate(ZDL21)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZDL22)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZDL23)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_240 = Coupling(name = 'GC_240',
	 value = '-1*complex(0,1)*(ZUL11*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZUL12*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZUL13*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))', 
	 order = {'QED':1} ) 
 
GC_241 = Coupling(name = 'GC_241',
	 value = '1*complex(0,1)*(complexconjugate(ZDL31)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZDL32)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZDL33)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_242 = Coupling(name = 'GC_242',
	 value = '-1*complex(0,1)*(ZUL11*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZUL12*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZUL13*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))', 
	 order = {'QED':1} ) 
 
GC_243 = Coupling(name = 'GC_243',
	 value = '1*complex(0,1)*(complexconjugate(ZDL11)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZDL12)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZDL13)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_244 = Coupling(name = 'GC_244',
	 value = '-1*complex(0,1)*(ZUL21*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZUL22*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZUL23*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))', 
	 order = {'QED':1} ) 
 
GC_245 = Coupling(name = 'GC_245',
	 value = '1*complex(0,1)*(complexconjugate(ZDL21)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZDL22)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZDL23)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_246 = Coupling(name = 'GC_246',
	 value = '-1*complex(0,1)*(ZUL21*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZUL22*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZUL23*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))', 
	 order = {'QED':1} ) 
 
GC_247 = Coupling(name = 'GC_247',
	 value = '1*complex(0,1)*(complexconjugate(ZDL31)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZDL32)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZDL33)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_248 = Coupling(name = 'GC_248',
	 value = '-1*complex(0,1)*(ZUL21*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZUL22*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZUL23*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))', 
	 order = {'QED':1} ) 
 
GC_249 = Coupling(name = 'GC_249',
	 value = '1*complex(0,1)*(complexconjugate(ZDL11)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZDL12)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZDL13)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_250 = Coupling(name = 'GC_250',
	 value = '-1*complex(0,1)*(ZUL31*(ZDR11*complexconjugate(yd11) + ZDR12*complexconjugate(yd21) + ZDR13*complexconjugate(yd31)) + ZUL32*(ZDR11*complexconjugate(yd12) + ZDR12*complexconjugate(yd22) + ZDR13*complexconjugate(yd32)) + ZUL33*(ZDR11*complexconjugate(yd13) + ZDR12*complexconjugate(yd23) + ZDR13*complexconjugate(yd33)))', 
	 order = {'QED':1} ) 
 
GC_251 = Coupling(name = 'GC_251',
	 value = '1*complex(0,1)*(complexconjugate(ZDL21)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZDL22)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZDL23)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_252 = Coupling(name = 'GC_252',
	 value = '-1*complex(0,1)*(ZUL31*(ZDR21*complexconjugate(yd11) + ZDR22*complexconjugate(yd21) + ZDR23*complexconjugate(yd31)) + ZUL32*(ZDR21*complexconjugate(yd12) + ZDR22*complexconjugate(yd22) + ZDR23*complexconjugate(yd32)) + ZUL33*(ZDR21*complexconjugate(yd13) + ZDR22*complexconjugate(yd23) + ZDR23*complexconjugate(yd33)))', 
	 order = {'QED':1} ) 
 
GC_253 = Coupling(name = 'GC_253',
	 value = '1*complex(0,1)*(complexconjugate(ZDL31)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZDL32)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZDL33)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_254 = Coupling(name = 'GC_254',
	 value = '-1*complex(0,1)*(ZUL31*(ZDR31*complexconjugate(yd11) + ZDR32*complexconjugate(yd21) + ZDR33*complexconjugate(yd31)) + ZUL32*(ZDR31*complexconjugate(yd12) + ZDR32*complexconjugate(yd22) + ZDR33*complexconjugate(yd32)) + ZUL33*(ZDR31*complexconjugate(yd13) + ZDR32*complexconjugate(yd23) + ZDR33*complexconjugate(yd33)))', 
	 order = {'QED':1} ) 
 
GC_255 = Coupling(name = 'GC_255',
	 value = '-1*complex(0,1)*(ZDR11*(ZEL11*complexconjugate(Omega11) + ZEL12*complexconjugate(Omega21) + ZEL13*complexconjugate(Omega31)) + ZDR12*(ZEL11*complexconjugate(Omega12) + ZEL12*complexconjugate(Omega22) + ZEL13*complexconjugate(Omega32)) + ZDR13*(ZEL11*complexconjugate(Omega13) + ZEL12*complexconjugate(Omega23) + ZEL13*complexconjugate(Omega33)))', 
	 order = {'QED':1} ) 
 
GC_256 = Coupling(name = 'GC_256',
	 value = '-1*complex(0,1)*(ZDR21*(ZEL11*complexconjugate(Omega11) + ZEL12*complexconjugate(Omega21) + ZEL13*complexconjugate(Omega31)) + ZDR22*(ZEL11*complexconjugate(Omega12) + ZEL12*complexconjugate(Omega22) + ZEL13*complexconjugate(Omega32)) + ZDR23*(ZEL11*complexconjugate(Omega13) + ZEL12*complexconjugate(Omega23) + ZEL13*complexconjugate(Omega33)))', 
	 order = {'QED':1} ) 
 
GC_257 = Coupling(name = 'GC_257',
	 value = '-1*complex(0,1)*(ZDR31*(ZEL11*complexconjugate(Omega11) + ZEL12*complexconjugate(Omega21) + ZEL13*complexconjugate(Omega31)) + ZDR32*(ZEL11*complexconjugate(Omega12) + ZEL12*complexconjugate(Omega22) + ZEL13*complexconjugate(Omega32)) + ZDR33*(ZEL11*complexconjugate(Omega13) + ZEL12*complexconjugate(Omega23) + ZEL13*complexconjugate(Omega33)))', 
	 order = {'QED':1} ) 
 
GC_258 = Coupling(name = 'GC_258',
	 value = '-1*complex(0,1)*(ZDR11*(ZEL21*complexconjugate(Omega11) + ZEL22*complexconjugate(Omega21) + ZEL23*complexconjugate(Omega31)) + ZDR12*(ZEL21*complexconjugate(Omega12) + ZEL22*complexconjugate(Omega22) + ZEL23*complexconjugate(Omega32)) + ZDR13*(ZEL21*complexconjugate(Omega13) + ZEL22*complexconjugate(Omega23) + ZEL23*complexconjugate(Omega33)))', 
	 order = {'QED':1} ) 
 
GC_259 = Coupling(name = 'GC_259',
	 value = '-1*complex(0,1)*(ZDR21*(ZEL21*complexconjugate(Omega11) + ZEL22*complexconjugate(Omega21) + ZEL23*complexconjugate(Omega31)) + ZDR22*(ZEL21*complexconjugate(Omega12) + ZEL22*complexconjugate(Omega22) + ZEL23*complexconjugate(Omega32)) + ZDR23*(ZEL21*complexconjugate(Omega13) + ZEL22*complexconjugate(Omega23) + ZEL23*complexconjugate(Omega33)))', 
	 order = {'QED':1} ) 
 
GC_260 = Coupling(name = 'GC_260',
	 value = '-1*complex(0,1)*(ZDR31*(ZEL21*complexconjugate(Omega11) + ZEL22*complexconjugate(Omega21) + ZEL23*complexconjugate(Omega31)) + ZDR32*(ZEL21*complexconjugate(Omega12) + ZEL22*complexconjugate(Omega22) + ZEL23*complexconjugate(Omega32)) + ZDR33*(ZEL21*complexconjugate(Omega13) + ZEL22*complexconjugate(Omega23) + ZEL23*complexconjugate(Omega33)))', 
	 order = {'QED':1} ) 
 
GC_261 = Coupling(name = 'GC_261',
	 value = '-1*complex(0,1)*(ZDR11*(ZEL31*complexconjugate(Omega11) + ZEL32*complexconjugate(Omega21) + ZEL33*complexconjugate(Omega31)) + ZDR12*(ZEL31*complexconjugate(Omega12) + ZEL32*complexconjugate(Omega22) + ZEL33*complexconjugate(Omega32)) + ZDR13*(ZEL31*complexconjugate(Omega13) + ZEL32*complexconjugate(Omega23) + ZEL33*complexconjugate(Omega33)))', 
	 order = {'QED':1} ) 
 
GC_262 = Coupling(name = 'GC_262',
	 value = '-1*complex(0,1)*(ZDR21*(ZEL31*complexconjugate(Omega11) + ZEL32*complexconjugate(Omega21) + ZEL33*complexconjugate(Omega31)) + ZDR22*(ZEL31*complexconjugate(Omega12) + ZEL32*complexconjugate(Omega22) + ZEL33*complexconjugate(Omega32)) + ZDR23*(ZEL31*complexconjugate(Omega13) + ZEL32*complexconjugate(Omega23) + ZEL33*complexconjugate(Omega33)))', 
	 order = {'QED':1} ) 
 
GC_263 = Coupling(name = 'GC_263',
	 value = '-1*complex(0,1)*(ZDR31*(ZEL31*complexconjugate(Omega11) + ZEL32*complexconjugate(Omega21) + ZEL33*complexconjugate(Omega31)) + ZDR32*(ZEL31*complexconjugate(Omega12) + ZEL32*complexconjugate(Omega22) + ZEL33*complexconjugate(Omega32)) + ZDR33*(ZEL31*complexconjugate(Omega13) + ZEL32*complexconjugate(Omega23) + ZEL33*complexconjugate(Omega33)))', 
	 order = {'QED':1} ) 
 
GC_264 = Coupling(name = 'GC_264',
	 value = '1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_265 = Coupling(name = 'GC_265',
	 value = '-1*complex(0,1)*(ZER11*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon21) + ZUR13*complexconjugate(Upsilon31)) + ZER12*(ZUR11*complexconjugate(Upsilon12) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon32)) + ZER13*(ZUR11*complexconjugate(Upsilon13) + ZUR12*complexconjugate(Upsilon23) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {'QED':1} ) 
 
GC_266 = Coupling(name = 'GC_266',
	 value = '1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_267 = Coupling(name = 'GC_267',
	 value = '-1*complex(0,1)*(ZER11*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon21) + ZUR13*complexconjugate(Upsilon31)) + ZER12*(ZUR11*complexconjugate(Upsilon12) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon32)) + ZER13*(ZUR11*complexconjugate(Upsilon13) + ZUR12*complexconjugate(Upsilon23) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {'QED':1} ) 
 
GC_268 = Coupling(name = 'GC_268',
	 value = '1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_269 = Coupling(name = 'GC_269',
	 value = '-1*complex(0,1)*(ZER11*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon21) + ZUR23*complexconjugate(Upsilon31)) + ZER12*(ZUR21*complexconjugate(Upsilon12) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon32)) + ZER13*(ZUR21*complexconjugate(Upsilon13) + ZUR22*complexconjugate(Upsilon23) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {'QED':1} ) 
 
GC_270 = Coupling(name = 'GC_270',
	 value = '1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_271 = Coupling(name = 'GC_271',
	 value = '-1*complex(0,1)*(ZER11*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon21) + ZUR23*complexconjugate(Upsilon31)) + ZER12*(ZUR21*complexconjugate(Upsilon12) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon32)) + ZER13*(ZUR21*complexconjugate(Upsilon13) + ZUR22*complexconjugate(Upsilon23) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {'QED':1} ) 
 
GC_272 = Coupling(name = 'GC_272',
	 value = '1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_273 = Coupling(name = 'GC_273',
	 value = '-1*complex(0,1)*(ZER11*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon21) + ZUR33*complexconjugate(Upsilon31)) + ZER12*(ZUR31*complexconjugate(Upsilon12) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon32)) + ZER13*(ZUR31*complexconjugate(Upsilon13) + ZUR32*complexconjugate(Upsilon23) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {'QED':1} ) 
 
GC_274 = Coupling(name = 'GC_274',
	 value = '1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL11) + Theta21*complexconjugate(ZEL12) + Theta31*complexconjugate(ZEL13))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL11) + Theta22*complexconjugate(ZEL12) + Theta32*complexconjugate(ZEL13))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL11) + Theta23*complexconjugate(ZEL12) + Theta33*complexconjugate(ZEL13))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_275 = Coupling(name = 'GC_275',
	 value = '-1*complex(0,1)*(ZER11*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon21) + ZUR33*complexconjugate(Upsilon31)) + ZER12*(ZUR31*complexconjugate(Upsilon12) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon32)) + ZER13*(ZUR31*complexconjugate(Upsilon13) + ZUR32*complexconjugate(Upsilon23) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {'QED':1} ) 
 
GC_276 = Coupling(name = 'GC_276',
	 value = '1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_277 = Coupling(name = 'GC_277',
	 value = '-1*complex(0,1)*(ZER21*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon21) + ZUR13*complexconjugate(Upsilon31)) + ZER22*(ZUR11*complexconjugate(Upsilon12) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon32)) + ZER23*(ZUR11*complexconjugate(Upsilon13) + ZUR12*complexconjugate(Upsilon23) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {'QED':1} ) 
 
GC_278 = Coupling(name = 'GC_278',
	 value = '1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_279 = Coupling(name = 'GC_279',
	 value = '-1*complex(0,1)*(ZER21*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon21) + ZUR13*complexconjugate(Upsilon31)) + ZER22*(ZUR11*complexconjugate(Upsilon12) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon32)) + ZER23*(ZUR11*complexconjugate(Upsilon13) + ZUR12*complexconjugate(Upsilon23) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {'QED':1} ) 
 
GC_280 = Coupling(name = 'GC_280',
	 value = '1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_281 = Coupling(name = 'GC_281',
	 value = '-1*complex(0,1)*(ZER21*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon21) + ZUR23*complexconjugate(Upsilon31)) + ZER22*(ZUR21*complexconjugate(Upsilon12) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon32)) + ZER23*(ZUR21*complexconjugate(Upsilon13) + ZUR22*complexconjugate(Upsilon23) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {'QED':1} ) 
 
GC_282 = Coupling(name = 'GC_282',
	 value = '1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_283 = Coupling(name = 'GC_283',
	 value = '-1*complex(0,1)*(ZER21*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon21) + ZUR23*complexconjugate(Upsilon31)) + ZER22*(ZUR21*complexconjugate(Upsilon12) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon32)) + ZER23*(ZUR21*complexconjugate(Upsilon13) + ZUR22*complexconjugate(Upsilon23) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {'QED':1} ) 
 
GC_284 = Coupling(name = 'GC_284',
	 value = '1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_285 = Coupling(name = 'GC_285',
	 value = '-1*complex(0,1)*(ZER21*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon21) + ZUR33*complexconjugate(Upsilon31)) + ZER22*(ZUR31*complexconjugate(Upsilon12) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon32)) + ZER23*(ZUR31*complexconjugate(Upsilon13) + ZUR32*complexconjugate(Upsilon23) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {'QED':1} ) 
 
GC_286 = Coupling(name = 'GC_286',
	 value = '1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL21) + Theta21*complexconjugate(ZEL22) + Theta31*complexconjugate(ZEL23))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL21) + Theta22*complexconjugate(ZEL22) + Theta32*complexconjugate(ZEL23))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL21) + Theta23*complexconjugate(ZEL22) + Theta33*complexconjugate(ZEL23))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_287 = Coupling(name = 'GC_287',
	 value = '-1*complex(0,1)*(ZER21*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon21) + ZUR33*complexconjugate(Upsilon31)) + ZER22*(ZUR31*complexconjugate(Upsilon12) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon32)) + ZER23*(ZUR31*complexconjugate(Upsilon13) + ZUR32*complexconjugate(Upsilon23) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {'QED':1} ) 
 
GC_288 = Coupling(name = 'GC_288',
	 value = '1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_289 = Coupling(name = 'GC_289',
	 value = '-1*complex(0,1)*(ZER31*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon21) + ZUR13*complexconjugate(Upsilon31)) + ZER32*(ZUR11*complexconjugate(Upsilon12) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon32)) + ZER33*(ZUR11*complexconjugate(Upsilon13) + ZUR12*complexconjugate(Upsilon23) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {'QED':1} ) 
 
GC_290 = Coupling(name = 'GC_290',
	 value = '1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL11) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL12) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_291 = Coupling(name = 'GC_291',
	 value = '-1*complex(0,1)*(ZER31*(ZUR11*complexconjugate(Upsilon11) + ZUR12*complexconjugate(Upsilon21) + ZUR13*complexconjugate(Upsilon31)) + ZER32*(ZUR11*complexconjugate(Upsilon12) + ZUR12*complexconjugate(Upsilon22) + ZUR13*complexconjugate(Upsilon32)) + ZER33*(ZUR11*complexconjugate(Upsilon13) + ZUR12*complexconjugate(Upsilon23) + ZUR13*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {'QED':1} ) 
 
GC_292 = Coupling(name = 'GC_292',
	 value = '1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_293 = Coupling(name = 'GC_293',
	 value = '-1*complex(0,1)*(ZER31*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon21) + ZUR23*complexconjugate(Upsilon31)) + ZER32*(ZUR21*complexconjugate(Upsilon12) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon32)) + ZER33*(ZUR21*complexconjugate(Upsilon13) + ZUR22*complexconjugate(Upsilon23) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {'QED':1} ) 
 
GC_294 = Coupling(name = 'GC_294',
	 value = '1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL21) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL22) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_295 = Coupling(name = 'GC_295',
	 value = '-1*complex(0,1)*(ZER31*(ZUR21*complexconjugate(Upsilon11) + ZUR22*complexconjugate(Upsilon21) + ZUR23*complexconjugate(Upsilon31)) + ZER32*(ZUR21*complexconjugate(Upsilon12) + ZUR22*complexconjugate(Upsilon22) + ZUR23*complexconjugate(Upsilon32)) + ZER33*(ZUR21*complexconjugate(Upsilon13) + ZUR22*complexconjugate(Upsilon23) + ZUR23*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {'QED':1} ) 
 
GC_296 = Coupling(name = 'GC_296',
	 value = '1*complex(0,1)*complexconjugate(ZH11)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_297 = Coupling(name = 'GC_297',
	 value = '-1*complex(0,1)*(ZER31*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon21) + ZUR33*complexconjugate(Upsilon31)) + ZER32*(ZUR31*complexconjugate(Upsilon12) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon32)) + ZER33*(ZUR31*complexconjugate(Upsilon13) + ZUR32*complexconjugate(Upsilon23) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH11)', 
	 order = {'QED':1} ) 
 
GC_298 = Coupling(name = 'GC_298',
	 value = '1*complex(0,1)*complexconjugate(ZH21)*((Theta11*complexconjugate(ZEL31) + Theta21*complexconjugate(ZEL32) + Theta31*complexconjugate(ZEL33))*complexconjugate(ZUL31) + (Theta12*complexconjugate(ZEL31) + Theta22*complexconjugate(ZEL32) + Theta32*complexconjugate(ZEL33))*complexconjugate(ZUL32) + (Theta13*complexconjugate(ZEL31) + Theta23*complexconjugate(ZEL32) + Theta33*complexconjugate(ZEL33))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_299 = Coupling(name = 'GC_299',
	 value = '-1*complex(0,1)*(ZER31*(ZUR31*complexconjugate(Upsilon11) + ZUR32*complexconjugate(Upsilon21) + ZUR33*complexconjugate(Upsilon31)) + ZER32*(ZUR31*complexconjugate(Upsilon12) + ZUR32*complexconjugate(Upsilon22) + ZUR33*complexconjugate(Upsilon32)) + ZER33*(ZUR31*complexconjugate(Upsilon13) + ZUR32*complexconjugate(Upsilon23) + ZUR33*complexconjugate(Upsilon33)))*complexconjugate(ZH21)', 
	 order = {'QED':1} ) 
 
GC_300 = Coupling(name = 'GC_300',
	 value = '(1*complex(0,1)*((CW111*complexconjugate(ZEL11) + CW121*complexconjugate(ZEL12) + CW131*complexconjugate(ZEL13))*complexconjugate(ZM11) + (CW112*complexconjugate(ZEL11) + CW122*complexconjugate(ZEL12) + CW132*complexconjugate(ZEL13))*complexconjugate(ZM12) + (CW113*complexconjugate(ZEL11) + CW123*complexconjugate(ZEL12) + CW133*complexconjugate(ZEL13))*complexconjugate(ZM13) + complexconjugate(ZEL11)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + complexconjugate(ZEL12)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + complexconjugate(ZEL13)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_301 = Coupling(name = 'GC_301',
	 value = '-1*complex(0,1)*(ZM11*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZM12*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZM13*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))', 
	 order = {'QED':1} ) 
 
GC_302 = Coupling(name = 'GC_302',
	 value = '(1*complex(0,1)*((CW111*complexconjugate(ZEL21) + CW121*complexconjugate(ZEL22) + CW131*complexconjugate(ZEL23))*complexconjugate(ZM11) + (CW112*complexconjugate(ZEL21) + CW122*complexconjugate(ZEL22) + CW132*complexconjugate(ZEL23))*complexconjugate(ZM12) + (CW113*complexconjugate(ZEL21) + CW123*complexconjugate(ZEL22) + CW133*complexconjugate(ZEL23))*complexconjugate(ZM13) + complexconjugate(ZEL21)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + complexconjugate(ZEL22)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + complexconjugate(ZEL23)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_303 = Coupling(name = 'GC_303',
	 value = '-1*complex(0,1)*(ZM11*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZM12*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZM13*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))', 
	 order = {'QED':1} ) 
 
GC_304 = Coupling(name = 'GC_304',
	 value = '(1*complex(0,1)*((CW111*complexconjugate(ZEL31) + CW121*complexconjugate(ZEL32) + CW131*complexconjugate(ZEL33))*complexconjugate(ZM11) + (CW112*complexconjugate(ZEL31) + CW122*complexconjugate(ZEL32) + CW132*complexconjugate(ZEL33))*complexconjugate(ZM12) + (CW113*complexconjugate(ZEL31) + CW123*complexconjugate(ZEL32) + CW133*complexconjugate(ZEL33))*complexconjugate(ZM13) + complexconjugate(ZEL31)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + complexconjugate(ZEL32)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + complexconjugate(ZEL33)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_305 = Coupling(name = 'GC_305',
	 value = '-1*complex(0,1)*(ZM11*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZM12*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZM13*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))', 
	 order = {'QED':1} ) 
 
GC_306 = Coupling(name = 'GC_306',
	 value = '(1*complex(0,1)*((CW111*complexconjugate(ZEL11) + CW121*complexconjugate(ZEL12) + CW131*complexconjugate(ZEL13))*complexconjugate(ZM21) + (CW112*complexconjugate(ZEL11) + CW122*complexconjugate(ZEL12) + CW132*complexconjugate(ZEL13))*complexconjugate(ZM22) + (CW113*complexconjugate(ZEL11) + CW123*complexconjugate(ZEL12) + CW133*complexconjugate(ZEL13))*complexconjugate(ZM23) + complexconjugate(ZEL11)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZEL12)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZEL13)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_307 = Coupling(name = 'GC_307',
	 value = '-1*complex(0,1)*(ZM21*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZM22*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZM23*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))', 
	 order = {'QED':1} ) 
 
GC_308 = Coupling(name = 'GC_308',
	 value = '(1*complex(0,1)*((CW111*complexconjugate(ZEL21) + CW121*complexconjugate(ZEL22) + CW131*complexconjugate(ZEL23))*complexconjugate(ZM21) + (CW112*complexconjugate(ZEL21) + CW122*complexconjugate(ZEL22) + CW132*complexconjugate(ZEL23))*complexconjugate(ZM22) + (CW113*complexconjugate(ZEL21) + CW123*complexconjugate(ZEL22) + CW133*complexconjugate(ZEL23))*complexconjugate(ZM23) + complexconjugate(ZEL21)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZEL22)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZEL23)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_309 = Coupling(name = 'GC_309',
	 value = '-1*complex(0,1)*(ZM21*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZM22*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZM23*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))', 
	 order = {'QED':1} ) 
 
GC_310 = Coupling(name = 'GC_310',
	 value = '(1*complex(0,1)*((CW111*complexconjugate(ZEL31) + CW121*complexconjugate(ZEL32) + CW131*complexconjugate(ZEL33))*complexconjugate(ZM21) + (CW112*complexconjugate(ZEL31) + CW122*complexconjugate(ZEL32) + CW132*complexconjugate(ZEL33))*complexconjugate(ZM22) + (CW113*complexconjugate(ZEL31) + CW123*complexconjugate(ZEL32) + CW133*complexconjugate(ZEL33))*complexconjugate(ZM23) + complexconjugate(ZEL31)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZEL32)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZEL33)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_311 = Coupling(name = 'GC_311',
	 value = '-1*complex(0,1)*(ZM21*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZM22*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZM23*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))', 
	 order = {'QED':1} ) 
 
GC_312 = Coupling(name = 'GC_312',
	 value = '(1*complex(0,1)*((CW111*complexconjugate(ZEL11) + CW121*complexconjugate(ZEL12) + CW131*complexconjugate(ZEL13))*complexconjugate(ZM31) + (CW112*complexconjugate(ZEL11) + CW122*complexconjugate(ZEL12) + CW132*complexconjugate(ZEL13))*complexconjugate(ZM32) + (CW113*complexconjugate(ZEL11) + CW123*complexconjugate(ZEL12) + CW133*complexconjugate(ZEL13))*complexconjugate(ZM33) + complexconjugate(ZEL11)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZEL12)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZEL13)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_313 = Coupling(name = 'GC_313',
	 value = '-1*complex(0,1)*(ZM31*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZM32*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZM33*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33)))', 
	 order = {'QED':1} ) 
 
GC_314 = Coupling(name = 'GC_314',
	 value = '(1*complex(0,1)*((CW111*complexconjugate(ZEL21) + CW121*complexconjugate(ZEL22) + CW131*complexconjugate(ZEL23))*complexconjugate(ZM31) + (CW112*complexconjugate(ZEL21) + CW122*complexconjugate(ZEL22) + CW132*complexconjugate(ZEL23))*complexconjugate(ZM32) + (CW113*complexconjugate(ZEL21) + CW123*complexconjugate(ZEL22) + CW133*complexconjugate(ZEL23))*complexconjugate(ZM33) + complexconjugate(ZEL21)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZEL22)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZEL23)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_315 = Coupling(name = 'GC_315',
	 value = '-1*complex(0,1)*(ZM31*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZM32*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZM33*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33)))', 
	 order = {'QED':1} ) 
 
GC_316 = Coupling(name = 'GC_316',
	 value = '(1*complex(0,1)*((CW111*complexconjugate(ZEL31) + CW121*complexconjugate(ZEL32) + CW131*complexconjugate(ZEL33))*complexconjugate(ZM31) + (CW112*complexconjugate(ZEL31) + CW122*complexconjugate(ZEL32) + CW132*complexconjugate(ZEL33))*complexconjugate(ZM32) + (CW113*complexconjugate(ZEL31) + CW123*complexconjugate(ZEL32) + CW133*complexconjugate(ZEL33))*complexconjugate(ZM33) + complexconjugate(ZEL31)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZEL32)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZEL33)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_317 = Coupling(name = 'GC_317',
	 value = '-1*complex(0,1)*(ZM31*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZM32*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZM33*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33)))', 
	 order = {'QED':1} ) 
 
GC_318 = Coupling(name = 'GC_318',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL11)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_319 = Coupling(name = 'GC_319',
	 value = '(-1*complex(0,1)*(ZEL11*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL12*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL13*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_320 = Coupling(name = 'GC_320',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL21)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_321 = Coupling(name = 'GC_321',
	 value = '(-1*complex(0,1)*(ZEL11*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL12*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL13*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_322 = Coupling(name = 'GC_322',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL31)*(ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_323 = Coupling(name = 'GC_323',
	 value = '(-1*complex(0,1)*(ZEL11*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL12*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL13*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_324 = Coupling(name = 'GC_324',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL11)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_325 = Coupling(name = 'GC_325',
	 value = '(-1*complex(0,1)*(ZEL21*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL22*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL23*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_326 = Coupling(name = 'GC_326',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL21)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_327 = Coupling(name = 'GC_327',
	 value = '(-1*complex(0,1)*(ZEL21*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL22*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL23*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_328 = Coupling(name = 'GC_328',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL31)*(ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_329 = Coupling(name = 'GC_329',
	 value = '(-1*complex(0,1)*(ZEL21*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL22*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL23*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_330 = Coupling(name = 'GC_330',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL11)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL12)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL13)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_331 = Coupling(name = 'GC_331',
	 value = '(-1*complex(0,1)*(ZEL31*(ZER11*complexconjugate(ye11) + ZER12*complexconjugate(ye21) + ZER13*complexconjugate(ye31)) + ZEL32*(ZER11*complexconjugate(ye12) + ZER12*complexconjugate(ye22) + ZER13*complexconjugate(ye32)) + ZEL33*(ZER11*complexconjugate(ye13) + ZER12*complexconjugate(ye23) + ZER13*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_332 = Coupling(name = 'GC_332',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL21)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL22)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL23)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_333 = Coupling(name = 'GC_333',
	 value = '(-1*complex(0,1)*(ZEL31*(ZER21*complexconjugate(ye11) + ZER22*complexconjugate(ye21) + ZER23*complexconjugate(ye31)) + ZEL32*(ZER21*complexconjugate(ye12) + ZER22*complexconjugate(ye22) + ZER23*complexconjugate(ye32)) + ZEL33*(ZER21*complexconjugate(ye13) + ZER22*complexconjugate(ye23) + ZER23*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_334 = Coupling(name = 'GC_334',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL31)*(ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33)) + complexconjugate(ZEL32)*(ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33)) + complexconjugate(ZEL33)*(ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_335 = Coupling(name = 'GC_335',
	 value = '(-1*complex(0,1)*(ZEL31*(ZER31*complexconjugate(ye11) + ZER32*complexconjugate(ye21) + ZER33*complexconjugate(ye31)) + ZEL32*(ZER31*complexconjugate(ye12) + ZER32*complexconjugate(ye22) + ZER33*complexconjugate(ye32)) + ZEL33*(ZER31*complexconjugate(ye13) + ZER32*complexconjugate(ye23) + ZER33*complexconjugate(ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_336 = Coupling(name = 'GC_336',
	 value = '-1*complex(0,1)*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZEL11) + Omega21*complexconjugate(ZEL12) + Omega31*complexconjugate(ZEL13)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZEL11) + Omega22*complexconjugate(ZEL12) + Omega32*complexconjugate(ZEL13)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZEL11) + Omega23*complexconjugate(ZEL12) + Omega33*complexconjugate(ZEL13)))', 
	 order = {'QED':1} ) 
 
GC_337 = Coupling(name = 'GC_337',
	 value = '-1*complex(0,1)*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZEL21) + Omega21*complexconjugate(ZEL22) + Omega31*complexconjugate(ZEL23)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZEL21) + Omega22*complexconjugate(ZEL22) + Omega32*complexconjugate(ZEL23)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZEL21) + Omega23*complexconjugate(ZEL22) + Omega33*complexconjugate(ZEL23)))', 
	 order = {'QED':1} ) 
 
GC_338 = Coupling(name = 'GC_338',
	 value = '-1*complex(0,1)*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZEL31) + Omega21*complexconjugate(ZEL32) + Omega31*complexconjugate(ZEL33)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZEL31) + Omega22*complexconjugate(ZEL32) + Omega32*complexconjugate(ZEL33)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZEL31) + Omega23*complexconjugate(ZEL32) + Omega33*complexconjugate(ZEL33)))', 
	 order = {'QED':1} ) 
 
GC_339 = Coupling(name = 'GC_339',
	 value = '-1*complex(0,1)*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZEL11) + Omega21*complexconjugate(ZEL12) + Omega31*complexconjugate(ZEL13)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZEL11) + Omega22*complexconjugate(ZEL12) + Omega32*complexconjugate(ZEL13)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZEL11) + Omega23*complexconjugate(ZEL12) + Omega33*complexconjugate(ZEL13)))', 
	 order = {'QED':1} ) 
 
GC_340 = Coupling(name = 'GC_340',
	 value = '-1*complex(0,1)*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZEL21) + Omega21*complexconjugate(ZEL22) + Omega31*complexconjugate(ZEL23)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZEL21) + Omega22*complexconjugate(ZEL22) + Omega32*complexconjugate(ZEL23)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZEL21) + Omega23*complexconjugate(ZEL22) + Omega33*complexconjugate(ZEL23)))', 
	 order = {'QED':1} ) 
 
GC_341 = Coupling(name = 'GC_341',
	 value = '-1*complex(0,1)*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZEL31) + Omega21*complexconjugate(ZEL32) + Omega31*complexconjugate(ZEL33)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZEL31) + Omega22*complexconjugate(ZEL32) + Omega32*complexconjugate(ZEL33)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZEL31) + Omega23*complexconjugate(ZEL32) + Omega33*complexconjugate(ZEL33)))', 
	 order = {'QED':1} ) 
 
GC_342 = Coupling(name = 'GC_342',
	 value = '-1*complex(0,1)*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZEL11) + Omega21*complexconjugate(ZEL12) + Omega31*complexconjugate(ZEL13)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZEL11) + Omega22*complexconjugate(ZEL12) + Omega32*complexconjugate(ZEL13)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZEL11) + Omega23*complexconjugate(ZEL12) + Omega33*complexconjugate(ZEL13)))', 
	 order = {'QED':1} ) 
 
GC_343 = Coupling(name = 'GC_343',
	 value = '-1*complex(0,1)*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZEL21) + Omega21*complexconjugate(ZEL22) + Omega31*complexconjugate(ZEL23)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZEL21) + Omega22*complexconjugate(ZEL22) + Omega32*complexconjugate(ZEL23)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZEL21) + Omega23*complexconjugate(ZEL22) + Omega33*complexconjugate(ZEL23)))', 
	 order = {'QED':1} ) 
 
GC_344 = Coupling(name = 'GC_344',
	 value = '-1*complex(0,1)*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZEL31) + Omega21*complexconjugate(ZEL32) + Omega31*complexconjugate(ZEL33)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZEL31) + Omega22*complexconjugate(ZEL32) + Omega32*complexconjugate(ZEL33)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZEL31) + Omega23*complexconjugate(ZEL32) + Omega33*complexconjugate(ZEL33)))', 
	 order = {'QED':1} ) 
 
GC_345 = Coupling(name = 'GC_345',
	 value = '(-1*complex(0,1)*(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_346 = Coupling(name = 'GC_346',
	 value = '(-1*complex(0,1)*(ZUL11*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL12*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL13*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_347 = Coupling(name = 'GC_347',
	 value = '(-1*complex(0,1)*(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_348 = Coupling(name = 'GC_348',
	 value = '(-1*complex(0,1)*(ZUL11*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL12*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL13*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_349 = Coupling(name = 'GC_349',
	 value = '(-1*complex(0,1)*(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR11) + yu21*complexconjugate(ZUR12) + yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR11) + yu22*complexconjugate(ZUR12) + yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR11) + yu23*complexconjugate(ZUR12) + yu33*complexconjugate(ZUR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_350 = Coupling(name = 'GC_350',
	 value = '(-1*complex(0,1)*(ZUL11*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL12*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL13*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_351 = Coupling(name = 'GC_351',
	 value = '(-1*complex(0,1)*(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_352 = Coupling(name = 'GC_352',
	 value = '(-1*complex(0,1)*(ZUL21*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL22*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL23*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_353 = Coupling(name = 'GC_353',
	 value = '(-1*complex(0,1)*(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_354 = Coupling(name = 'GC_354',
	 value = '(-1*complex(0,1)*(ZUL21*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL22*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL23*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_355 = Coupling(name = 'GC_355',
	 value = '(-1*complex(0,1)*(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR21) + yu21*complexconjugate(ZUR22) + yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR21) + yu22*complexconjugate(ZUR22) + yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR21) + yu23*complexconjugate(ZUR22) + yu33*complexconjugate(ZUR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_356 = Coupling(name = 'GC_356',
	 value = '(-1*complex(0,1)*(ZUL21*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL22*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL23*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_357 = Coupling(name = 'GC_357',
	 value = '(-1*complex(0,1)*(complexconjugate(ZUL11)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL12)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL13)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_358 = Coupling(name = 'GC_358',
	 value = '(-1*complex(0,1)*(ZUL31*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZUL32*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZUL33*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_359 = Coupling(name = 'GC_359',
	 value = '(-1*complex(0,1)*(complexconjugate(ZUL21)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL22)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL23)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_360 = Coupling(name = 'GC_360',
	 value = '(-1*complex(0,1)*(ZUL31*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZUL32*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZUL33*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_361 = Coupling(name = 'GC_361',
	 value = '(-1*complex(0,1)*(complexconjugate(ZUL31)*(yu11*complexconjugate(ZUR31) + yu21*complexconjugate(ZUR32) + yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL32)*(yu12*complexconjugate(ZUR31) + yu22*complexconjugate(ZUR32) + yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL33)*(yu13*complexconjugate(ZUR31) + yu23*complexconjugate(ZUR32) + yu33*complexconjugate(ZUR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_362 = Coupling(name = 'GC_362',
	 value = '(-1*complex(0,1)*(ZUL31*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZUL32*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZUL33*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_363 = Coupling(name = 'GC_363',
	 value = '-1*complex(0,1)*((yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13))*complexconjugate(ZUL11) + (yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13))*complexconjugate(ZUL12) + (yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_364 = Coupling(name = 'GC_364',
	 value = '1*complex(0,1)*(ZDL11*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZDL12*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZDL13*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))', 
	 order = {'QED':1} ) 
 
GC_365 = Coupling(name = 'GC_365',
	 value = '-1*complex(0,1)*((yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13))*complexconjugate(ZUL21) + (yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13))*complexconjugate(ZUL22) + (yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_366 = Coupling(name = 'GC_366',
	 value = '1*complex(0,1)*(ZDL11*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZDL12*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZDL13*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))', 
	 order = {'QED':1} ) 
 
GC_367 = Coupling(name = 'GC_367',
	 value = '-1*complex(0,1)*((yd11*complexconjugate(ZDR11) + yd21*complexconjugate(ZDR12) + yd31*complexconjugate(ZDR13))*complexconjugate(ZUL31) + (yd12*complexconjugate(ZDR11) + yd22*complexconjugate(ZDR12) + yd32*complexconjugate(ZDR13))*complexconjugate(ZUL32) + (yd13*complexconjugate(ZDR11) + yd23*complexconjugate(ZDR12) + yd33*complexconjugate(ZDR13))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_368 = Coupling(name = 'GC_368',
	 value = '1*complex(0,1)*(ZDL11*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZDL12*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZDL13*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))', 
	 order = {'QED':1} ) 
 
GC_369 = Coupling(name = 'GC_369',
	 value = '-1*complex(0,1)*((yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23))*complexconjugate(ZUL11) + (yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23))*complexconjugate(ZUL12) + (yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_370 = Coupling(name = 'GC_370',
	 value = '1*complex(0,1)*(ZDL21*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZDL22*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZDL23*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))', 
	 order = {'QED':1} ) 
 
GC_371 = Coupling(name = 'GC_371',
	 value = '-1*complex(0,1)*((yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23))*complexconjugate(ZUL21) + (yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23))*complexconjugate(ZUL22) + (yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_372 = Coupling(name = 'GC_372',
	 value = '1*complex(0,1)*(ZDL21*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZDL22*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZDL23*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))', 
	 order = {'QED':1} ) 
 
GC_373 = Coupling(name = 'GC_373',
	 value = '-1*complex(0,1)*((yd11*complexconjugate(ZDR21) + yd21*complexconjugate(ZDR22) + yd31*complexconjugate(ZDR23))*complexconjugate(ZUL31) + (yd12*complexconjugate(ZDR21) + yd22*complexconjugate(ZDR22) + yd32*complexconjugate(ZDR23))*complexconjugate(ZUL32) + (yd13*complexconjugate(ZDR21) + yd23*complexconjugate(ZDR22) + yd33*complexconjugate(ZDR23))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_374 = Coupling(name = 'GC_374',
	 value = '1*complex(0,1)*(ZDL21*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZDL22*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZDL23*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))', 
	 order = {'QED':1} ) 
 
GC_375 = Coupling(name = 'GC_375',
	 value = '-1*complex(0,1)*((yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33))*complexconjugate(ZUL11) + (yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33))*complexconjugate(ZUL12) + (yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_376 = Coupling(name = 'GC_376',
	 value = '1*complex(0,1)*(ZDL31*(ZUR11*complexconjugate(yu11) + ZUR12*complexconjugate(yu21) + ZUR13*complexconjugate(yu31)) + ZDL32*(ZUR11*complexconjugate(yu12) + ZUR12*complexconjugate(yu22) + ZUR13*complexconjugate(yu32)) + ZDL33*(ZUR11*complexconjugate(yu13) + ZUR12*complexconjugate(yu23) + ZUR13*complexconjugate(yu33)))', 
	 order = {'QED':1} ) 
 
GC_377 = Coupling(name = 'GC_377',
	 value = '-1*complex(0,1)*((yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33))*complexconjugate(ZUL21) + (yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33))*complexconjugate(ZUL22) + (yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_378 = Coupling(name = 'GC_378',
	 value = '1*complex(0,1)*(ZDL31*(ZUR21*complexconjugate(yu11) + ZUR22*complexconjugate(yu21) + ZUR23*complexconjugate(yu31)) + ZDL32*(ZUR21*complexconjugate(yu12) + ZUR22*complexconjugate(yu22) + ZUR23*complexconjugate(yu32)) + ZDL33*(ZUR21*complexconjugate(yu13) + ZUR22*complexconjugate(yu23) + ZUR23*complexconjugate(yu33)))', 
	 order = {'QED':1} ) 
 
GC_379 = Coupling(name = 'GC_379',
	 value = '-1*complex(0,1)*((yd11*complexconjugate(ZDR31) + yd21*complexconjugate(ZDR32) + yd31*complexconjugate(ZDR33))*complexconjugate(ZUL31) + (yd12*complexconjugate(ZDR31) + yd22*complexconjugate(ZDR32) + yd32*complexconjugate(ZDR33))*complexconjugate(ZUL32) + (yd13*complexconjugate(ZDR31) + yd23*complexconjugate(ZDR32) + yd33*complexconjugate(ZDR33))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_380 = Coupling(name = 'GC_380',
	 value = '1*complex(0,1)*(ZDL31*(ZUR31*complexconjugate(yu11) + ZUR32*complexconjugate(yu21) + ZUR33*complexconjugate(yu31)) + ZDL32*(ZUR31*complexconjugate(yu12) + ZUR32*complexconjugate(yu22) + ZUR33*complexconjugate(yu32)) + ZDL33*(ZUR31*complexconjugate(yu13) + ZUR32*complexconjugate(yu23) + ZUR33*complexconjugate(yu33)))', 
	 order = {'QED':1} ) 
 
GC_381 = Coupling(name = 'GC_381',
	 value = '(-1*complex(0,1)*(2*complexconjugate(ZM11)*(CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13)) + 2*complexconjugate(ZM12)*(CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13)) + 2*complexconjugate(ZM13)*(CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_382 = Coupling(name = 'GC_382',
	 value = '(-1*complex(0,1)*(2*ZM11*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + 2*ZM12*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + 2*ZM13*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_383 = Coupling(name = 'GC_383',
	 value = '(-1*complex(0,1)*((CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13))*complexconjugate(ZM21) + (CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13))*complexconjugate(ZM22) + (CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))*complexconjugate(ZM23) + complexconjugate(ZM11)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + complexconjugate(ZM12)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + complexconjugate(ZM13)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_384 = Coupling(name = 'GC_384',
	 value = '(-1*complex(0,1)*(ZM21*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM11*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM12*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)) + ZM13*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_385 = Coupling(name = 'GC_385',
	 value = '(-1*complex(0,1)*((CW111*complexconjugate(ZM11) + CW121*complexconjugate(ZM12) + CW131*complexconjugate(ZM13))*complexconjugate(ZM31) + (CW112*complexconjugate(ZM11) + CW122*complexconjugate(ZM12) + CW132*complexconjugate(ZM13))*complexconjugate(ZM32) + (CW113*complexconjugate(ZM11) + CW123*complexconjugate(ZM12) + CW133*complexconjugate(ZM13))*complexconjugate(ZM33) + complexconjugate(ZM11)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZM12)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZM13)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_386 = Coupling(name = 'GC_386',
	 value = '(-1*complex(0,1)*(ZM31*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM11*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM12*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133)) + ZM13*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_387 = Coupling(name = 'GC_387',
	 value = '(-1*complex(0,1)*(2*complexconjugate(ZM21)*(CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23)) + 2*complexconjugate(ZM22)*(CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23)) + 2*complexconjugate(ZM23)*(CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_388 = Coupling(name = 'GC_388',
	 value = '(-1*complex(0,1)*(2*ZM21*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + 2*ZM22*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + 2*ZM23*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_389 = Coupling(name = 'GC_389',
	 value = '(-1*complex(0,1)*((CW111*complexconjugate(ZM21) + CW121*complexconjugate(ZM22) + CW131*complexconjugate(ZM23))*complexconjugate(ZM31) + (CW112*complexconjugate(ZM21) + CW122*complexconjugate(ZM22) + CW132*complexconjugate(ZM23))*complexconjugate(ZM32) + (CW113*complexconjugate(ZM21) + CW123*complexconjugate(ZM22) + CW133*complexconjugate(ZM23))*complexconjugate(ZM33) + complexconjugate(ZM21)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + complexconjugate(ZM22)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + complexconjugate(ZM23)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_390 = Coupling(name = 'GC_390',
	 value = '(-1*complex(0,1)*(ZM31*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM21*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM22*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133)) + ZM23*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_391 = Coupling(name = 'GC_391',
	 value = '(-1*complex(0,1)*(2*complexconjugate(ZM31)*(CW111*complexconjugate(ZM31) + CW121*complexconjugate(ZM32) + CW131*complexconjugate(ZM33)) + 2*complexconjugate(ZM32)*(CW112*complexconjugate(ZM31) + CW122*complexconjugate(ZM32) + CW132*complexconjugate(ZM33)) + 2*complexconjugate(ZM33)*(CW113*complexconjugate(ZM31) + CW123*complexconjugate(ZM32) + CW133*complexconjugate(ZM33))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_392 = Coupling(name = 'GC_392',
	 value = '(-1*complex(0,1)*(2*ZM31*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + 2*ZM32*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + 2*ZM33*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/vvSM', 
	 order = {'QED':1} ) 
 
GC_393 = Coupling(name = 'GC_393',
	 value = '1*complex(0,1)*ZH12*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_394 = Coupling(name = 'GC_394',
	 value = '-1*complex(0,1)*ZH11*(ZDL11*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL12*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL13*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_395 = Coupling(name = 'GC_395',
	 value = '1*complex(0,1)*ZH22*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_396 = Coupling(name = 'GC_396',
	 value = '-1*complex(0,1)*ZH21*(ZDL11*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL12*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL13*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_397 = Coupling(name = 'GC_397',
	 value = '1*complex(0,1)*ZH12*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_398 = Coupling(name = 'GC_398',
	 value = '-1*complex(0,1)*ZH11*(ZDL11*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL12*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL13*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_399 = Coupling(name = 'GC_399',
	 value = '1*complex(0,1)*ZH22*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_400 = Coupling(name = 'GC_400',
	 value = '-1*complex(0,1)*ZH21*(ZDL11*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL12*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL13*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_401 = Coupling(name = 'GC_401',
	 value = '1*complex(0,1)*ZH12*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_402 = Coupling(name = 'GC_402',
	 value = '-1*complex(0,1)*ZH11*(ZDL11*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL12*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL13*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_403 = Coupling(name = 'GC_403',
	 value = '1*complex(0,1)*ZH22*(complexconjugate(ZDR11)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR12)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR13)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_404 = Coupling(name = 'GC_404',
	 value = '-1*complex(0,1)*ZH21*(ZDL11*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL12*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL13*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_405 = Coupling(name = 'GC_405',
	 value = '1*complex(0,1)*ZH12*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_406 = Coupling(name = 'GC_406',
	 value = '-1*complex(0,1)*ZH11*(ZDL21*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL22*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL23*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_407 = Coupling(name = 'GC_407',
	 value = '1*complex(0,1)*ZH22*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_408 = Coupling(name = 'GC_408',
	 value = '-1*complex(0,1)*ZH21*(ZDL21*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL22*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL23*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_409 = Coupling(name = 'GC_409',
	 value = '1*complex(0,1)*ZH12*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_410 = Coupling(name = 'GC_410',
	 value = '-1*complex(0,1)*ZH11*(ZDL21*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL22*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL23*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_411 = Coupling(name = 'GC_411',
	 value = '1*complex(0,1)*ZH22*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_412 = Coupling(name = 'GC_412',
	 value = '-1*complex(0,1)*ZH21*(ZDL21*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL22*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL23*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_413 = Coupling(name = 'GC_413',
	 value = '1*complex(0,1)*ZH12*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_414 = Coupling(name = 'GC_414',
	 value = '-1*complex(0,1)*ZH11*(ZDL21*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL22*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL23*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_415 = Coupling(name = 'GC_415',
	 value = '1*complex(0,1)*ZH22*(complexconjugate(ZDR21)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR22)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR23)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_416 = Coupling(name = 'GC_416',
	 value = '-1*complex(0,1)*ZH21*(ZDL21*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL22*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL23*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_417 = Coupling(name = 'GC_417',
	 value = '1*complex(0,1)*ZH12*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_418 = Coupling(name = 'GC_418',
	 value = '-1*complex(0,1)*ZH11*(ZDL31*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL32*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL33*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_419 = Coupling(name = 'GC_419',
	 value = '1*complex(0,1)*ZH22*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM11) + Omega21*complexconjugate(ZM12) + Omega31*complexconjugate(ZM13)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM11) + Omega22*complexconjugate(ZM12) + Omega32*complexconjugate(ZM13)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM11) + Omega23*complexconjugate(ZM12) + Omega33*complexconjugate(ZM13)))', 
	 order = {'QED':1} ) 
 
GC_420 = Coupling(name = 'GC_420',
	 value = '-1*complex(0,1)*ZH21*(ZDL31*(ZM11*complexconjugate(Theta11) + ZM12*complexconjugate(Theta21) + ZM13*complexconjugate(Theta31)) + ZDL32*(ZM11*complexconjugate(Theta12) + ZM12*complexconjugate(Theta22) + ZM13*complexconjugate(Theta32)) + ZDL33*(ZM11*complexconjugate(Theta13) + ZM12*complexconjugate(Theta23) + ZM13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_421 = Coupling(name = 'GC_421',
	 value = '1*complex(0,1)*ZH12*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_422 = Coupling(name = 'GC_422',
	 value = '-1*complex(0,1)*ZH11*(ZDL31*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL32*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL33*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_423 = Coupling(name = 'GC_423',
	 value = '1*complex(0,1)*ZH22*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM21) + Omega21*complexconjugate(ZM22) + Omega31*complexconjugate(ZM23)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM21) + Omega22*complexconjugate(ZM22) + Omega32*complexconjugate(ZM23)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM21) + Omega23*complexconjugate(ZM22) + Omega33*complexconjugate(ZM23)))', 
	 order = {'QED':1} ) 
 
GC_424 = Coupling(name = 'GC_424',
	 value = '-1*complex(0,1)*ZH21*(ZDL31*(ZM21*complexconjugate(Theta11) + ZM22*complexconjugate(Theta21) + ZM23*complexconjugate(Theta31)) + ZDL32*(ZM21*complexconjugate(Theta12) + ZM22*complexconjugate(Theta22) + ZM23*complexconjugate(Theta32)) + ZDL33*(ZM21*complexconjugate(Theta13) + ZM22*complexconjugate(Theta23) + ZM23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_425 = Coupling(name = 'GC_425',
	 value = '1*complex(0,1)*ZH12*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_426 = Coupling(name = 'GC_426',
	 value = '-1*complex(0,1)*ZH11*(ZDL31*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL32*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL33*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_427 = Coupling(name = 'GC_427',
	 value = '1*complex(0,1)*ZH22*(complexconjugate(ZDR31)*(Omega11*complexconjugate(ZM31) + Omega21*complexconjugate(ZM32) + Omega31*complexconjugate(ZM33)) + complexconjugate(ZDR32)*(Omega12*complexconjugate(ZM31) + Omega22*complexconjugate(ZM32) + Omega32*complexconjugate(ZM33)) + complexconjugate(ZDR33)*(Omega13*complexconjugate(ZM31) + Omega23*complexconjugate(ZM32) + Omega33*complexconjugate(ZM33)))', 
	 order = {'QED':1} ) 
 
GC_428 = Coupling(name = 'GC_428',
	 value = '-1*complex(0,1)*ZH21*(ZDL31*(ZM31*complexconjugate(Theta11) + ZM32*complexconjugate(Theta21) + ZM33*complexconjugate(Theta31)) + ZDL32*(ZM31*complexconjugate(Theta12) + ZM32*complexconjugate(Theta22) + ZM33*complexconjugate(Theta32)) + ZDL33*(ZM31*complexconjugate(Theta13) + ZM32*complexconjugate(Theta23) + ZM33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_429 = Coupling(name = 'GC_429',
	 value = '-1*complex(0,1)*((ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13))*complexconjugate(ZM11) + (ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13))*complexconjugate(ZM12) + (ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))*complexconjugate(ZM13))', 
	 order = {'QED':1} ) 
 
GC_430 = Coupling(name = 'GC_430',
	 value = '(1*complex(0,1)*(ZM11*(ZEL11*complexconjugate(CW111) + ZEL12*complexconjugate(CW121) + ZEL13*complexconjugate(CW131)) + ZEL11*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM12*(ZEL11*complexconjugate(CW112) + ZEL12*complexconjugate(CW122) + ZEL13*complexconjugate(CW132)) + ZEL12*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM13*(ZEL11*complexconjugate(CW113) + ZEL12*complexconjugate(CW123) + ZEL13*complexconjugate(CW133)) + ZEL13*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_431 = Coupling(name = 'GC_431',
	 value = '-1*complex(0,1)*((ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13))*complexconjugate(ZM21) + (ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13))*complexconjugate(ZM22) + (ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))*complexconjugate(ZM23))', 
	 order = {'QED':1} ) 
 
GC_432 = Coupling(name = 'GC_432',
	 value = '(1*complex(0,1)*(ZM21*(ZEL11*complexconjugate(CW111) + ZEL12*complexconjugate(CW121) + ZEL13*complexconjugate(CW131)) + ZEL11*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZEL11*complexconjugate(CW112) + ZEL12*complexconjugate(CW122) + ZEL13*complexconjugate(CW132)) + ZEL12*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZEL11*complexconjugate(CW113) + ZEL12*complexconjugate(CW123) + ZEL13*complexconjugate(CW133)) + ZEL13*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_433 = Coupling(name = 'GC_433',
	 value = '-1*complex(0,1)*((ye11*complexconjugate(ZER11) + ye21*complexconjugate(ZER12) + ye31*complexconjugate(ZER13))*complexconjugate(ZM31) + (ye12*complexconjugate(ZER11) + ye22*complexconjugate(ZER12) + ye32*complexconjugate(ZER13))*complexconjugate(ZM32) + (ye13*complexconjugate(ZER11) + ye23*complexconjugate(ZER12) + ye33*complexconjugate(ZER13))*complexconjugate(ZM33))', 
	 order = {'QED':1} ) 
 
GC_434 = Coupling(name = 'GC_434',
	 value = '(1*complex(0,1)*(ZM31*(ZEL11*complexconjugate(CW111) + ZEL12*complexconjugate(CW121) + ZEL13*complexconjugate(CW131)) + ZEL11*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZEL11*complexconjugate(CW112) + ZEL12*complexconjugate(CW122) + ZEL13*complexconjugate(CW132)) + ZEL12*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZEL11*complexconjugate(CW113) + ZEL12*complexconjugate(CW123) + ZEL13*complexconjugate(CW133)) + ZEL13*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_435 = Coupling(name = 'GC_435',
	 value = '-1*complex(0,1)*((ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23))*complexconjugate(ZM11) + (ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23))*complexconjugate(ZM12) + (ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))*complexconjugate(ZM13))', 
	 order = {'QED':1} ) 
 
GC_436 = Coupling(name = 'GC_436',
	 value = '(1*complex(0,1)*(ZM11*(ZEL21*complexconjugate(CW111) + ZEL22*complexconjugate(CW121) + ZEL23*complexconjugate(CW131)) + ZEL21*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM12*(ZEL21*complexconjugate(CW112) + ZEL22*complexconjugate(CW122) + ZEL23*complexconjugate(CW132)) + ZEL22*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM13*(ZEL21*complexconjugate(CW113) + ZEL22*complexconjugate(CW123) + ZEL23*complexconjugate(CW133)) + ZEL23*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_437 = Coupling(name = 'GC_437',
	 value = '-1*complex(0,1)*((ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23))*complexconjugate(ZM21) + (ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23))*complexconjugate(ZM22) + (ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))*complexconjugate(ZM23))', 
	 order = {'QED':1} ) 
 
GC_438 = Coupling(name = 'GC_438',
	 value = '(1*complex(0,1)*(ZM21*(ZEL21*complexconjugate(CW111) + ZEL22*complexconjugate(CW121) + ZEL23*complexconjugate(CW131)) + ZEL21*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZEL21*complexconjugate(CW112) + ZEL22*complexconjugate(CW122) + ZEL23*complexconjugate(CW132)) + ZEL22*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZEL21*complexconjugate(CW113) + ZEL22*complexconjugate(CW123) + ZEL23*complexconjugate(CW133)) + ZEL23*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_439 = Coupling(name = 'GC_439',
	 value = '-1*complex(0,1)*((ye11*complexconjugate(ZER21) + ye21*complexconjugate(ZER22) + ye31*complexconjugate(ZER23))*complexconjugate(ZM31) + (ye12*complexconjugate(ZER21) + ye22*complexconjugate(ZER22) + ye32*complexconjugate(ZER23))*complexconjugate(ZM32) + (ye13*complexconjugate(ZER21) + ye23*complexconjugate(ZER22) + ye33*complexconjugate(ZER23))*complexconjugate(ZM33))', 
	 order = {'QED':1} ) 
 
GC_440 = Coupling(name = 'GC_440',
	 value = '(1*complex(0,1)*(ZM31*(ZEL21*complexconjugate(CW111) + ZEL22*complexconjugate(CW121) + ZEL23*complexconjugate(CW131)) + ZEL21*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZEL21*complexconjugate(CW112) + ZEL22*complexconjugate(CW122) + ZEL23*complexconjugate(CW132)) + ZEL22*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZEL21*complexconjugate(CW113) + ZEL22*complexconjugate(CW123) + ZEL23*complexconjugate(CW133)) + ZEL23*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_441 = Coupling(name = 'GC_441',
	 value = '-1*complex(0,1)*((ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33))*complexconjugate(ZM11) + (ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33))*complexconjugate(ZM12) + (ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))*complexconjugate(ZM13))', 
	 order = {'QED':1} ) 
 
GC_442 = Coupling(name = 'GC_442',
	 value = '(1*complex(0,1)*(ZM11*(ZEL31*complexconjugate(CW111) + ZEL32*complexconjugate(CW121) + ZEL33*complexconjugate(CW131)) + ZEL31*(ZM11*complexconjugate(CW111) + ZM12*complexconjugate(CW121) + ZM13*complexconjugate(CW131)) + ZM12*(ZEL31*complexconjugate(CW112) + ZEL32*complexconjugate(CW122) + ZEL33*complexconjugate(CW132)) + ZEL32*(ZM11*complexconjugate(CW112) + ZM12*complexconjugate(CW122) + ZM13*complexconjugate(CW132)) + ZM13*(ZEL31*complexconjugate(CW113) + ZEL32*complexconjugate(CW123) + ZEL33*complexconjugate(CW133)) + ZEL33*(ZM11*complexconjugate(CW113) + ZM12*complexconjugate(CW123) + ZM13*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_443 = Coupling(name = 'GC_443',
	 value = '-1*complex(0,1)*((ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33))*complexconjugate(ZM21) + (ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33))*complexconjugate(ZM22) + (ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))*complexconjugate(ZM23))', 
	 order = {'QED':1} ) 
 
GC_444 = Coupling(name = 'GC_444',
	 value = '(1*complex(0,1)*(ZM21*(ZEL31*complexconjugate(CW111) + ZEL32*complexconjugate(CW121) + ZEL33*complexconjugate(CW131)) + ZEL31*(ZM21*complexconjugate(CW111) + ZM22*complexconjugate(CW121) + ZM23*complexconjugate(CW131)) + ZM22*(ZEL31*complexconjugate(CW112) + ZEL32*complexconjugate(CW122) + ZEL33*complexconjugate(CW132)) + ZEL32*(ZM21*complexconjugate(CW112) + ZM22*complexconjugate(CW122) + ZM23*complexconjugate(CW132)) + ZM23*(ZEL31*complexconjugate(CW113) + ZEL32*complexconjugate(CW123) + ZEL33*complexconjugate(CW133)) + ZEL33*(ZM21*complexconjugate(CW113) + ZM22*complexconjugate(CW123) + ZM23*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_445 = Coupling(name = 'GC_445',
	 value = '-1*complex(0,1)*((ye11*complexconjugate(ZER31) + ye21*complexconjugate(ZER32) + ye31*complexconjugate(ZER33))*complexconjugate(ZM31) + (ye12*complexconjugate(ZER31) + ye22*complexconjugate(ZER32) + ye32*complexconjugate(ZER33))*complexconjugate(ZM32) + (ye13*complexconjugate(ZER31) + ye23*complexconjugate(ZER32) + ye33*complexconjugate(ZER33))*complexconjugate(ZM33))', 
	 order = {'QED':1} ) 
 
GC_446 = Coupling(name = 'GC_446',
	 value = '(1*complex(0,1)*(ZM31*(ZEL31*complexconjugate(CW111) + ZEL32*complexconjugate(CW121) + ZEL33*complexconjugate(CW131)) + ZEL31*(ZM31*complexconjugate(CW111) + ZM32*complexconjugate(CW121) + ZM33*complexconjugate(CW131)) + ZM32*(ZEL31*complexconjugate(CW112) + ZEL32*complexconjugate(CW122) + ZEL33*complexconjugate(CW132)) + ZEL32*(ZM31*complexconjugate(CW112) + ZM32*complexconjugate(CW122) + ZM33*complexconjugate(CW132)) + ZM33*(ZEL31*complexconjugate(CW113) + ZEL32*complexconjugate(CW123) + ZEL33*complexconjugate(CW133)) + ZEL33*(ZM31*complexconjugate(CW113) + ZM32*complexconjugate(CW123) + ZM33*complexconjugate(CW133))))/(cmath.sqrt(2)*vvSM)', 
	 order = {'QED':1} ) 
 
GC_447 = Coupling(name = 'GC_447',
	 value = '-1*complex(0,1)*ZH11*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR11) + Upsilon21*complexconjugate(ZUR12) + Upsilon31*complexconjugate(ZUR13)) + complexconjugate(ZER12)*(Upsilon12*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon32*complexconjugate(ZUR13)) + complexconjugate(ZER13)*(Upsilon13*complexconjugate(ZUR11) + Upsilon23*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_448 = Coupling(name = 'GC_448',
	 value = '1*complex(0,1)*ZH11*(ZUL11*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL12*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL13*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_449 = Coupling(name = 'GC_449',
	 value = '-1*complex(0,1)*ZH21*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR11) + Upsilon21*complexconjugate(ZUR12) + Upsilon31*complexconjugate(ZUR13)) + complexconjugate(ZER12)*(Upsilon12*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon32*complexconjugate(ZUR13)) + complexconjugate(ZER13)*(Upsilon13*complexconjugate(ZUR11) + Upsilon23*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_450 = Coupling(name = 'GC_450',
	 value = '1*complex(0,1)*ZH21*(ZUL11*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL12*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL13*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_451 = Coupling(name = 'GC_451',
	 value = '-1*complex(0,1)*ZH11*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR21) + Upsilon21*complexconjugate(ZUR22) + Upsilon31*complexconjugate(ZUR23)) + complexconjugate(ZER12)*(Upsilon12*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon32*complexconjugate(ZUR23)) + complexconjugate(ZER13)*(Upsilon13*complexconjugate(ZUR21) + Upsilon23*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_452 = Coupling(name = 'GC_452',
	 value = '1*complex(0,1)*ZH11*(ZUL21*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL22*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL23*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_453 = Coupling(name = 'GC_453',
	 value = '-1*complex(0,1)*ZH21*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR21) + Upsilon21*complexconjugate(ZUR22) + Upsilon31*complexconjugate(ZUR23)) + complexconjugate(ZER12)*(Upsilon12*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon32*complexconjugate(ZUR23)) + complexconjugate(ZER13)*(Upsilon13*complexconjugate(ZUR21) + Upsilon23*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_454 = Coupling(name = 'GC_454',
	 value = '1*complex(0,1)*ZH21*(ZUL21*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL22*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL23*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_455 = Coupling(name = 'GC_455',
	 value = '-1*complex(0,1)*ZH11*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR31) + Upsilon21*complexconjugate(ZUR32) + Upsilon31*complexconjugate(ZUR33)) + complexconjugate(ZER12)*(Upsilon12*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon32*complexconjugate(ZUR33)) + complexconjugate(ZER13)*(Upsilon13*complexconjugate(ZUR31) + Upsilon23*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_456 = Coupling(name = 'GC_456',
	 value = '1*complex(0,1)*ZH11*(ZUL31*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL32*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL33*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_457 = Coupling(name = 'GC_457',
	 value = '-1*complex(0,1)*ZH21*(complexconjugate(ZER11)*(Upsilon11*complexconjugate(ZUR31) + Upsilon21*complexconjugate(ZUR32) + Upsilon31*complexconjugate(ZUR33)) + complexconjugate(ZER12)*(Upsilon12*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon32*complexconjugate(ZUR33)) + complexconjugate(ZER13)*(Upsilon13*complexconjugate(ZUR31) + Upsilon23*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_458 = Coupling(name = 'GC_458',
	 value = '1*complex(0,1)*ZH21*(ZUL31*(ZEL11*complexconjugate(Theta11) + ZEL12*complexconjugate(Theta21) + ZEL13*complexconjugate(Theta31)) + ZUL32*(ZEL11*complexconjugate(Theta12) + ZEL12*complexconjugate(Theta22) + ZEL13*complexconjugate(Theta32)) + ZUL33*(ZEL11*complexconjugate(Theta13) + ZEL12*complexconjugate(Theta23) + ZEL13*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_459 = Coupling(name = 'GC_459',
	 value = '-1*complex(0,1)*ZH11*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR11) + Upsilon21*complexconjugate(ZUR12) + Upsilon31*complexconjugate(ZUR13)) + complexconjugate(ZER22)*(Upsilon12*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon32*complexconjugate(ZUR13)) + complexconjugate(ZER23)*(Upsilon13*complexconjugate(ZUR11) + Upsilon23*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_460 = Coupling(name = 'GC_460',
	 value = '1*complex(0,1)*ZH11*(ZUL11*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL12*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL13*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_461 = Coupling(name = 'GC_461',
	 value = '-1*complex(0,1)*ZH21*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR11) + Upsilon21*complexconjugate(ZUR12) + Upsilon31*complexconjugate(ZUR13)) + complexconjugate(ZER22)*(Upsilon12*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon32*complexconjugate(ZUR13)) + complexconjugate(ZER23)*(Upsilon13*complexconjugate(ZUR11) + Upsilon23*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_462 = Coupling(name = 'GC_462',
	 value = '1*complex(0,1)*ZH21*(ZUL11*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL12*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL13*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_463 = Coupling(name = 'GC_463',
	 value = '-1*complex(0,1)*ZH11*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR21) + Upsilon21*complexconjugate(ZUR22) + Upsilon31*complexconjugate(ZUR23)) + complexconjugate(ZER22)*(Upsilon12*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon32*complexconjugate(ZUR23)) + complexconjugate(ZER23)*(Upsilon13*complexconjugate(ZUR21) + Upsilon23*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_464 = Coupling(name = 'GC_464',
	 value = '1*complex(0,1)*ZH11*(ZUL21*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL22*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL23*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_465 = Coupling(name = 'GC_465',
	 value = '-1*complex(0,1)*ZH21*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR21) + Upsilon21*complexconjugate(ZUR22) + Upsilon31*complexconjugate(ZUR23)) + complexconjugate(ZER22)*(Upsilon12*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon32*complexconjugate(ZUR23)) + complexconjugate(ZER23)*(Upsilon13*complexconjugate(ZUR21) + Upsilon23*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_466 = Coupling(name = 'GC_466',
	 value = '1*complex(0,1)*ZH21*(ZUL21*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL22*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL23*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_467 = Coupling(name = 'GC_467',
	 value = '-1*complex(0,1)*ZH11*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR31) + Upsilon21*complexconjugate(ZUR32) + Upsilon31*complexconjugate(ZUR33)) + complexconjugate(ZER22)*(Upsilon12*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon32*complexconjugate(ZUR33)) + complexconjugate(ZER23)*(Upsilon13*complexconjugate(ZUR31) + Upsilon23*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_468 = Coupling(name = 'GC_468',
	 value = '1*complex(0,1)*ZH11*(ZUL31*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL32*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL33*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_469 = Coupling(name = 'GC_469',
	 value = '-1*complex(0,1)*ZH21*(complexconjugate(ZER21)*(Upsilon11*complexconjugate(ZUR31) + Upsilon21*complexconjugate(ZUR32) + Upsilon31*complexconjugate(ZUR33)) + complexconjugate(ZER22)*(Upsilon12*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon32*complexconjugate(ZUR33)) + complexconjugate(ZER23)*(Upsilon13*complexconjugate(ZUR31) + Upsilon23*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_470 = Coupling(name = 'GC_470',
	 value = '1*complex(0,1)*ZH21*(ZUL31*(ZEL21*complexconjugate(Theta11) + ZEL22*complexconjugate(Theta21) + ZEL23*complexconjugate(Theta31)) + ZUL32*(ZEL21*complexconjugate(Theta12) + ZEL22*complexconjugate(Theta22) + ZEL23*complexconjugate(Theta32)) + ZUL33*(ZEL21*complexconjugate(Theta13) + ZEL22*complexconjugate(Theta23) + ZEL23*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_471 = Coupling(name = 'GC_471',
	 value = '-1*complex(0,1)*ZH11*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR11) + Upsilon21*complexconjugate(ZUR12) + Upsilon31*complexconjugate(ZUR13)) + complexconjugate(ZER32)*(Upsilon12*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon32*complexconjugate(ZUR13)) + complexconjugate(ZER33)*(Upsilon13*complexconjugate(ZUR11) + Upsilon23*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_472 = Coupling(name = 'GC_472',
	 value = '1*complex(0,1)*ZH11*(ZUL11*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL12*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL13*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_473 = Coupling(name = 'GC_473',
	 value = '-1*complex(0,1)*ZH21*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR11) + Upsilon21*complexconjugate(ZUR12) + Upsilon31*complexconjugate(ZUR13)) + complexconjugate(ZER32)*(Upsilon12*complexconjugate(ZUR11) + Upsilon22*complexconjugate(ZUR12) + Upsilon32*complexconjugate(ZUR13)) + complexconjugate(ZER33)*(Upsilon13*complexconjugate(ZUR11) + Upsilon23*complexconjugate(ZUR12) + Upsilon33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_474 = Coupling(name = 'GC_474',
	 value = '1*complex(0,1)*ZH21*(ZUL11*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL12*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL13*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_475 = Coupling(name = 'GC_475',
	 value = '-1*complex(0,1)*ZH11*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR21) + Upsilon21*complexconjugate(ZUR22) + Upsilon31*complexconjugate(ZUR23)) + complexconjugate(ZER32)*(Upsilon12*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon32*complexconjugate(ZUR23)) + complexconjugate(ZER33)*(Upsilon13*complexconjugate(ZUR21) + Upsilon23*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_476 = Coupling(name = 'GC_476',
	 value = '1*complex(0,1)*ZH11*(ZUL21*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL22*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL23*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_477 = Coupling(name = 'GC_477',
	 value = '-1*complex(0,1)*ZH21*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR21) + Upsilon21*complexconjugate(ZUR22) + Upsilon31*complexconjugate(ZUR23)) + complexconjugate(ZER32)*(Upsilon12*complexconjugate(ZUR21) + Upsilon22*complexconjugate(ZUR22) + Upsilon32*complexconjugate(ZUR23)) + complexconjugate(ZER33)*(Upsilon13*complexconjugate(ZUR21) + Upsilon23*complexconjugate(ZUR22) + Upsilon33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_478 = Coupling(name = 'GC_478',
	 value = '1*complex(0,1)*ZH21*(ZUL21*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL22*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL23*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_479 = Coupling(name = 'GC_479',
	 value = '-1*complex(0,1)*ZH11*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR31) + Upsilon21*complexconjugate(ZUR32) + Upsilon31*complexconjugate(ZUR33)) + complexconjugate(ZER32)*(Upsilon12*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon32*complexconjugate(ZUR33)) + complexconjugate(ZER33)*(Upsilon13*complexconjugate(ZUR31) + Upsilon23*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_480 = Coupling(name = 'GC_480',
	 value = '1*complex(0,1)*ZH11*(ZUL31*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL32*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL33*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_481 = Coupling(name = 'GC_481',
	 value = '-1*complex(0,1)*ZH21*(complexconjugate(ZER31)*(Upsilon11*complexconjugate(ZUR31) + Upsilon21*complexconjugate(ZUR32) + Upsilon31*complexconjugate(ZUR33)) + complexconjugate(ZER32)*(Upsilon12*complexconjugate(ZUR31) + Upsilon22*complexconjugate(ZUR32) + Upsilon32*complexconjugate(ZUR33)) + complexconjugate(ZER33)*(Upsilon13*complexconjugate(ZUR31) + Upsilon23*complexconjugate(ZUR32) + Upsilon33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_482 = Coupling(name = 'GC_482',
	 value = '1*complex(0,1)*ZH21*(ZUL31*(ZEL31*complexconjugate(Theta11) + ZEL32*complexconjugate(Theta21) + ZEL33*complexconjugate(Theta31)) + ZUL32*(ZEL31*complexconjugate(Theta12) + ZEL32*complexconjugate(Theta22) + ZEL33*complexconjugate(Theta32)) + ZUL33*(ZEL31*complexconjugate(Theta13) + ZEL32*complexconjugate(Theta23) + ZEL33*complexconjugate(Theta33)))', 
	 order = {'QED':1} ) 
 
GC_483 = Coupling(name = 'GC_483',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_484 = Coupling(name = 'GC_484',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_485 = Coupling(name = 'GC_485',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_486 = Coupling(name = 'GC_486',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_487 = Coupling(name = 'GC_487',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_488 = Coupling(name = 'GC_488',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_489 = Coupling(name = 'GC_489',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) - 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_490 = Coupling(name = 'GC_490',
	 value = '-1./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_491 = Coupling(name = 'GC_491',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) - 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_492 = Coupling(name = 'GC_492',
	 value = '-1./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_493 = Coupling(name = 'GC_493',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) - 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_494 = Coupling(name = 'GC_494',
	 value = '-1./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_495 = Coupling(name = 'GC_495',
	 value = '-1./6.*complex(0,1)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_496 = Coupling(name = 'GC_496',
	 value = '1./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_497 = Coupling(name = 'GC_497',
	 value = '-1./6.*complex(0,1)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_498 = Coupling(name = 'GC_498',
	 value = '1./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_499 = Coupling(name = 'GC_499',
	 value = '-1./6.*complex(0,1)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_500 = Coupling(name = 'GC_500',
	 value = '1./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_501 = Coupling(name = 'GC_501',
	 value = '(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL11) + ZUL12*complexconjugate(ZDL12) + ZUL13*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_502 = Coupling(name = 'GC_502',
	 value = '(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL21) + ZUL12*complexconjugate(ZDL22) + ZUL13*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_503 = Coupling(name = 'GC_503',
	 value = '(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL31) + ZUL12*complexconjugate(ZDL32) + ZUL13*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_504 = Coupling(name = 'GC_504',
	 value = '(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL11) + ZUL22*complexconjugate(ZDL12) + ZUL23*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_505 = Coupling(name = 'GC_505',
	 value = '(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL21) + ZUL22*complexconjugate(ZDL22) + ZUL23*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_506 = Coupling(name = 'GC_506',
	 value = '(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL31) + ZUL22*complexconjugate(ZDL32) + ZUL23*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_507 = Coupling(name = 'GC_507',
	 value = '(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL11) + ZUL32*complexconjugate(ZDL12) + ZUL33*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_508 = Coupling(name = 'GC_508',
	 value = '(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL21) + ZUL32*complexconjugate(ZDL22) + ZUL33*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_509 = Coupling(name = 'GC_509',
	 value = '(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL31) + ZUL32*complexconjugate(ZDL32) + ZUL33*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_510 = Coupling(name = 'GC_510',
	 value = '(1*complex(0,1)*g2*(ZM11*complexconjugate(ZEL11) + ZM12*complexconjugate(ZEL12) + ZM13*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_511 = Coupling(name = 'GC_511',
	 value = '(1*complex(0,1)*g2*(ZM11*complexconjugate(ZEL21) + ZM12*complexconjugate(ZEL22) + ZM13*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_512 = Coupling(name = 'GC_512',
	 value = '(1*complex(0,1)*g2*(ZM11*complexconjugate(ZEL31) + ZM12*complexconjugate(ZEL32) + ZM13*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_513 = Coupling(name = 'GC_513',
	 value = '(1*complex(0,1)*g2*(ZM21*complexconjugate(ZEL11) + ZM22*complexconjugate(ZEL12) + ZM23*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_514 = Coupling(name = 'GC_514',
	 value = '(1*complex(0,1)*g2*(ZM21*complexconjugate(ZEL21) + ZM22*complexconjugate(ZEL22) + ZM23*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_515 = Coupling(name = 'GC_515',
	 value = '(1*complex(0,1)*g2*(ZM21*complexconjugate(ZEL31) + ZM22*complexconjugate(ZEL32) + ZM23*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_516 = Coupling(name = 'GC_516',
	 value = '(1*complex(0,1)*g2*(ZM31*complexconjugate(ZEL11) + ZM32*complexconjugate(ZEL12) + ZM33*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_517 = Coupling(name = 'GC_517',
	 value = '(1*complex(0,1)*g2*(ZM31*complexconjugate(ZEL21) + ZM32*complexconjugate(ZEL22) + ZM33*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_518 = Coupling(name = 'GC_518',
	 value = '(1*complex(0,1)*g2*(ZM31*complexconjugate(ZEL31) + ZM32*complexconjugate(ZEL32) + ZM33*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_519 = Coupling(name = 'GC_519',
	 value = '-1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_520 = Coupling(name = 'GC_520',
	 value = '-1*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_521 = Coupling(name = 'GC_521',
	 value = '-1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_522 = Coupling(name = 'GC_522',
	 value = '-1*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_523 = Coupling(name = 'GC_523',
	 value = '-1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_524 = Coupling(name = 'GC_524',
	 value = '-1*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_525 = Coupling(name = 'GC_525',
	 value = '-1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_526 = Coupling(name = 'GC_526',
	 value = '1*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_527 = Coupling(name = 'GC_527',
	 value = '-1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_528 = Coupling(name = 'GC_528',
	 value = '1*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_529 = Coupling(name = 'GC_529',
	 value = '-1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_530 = Coupling(name = 'GC_530',
	 value = '1*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_531 = Coupling(name = 'GC_531',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_532 = Coupling(name = 'GC_532',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_533 = Coupling(name = 'GC_533',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_534 = Coupling(name = 'GC_534',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_535 = Coupling(name = 'GC_535',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_536 = Coupling(name = 'GC_536',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_537 = Coupling(name = 'GC_537',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_538 = Coupling(name = 'GC_538',
	 value = '2./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_539 = Coupling(name = 'GC_539',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_540 = Coupling(name = 'GC_540',
	 value = '2./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_541 = Coupling(name = 'GC_541',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_542 = Coupling(name = 'GC_542',
	 value = '2./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_543 = Coupling(name = 'GC_543',
	 value = '(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL11) + ZDL12*complexconjugate(ZUL12) + ZDL13*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_544 = Coupling(name = 'GC_544',
	 value = '(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL21) + ZDL12*complexconjugate(ZUL22) + ZDL13*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_545 = Coupling(name = 'GC_545',
	 value = '(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL31) + ZDL12*complexconjugate(ZUL32) + ZDL13*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_546 = Coupling(name = 'GC_546',
	 value = '(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL11) + ZDL22*complexconjugate(ZUL12) + ZDL23*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_547 = Coupling(name = 'GC_547',
	 value = '(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL21) + ZDL22*complexconjugate(ZUL22) + ZDL23*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_548 = Coupling(name = 'GC_548',
	 value = '(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL31) + ZDL22*complexconjugate(ZUL32) + ZDL23*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_549 = Coupling(name = 'GC_549',
	 value = '(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL11) + ZDL32*complexconjugate(ZUL12) + ZDL33*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_550 = Coupling(name = 'GC_550',
	 value = '(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL21) + ZDL32*complexconjugate(ZUL22) + ZDL33*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_551 = Coupling(name = 'GC_551',
	 value = '(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL31) + ZDL32*complexconjugate(ZUL32) + ZDL33*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_552 = Coupling(name = 'GC_552',
	 value = '1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_553 = Coupling(name = 'GC_553',
	 value = '-2./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_554 = Coupling(name = 'GC_554',
	 value = '1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_555 = Coupling(name = 'GC_555',
	 value = '-2./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_556 = Coupling(name = 'GC_556',
	 value = '1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_557 = Coupling(name = 'GC_557',
	 value = '-2./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_558 = Coupling(name = 'GC_558',
	 value = '1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_559 = Coupling(name = 'GC_559',
	 value = '-1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_560 = Coupling(name = 'GC_560',
	 value = '1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_561 = Coupling(name = 'GC_561',
	 value = '-1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_562 = Coupling(name = 'GC_562',
	 value = '1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_563 = Coupling(name = 'GC_563',
	 value = '-1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_564 = Coupling(name = 'GC_564',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(ZM11) + ZEL12*complexconjugate(ZM12) + ZEL13*complexconjugate(ZM13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_565 = Coupling(name = 'GC_565',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(ZM21) + ZEL12*complexconjugate(ZM22) + ZEL13*complexconjugate(ZM23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_566 = Coupling(name = 'GC_566',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(ZM31) + ZEL12*complexconjugate(ZM32) + ZEL13*complexconjugate(ZM33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_567 = Coupling(name = 'GC_567',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(ZM11) + ZEL22*complexconjugate(ZM12) + ZEL23*complexconjugate(ZM13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_568 = Coupling(name = 'GC_568',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(ZM21) + ZEL22*complexconjugate(ZM22) + ZEL23*complexconjugate(ZM23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_569 = Coupling(name = 'GC_569',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(ZM31) + ZEL22*complexconjugate(ZM32) + ZEL23*complexconjugate(ZM33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_570 = Coupling(name = 'GC_570',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(ZM11) + ZEL32*complexconjugate(ZM12) + ZEL33*complexconjugate(ZM13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_571 = Coupling(name = 'GC_571',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(ZM21) + ZEL32*complexconjugate(ZM22) + ZEL33*complexconjugate(ZM23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_572 = Coupling(name = 'GC_572',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(ZM31) + ZEL32*complexconjugate(ZM32) + ZEL33*complexconjugate(ZM33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_573 = Coupling(name = 'GC_573',
	 value = 'G', 
	 order = {'QCD':1} ) 
 
GC_574 = Coupling(name = 'GC_574',
	 value = '-1*complex(0,1)*g2*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_575 = Coupling(name = 'GC_575',
	 value = '1*complex(0,1)*g2*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_576 = Coupling(name = 'GC_576',
	 value = '-1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_577 = Coupling(name = 'GC_577',
	 value = '-1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_578 = Coupling(name = 'GC_578',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_579 = Coupling(name = 'GC_579',
	 value = '-1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_580 = Coupling(name = 'GC_580',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_581 = Coupling(name = 'GC_581',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_582 = Coupling(name = 'GC_582',
	 value = '1*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_583 = Coupling(name = 'GC_583',
	 value = '1*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_584 = Coupling(name = 'GC_584',
	 value = '-2*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_585 = Coupling(name = 'GC_585',
	 value = '1./2.*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_586 = Coupling(name = 'GC_586',
	 value = '-1*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_587 = Coupling(name = 'GC_587',
	 value = '1./2.*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_588 = Coupling(name = 'GC_588',
	 value = '2*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_589 = Coupling(name = 'GC_589',
	 value = '-1*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_590 = Coupling(name = 'GC_590',
	 value = '-1*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_591 = Coupling(name = 'GC_591',
	 value = '-2*complex(0,1)*g2**2*cmath.cos(TW)**2', 
	 order = {'QED':2} ) 
 
GC_592 = Coupling(name = 'GC_592',
	 value = '1*complex(0,1)*g2**2*cmath.cos(TW)**2', 
	 order = {'QED':2} ) 
 
GC_593 = Coupling(name = 'GC_593',
	 value = '1*complex(0,1)*g2**2*cmath.cos(TW)**2', 
	 order = {'QED':2} ) 
 
GC_594=Coupling(name='GC_594',
	 value='-(HPP1*complex(0,1))', 
	 order={'HIW':1})

GC_595=Coupling(name='GC_595',
	 value='-(HGG1*complex(0,1))', 
	 order={'HIG':1})

