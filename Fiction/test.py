# -*- coding: utf-8 -*-

import re

teststr = '\u6b63\u6587 \u56fd\u5e86\u8d3a\u6587\uff0c\u975e\u76d7\u5893\u7b14\u8bb0\uff0c\u514d\u8d39\u5949\u9001\u3002'
teststr1 = teststr.decode('unicode_escape')
teststr2 = str(teststr)

print teststr2