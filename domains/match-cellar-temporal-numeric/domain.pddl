(define (domain matchcellar)
    (:requirements :durative-actions :fluents)
    (:predicates
        (handfree)
    )

    (:functions
        (num-matches) ; Number of available matches
        (num-fuses) ; Number of available fuses
        (num-lit-matches) ; Number of matches currently giving light
        (num-mended-fuses) ; Number of fuses mended
    )

    (:durative-action LIGHT_MATCH
        :parameters ()
        :duration (= ?duration 5)
        :condition (and
            (at start (handfree))
            (at start (> num-matches 0)))
        :effect (and
            (at start (decrease num-matches 1))
            (at start (increase num-lit-matches 1))
            (at end (decrease num-lit-matches 1)))
    )

    (:durative-action MEND_FUSE
        :parameters ()
        :duration (= ?duration 2)
        :condition (and
            (at start (handfree))
            (at start (> num-lit-matches 0))
            (at end (> num-lit-matches 0)))
        :effect (and
            (at start (not (handfree)))
            (at end (increase num-mended-fuses 1))
            (at end (handfree)))
    )
)