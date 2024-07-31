 ;; Enrico Scala <enricos83@gmail.com>

;; This is a domain modeling a 3D-located UAV whose task is to visit a certain number of locations whose description
;; is also given in terms of their exact 3D position. A challenging aspect here is to account for the battery
;; since the UAV cannot do all visit at once but needs to recharge at the starting location. Therefore, multiple
;; travels back and forth may be necessary to cover visit all locations.

(define (domain domain_name)

    (:types
        location - object
    )

    (:predicates
        (visited ?x - location)
    )
    (:functions
        (x)
        (y)
        (z)
        (xl ?l - location)
        (yl ?l - location)
        (zl ?l - location)
        (battery-level)
        (battery-level-full)
        (min_x)
        (max_x)
        (min_y)
        (max_y)
        (min_z)
        (max_z)
        (total_cost)
    )

    (:durative-action increase_x
        :parameters ()
        :duration (= ?duration 1)
        :condition (and
            (at start (>= (battery-level) 1))
            (at start (<= (x) (- (max_x) 1)))
        )
        :effect (and(at end (increase (x) 1))
            (at end (decrease (battery-level) 1))
            (at end (increase (total_cost) 1))
        )
    )

    (:durative-action decrease_x
        :parameters ()
        :duration (= ?duration 1)
        :condition (and
            (at start (>= (battery-level) 1))
            (at start (>= (x) (+ (min_x) 1)))
        )
        :effect (and (at end (decrease (x) 1))
            (at end (decrease (battery-level) 1))
            (at end (increase (total_cost) 1))
        )
    )

    (:durative-action increase_y
        :parameters ()
        :duration (= ?duration 1)
        :condition (and
            (at start (>= (battery-level) 1))
            (at start (<= (y) (- (max_y) 1)))
        )
        :effect (and (at end (increase (y) 1))
            (at end (decrease (battery-level) 1))
            (at end (increase (total_cost) 1))
        )
    )
    (:durative-action decrease_y
        :parameters ()
        :duration (= ?duration 1)
        :condition (and
            (at start (>= (battery-level) 1))
            (at start (>= (y) (+ (min_y) 1)))
        )
        :effect (and (at end (decrease (y) 1))
            (at end (decrease (battery-level) 1))
            (at end (increase (total_cost) 1))
        )
    )

    (:durative-action increase_z
        :parameters ()
        :duration (= ?duration 1)
        :condition (and
            (at start (>= (battery-level) 1))
            (at start (<= (z) (- (max_z) 1)))
        )
        :effect (and (at end (increase (z) 1))
            (at end (decrease (battery-level) 1))
            (at end (increase (total_cost) 1))
        )
    )
    (:durative-action decrease_z
        :parameters ()
        :duration (= ?duration 1)
        :condition (and
            (at start (>= (battery-level) 1))
            (at start (>= (z) (+ (min_z) 1)))
        )
        :effect (and (at end (decrease (z) 1))
            (at end (decrease (battery-level) 1))
            (at end (increase (total_cost) 1))
        )
    )

    (:action visit
        :parameters (?l - location)
        :precondition (and
            (>= (battery-level) 1)
            (= (xl ?l) (x))
            (= (yl ?l) (y))
            (= (zl ?l) (z))
        )
        :effect (and (visited ?l)
            (decrease (battery-level) 1)
            (increase (total_cost) 1))
    )

    (:action recharge
        :parameters ()
        :precondition (and
            (= (x) 0)
            (= (y) 0)
            (= (z) 0)
        )
        :effect (and
            (assign (battery-level) (battery-level-full))
            (increase (total_cost) 1))
    )

)