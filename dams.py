from  outils import voidIt, isIN, isIN_all, eps, intersect
print("P: peter // J:john // M: mary")

P={'O':0,'P':0,'J':0,'M':0,'PJ':0.5,'PM':0,'JM':0.2,'PJM':0.3}


kk=""
for k in P.keys():
    kk+=k+"     "
print(kk)

vv=""
for v in P.values():
    vv+=str(v)+"     "
print(vv)


Pla = {'O':0,'P':0,'J':0,'M':0,'PJ':0,'PM':0,'JM':0,'PJM':0}
def belief(Pla,P):
    pla_ = voidIt(Pla)
    for e in P.keys():
        for ee in P.keys():
            if(isIN(e,ee)):
                pla_[e]+=P[ee]
    return pla_
print("belief M1")
print(belief(Pla,P))

Pl = {'O':0,'P':0,'J':0,'M':0,'PJ':0,'PM':0,'JM':0,'PJM':0}
def plausabilite(Pl,P):
    pl_ = voidIt(Pl)
    for e in P.keys():
        for ee in P.keys():
            if(isIN_all(e,ee)):
                pl_[ee]+=P[e]
    return pl_

plausabilite(Pl,P)
print("plausabilite M1")
print(plausabilite(Pl,P))

m2 = {'O':0,'P':0.6,'J':0,'M':0,'PJ':0,'PM':0,'JM':0,'PJM':0.4}

print(m2)

PL_M2 = {'O':0,'P':0,'J':0,'M':0,'PJ':0,'PM':0,'JM':0,'PJM':0}

print("belief M2")
print(belief(PL_M2,m2))
print("plausabilite M2")
print(plausabilite(PL_M2,m2))



eps_1 = eps(P)
eps_2 = eps(m2)
print("epsilon 1")
print(eps_1)
print("epsilon 2")
print(eps_2)
def epsilon(li,ep):
    for k in ep:
        print(li[k])

def dempster_Shafer(mm1,eps1,mm2,eps2):
    T = {}
    for element in mm2.keys():
        val1 = 0
        val2 = 0
        for e1 in eps1:  
            for e2 in eps2:
                if element == intersect(e1,e2):
                    val1 +=  mm1[e1]*mm2[e2]
                elif len(intersect(e1,e2)) == 0:
                    val2 = 0.12
        T[element]=(val1/(1-val2))
    print(T)

print("dempster_Shafer ")

print(dempster_Shafer(P,eps_1,m2,eps_2))

