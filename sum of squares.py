def sumsquare(l):
    odd=0
    even=0
    for i in l:
        if(i%2==0):
            even=+(i*i)
        else:
            odd=+(i*i)
    return(odd,even)
n=int(input("enter no of elements:"))
if(n<=0):
    print("invalid!!")
else:
    l=[]
    for i in range(n):
        l.append(int(input("enter the number:")))
    print(sumsquare(l))
    
