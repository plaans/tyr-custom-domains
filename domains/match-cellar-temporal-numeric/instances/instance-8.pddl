(define (problem instance8)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 10)
        (= (num-fuses) 20)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 20)
        )
    )
    (:metric minimize
        (total-time)
    )
)