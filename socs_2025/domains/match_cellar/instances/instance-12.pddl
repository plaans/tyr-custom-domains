(define (problem instance12)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 14)
        (= (num-fuses) 28)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 28)
        )
    )
    (:metric minimize
        (total-time)
    )
)