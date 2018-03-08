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
	for _ in range(10):
		x = random.randint(0, 10315)
		y = random.randint(0, 10315)
		boats.append((x, y))
	i=0
	data=()
	for x, y in boats:
		data+=(boats[i])
		mytree.ajouter(x, y)
		i+=1
	print(data)
	print(len(mytree))
	print(mytree)
