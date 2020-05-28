Counting Valley Problem
------

Explanation:
---
Traverse all path one by one, valley identify when sea level is from 0 going to -1, so we check it first when Down before minus it.  and then when we traverse every step, when Up, add 1 sea level and when Down, we minus 1 sea level. 

Requirement:
> Python 3.x

How to Run?
---
```
python3 main.py
```

Input?
---
First Line is number of steps
_ex : 8_
Second Line is _n_ characters that decribe paths
_ex : UDDDUUU_