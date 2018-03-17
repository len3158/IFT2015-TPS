from LinkedQuadTree import LinkedQuadTree

def test_arbre_vide():
	mytree = LinkedQuadTree()
	assert mytree.is_empty()
	assert len(mytree) == 0

def test_ajoute_un_noeud_et_le_retrouve():
	mytree = LinkedQuadTree()
	mytree.ajouter(9,3)
	assert len(mytree) == 2
	assert mytree._subtree_search(mytree._root, 9, 3)

def test_ajoute_plusieurs_noeuds_et_les_retrouvent():
	mytree = LinkedQuadTree()
	mytree.ajouter(0, 0)
	mytree.ajouter(9, 3)
	mytree.ajouter(10, 14)
	mytree.ajouter(99, 80)
	mytree.ajouter(10315, 10315)
	assert mytree._subtree_search(mytree._root, 0, 0)
	assert mytree._subtree_search(mytree._root, 9, 3)
	assert mytree._subtree_search(mytree._root, 10, 14)
	assert mytree._subtree_search(mytree._root, 99, 80)
	assert mytree._subtree_search(mytree._root, 10315, 10315)

def test_arbre_vide_apres_ajout_suppresion_de_plusieurs_noeuds():
	mytree = LinkedQuadTree()
	mytree.ajouter(0, 0)
	mytree.ajouter(9, 3)
	mytree.ajouter(10, 14)
	mytree.ajouter(99, 80)
	mytree.ajouter(10315, 10315)
	assert mytree._subtree_search(mytree._root, 0, 0)
	assert mytree._subtree_search(mytree._root, 9, 3)
	assert mytree._subtree_search(mytree._root, 10, 14)
	assert mytree._subtree_search(mytree._root, 99, 80)
	assert mytree._subtree_search(mytree._root, 10315, 10315)
	mytree.test_bombes(0, 0, 0, 0)
	mytree.test_bombes(9, 9, 3, 3)
	mytree.test_bombes(10, 10, 14, 14)
	mytree.test_bombes(99, 99, 80, 80)
	mytree.test_bombes(10315, 10315, 10315, 10315)
	assert mytree.is_empty()
	
def test_une_bombe_supprime_un_seul_bateau():
	mytree = LinkedQuadTree()
	mytree.ajouter(0, 0)
	mytree.ajouter(9, 3)
	mytree.ajouter(10, 14)
	mytree.ajouter(99, 80)
	mytree.ajouter(10315, 10315)
	mytree.test_bombes(9, 9, 3, 3)
	assert not mytree.is_empty()

def test_une_bombe_supprime_tous_les_bateaux():
	mytree = LinkedQuadTree()
	mytree.ajouter(0, 0)
	mytree.ajouter(9, 3)
	mytree.ajouter(10, 14)
	mytree.ajouter(99, 80)
	mytree.ajouter(10315, 10315)
	mytree.test_bombes(0, 10315, 0, 10315)
	assert mytree.is_empty()

def test_stabilite_insertion_bateau_identique():
	mytree = LinkedQuadTree()
	mytree.ajouter(0, 0)
	mytree.ajouter(0, 0)
	mytree.ajouter(0, 0)
	mytree.ajouter(0, 0)
	assert len(mytree)==2
	
if __name__=="__main__":
	test_arbre_vide()
	test_ajoute_un_noeud_et_le_retrouve()
	test_ajoute_plusieurs_noeuds_et_les_retrouvent()
	test_arbre_vide_apres_ajout_suppresion_de_plusieurs_noeuds()
	test_une_bombe_supprime_un_seul_bateau()
	test_une_bombe_supprime_tous_les_bateaux()
	test_stabilite_insertion_bateau_identique()
	