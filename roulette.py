n = int(input("n:"))
doors = list(map(int,input("arr:").split()))
m=0
if(doors[0]==1):
    m+=1
elif(doors[1]==1 and doors[0]==0):
    m+=1
    print(m)
for i in range(2,n):
    print(doors[i])
    if(doors[i]==1 and doors[i-1]==1 and doors[i-2]==1):
        m+=1
print(m,doors.count(1))