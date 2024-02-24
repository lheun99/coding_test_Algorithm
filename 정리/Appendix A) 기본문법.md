# Appendix A) 기본

Created: January 27, 2024 3:52 PM

### 입출력

```python
import sys
data = sys.stdin.readline().rstrip()
print(data)
```

### 주요 라이브러리의 문법과 유의점

- **itertools**

```python
data = ['A', 'B', 'C']

from itertools import permutations as pm
list(permutations(data, 3))
# [('A', 'B', 'C'), ... ('C', 'B', 'A')]

from itertools import combinations as cb
list(combinations(data, 2))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

from itertools import product
list(product(data, repeat=2))
# [('A', 'A'), ('A', 'B'), ... ('C', 'B'), ('C', 'C')]

from itertools import combinations_with_replacement
list(combinations_with_replacement(data, repeat=2))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```

- **Heap**
  - 최소힙 : 오름차순 정렬

```python
import heapq

heapq.heappush(1)
heapq.heappop(1)
```

- **Bisect**

```python
from bisect import bisect_left, bisect_right
# [1, 2, 4, 4, 8]

bisect_left(a, 4)
# [1, 2, 4, 4, 4, 8]
bisect_right(a, 4)
# [1, 2, 4, 4, 4, 4, 8]
```

- **Collections**

```python
from collections import deque

data.appendleft()
data.append()
data.pop()
data.popleft()

from collections import Counter
counter = Counter(['red', 'blue', ...])

counter['blue']
dict(counter)
```
