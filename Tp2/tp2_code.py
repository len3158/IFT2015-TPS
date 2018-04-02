PONC = ["!",'"',"'",")","(",",",".",";",":","?", "-", "_"]

class TextDict:
    """
    Represents a text as a dictionary of word doublet frequencies.
    """

    def __init__(self):
    	######## VOUS INITIALISEZ VOTRE DICTIONNAIRE ICI #######################


    def treatText(self, filename):
        """
        Represents text with doublet frequencies.
        """
        prevword = None
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip()
                if line == '': continue
                words = self.treatLine(line)
                ####### À COMPLÉTER ############################################



    def treatLine(self, line):
        """
        Separates words and removes punctuation.
        """
        noponc = ""
        for c in line:
            if c in PONC:
                noponc = noponc + " "
            else:
                noponc = noponc + c
        words = noponc.split()
        wlower = []
        for w in words:
            if len(w) > 2:
                wlower.append(w.lower())
        return wlower
