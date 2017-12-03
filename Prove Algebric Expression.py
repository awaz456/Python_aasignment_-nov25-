def lhs(a,b):
    return (a-b)**2

def rhs(a,b):
    return a**2-2*a*b+b**2

ls=lhs(5,7)
rs=rhs(5,7)

print(" lhs={},rhs={}".format(ls,rs))
