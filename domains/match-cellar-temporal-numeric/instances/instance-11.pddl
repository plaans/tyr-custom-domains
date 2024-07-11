(define (problem instance11)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 13)
        (= (num-fuses) 26)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 26)
        )
    )
    (:metric minimize
        (total-time)
    )
)