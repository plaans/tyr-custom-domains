(define (problem instance13)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 15)
        (= (num-fuses) 30)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 30)
        )
    )
    (:metric minimize
        (total-time)
    )
)