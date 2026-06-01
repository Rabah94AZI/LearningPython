
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
# tres important: en python si je fais print ca va m'afficher none a la fin de la boucle 
#solution A
def mult(n):
    for i in range(11):
        print(i, "*",n,'=', i*n)
     
#mult(5)

for i in range(11):
    print(f'table de mult de {i}')
    mult(i)

# un affichage dans une liste
def mult1(n):
    lis=[]
    for i in range(11):
        lis.append(i*n)
    return lis
print(mult1(5))

 #methode plus optimale    
def mult2(n):
    return [i*n for i in range(11)]

print(mult2(5))

#ajouter un programme qui  devine un nombre 

n=100
import random
rr= random.randint(1,100)
print("la valeur de random est :",rr)
print("la valeur de n est :", n)
if rr==n:
    print("vous avez gagné!")
elif rr>n:
    print("tres petit")
elif rr<n:
    print("tres grand")

print("affichage inv d'une chaine de caractere")
mot="david raya"
print(mot[::-1])
print("affichage de l'in en utilisant boucle for")
mot2="david raya"
inv=""
for i in mot2:
    inv=i+inv
print(inv)

mot3="salut rabah"
inv_word=reversed(mot3)
print(inv_word)

mot3 = "salut rabah"
inv_word = ''.join(reversed(mot3))
print(inv_word)
#compter les voyelles 
print("compter le nombre des voyelles")
mot="abcefgiuo"
s=0
for i in mot:
    if i in ("a","u","i","o","e","y"):
        s=s+1
print(s)   

#factoreil
print("afficher le factoriel d'un nombre donner")
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(3))

#nombre premier 

def premier(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True        
print(premier(5))
print(premier(10))


def comp(mot):
    #cpt=" ".join(mot) #pour les caracteres 
    cpt = mot.split()
    return cpt.__len__()

a="bonjour dev, comment vas tu !"
print(comp(a))
import random
a=random.randint(1,3)
print(a)

import random

def jeu():
    choix = ["pierre", "papier", "ciseaux"]
    #random.choice c'est prédéfinie 
    ordi = random.choice(choix)
    
    joueur = input("choisis pierre, papier ou ciseaux : ").lower()

    print("ordinateur :", ordi)

    if joueur == ordi:
        print("égalité")
    elif (joueur == "pierre" and ordi == "ciseaux") or \
         (joueur == "papier" and ordi == "pierre") or \
         (joueur == "ciseaux" and ordi == "papier"):
        print("tu as gagné !")
    else:
        print("tu as perdu ")

jeu()