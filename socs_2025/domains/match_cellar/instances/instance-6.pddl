(define (problem instance6)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 8)
        (= (num-fuses) 16)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 16)
        )
    )
    (:metric minimize
        (total-time)
    )
)