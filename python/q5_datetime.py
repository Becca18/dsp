# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'  

from datetime import *

date_start = '01-02-2013'
date_start=datetime.strptime(date_start, '%m-%d-%Y')

date_stop = '07-28-2015'
date_stop = datetime.strptime(date_stop, '%m-%d-%Y')

print date_stop-date_start 

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_start1 = '12312013'
date_start1=datetime.strptime(date_start1, '%m%d%Y')

date_stop1 = '05282015'
date_stop1 = datetime.strptime(date_stop1, '%m%d%Y')

print date_stop1-date_start1

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

date_start2 = '15-Jan-1994'
date_start2 = datetime.strptime(date_start2, '%d-%b-%Y')

date_stop2 = '14-Jul-2015'
date_stop2 = datetime.strptime(date_stop2, '%d-%b-%Y')

print date_stop2-date_start2