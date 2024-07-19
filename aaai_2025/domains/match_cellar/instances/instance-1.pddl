(define (problem instance1)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 3)
        (= (num-fuses) 6)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 6)
        )
    )
    (:metric minimize
        (total-time)
    )
)