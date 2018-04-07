from Tp2_1055234_1047837_b1 import Tp2_1055234_1047837_b1
class test():
		table = Tp2_1055234_1047837_b1()
		table.insert("bonjour toi")
		table.insert("manger chat")
		table.insert("salut")
		table.insert("salut")
		table.insert("salutt")
		table.insert("manger chien")
		table.insert("mangerchoroclat")
		table.insert("Bonjour moi")
		
		print("Afficher la table apres insertion de 11 element")
		print(table)
        
        
		table["manger chien"] = 7
		del table["bonjour toi"]
		print("Afficher la table apres (manger chier = 7) et delete (bonjour toi)") 
		print(table)


		

		
                
		

		

	
