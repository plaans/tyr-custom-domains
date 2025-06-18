;; Based on the Counter paper domain originally created by 
;; Guillem Franc`es (guillem.frances@upf.edu) and Hector Geffner (hector.geffner@upf.edu) 
;; and adapted to numeric planning by Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com); 
;; F-Strips version: Frances, Guillem, and Hector Geffner. "Modeling and computation in planning: 
;;                   Better heuristics from more expressive languages." 
;;                   In Proceedings of the International Conference on Automated Planning and Scheduling, 
;;                   vol. 25, pp. 70-78. 2015.
;; Numeric Version: Scala, Enrico, Patrik Haslum, Sylvie Thiébaux, and Miquel Ramirez. 
;;                   "Subgoaling techniques for satisficing and optimal numeric planning." 
;;                   Journal of Artificial Intelligence Research 68 (2020): 691-752. 
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; This domain models a set of counters whose values can be controlled by two actions, respectively
;; for increase and decrease. A Planning problem for this domain is one where we look for particular
;; configurations of such counters.  

(define (domain fn-counters)
    (:requirements :strips :typing :numeric-fluents :durative-actions :action-costs)
    (:types
        counter
    )

    (:functions
        (value ?c - counter);; - int  ;; The value shown in counter ?c
        (max_int);; - int ;; The maximum integer we consider - a static value
        (total_cost);; - int ;; The total cost of the plan
    )

    ;; Increment the value in the given counter by one
    (:durative-action increment
        :parameters (?c - counter)
        :duration (= ?duration 1)
        :condition (and (at start (<= (+ (value ?c) 1) (max_int))))
        :effect (and (at end (increase (value ?c) 1)) (at end (increase (total_cost) 1)))
    )

    ;; Decrement the value in the given counter by one
    (:durative-action decrement
        :parameters (?c - counter)
        :duration (= ?duration 1)
        :condition (and (at start (>= (value ?c) 1)))
        :effect (and (at end (decrease (value ?c) 1)) (at end (increase (total_cost) 1)))
    )
)