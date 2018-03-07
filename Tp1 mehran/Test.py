from LinkedQuadTree import LinkedQuadTree
import random
class Test:
		
	mytree = LinkedQuadTree()
	#level 0
#	mytree.ajouter(1,2)
#	mytree.ajouter(2,2)
	boats = []
	for _ in range(2):
		x = random.randint(0, 10300)
		y = random.randint(0, 10300)
		boats.append((x, y))
		 
	print(boats[0], boats[1])
	for x, y in boats:
		mytree.ajouter(x, y)
	print(mytree)
