(define (problem instance14)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 16)
        (= (num-fuses) 32)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 32)
        )
    )
    (:metric minimize
        (total-time)
    )
)