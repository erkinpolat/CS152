class Symbol:
    def __init__(self):
        pass
    
class DefiniteClaue:
    def __init__(self):
        pass
    
def forward_chaining(KB, q):
    count = [([cl.premise],[cl.conslusion]) for cl in KB]
    inferred = [False for cl in KB]
    agenda = []
    for cl in KB:
        if cl.truth value == 1:
            agenda.append(cl)
            
    while agenda:
        p = pop(agenda)
        if p == q:
            return True
        if inferred[p] == False:
            inferred[p] == True
            
        for cl in KB:
            if p == cl.premise:
                count[c] -= 1
            if count[c] == 0:
                agenda.append(c.conclusion)
                
    return False
