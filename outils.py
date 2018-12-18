def voidIt(lis):
    for k in lis.keys():
        lis[k] = 0
    return lis

def isIN(str_,alpha):
    # check if alpha in str_
    if(alpha in str_):
        return 1


def isIN_all(sentence,alpha):
    # check if any lettre of alpha is in sentence
    for lettre in alpha:
        if(isIN(sentence,lettre) == 1):
            return True


def eps(F):
    eps = []
    for k in F.keys():
        if(F[k]>0):
            eps.append(k)
    return eps



def intersect(str1,str2):
    if str1 in str2:
        inter = str1
    elif str2 in str1:
        inter = str2
    else:
        inter = ""
    return inter
