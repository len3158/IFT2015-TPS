from Bucket import Bucket
class test():
		table = Bucket()
		table.ajouter("bonjour toi")
		table.ajouter("manger chat")
		table.ajouter("salut")
		table.ajouter("salut")
		table.ajouter("salutt")
		table.ajouter("manger chien")
		table.ajouter("mangerchoroclat")
		table.ajouter("Bonjour moi")
		print(table)
                
		print(table["salut"])
		
		table["manger chien"] = 5
		print(table["manger chien"])

		

	
