(defrule calculate
  (declare (salience 1))
  (eval (sqrt 5))
  (eval (+ 5 1))
  (eval (sqrt 72))
  (eval (in 20.5))
  =>
  (printout t "Result: " (eval (+ (+ (+ 2.23606797749979 5) 8.48528137423857) 20.5)) crlf))
