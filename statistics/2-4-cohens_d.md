[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

Python code:  

```
import nsfg
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1, group2):
    import math
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

print CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
```
Result:
-0.0886729270726 
The difference in means in weight of first babies versus other babies is -.089 standard deviations, which is very small. First babies are slightly lighter; other babies are slightly heavier. This difference is however slightly larger than the difference in means in pregnancy length for first babies versus other babies, which is .029 standard deviations. Pregnancy length for first babies is slightly larger than for other babies.
