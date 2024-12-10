(define (problem instance2)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 4)
        (= (num-fuses) 8)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 8)
        )
    )
    (:metric minimize
        (total-time)
    )
)