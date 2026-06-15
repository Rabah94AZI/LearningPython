print("lancer mon premier programme python")
print("Bonjour")#python va afficher Bonjour a l'ecran
#il faudra le lancer sur un terminal 
#nom = input("Quel est votre nom")
#print("Bonjour"+nom)# si tu as code runner sur vscode ca va pas te donner la main pour interagir 
#sol : # selectionner la ligne, clique droit puis run dans un terminal 
#utilisation des variables 
nom="rabs"
print(nom)# le programme va récuerer rabs et l'afficher sur l'ecran

#concaténer des chaine 
print("bonjour "+nom+"!")#le + permet de concat les chaine de caracteres 

#faire des opération sur les nombres

age=31
print(type(age)) #<class: 'int'>
print("vous avez :",age,"ans")
print("vous avez :",age+1,"ans")

#gestion des exceptions

charr="33"
try :
    age_prochain=charr+1#il faut mettre int(charr)
    print(charr)
except:
    print("erreur")

#les listes 
print("des opérations sur les listes")
li = [10,20,30,40,50]
print(li[0])#le premier element :10
print(li[-1])#le dernier element : 50
print(li[1:3])#récupérer 20 30
print(li[:3])# récupére 10 20 30 
print(li[2:])#les elements a partir de l'indice 2 : 30 40 50

li2=['pomme','banane','cerise']
print(li2)                       #['pomme','banane','cerise']
li2.append('pasteque')           #['pomme','banane','cerise','pasteque']
print(li2)
li2.insert(1,'ananas')           # ['pomme','ananas','banane','cerise','pasteque']
print(li2)
li2.extend(['dates','oignons'])#['pomme','ananas','banane','cerise','pasteque','dates','oignons']
print(li2)
li2.remove("dates")#['pomme','ananas','banane','cerise','pasteque','oignons']
print(li2)
li2.pop()#['pomme','ananas','banane','cerise','pasteque']
print(li2)
li2.sort()#['ananas', 'banane', 'cerise', 'pasteque', 'pomme']
print(li2)
li2.reverse()
print(li2)#['pomme','pasteque','cerise','banane','ananas']

#les matrix
print("des operatioins sur les matrix")
m=[[5,4,3],
   [3,4,5],
   [1,2,3]]
print(m[1][2])
print('affichage de la matrice ')
for i in m:
    for j in i:
        print(j, end=" ")
    print()
    
print("un autre affichage :")
for i in m:
    print(i)      

lig = len(m)
print(lig)
colonnes = len(m[0])
print(colonnes)

print("imp de la bib numpy")
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(a + b)
print(a - b)
print(a * 2)
print(a.dot(b))
print(a.T)

#
print({1,2,3}&{2,3,4})
print({1,2,3}or{2,3,4})

for i in range(1,4):
    print(i,end="\n")

nums=[1,2,3,4]
result= list(map(lambda x:x*2 , nums))
print(result)

li=["python is fun"]
si="java is not"
#pour retourner une chaine de caracter
print(" ".join(li))
#pour retourner une liste des chaine de caractere 
print(si.split(" "))      

for i in range(1,4):
    print(i)
for i in range(1,4):
    print(i,end=" ")
#par default quand tu afis un print ya un saut de ligne automatique 
print("")
for i in range(1,4):
    print(i,end="\n")

#on peut simuler un barre de progression 
import time
for i in range(5):
    print(".", end="")
    time.sleep(0.5)

x=[1,2,3]
y=x
c=x.copy()
y+=[4]
print(x)
print(y)
print(c)

x= [3,1,2,1]
y=x.sort()
print(y, x)

names=["rabah","anis"]
ages = [31,32]
print(list(zip(names,ages)))

#si tu veux utiliser un retour multiple(flux de valeurs) et quand tu veux pas stocker en mémoire 
def count_up():

    yield 1 
    yield 2
gen = count_up()
print(next(gen))