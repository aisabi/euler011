import copy
testGrid = [
  [40, 17, 81, 18, 57],
  [74, 4, 36, 16, 29],
  [36, 42, 69, 73, 45],
  [51, 54, 69, 16, 92],
  [7, 97, 57, 32, 16]
]

for donnee in testGrid:
	print(donnee)

grid1 = copy.deepcopy(testGrid)

i = 0
for donnee in range(len(grid1)):
	del grid1[i][0]
	i = i + 1

#Creation grille sans 1ere ligne, elle sera utilisée pour la suite du calcul haut en bas
# Grid made without the 1st line.Use it for calculation top down
grid2 = copy.deepcopy(testGrid)
del grid2[0]

#Creation grille inversé , elle sera utilisée pour le calcul droite à gauche
# Reversed grid. Use it for calculation right to left

grid3 = copy.deepcopy(testGrid)
for i in range(len(testGrid)):
	grid3[i].reverse()
	
i = 0
for donnee in range(len(grid3)):
	del grid3[i][0]
	i = i + 1
grid3bis = copy.deepcopy(grid3)

print('\n------------\n')
#1st round line left to right
#calcul testGrid de gauche à droite

listeCalcul1 = [] #exemple : 40 * 17 * 81 * 18 = 991440 
for i in range(5):
	resultat = 1 # initialize the variable resultat
	for j in range(4):
		sol= testGrid[i][j] # iteration in matrix left to right for 4 numbers
		resultat = resultat * sol # calculation of result
	listeCalcul1.append(resultat) # append all result in list 'listeCalcul1'

#17 * 81 * 18 * 57 = 1412802, ...
# print('here grid1 : ', grid1)
for i in range(5):
	resultat = 1
	for j in range(4):
		sola= grid1[i][j]
		resultat = resultat * sola
	listeCalcul1.append(resultat) 

#2ndcalcul testGrid de haut en basP
# 40 * 74 * 36 * 51 = 5434560, ...
for i in range(4):
	resultat = 1
	for j in range(4):
		sol= testGrid[j][i]
		resultat = resultat * sol
	listeCalcul1.append(resultat) 

# 74 * 36 * 51 * 7 = 951048
for i in range(5):
	resultat = 1
	for j in range(4):
		solahb= grid2[j][i]
		resultat = resultat * solahb
	listeCalcul1.append(resultat) 


# print('Results : ',listeCalcul1,'\n')
# print("Highest multiplication of 4 numbers : ",max(listeCalcul1))

# calcul testGrid en diagonal :
liste=[]
for i in range(len(testGrid)-1):
	print(testGrid[i][i])
	liste.append(testGrid[i][i])
	print(liste)
resultat=1
for i in liste:
	resultat = resultat * i
	print('resultat1',resultat)
listeCalcul1.append(resultat) 

print('\n')
liste=[]
for i in range(len(testGrid)-1):
	print(testGrid[i][i+1])
	liste.append(testGrid[i][i+1])
	print(liste)
	
resultat=1
for i in liste:
	resultat = resultat * i
	print('resultat1',resultat)
listeCalcul1.append(resultat) 

print('\n')
liste=[]
for i in range(len(testGrid)-1):
	print(testGrid[i+1][i])
	liste.append(testGrid[i+1][i])
	print(liste)
resultat=1
for i in liste:
	resultat = resultat * i
	print('resultat1',resultat)
listeCalcul1.append(resultat) 

liste=[]
for i in range(len(testGrid)-1):
	print(testGrid[i][len(testGrid)-i-1])
	liste.append((testGrid[i][len(testGrid)-i-1]))
	print(liste)
resultat=1
for i in liste:
	resultat = resultat * i
	print('resultat1',resultat)
liste=[]
for i in range(len(testGrid)-1):
	print(testGrid[i][len(testGrid)-i-2])
	liste.append((testGrid[i][len(testGrid)-i-2]))
	print(liste)
resultat=1
for i in liste:
	resultat = resultat * i
	print('resultat1',resultat)
listeCalcul1.append(resultat) 

liste=[]
for i in range(len(testGrid)-1):
	print(testGrid [i+1][len(testGrid)-i-1])
	liste.append((testGrid [i+1][len(testGrid)-i-1]))
	print(liste)
resultat=1
for i in liste:
	resultat = resultat * i
	print('resultat1',resultat)
listeCalcul1.append(resultat)

print('Results : ',listeCalcul1,'\n')
print("Highest multiplication of 4 numbers : ",max(listeCalcul1))