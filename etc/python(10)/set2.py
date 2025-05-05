def slen(s):
    return len(s)

def add(s,x):
    s.add(x)
    return s

def remove2(s,x):
    if x in s:
        s.remove(x)
    return s 