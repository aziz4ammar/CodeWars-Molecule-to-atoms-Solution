def parse_molecule (formula):
    L = spread(formula)
    d = {}
    for each in set(L):
        d[each] = L.count(each)
    return d

def spread(s):
    L = []
    d = {'{': '}', '[': ']', '(': ')'}
    i = 0
    while i < len(s):
        if s[i].isalpha() and s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            L.append(s[i])
            i += 1
        elif s[i].isalpha() and s[i] in 'abcdefghijklmnopqrstuvwxyz':
            L[-1] += s[i]
            i += 1
        elif s[i].isdigit() and not s[i-1].isdigit():
            L.extend([L[-1]]*(int(s[i])-1))
            i += 1
        elif s[i].isdigit() and s[i-1].isdigit():
            L.extend([L[-1]]*(int(s[i-1])*9+int(s[i])))
            i += 1
        elif s[i] in '{[(':
            n = s[i:].find(d[s[i]])
            if s[i+n+1].isdigit():
                L += spread(s[i+1: i+n]) * int(s[i+n+1])
                i += n+2
            else:
                L += spread(s[i+1: i+n])
                i = n+1
    return L