(define (problem instance16)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 18)
        (= (num-fuses) 36)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 36)
        )
    )
    (:metric minimize
        (total-time)
    )
)