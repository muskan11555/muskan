def append1(lst,x):
    lst.append(x)
    return lst

def extend1(lst,l):
    lst.extendl(l)
    return lst

def pop1(lst):
if len(lst) ==0:
    return "list is empty"
return lst.pop()

def remove1(lst,x):
    if x in lst:
        lst.remove(x)
    return lst