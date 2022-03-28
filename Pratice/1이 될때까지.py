n, k = map(int, input('숫자 두개 입력').split())

result = 0

while True:
    target = (n//k) * k
    result += (n-target)
    n = target
    if n < k:
        break

    result += 1 
    n //= k


result += (n-1)
print(result)
