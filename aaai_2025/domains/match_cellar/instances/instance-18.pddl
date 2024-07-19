(define (problem instance18)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 20)
        (= (num-fuses) 40)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 40)
        )
    )
    (:metric minimize
        (total-time)
    )
)