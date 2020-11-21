;*****************************************************************************;
;EX1;
( defun CHERCHE ( e l ) 
(cond ((null l ) nil )
((eq (car l) e) t)
(t   (CHERCHE e (cdr l) )) ) )
;Test;
(CHERCHE 5 '(1 2 3) ) 
;*****************************************************************************;
;EX2;
( defun ENSEMBLE (  l ) 
(cond ((null l ) t )
((CHERCHE(car l) (cdr l)) nil))
(t   ENSEMBLE (cdr l) ) ) )
;Test;
(ENSEMBLE  '(1 2 3) ) 
;*****************************************************************************;
;EX3;
( defun UNIQUE (  l ) 
(cond ((null l ) nil )
((CHERCHE(car l) (cdr l)) UNIQUE(cdr l))
(t   (cons (car l) UNIQUE(cdr l) )) ) )
;Test;
(UNIQUE  '(1 2 3) ) 
;*****************************************************************************;
;EX4;
( defun INCLUS (  l l2 ) 
(cond ((null l ) t )
((= nil (CHERCHE(car l) l2)  nil)
(t   INCLUS(cdr l) l2  )
;Test;
(INCLUS  '(1 2 3) '(1 2 4) ) 
;*****************************************************************************;
;EX5;
( defun INTER (  l l2 ) 
(cond ((null l ) nil )
((CHERCHE(car l) l2)  (cons (car l) (INTER (cdr l))  ))
(t   INTER(cdr l) l2  )
;Test;
(INTER  '(1 2 3) '(1 2 4) ) 
;*****************************************************************************;
;EX5;
( defun UNION (  l l2 ) 
(cond ((null l ) l2 )
(t   cons (car l) (UNION(cdr l) l2)  )
;Test;
(UNION  '(1 2 3) '(1 2 4) ) 


