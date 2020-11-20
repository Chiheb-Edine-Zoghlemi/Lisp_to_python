##########################################################
# LISP  ==> Python 
def car(L): return L[0]
def cdr(L): return L[1:]
def cons(x, xs):
  return [x, *xs]
lst=[1,2,5,6,7,8]
##########################################################
#EX1
def snoc (e,lst) : 
    if not lst : 
        return [e]
    else: 
        return cons(car(lst),snoc(e,cdr(lst)))
#Test
#print(snoc(2,lst))

##########################################################
#EX2
def rdc (lst) : 
    if len(lst)==1 : 
        return []
    else: 
        return cons(car(lst),rdc(cdr(lst)))
#Test
#print(rdc(lst))

##########################################################
#EX3
def rac (lst) : 
    if len(lst)==1 : 
        return car(lst)
    else: 
        return rac(cdr(lst))
#Test
#print(rac(lst))

##########################################################
#EX4
def swap_first_last (lst) : 
    return snoc( car(lst),cons(rac(lst), rdc(cdr(lst))))
#Test
#print(swap_first_last(lst))

##########################################################
#EX5
def ajoutN (e,n,lst) : 
    if n > len(lst) : 
        return 'Invalid N position/ position  N est invalidé'
    elif n==1 : 
        return cons(e,lst)
    else: 
        return cons(car(lst),ajoutN(e,n-1,cdr(lst)))
#Test
#print(ajoutN(10,5,lst))

##########################################################
#EX6
def rech (e,p,lst) : 
    if p > len(lst) : 
        return 'Invalid N position/ position  N est invalidé'
    elif p==1 : 
        return e == car(lst)
    else: 
        return rech(e,p-1,cdr(lst))
#Test
#print(rech(5,3,lst))

##########################################################
#EX7
def inverser(lst):
    if len(lst) == 0:
        return [] 
    else:
        return cons(rac(lst),inverser(rdc(lst)))
#Test
#print(inverser(lst))

