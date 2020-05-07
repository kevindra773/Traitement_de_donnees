ListeEleves = [["Othman","Aminata","Jeras"],["Aminata","Jeras"]]
L = []

def Tri():
    for i in ListesEleves:
        for e in i:
            if e not in L:
                L.appen(e)
                return L


def classement():
    Dico={}
    Eleve=Tri()
    for i in Eleve:
        score = 0
        for e in ListesEleves:
            for f in e:
                if f == i:
                    score += 100- e.index(f)
        Dico[i]= score
    print(Dico)