n = int(input())
p = list(map(int, input().split()))
p.sort()

count = 0
time = 0

for i in p:
    count += i
    time += count


print(time)