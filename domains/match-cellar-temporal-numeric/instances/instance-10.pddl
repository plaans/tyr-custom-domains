(define (problem instance10)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 12)
        (= (num-fuses) 24)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 24)
        )
    )
    (:metric minimize
        (total-time)
    )
)