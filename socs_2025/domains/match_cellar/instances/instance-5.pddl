(define (problem instance5)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 7)
        (= (num-fuses) 14)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 14)
        )
    )
    (:metric minimize
        (total-time)
    )
)