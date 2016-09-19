[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

Python code:  
```
import chap01soln
resp = chap01soln.ReadFemResp()

import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

biased_pmf = BiasPmf(pmf, label='biased')

import thinkplot
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='children in household', ylabel='PMF')

print pmf.Mean()
print biased_pmf.Mean()
```

Result:  
[Children in Household PMF](https://github.com/Becca18/dsp/blob/master/img/children_in_household.png)

The mean of the actual distribution of the number of children under 18 in the household is 1.02.
The mean of the biased distribution of the number of children under 18 in the household is 2.40.
