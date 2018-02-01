"""" Auteurs : Mehran Asadi  Matricule : 1047837
			   Lenny Siemeni Matricule : 1055234 """
import io
from contextlib import redirect_stdout
import sys
import glob
import shutil
# Changer cette ligne pour le nom de votre script
# Change this line to your script name
from Tp0_1055234_b1 import test as test

def test_all():
	"""
	Tous vos tests unitaires doivent suivre cette nomenclature :
	unit_tests_tp0/test* (* peut être toute suite de caractères)
	chaque test est un dossier contenant quatre fichiers :
	rules.txt
	config.txt
	arg.txt
	out.txt
	Le dossier unit_tests_tp0 doit se trouver dans le même dossier que le
	présent script (test_tp0.py)
	"""
	tests = glob.glob("unit_tests_tp0/test*")
	passed = 0
	for t in tests:
		for fn in ["rules.txt", "config.txt", "out.txt", "arg.txt"]:
			shutil.copyfile("{}/{}".format(t, fn), "{}".format(fn))
		f = io.StringIO()
		with redirect_stdout(f):
			test(readarg())
		output = f.getvalue()
		expected = readout()
		print("########## Currently testing: {} ##########".format(t))
		if output == expected:
			print("Test passed!\n")
			passed += 1
		else:
			print("Test failed...")
			print("Expected output:\n{}Your output:\n{}\n\n".format(expected,
																	output))
	print("{}/{} unit tests passed.".format(passed,len(tests)))


def readarg():
	with open("arg.txt", "r") as f:
		return f.readline().rstrip()

def readout():
	with open("out.txt", "r") as f:
		return f.read()

if __name__ == "__main__":
	test_all()









