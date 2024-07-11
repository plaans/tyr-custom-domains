(define (problem instance9)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 11)
        (= (num-fuses) 22)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 22)
        )
    )
    (:metric minimize
        (total-time)
    )
)