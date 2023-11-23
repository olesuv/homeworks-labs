; Правило 1 з пріоритетом 4
(defrule rule1 
   (declare (salience 4))
   => 
   (printout t "Правило 1 активовано без введення початкового факту!" crlf))

; Правило 2 з пріоритетом 3
(defrule rule2
   (declare (salience 3))
   =>
   (printout t "Правило 2 активовано!" crlf))

; Правило 3 з пріоритетом 2
(defrule rule3
   (declare (salience 2))
   =>
   (printout t "Правило 3 активовано!" crlf))

; Правило 4 з пріоритетом 1
(defrule rule4
   (declare (salience 1))
   =>
   (printout t "Всі правила активовано!" crlf))

