
#test sur les fonctions 
def lo(x):
    if x==1:
        return 1
    else:
        return (x+lo(x-1))

res=lo(3)
print(res)

#test sur les listes, 
w=["python","is","awesoome"]
#test join retour ?
print("-".join(w))

z="ami"
print(z*3) #ca doit retourner amiamiami

a=int('11',2)
print(a)#affichage dans la base 2


var = int(8.9)
print(var)#récupérer la partie entière 

l=[1,2,3,4]
print("|")
for i in range(3):
    
    print(i,end="|")

    