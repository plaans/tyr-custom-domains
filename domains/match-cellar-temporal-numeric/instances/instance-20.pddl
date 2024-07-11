(define (problem instance20)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 22)
        (= (num-fuses) 44)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 44)
        )
    )
    (:metric minimize
        (total-time)
    )
)