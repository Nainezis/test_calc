
from collections import deque
 
dexp = deque(list(input()))
 
def mop(val1, op, val2):
    if op == '+':
        return int(val1) + int(val2)
    if op == '-':
        return int(val1) - int(val2)
    if op == '*':
        return int(val1) * int(val2)
    if op == '/':
        return int(val1) / int(val2)
 
def calc(dexp):
    if len(dexp) == 1:
        return dexp[0]
    dexp.appendleft(mop(dexp.popleft(), dexp.popleft(), dexp.popleft()))
    return calc(dexp)
 
 
print(calc(dexp))