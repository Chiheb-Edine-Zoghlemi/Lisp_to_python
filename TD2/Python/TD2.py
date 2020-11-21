##########################################################
# LISP  ==> Python 
def car(L): return L[0]
def cdr(L): return L[1:]
def cons(x, xs):
  return [x, *xs]
lst=[1,2,8,5,6,7,8]
##########################################################
#EX1
def CHERCHE (e,lst) : 
    if not lst : 
        return False
    elif car(lst) == e :
        return True
    else: 
        return CHERCHE(e,cdr(lst))
#Test
#print(CHERCHE(2,lst))

##########################################################
#EX2
def ENSEMBLE (lst) : 
    if not lst : 
        return True
    elif CHERCHE( car(lst) , cdr(lst)) :
        return False
    else: 
        return ENSEMBLE(cdr(lst))
#Test
#print(ENSEMBLE(lst))

##########################################################
#EX3
def UNIQUE (lst) : 
    if ENSEMBLE (lst) : 
        return lst
    elif CHERCHE( car(lst) , cdr(lst)) :
        return UNIQUE(cdr(lst)) 
    else: 
        return cons(car(lst),UNIQUE(cdr(lst)) )
#Test
#print(UNIQUE(lst))

##########################################################
lst1=[1,2,5,6,7,8]
lst2=[1,9,5,6,7,8]
##########################################################

#EX4
def INCLUS (lst1,lst2) : 
    if not lst1 : 
        return True
    elif CHERCHE( car(lst1) , lst2) == False :
        return False 
    else: 
        return INCLUS(cdr( lst1 ),lst2)
#Test
#print(INCLUS(lst1,lst2))

##########################################################
#EX5
def INTER (lst1,lst2) : 
    if not lst1 : 
        return []
    elif CHERCHE( car(lst1) , lst2) == False :
        return INTER(cdr( lst1 ),lst2) 
    else: 
        return cons(car(lst1),INTER(cdr( lst1 ),lst2))
#Test
#print(INTER(lst1,lst2))

##########################################################
#EX6
def UNION (lst1,lst2) : 
    if not lst1 : 
        return lst2
    else: 
        return cons(car(lst1),UNION(cdr( lst1 ),lst2))
#Test
#print(UNION(lst1,lst2))

