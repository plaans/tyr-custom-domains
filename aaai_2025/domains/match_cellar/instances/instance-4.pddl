(define (problem instance4)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 6)
        (= (num-fuses) 12)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 12)
        )
    )
    (:metric minimize
        (total-time)
    )
)