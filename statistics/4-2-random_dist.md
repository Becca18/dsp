[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

Code:  

```
import random
sample = []
for i in range(0,1000):
    sample.append(random.random())

import thinkstats2
pmf = thinkstats2.Pmf(sample)
cdf = thinkstats2.Cdf(sample)

import thinkplot
thinkplot.Pmf(pmf, label='PMF')
thinkplot.Show(xlabel='Random Number between 0 and 1', ylabel='PMF')

thinkplot.Cdf(cdf, label='CDF')
thinkplot.Show(xlabel='Random Number between 0 and 1', ylabel='CDF')
```
Result:  
Yes, the function produces random numbers - the distribution is shown to be uniform in the PMF plot and the CDF plot.

