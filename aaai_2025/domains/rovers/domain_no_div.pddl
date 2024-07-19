(define (domain Rover)
(:requirements :typing :durative-actions :fluents)
(:types rover waypoint store camera mode lander objective)

(:predicates (at ?x - rover ?y - waypoint) 
             (at_lander ?x - lander ?y - waypoint)
             (can_traverse ?r - rover ?x - waypoint ?y - waypoint)
	         (equipped_for_soil_analysis ?r - rover)
             (equipped_for_rock_analysis ?r - rover)
             (equipped_for_imaging ?r - rover)
             (empty ?s - store)
             (have_rock_analysis ?r - rover ?w - waypoint)
             (have_soil_analysis ?r - rover ?w - waypoint)
             (full ?s - store)
	         (calibrated ?c - camera ?r - rover) 
	         (supports ?c - camera ?m - mode)
             (available ?r - rover)
             (visible ?w - waypoint ?p - waypoint)
             (have_image ?r - rover ?o - objective ?m - mode)
             (communicated_soil_data ?w - waypoint)
             (communicated_rock_data ?w - waypoint)
             (communicated_image_data ?o - objective ?m - mode)
	         (at_soil_sample ?w - waypoint)
	         (at_rock_sample ?w - waypoint)
             (visible_from ?o - objective ?w - waypoint)
	         (store_of ?s - store ?r - rover)
	         (calibration_target ?i - camera ?o - objective)
	         (on_board ?i - camera ?r - rover)
	         (channel_free ?l - lander)
	         (in_sun ?w - waypoint)

)
(:functions 
       (recharge-duration ?x - rover)
       (recharge-duration-max ?x - rover)
       (recharge-duration-1 ?x - rover)
       (recharge-duration-2 ?x - rover)
       (recharge-duration-3 ?x - rover)
       (recharge-duration-4 ?x - rover)
       (recharge-duration-5 ?x - rover)
       (recharge-duration-6 ?x - rover)
       (recharge-duration-8 ?x - rover)
)
	
(:durative-action navigate
:parameters (?x - rover ?y - waypoint ?z - waypoint) 
:duration (= ?duration 5)
:condition (and (over all (can_traverse ?x ?y ?z)) (at start (available ?x)) (at start (at ?x ?y))  (at start (<= (recharge-duration ?x) (- (recharge-duration-max ?x) (recharge-duration-8 ?x))))
                (over all (visible ?y ?z))
	    )
:effect (and (at start (increase (recharge-duration ?x) (recharge-duration-8 ?x))) (at start (not (at ?x ?y))) (at end (at ?x ?z))))

(:durative-action recharge
:parameters (?x - rover ?w - waypoint)
:duration (= ?duration (recharge-duration ?x))
:condition (and (at start (at ?x ?w)) (over all (at ?x ?w)) 
					(at start (in_sun ?w)) (at start (>= (recharge-duration ?x) 0)))
:effect (and (at end (assign (recharge-duration ?x) 0)))
)


(:durative-action sample_soil
:parameters (?x - rover ?s - store ?p - waypoint)
:duration (= ?duration 10)
:condition (and (over all (at ?x ?p)) (at start (at ?x ?p)) (at start (at_soil_sample ?p)) (at start (equipped_for_soil_analysis ?x)) (at start (<= (recharge-duration ?x) (- (recharge-duration-max ?x) (recharge-duration-3 ?x)))) (at start (store_of ?s ?x)) (at start (empty ?s))
		)
:effect (and (at start (not (empty ?s))) (at end (full ?s)) (at start (increase (recharge-duration ?x) (recharge-duration-3 ?x))) (at end (have_soil_analysis ?x ?p)) (at end (not (at_soil_sample ?p)))
		)
)

(:durative-action sample_rock
:parameters (?x - rover ?s - store ?p - waypoint)
:duration (= ?duration 8)
:condition (and (over all (at ?x ?p)) (at start (at ?x ?p)) (at start (<= (recharge-duration ?x) (- (recharge-duration-max ?x) (recharge-duration-5 ?x)))) (at start (at_rock_sample ?p)) (at start (equipped_for_rock_analysis ?x)) (at start (store_of ?s ?x)) (at start (empty ?s))
		)
:effect (and (at start (not (empty ?s))) (at end (full ?s)) (at end (have_rock_analysis ?x ?p)) (at start (increase (recharge-duration ?x) (recharge-duration-5 ?x))) (at end (not (at_rock_sample ?p)))
		)
)

(:durative-action drop
:parameters (?x - rover ?y - store)
:duration (= ?duration 1)
:condition (and (at start (store_of ?y ?x)) (at start (full ?y))
		)
:effect (and (at end (not (full ?y))) (at end (empty ?y))
	)
)

(:durative-action calibrate
 :parameters (?r - rover ?i - camera ?t - objective ?w - waypoint)
 :duration (= ?duration 5)
 :condition (and (at start (equipped_for_imaging ?r)) (at start (<= (recharge-duration ?r) (- (recharge-duration-max ?r) (recharge-duration-2 ?r)))) (at start (calibration_target ?i ?t)) (over all (at ?r ?w)) (at start (visible_from ?t ?w)) (at start (on_board ?i ?r))
		)
 :effect (and (at end (calibrated ?i ?r)) (at start (increase (recharge-duration ?r) (recharge-duration-2 ?r))))
)




(:durative-action take_image
 :parameters (?r - rover ?p - waypoint ?o - objective ?i - camera ?m - mode)
 :duration (= ?duration 7)
 :condition (and (over all (calibrated ?i ?r))
			 (at start (on_board ?i ?r))
                      (over all (equipped_for_imaging ?r))
                      (over all (supports ?i ?m) )
			  (over all (visible_from ?o ?p))
                      (over all (at ?r ?p))
                      (at start (<= (recharge-duration ?r) (- (recharge-duration-max ?r) (recharge-duration-1 ?r))))
               )
 :effect (and (at end (have_image ?r ?o ?m)) (at start (increase (recharge-duration ?r) (recharge-duration-1 ?r))) (at end (not (calibrated ?i ?r)))
		)
)


(:durative-action communicate_soil_data
 :parameters (?r - rover ?l - lander ?p - waypoint ?x - waypoint ?y - waypoint)
 :duration (= ?duration 10)
 :condition (and (over all (at ?r ?x)) (over all (at_lander ?l ?y)) (at start (have_soil_analysis ?r ?p)) (at start (<= (recharge-duration ?r) (- (recharge-duration-max ?r) (recharge-duration-4 ?r))))
                   (at start (visible ?x ?y)) (at start (available ?r))(at start (channel_free ?l))
            )
 :effect (and (at start (not (available ?r))) (at start (not (channel_free ?l))) (at end (channel_free ?l))
		(at end (communicated_soil_data ?p))(at end (available ?r))(at start (increase (recharge-duration ?r) (recharge-duration-4 ?r)))
	)
)

(:durative-action communicate_rock_data
 :parameters (?r - rover ?l - lander ?p - waypoint ?x - waypoint ?y - waypoint)
 :duration (= ?duration 10)
 :condition (and (over all (at ?r ?x)) (over all (at_lander ?l ?y)) (at start (have_rock_analysis ?r ?p)) 
                   (at start (visible ?x ?y)) (at start (available ?r))(at start (channel_free ?l)) (at start (<= (recharge-duration ?r) (- (recharge-duration-max ?r) (recharge-duration-4 ?r))))
            )
 :effect (and (at start (not (available ?r))) (at start (not (channel_free ?l))) (at end (channel_free ?l))(at end (communicated_rock_data ?p))(at end (available ?r)) (at start (increase (recharge-duration ?r) (recharge-duration-4 ?r)))
          )
)


(:durative-action communicate_image_data
 :parameters (?r - rover ?l - lander ?o - objective ?m - mode ?x - waypoint ?y - waypoint)
 :duration (= ?duration 15)
 :condition (and (over all (at ?r ?x)) (over all (at_lander ?l ?y)) (at start (have_image ?r ?o ?m)) 
                   (at start (visible ?x ?y)) (at start (available ?r)) (at start (channel_free ?l)) (at start (<= (recharge-duration ?r) (- (recharge-duration-max ?r) (recharge-duration-6 ?r))))
            )
 :effect (and (at start (not (available ?r))) (at start (not (channel_free ?l))) (at end (channel_free ?l)) (at end (communicated_image_data ?o ?m)) (at end (available ?r)) (at start (increase (recharge-duration ?r) (recharge-duration-6 ?r)))
          )
)

)
