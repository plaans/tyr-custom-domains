(define (problem instance15)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 17)
        (= (num-fuses) 34)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 34)
        )
    )
    (:metric minimize
        (total-time)
    )
)