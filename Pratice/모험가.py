
a = int(input())

data = list(map(int, input().split()))
data.sort()

print(data)

group = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        group += 1
        count = 0
    # if count >= data[i]:
    #     group += 1
    # else:
    #     count += data[i] 
    #     group = group

# for i in data:
#     group += 1
#     if group >= i:
#         result +=1
#         group = 0


print(group)