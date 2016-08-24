# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

**Similarities between Lists and Tuples**  
- each a sequence of values   
- the values can be any type  
- indexed by integers   
- bracket operator indexes an element
- slice operator selects a range of elements  

**Differences between Lists and Tuples**  
- Tuples are immutable  
- Lists are mutable  
  
Tuples will work as keys in dictionaries because keys must be immutable.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

**Similar:**  
They both contain values. 

**Different:**  
Order—  
A list keeps order and a set does not. So if you care about order, you should use a list. Also, sets do not support indexing, slicing, or other sequence-like behavior.  
Hashable—  
Set requires items to be hashable; list doesn’t. If you have non-hashable items, you must use list.  
Duplicates—  
Set forbids duplicates and list does not.  
Comparing 2 sets —  
Sets allow you to do operations such as intersection, union, difference, and symmetric difference. 

Checking for membership of a value in a set is super fast, while checking for membership in a list takes time proportional to the list’s length in the average and worst cases. So if you have hashable items, don’t care either way about order or duplicates, and want speedy membership checking, set is better than list.

**List:**  
```python  
ways_to_greet = [“Hi”, “Hello”, “Howdy”, “Nice to meet you”, “Wuz up??”]
ways_to_greet[0]
```

**Set:**
```python
a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
a | b # Union
{1, 2, 3, 4, 5, 6}
a & b # Intersection
{3, 4}
a < b # Subset
False
a - b # Difference
{1, 2}
a ^ b # Symmetric Difference
{1, 2, 5, 6}
```  
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is a fancy word for function that is not bound to a name.  It takes any number of arguments and returns the value of a single expression. It is often used in conjunction with typical functional concepts like filter(), map(), reduce().

```python
sum = lambda x, y:   x + y
print sum (7,8)
foo = [2,18,9,22,17,24,8,12,27]
print filter(lambda x: x %3 ==0, foo)
print map(lambda x: x * 2 + 10, foo)
print reduce(lambda x, y: x + y, foo)

sorted([‘Hello’, 'weigh’, 'sort', ‘cat’], key=lambda word: word.lower())
[‘cat’, ‘Hello’, 'sort', 'weigh’]
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition. List comprehensions are essentially a filter followed by a map.
```python
example_with_map_and_filter = map(lambda n: n*2, filter(lambda n: n %2 == 1, numbers))
example_with_list_comprehension = [n*2 for n in numbers if n % 2 == 1]
```

*list comprehension formula:*
new_things = [“something with “ + ITEM for ITEM in old_things if condition_based on(ITEM)]

*set comprehension:*
x = {i**2 for i in range(10)}

*dictionary comprehension:*
x = {i:i**2 for i in range(10)}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
Answer: 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

Answer: 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

Answer: 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)  
*Ok done.*

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)  
*Ok done.*

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)  
*Ok done.*

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py) 
*Ok done. Although I don’t see 3 functions to edit in Q8. It asks me to write a program to read a file, manipulate the file and print output.*

