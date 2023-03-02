# This file is part of the UFO.
#
# This file contains definitions for functions that
# are extensions of the cmath library, and correspond
# either to functions that are in cmath, but inconvenient
# to access from there (e.g. z.conjugate()),
# or functions that are simply not defined.
#
#

from __future__ import absolute_import
__date__ = u"22 July 2010"
__author__ = u"claude.duhr@durham.ac.uk"

import cmath
from object_library import all_functions, Function

#
# shortcuts for functions from cmath
#

complexconjugate = Function(name = u'complexconjugate',
                            arguments = (u'z',),
                            expression = u'z.conjugate()')


re = Function(name = u're',
              arguments = (u'z',),
              expression = u'z.real')

im = Function(name = u'im',
              arguments = (u'z',),
              expression = u'z.imag')

# New functions (trigonometric)

sec = Function(name = u'sec',
             arguments = (u'z',),
             expression = u'1./cmath.cos(z)')

asec = Function(name = u'asec',
             arguments = (u'z',),
             expression = u'cmath.acos(1./z)')

csc = Function(name = u'csc',
             arguments = (u'z',),
             expression = u'1./cmath.sin(z)')

acsc = Function(name = u'acsc',
             arguments = (u'z',),
             expression = u'cmath.asin(1./z)')




