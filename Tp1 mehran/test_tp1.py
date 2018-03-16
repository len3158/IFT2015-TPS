import io
from contextlib import redirect_stdout
import sys
import glob
import shutil

# Changer cette ligne pour le nom de votre script. 
# Change this line to your script name
from Tp1_1055234_1047837_b1 import test as test
# Votre script doit comprendre une méthode test qui sera exécutée par le présent
# script. Cette méthode ne prend aucun argument en entrée (elle fait la même
# chose que votre __main__).

# Your script must have a method called test which will be executed by the
# present script. This method has no argument (it does the same thing that your
# __main__ does).

def test_all():
	"""
	Tous vos tests unitaires doivent suivre cette nomenclature :
	unit_tests_tp1/test* (* peut être toute suite de caractères)
	chaque test est un dossier contenant trois fichiers :
	bateaux.txt
	bombes.txt
	out.txt
	Le dossier unit_tests_tp1 doit se trouver dans le même dossier que le
	présent script (test_tp1.py)
	"""
	tests = glob.glob("unit_tests_tp1/test*")
	passed = 0
	temps = 0
	for t in tests:
		for fn in ["bateaux.txt", "bombes.txt", "out.txt"]:
			shutil.copyfile("{}/{}".format(t, fn), "{}".format(fn))
		f = io.StringIO()
		with redirect_stdout(f):
			temps = test()
		output = f.getvalue()
		expected = readout()
		print("########## Currently testing: {} ##########".format(t))
		if output == expected:
			print("Test passed!\n Times:\n{}".format(temps))
			passed += 1
		else:
			print("Test failed...")
			print("Expected output:\n{}Your output:\n{}Your times:\n{}\n\n".format(expected,output,temps))
	print("{}/{} unit tests passed.".format(passed,len(tests)))

def readout():
	with open("out.txt", "r") as f:
		return f.read()

if __name__ == "__main__":
	test_all()









