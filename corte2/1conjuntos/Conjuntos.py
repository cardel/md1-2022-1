
conjunto = set()

conjuntoB = {1,2,3,4}

conjuntoC = {1,2,2,2,2,3,3,3,3,4,4,4}

print(conjunto,conjuntoB,conjuntoC)

for e in conjuntoB:
    print(e)


print(conjuntoB==conjuntoC)

def cartesian_product(a,b):
    salida = []
    for ai in a:
        for bi in b:
            elm = (ai,bi)
            salida.append(elm)
    return set(salida)


print(cartesian_product(conjuntoB,conjuntoC))

def power_set(a,output=[set()],cnt=0):
    out = output.copy()
    if cnt == len(a):
        return out
    else:
        for e in output:            
            for ai in a:
                new = e.union({ai})
                if not(ai in e) and not(new in out):                    
                    out.append(new)


    return power_set(a,out,cnt+1)

print(power_set(conjuntoB))
print(len(power_set(conjuntoB)))


print(len(power_set({1,2,3,4,5,6,7,8,9,10})))
        