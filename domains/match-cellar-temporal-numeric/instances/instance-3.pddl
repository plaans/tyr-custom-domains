(define (problem instance3)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 5)
        (= (num-fuses) 10)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 10)
        )
    )
    (:metric minimize
        (total-time)
    )
)