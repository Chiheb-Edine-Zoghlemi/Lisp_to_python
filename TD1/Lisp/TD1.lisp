;*****************************************************************************;
;EX1;
( defun snoc ( e l ) 
(cond ((null l ) (list e ))
(t ( cons ( car l ) ( snoc e (cdr l ) ) ) ) ) )
;Test;
(SNOC 5 '(1 2 3) )
;*****************************************************************************;
;EX2;
( defun rdc (  l ) 
(cond ( (= (length l ) 1) NIL)
(t ( cons ( car l ) ( rdc  (cdr l ) ) ) ) ) )
;Test;
(rdc '(1 2 3) )
;*****************************************************************************;
;EX3;
( defun rac (  l ) 
(cond ( (= (length l ) 1) (car l))
(t (    rac  (cdr l )   ) )))
;Test;
(rac '(1 2 3) )
;*****************************************************************************;
;EX4;
( defun swap_first_last (l) 
( snoc (car l) (cons (rac l)  (rdc ( cdr l) )  ) ))
;Test;
(swap_first_last '(1 2 3) )
;*****************************************************************************;
;EX5;
( defun ajoutN (e n l) 
( cond (
    (< n (length l)) '"Invalid N position/ position  N est invalidé" )
((= n 1) (cons e l) )
(t cons((car l)(ajoutN( e n (cdr l))  )) )
))
;Test;
(ajoutN 5 2 '(1 2 3) )
;*****************************************************************************;
;EX6;
( defun rech (e p l) 
( cond (
    (< p (length l)) '"Invalid N position/ position  N est invalidé" )
((= p 1) (eq e car(l)) )
(t  rech  e (- p 1 ) (cdr l) )
))
;Test;
(rech 5 2 '(1 2 3) )
;*****************************************************************************;
;EX7;
( defun inverser ( l) 
( cond ( (null l) nil)
(t (cons (rac l) inverser (cdr ( rdc l) )  (car l)) )
))
;Test;
( inverser '(1 2 3) )
;*****************************************************************************;