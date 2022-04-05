from collections import deque
import collections


from collections import deque

#큐 구현을 위해 deque라이브러리 사용
queue = deque()

# 삽입 5237 삭제 삽입 14 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()


print(queue)
queue.reverse()
print(queue)