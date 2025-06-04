(define (problem instance19)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 21)
        (= (num-fuses) 42)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 42)
        )
    )
    (:metric minimize
        (total-time)
    )
)