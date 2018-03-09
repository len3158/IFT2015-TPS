from LinkedQuadTree import LinkedQuadTree
import random
class Test:
#5157 erreur
	mytree = LinkedQuadTree()
	#level 0
#	mytree.ajouter(5159,5157)
#	mytree.ajouter(2,2)
#	mytree.ajouter(12,10)
#	mytree.ajouter(5,2)
#	mytree.ajouter(9,6)
#	mytree.ajouter(3,2)
	boats = []
	ecrire  = open("bateaux.txt", "w")
	for _ in range(10):
			x = random.randint(0, 10315)
			y = random.randint(0, 10315)
			mytree.ajouter(x,y)
	print(mytree)

