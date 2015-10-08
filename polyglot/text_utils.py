# -*- coding: utf-8 -*-

import sys
import unicodedata

# For more information about symbols categories visit
# http://www.fileformat.info/info/unicode/category/[category code]/list.htm
def is_redundant_symbol(symbol):
  category = unicodedata.category(unichr(symbol))

  # All punctuation symbols = Pc | Pd | Ps | Pe | Pi | Pf | Po
  if category.startswith('P'):
    return True

  # Math, currency symbols and etc. = Sm | Sc | Sk | So
  if category.startswith('S'):
    return True

  return False

PUNCTUATION_SET = frozenset(
  unichr(i)
  for i in xrange(sys.maxunicode)
  if is_redundant_symbol(i)
)
