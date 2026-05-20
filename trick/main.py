
def lo(x):
    if x==1:
        return 1
    else:
        return (x+lo(x-1))

res=lo(3)
print(res)

w=["python","is","awesoome"]
print("-".join(w))

z="ami"
print(z*3)

a=int('11',2)
print(a)


var = int(8.9)
print(var)

l=[1,2,3,4]
print("|")
for i in range(3):
    
    print(i,end="|")

    