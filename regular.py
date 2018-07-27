#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=22%20text%20.23&-2

import re

txt='22 17.0.19.22 .23'

re1='.*?'	# Non-greedy match on filler
re2='(text)'	# Variable Name 1

rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    var1=m.group(1)
    print("("+var1+")"+"\n")

#-----
# Paste the code into a new python file. Then in Unix:'
# $ python x.py 
#-----