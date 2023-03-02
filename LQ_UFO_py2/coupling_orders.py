# last update 13/01/2016

from __future__ import absolute_import
from object_library import all_orders, CouplingOrder


QCD = CouplingOrder(name = u'QCD',
                    expansion_order = 99,
                    hierarchy = 1)

QED = CouplingOrder(name = u'QED',
                    expansion_order = 99,
                    hierarchy = 2)

HIG = CouplingOrder(name = u'HIG',
                    expansion_order = 1,
                    hierarchy = 2)

HIW = CouplingOrder(name = u'HIW',
                    expansion_order = 1,
                    hierarchy = 2)
                    
BSM = CouplingOrder(name = u'BSM',
                    expansion_order = 1,
                    hierarchy = 2)                    
