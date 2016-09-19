[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 

Code:  
```
#5'10" = 70" = 177.8cm
#6'1" = 73" = 185.42cm

import scipy.stats
Blue_man_range = scipy.stats.norm.cdf(185.42, loc=178, scale=7.7)-scipy.stats.norm.cdf(177.8, loc=178, scale=7.7)
print Blue_man_range
```

Result:  
34.27% of the U.S. male population is in the Blue Man Group height range.  