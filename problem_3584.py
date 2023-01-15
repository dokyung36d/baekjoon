import sys

class tree(object):
    def __init__(self, value, children = None):
        self.value = value
        self.children = children or []
        self.parent = None
        for child in self.children:
            child.parent = self


t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())

    class_list=[tree(i+1) for i in range(n)]

    for i in range(n-1):
        par, chi = map(int, sys.stdin.readline().split())
        class_list[par-1].children.append(chi)
        class_list[chi-1].parent = par

    x1, x2=map(int, sys.stdin.readline().split())
    x1=class_list[x1-1]
    x2=class_list[x2-1]
    
    x1_parents=[x1.value]
    x2_parents=[x2.value]
    while True:
        try:
            x1_parent=class_list[x1.parent -1]
        except TypeError:
            pass

        try:
            x2_parent=class_list[x2.parent -1]
        
        except TypeError:
            pass

        if x1_parent != []:
            x1_parents.append(x1_parent.value)
        
        if x2_parent != []:
            x2_parents.append(x2_parent.value)


        chcek_duplicate=list(set(x1_parents) & set(x2_parents))

        if chcek_duplicate != []:
            print(chcek_duplicate[0])
            break

        try:
            x1=class_list[x1.parent -1]
        except TypeError:
            pass

        try:
            x2=class_list[x2.parent -1]
        except TypeError:
            pass