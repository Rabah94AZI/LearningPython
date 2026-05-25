
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

for i in range(3): 
    print(i)

print()
print("----------parité")
#programme pour afficher les noms paires et impaires
nbr=5

if(nbr % 2 ==0):
    print(f"le nombre {nbr} est paire")
else:
    print(f"le nombre {nbr} est impaire")

#programme calculatrice 
print("-----------calculatrice ")

def cal(a,b,op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b 
print(cal(2,3,"+"))  #5
print(cal(2,3,"-")) #-1
print(cal(2,3,"*")) #6
print(cal(2,3,"/")) #0.666
print(cal(6,3,"/")) #2

#programme afficher le plus grand nombre entre 3 nombres
print("programme afficher le plus grand nombre entre 3 nombres")
def maxi(a,b,c):
    if a>b & a>c:
        return a
    elif b>a & b>c:
        return b
    else: 
        return c
    
print(maxi(1,2,3)) #3
print(maxi(-1,-2,-3)) #-1


print("afficher la somme de 1 a N")

def som(n):
    s=0
    for i in range(n+1):
        #print(i)
        s+=i
    return s

print(som(3))#6
print(som(10))#6



