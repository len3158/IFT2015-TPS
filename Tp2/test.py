from Bucket import Bucket
class test():
		table = Bucket()
		table.insert("bonjour toi")
		table.insert("manger chat")
		table.insert("salut")
		table.insert("salut")
		table.insert("salutt")
		table.insert("manger chien")
		table.insert("mangerchoroclat")
		table.insert("Bonjour moi")
		print(table)

		table["manger chien"] = 7

		print(table["manger chien"])

		del table["bonjour toi"]
		print(table)


		

		
                
		

		

	
