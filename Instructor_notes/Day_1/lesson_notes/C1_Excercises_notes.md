
Consider teaching basics about indexing data structures

Zero-based numbering is a way of numbering in which the initial element of a sequence is assigned the index 0, rather than the index 1 as is typical in everyday non-mathematical or non-programming circumstances. Under zero-based numbering, the initial element is sometimes termed the zeroth element,[1] rather than the first element; zeroth is a coined ordinal number corresponding to the number zero. 

(Maybe the exercises can have some subheader like indexing, or maybe it can be just a note)

```python
>>> import numpy as np
>>> x = "string"
>>> x[1]
't'

>>> x = np.arange(10)
>>> x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> x.shape
(10,)
>>> x.shape(2,5)
>>> x.shape= (2,5)
>>> x
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])

>>> x[0][2]
2

>>> x[0,2]
2
```
