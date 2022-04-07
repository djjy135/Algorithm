

n = int(input())
#a,b,c,d,e = map(int,input().split())

a = list(map(int,input().split()))
max_a = a[0]
min_a = a[0]
    #print(a)        
#for k in range(len(a)-1):
for i in range(len(a)):

    if a[i] > max_a:
        max_a = a[i]

    elif a[i] < min_a:
       # max_a = a[i+1]
        min_a = a[i]
        
        
print(min_a,max_a,end= '')
#print(a[len(a)-1])

   


        