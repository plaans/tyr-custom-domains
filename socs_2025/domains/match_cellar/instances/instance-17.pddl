(define (problem instance17)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 19)
        (= (num-fuses) 38)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 38)
        )
    )
    (:metric minimize
        (total-time)
    )
)