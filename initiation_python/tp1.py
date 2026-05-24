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
