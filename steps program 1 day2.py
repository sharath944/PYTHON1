steps=int(input())
one=1
two=1
for i in range(1,steps,1):
    temp=one
    one=one+two
    two=temp
print(one)
